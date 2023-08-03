FROM python:3.10.9

RUN pip install fastapi[all] \
  && pip install uvicorn[standard]==0.23.1 \
  && pip install pydantic==2.1.1 \
  && pip install typing-extensions==4.7.1 \
  && pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]