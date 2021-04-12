FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8
COPY ./project1.py /project1.py
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt