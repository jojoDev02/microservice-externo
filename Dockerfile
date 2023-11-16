FROM python:3.9

WORKDIR /src

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

USER nonroot

COPY src/ .

EXPOSE 5000

CMD ["python3", "main.py"]