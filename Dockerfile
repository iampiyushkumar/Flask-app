# slim Python image
FROM python:3.11-slim

# set workdir
WORKDIR /app

# install deps first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY app.py .

# non-root (optional, good practice)
RUN useradd -m appuser
USER appuser

EXPOSE 5000
CMD ["python", "app.py"]

