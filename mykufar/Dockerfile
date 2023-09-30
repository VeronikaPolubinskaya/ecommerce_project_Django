#FROM python:3.7
#ENV PYTHONUNBUFFERED 1
#
#RUN mkdir /app
#WORKDIR /app
#COPY ./mykufar /app
#COPY ./db.sqlite3 /app/db.sqlite3
#
#RUN adduser --disabled-password --no-create-home mykufar
#USER mykufar
#
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mykufar.wsgi:application"]