FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN pip install uvicorn aiofiles

ENV PORT=8000
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", PORT]