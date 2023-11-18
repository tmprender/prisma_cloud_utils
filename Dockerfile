FROM python:3.11

WORKDIR  /app

COPY prisma_utils/ prisma_utils/
COPY setup.py setup.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 
RUN pip install -e .


COPY examples/ examples/

COPY .env .env

CMD ["python3", "examples/cspm_login.py"]