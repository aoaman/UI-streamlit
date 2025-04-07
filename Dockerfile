FROM python:3.10-slim

WORKDIR /app

COPY /src/app.py /app/app.py
COPY /src/requirements.txt /app/requirements.txt
COPY /src/fetch_data.py /app/fetch_data.py
COPY data /app/data
COPY /src/pages /app/pages

RUN pip install --no-cache-dir -r requirements.txt  

EXPOSE 8501  

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
