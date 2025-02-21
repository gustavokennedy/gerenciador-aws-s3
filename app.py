from flask import Flask, jsonify, request
from flask_cors import CORS
import boto3
from botocore.exceptions import ClientError
import base64
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)
CORS(app)  # Permitir requisições cross-origin

# Configuração do S3 com variáveis de ambiente
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)

# Listar buckets
@app.route('/api/buckets', methods=['GET'])
def list_buckets():
    try:
        response = s3_client.list_buckets()
        buckets = [{'Name': bucket['Name']} for bucket in response['Buckets']]
        return jsonify(buckets)
    except ClientError as e:
        return jsonify({'error': str(e)}), 500

# Listar arquivos e pastas em um bucket
@app.route('/api/bucket/<bucket_name>', methods=['GET'])
def list_files(bucket_name):
    prefix = request.args.get('prefix', '')  # Parâmetro opcional para subpastas
    try:
        response = s3_client.list_objects_v2(
            Bucket=bucket_name,
            Prefix=prefix,
            Delimiter='/'
        )
        # Lista de arquivos
        files = [{'Key': obj['Key']} for obj in response.get('Contents', []) if obj['Key'] != prefix]
        # Lista de pastas (prefixos)
        folders = [{'Prefix': prefix_obj['Prefix']} for prefix_obj in response.get('CommonPrefixes', [])]
        return jsonify({'files': files, 'folders': folders})
    except ClientError as e:
        return jsonify({'error': str(e)}), 500

# Upload de arquivo
@app.route('/api/upload/<bucket_name>', methods=['POST'])
def upload_file(bucket_name):
    try:
        data = request.json
        file_name = data['fileName']
        file_content = base64.b64decode(data['fileContent'])
        
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_content
        )
        return jsonify({'message': 'Upload concluído', 'Key': file_name})
    except ClientError as e:
        return jsonify({'error': str(e)}), 500

# Download de arquivo
@app.route('/api/download/<bucket_name>/<path:file_name>', methods=['GET'])
def download_file(bucket_name, file_name):
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=file_name)
        file_content = base64.b64encode(response['Body'].read()).decode('utf-8')
        return jsonify({'content': file_content})
    except ClientError as e:
        return jsonify({'error': str(e)}), 500

# Deletar arquivo
@app.route('/api/delete/<bucket_name>/<path:file_name>', methods=['DELETE'])
def delete_file(bucket_name, file_name):
    try:
        s3_client.delete_object(Bucket=bucket_name, Key=file_name)
        return jsonify({'message': 'Arquivo deletado com sucesso'})
    except ClientError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    required_vars = ['AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'AWS_REGION']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        print(f"Erro: Variáveis de ambiente faltando: {', '.join(missing_vars)}")
        exit(1)
    app.run(debug=True, port=5000)
