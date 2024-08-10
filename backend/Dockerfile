FROM python:3.11.8

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY ./images /app/images/

COPY ./models /app/models/

COPY ./main.py /app/main.py

EXPOSE 8001

CMD ["uvicorn", "main:app", "--port", "8001", "--host", "0.0.0.0", "--reload"]
