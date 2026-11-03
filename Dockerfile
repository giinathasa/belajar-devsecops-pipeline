FROM python:latest

RUN pip install flask

COPY . .
USER root
EXPOSE 5000
CMD python app.py
