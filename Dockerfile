FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8
COPY requirements.txt .
COPY project1.py .
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt
EXPOSE 8080
RUN uvicorn project1:app --reload
