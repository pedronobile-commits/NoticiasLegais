(https://github.com/user-attachments/files/26732465/NoticiasLegais.md)
📰 NoticiasLegais

Sistema web de gerenciamento de notícias desenvolvido com Python + Flask, utilizando arquitetura MVC (Model-View-Controller). O projeto permite criar, visualizar, editar e excluir notícias, além de organizar categorias e gerenciar favoritos.

🚀 Funcionalidades
✅ Cadastro de notícias
✅ Listagem de notícias
✅ Edição e exclusão (CRUD completo)
✅ Sistema de categorias
✅ Marcação de favoritos
✅ Organização em arquitetura MVC
✅ Integração com banco de dados (MySQL)
🛠️ Tecnologias utilizadas
Python
Flask
HTML5
CSS3
MySQL
Jinja2 (templates)
📁 Estrutura do projeto
NoticiasLegais/
│
├── blueprints/     # Rotas da aplicação (controllers)
├── templates/      # Arquivos HTML
├── static/         # CSS, JS e imagens
├── app.py          # Arquivo principal
├── utils.py        # Funções auxiliares
├── script.sql      # Script do banco de dados
└── .env            # Variáveis de ambiente
⚙️ Como executar o projeto
Clone o repositório:
git clone https://github.com/pedronobile-commits/NoticiasLegais.git
Acesse a pasta:
cd NoticiasLegais
comando para iniciar: source venv/bin/activate && python app.py
Crie e ative um ambiente virtual (opcional, mas recomendado):
python -m venv venv
venv\Scripts\activate
Instale as dependências:
pip install flask python-dotenv
Configure o banco de dados:
Execute o arquivo script.sql no seu MySQL
Configure o .env:
SECRET_KEY=sua_chave
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=nome_do_banco
Execute o projeto:
python app.py
Acesse no navegador:
http://localhost:5000
📌 Observações
Este projeto foi desenvolvido para fins educacionais
Pode ser expandido com autenticação de usuários
Estrutura preparada para crescimento e novas funcionalidades

Desenvolvedores: Pedro Nobile, Laura Brasão, Michel
