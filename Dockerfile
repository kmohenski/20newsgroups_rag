FROM python:3.11.9

WORKDIR .

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY . .
COPY ./dist ./dist

RUN pip install dist/*.tar.gz --no-cache-dir
RUN pip list
RUN pip install streamlit

EXPOSE 8501

CMD ["streamlit", "run", "app/main.py"]