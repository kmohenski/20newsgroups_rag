# Retrieval-Augmented Generation using LangChain

A RAG model using using the 20 Newsgroups science and computer messages.

If you don't want to embed the files yourself you can download them here: [mega.nz link](https://mega.nz/file/uZoxwJqL#-je67pJtlhaz5gd_BcPVd1wSE7-cYige0wo_MbQLhW0)

You can also download the docker files here: [mega.nz link](https://mega.nz/file/LEw0nACC#Jt7BQFl4hVwmRa_MMIwHPElM0WtiRAL_huYWqExPBZ0)

Streamlit application files are located in [the app directory](app/).

### How to run

First make a .env file with your OpenAI API key (format)

Either
1. Install Python 3.11.9
2. Change the `python = "^3.11.9"` line in the [pyproject](pyproject.toml) file to your python version (Python 3.10 or over recommended)

- Install Poetry if it's not already installed:
```bash
pip install poetry
```

- Install project dependencies with Poetry:
```bash
poetry install
```

- Run streamlit application
```bash
streamlit run app\main.py
```

This will open the application on http://localhost:8501

### How to build docker

- Build a *.tar.gz file:
```bash
poetry build
```
You can [download them here](https://mega.nz/file/LEw0nACC#Jt7BQFl4hVwmRa_MMIwHPElM0WtiRAL_huYWqExPBZ0)


- Run docker:
```bash
docker-compose up --build
```