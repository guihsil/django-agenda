# 📖 Agenda de Contatos - Django

Projeto de uma Agenda de Contatos desenvolvida com **Python** e **Django** durante o curso de Python 3 do professor Otávio Miranda.

## 🎯 Objetivo do Projeto

O objetivo deste projeto é criar uma aplicação web para gerenciamento de contatos, colocando em prática conceitos fundamentais do framework Django, como Models, Views, Templates, URLs, relacionamento de banco de dados e arquivos estáticos/mídia.

## ✨ Funcionalidades

- Listagem de contatos com paginação (10 contatos por página).
- Busca de contatos por nome, sobrenome, telefone ou e-mail.
- Visualização detalhada do perfil do contato.
- Categorização de contatos (Ex: Amigos, Família, Conhecidos).
- Suporte a upload de imagens de perfil dos contatos.
- Sistema de ocultar/exibir contatos específicos (`show`).
- Painel administrativo do Django configurado para gerenciar contatos e categorias.
- Script automatizado para popular o banco de dados com contatos fictícios para fins de teste.

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **Django 6.0.6**
- **SQLite3** (Banco de dados)
- **Pillow** (Para lidar com upload e processamento das imagens de perfil)
- **Faker** (Para geração de dados fictícios de teste)
- **HTML5 e CSS3** (Estilização própria sem frameworks css externos)

## 🛠️ Como executar o projeto na sua máquina

Siga o passo a passo abaixo para rodar o projeto localmente:

### 1. Clone o repositório
```bash
git clone https://github.com/guihsil/django-agenda
cd django-agenda
```

### 2. Ambiente virtual
```bash
python -m venv venv
```

### 3. Dependências do projeto
```bash
pip install -r requirements.txt
```

### 4. Execute as migrations
```bash
python manage.py migrate
```

### 5. Crie um super usuário
```bash
python manage.py createsuperuser
```

### 6. (Opicional) popular banco de dados com dados falsos
```bash
python utils/create_contacts.py
```

### 7. Rodar o servidor
```bash
python manage.py runserver
```