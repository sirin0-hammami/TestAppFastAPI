# Pull base image
FROM bitnami/python:3.7

COPY . /fastMiniApp

WORKDIR /fastMiniApp

RUN pip3 install install -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]