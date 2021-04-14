FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8
COPY requirements.txt requirements.txt
COPY project1.py project1.py
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "project1:app", "--host", "0.0.0.0", "--port", "8000"]
