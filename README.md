# python_ini_django
 Python Iniciante Django


Utilizar Python 3

Utilizar virtualenv
    Instalar ambiente virtual
        sudo apt install python3-virtualenv
    Criar Pasta para ambiente Virtual
        python3.9 -m virtualenv [nome do projeto]
    Ativar ambiente virtual (atenção o Bash não aceita rodar scripts, pode utilizar o cmd)
        python -m pip install django
    
    Instalar Django
        python -m pip install django


    Guardar Requerimentos de Biblioteca
        Criar Pasta packages
        python -m pip freeze > packages/requirements.txt
    
    Criar o projeto
        django-admin startproject [nome do projeto]
    
    Migrar o django para iniciar o projeto com banco de dados
        python manage.py migrate
    
    Iniciar o Servidor django
        python manage.py runserver [ip servido opcional] [porta opcional] 

    Criar a Aplicação
        phone_foward/phone_foward