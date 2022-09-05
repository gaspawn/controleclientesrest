FROM python:3.9
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt && python manage.py migrate
ENTRYPOINT [ "python","manage.py","runserver","0.0.0.0:8000" ]
EXPOSE 8000

##para fazer o build docker build -t pi3 .
## para rodar container da imagem docker run --name pi3_1 -p 8080:8000 pi3