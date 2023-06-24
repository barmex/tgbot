FROM python:3.10
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./utils utils
COPY main.py main.py
CMD ["python3", "main.py"]