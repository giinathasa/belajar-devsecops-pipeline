
FROM python:3.10-slim

WORKDIR /app

# Update paket sistem Debian untuk memperbaiki vulnerability
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Membuat user non-root untuk keamanan container
RUN useradd -m appuser

COPY requirements.txt .

# Update pip, setuptools, dan wheel
RUN python -m pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

# Memberikan hak akses folder aplikasi kepada appuser
RUN chown -R appuser:appuser /app

# Menjalankan container menggunakan user non-root
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
