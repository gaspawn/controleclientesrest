# Passos para instalação da aplicação.

## instalação dos frameworks via pip
* django
* djangorestframework
* djangorestframework-simplejwt
* markdown (Não é necessário ainda)
* django-filter (Não é necessário ainda)


## Comandos do django
* python manage.py makemigrations --> quando é alterada a estrutura do banco de dados e ele precisa gerar código de criação das tabelas
* python manage.py migrate  --> executa no banco o código gerado pelo makemigrations
* python manage.py createsuperuser  --> cria o usuário para administração do sistema



## Referências:
* https://www.youtube.com/watch?v=wtl8ZyCbTbg (ensina criação básica da api com django)
* https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html (tutorial usado para autenticação)


### Documentação oficial 
* https://www.django-rest-framework.org/#requirements
* https://www.django-rest-framework.org/tutorial/quickstart/
* https://www.django-rest-framework.org/tutorial/1-serialization/
* https://www.django-rest-framework.org/api-guide/requests/