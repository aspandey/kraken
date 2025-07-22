FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5050

CMD ["gunicorn", "--bind", "0.0.0.0:5050", "main:app"]