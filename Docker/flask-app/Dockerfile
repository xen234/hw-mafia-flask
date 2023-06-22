FROM python:3.8


RUN mkdir /mafia
WORKDIR /mafia/app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y wkhtmltopdf


COPY . .

EXPOSE 3001
ENTRYPOINT [ "python", "api.py" ]