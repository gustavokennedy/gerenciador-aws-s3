# Gerenciador AWS S3 🚀

Um gerenciador visual robusto e intuitivo para controle rápido de objetos no AWS S3. Este projeto open-source foi criado para simplificar a interação com buckets e objetos no Amazon S3, oferecendo uma interface amigável e funcionalidades poderosas para desenvolvedores e administradores de sistemas.

![Screenshot 1](https://github.com/user-attachments/assets/75c048fc-76fe-47bd-b931-04d89b3967bd)  
![Screenshot 2](https://github.com/user-attachments/assets/a06afe03-cb77-4069-8e4e-9aca2b1b998b)

## ✨ Funcionalidades

- **Navegação Visual**: Explore buckets e objetos com uma interface gráfica simples e organizada.
- **Upload e Download**: Faça upload de arquivos para o S3 e baixe objetos com apenas alguns cliques.
- **Gerenciamento de Permissões**: Visualize e edite permissões de acesso diretamente na interface.
- **Pesquisa Rápida**: Encontre objetos específicos em seus buckets com filtros e buscas eficientes.
- **Suporte Multi-Conta**: Conecte-se a várias contas AWS sem complicações.
- **Pré-visualização**: Veja o conteúdo de arquivos (imagens, PDFs, etc.) sem precisar baixá-los.

## 🚀 Como Começar

### Pré-requisitos
- Python 3.8 ou superior
- Conta AWS com acesso ao S3
- Credenciais AWS configuradas (AWS Access Key e Secret Key)

### Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/gustavokennedy/gerenciador-aws-s3.git
2. Entre no diretório do projeto:
   ```bash
   cd gerenciador-aws-s3
3. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
4. Configure suas credenciais AWS em um arquivo .env (exemplo abaixo):
   ```bash
   AWS_ACCESS_KEY_ID=
   AWS_SECRET_ACCESS_KEY=
   AWS_REGION=us-east-1
5. Inicie o sistema (backend):
   ```bash
   python app.py

## 🤝 Contribuindo
Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

- Faça um fork do projeto.
- Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`).
- Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`).
- Envie para o repositório remoto (`git push origin feature/nova-funcionalidade`).
- Abra um Pull Request.
- Por favor, leia o Código de Conduta e as Diretrizes de Contribuição antes de começar.

## 🛠 Tecnologias Utilizadas
- Backend: Python, Flask
- Integração AWS: Boto3 (AWS SDK para Python)
- Frontend: HTML, CSS, JavaScript
