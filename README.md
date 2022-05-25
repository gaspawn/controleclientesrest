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

##Configurando o sistema
criar na raiz do sistema arquivo .env com suas configurações
* Exemplo: DEBUG=True
           AUTENTICAR=True

## Referências:
* https://www.youtube.com/watch?v=wtl8ZyCbTbg (ensina criação básica da api com django)
* https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html (tutorial usado para autenticação)
* https://suyojtamrakar.medium.com/how-to-provide-initial-data-in-django-models-2422aaf3c09a (popular banco inicial)
* https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html (usuário padrão com mais atributos)
* https://django-rest-framework-simplejwt.readthedocs.io/en/latest/customizing_token_claims.html (customizar as claws do token)
* https://medium.com/sulang/testing-django-rest-framework-d98279a5d3a5 (teste de software)
* https://www.django-rest-framework.org/api-guide/testing/#creating-test-requests (teste de software)
* https://www.youtube.com/watch?v=8l8xwvRO1_U (deploy no heroku)

### Documentação oficial 
* https://www.django-rest-framework.org/#requirements
* https://www.django-rest-framework.org/tutorial/quickstart/
* https://www.django-rest-framework.org/tutorial/1-serialization/
* https://www.django-rest-framework.org/api-guide/requests/