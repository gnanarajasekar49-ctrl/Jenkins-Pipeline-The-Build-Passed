FROM python:3.11-slim

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .

# Jenkins build metadata
ARG BUILD_NUMBER
ARG GIT_COMMIT
ARG BRANCH_NAME

# Store metadata as Docker labels
LABEL org.opencontainers.image.version="${BUILD_NUMBER}"
LABEL org.opencontainers.image.revision="${GIT_COMMIT}"
LABEL org.opencontainers.image.sourcebranch="${BRANCH_NAME}"

# Store metadata as application environment variables
ENV BUILD_NUMBER="${BUILD_NUMBER}"
ENV GIT_COMMIT="${GIT_COMMIT}"
ENV BRANCH_NAME="${BRANCH_NAME}"

EXPOSE 8080

CMD ["python", "app.py"]