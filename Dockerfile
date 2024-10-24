FROM python:3.10

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY .. ./
EXPOSE 8000/tcp

CMD gunicorn --bind :8000 --workers 1 main:app --worker-class uvicorn.workers.UvicornWorker --preload --timeout 120
