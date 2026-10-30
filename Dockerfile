
FROM python:3.10-slim

WORKDIR /app

# Update package OS untuk memperbaiki vulnerability Debian
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Membuat user non-root
RUN useradd -m appuser

COPY requirements.txt .

# Install dependencies Python
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir --upgrade \
    "jaraco.context>=6.1.0" \
    "wheel>=0.46.2"

COPY . .

# Memberikan hak akses aplikasi kepada appuser
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
