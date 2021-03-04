# Python Iniciante Django

Video Aula de Python com Django para um projeto POC com um CRUD baseado em SQLite



## Roteiro para Configuração inicia

1. Utilizar Python 3

2. Utilizar virtualenv
    
2.1 Instalar ambiente virtual
        sudo apt install python3-virtualenv
2.2 Criar Pasta para ambiente Virtual
        python3.9 -m virtualenv [nome do projeto]
2.3 Ativar ambiente virtual (atenção o Bash não aceita rodar scripts, pode utilizar o cmd)
        source ./venv_django_0304/bin/activate
        acesse a aplicação
    
3. Instalar Django
        python -m pip install django


4. Guardar Requerimentos de Biblioteca
        Criar Pasta packages
        python -m pip freeze > packages/requirements.txt
    
5. Criar o projeto
        django-admin startproject [nome do projeto]
    
6. Migrar o django para iniciar o projeto com banco de dados
        python manage.py migrate
    
7. Iniciar o Servidor django
        python manage.py runserver [ip servido opcional] [porta opcional] 

8. Criar a Aplicação
        phone_foward/phone_foward

9. Após criar o Model, executar migração novamente
        python manage.py makemigrations
        e
        python manage.py migrate
