# Pull base image
FROM python:3.7

COPY . /fastMiniApp

WORKDIR /fastMiniApp

# Install dependencies
RUN /usr/local/bin/python -m pip install --upgrade pip && \
    pip3 install install -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]