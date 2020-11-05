FROM python:3.7

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

#ENV FLASK_APP ./api/modelApi.py

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "modelApi.py" ]
