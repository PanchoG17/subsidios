FROM python:3.9-slim-buster
WORKDIR /app
COPY . .

RUN apt update && \
    apt install curl gnupg unixodbc-dev -y

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt update && \
    ACCEPT_EULA=Y apt install -y msodbcsql17

COPY openssl.cnf ../etc/ssl/openssl.cnf

RUN pip3 install -r requirements-docker.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]