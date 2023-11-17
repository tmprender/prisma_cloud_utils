FROM python:3.11

WORKDIR  /app

COPY requirements.txt requirements.txt
RUN pip install requests

COPY examples/ examples/

CMD ["python3", "examples/cspm_login.py"]