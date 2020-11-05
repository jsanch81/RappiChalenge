FROM python:3.7

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP ./api/modelApi.py

EXPOSE 5000

CMD [ "flask", "run"]
