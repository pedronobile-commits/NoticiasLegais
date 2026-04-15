Este projeto consiste no desenvolvimento de uma aplicação web de notícias utilizando o microframework Flask, estruturada com base no padrão arquitetural MVC (Model-View-Controller). O objetivo é criar uma plataforma organizada, escalável e de fácil manutenção para publicação e gerenciamento de conteúdos informativos, sem utilização de APIs externas.

No padrão MVC, a aplicação é dividida em três camadas principais:

Model (Modelo): responsável pela estrutura dos dados e interação com o banco de dados (como SQLite), incluindo a definição das entidades, como notícias, categorias e usuários.
View (Visão): responsável pela interface com o usuário, utilizando templates Jinja2 para renderizar páginas dinâmicas com HTML e CSS, proporcionando uma experiência visual clara e responsiva.
Controller (Controlador): gerencia a lógica da aplicação, recebendo as requisições do usuário, processando as informações e retornando as respostas adequadas por meio das views.

A aplicação permite o gerenciamento completo de notícias, incluindo criação, edição, exclusão e listagem de artigos. As notícias são organizadas por categorias, facilitando a navegação e a busca por conteúdos específicos.

O sistema também conta com autenticação de usuários, permitindo diferenciar administradores de usuários comuns. Administradores possuem acesso a funcionalidades de gerenciamento de conteúdo, enquanto visitantes podem visualizar as notícias publicadas.

Entre os recursos implementados estão a exibição de notícias recentes, paginação de conteúdo, organização modular do código e separação clara de responsabilidades, conforme proposto pelo padrão MVC.

O principal objetivo do projeto é demonstrar a construção de uma aplicação web completa com Flask, aplicando boas práticas de desenvolvimento e arquitetura de software, com foco em organização, manutenção e clareza estrutural.

Para iniciar a aplicação, basta iniciar um ambiente virtual (venv) e baixar as dependencias necessarias:
pip install Flask
pip install python-dotenv
pip install mysql-connector-python

e para rodar o código:

source venv/bin/activate && python app.py 
