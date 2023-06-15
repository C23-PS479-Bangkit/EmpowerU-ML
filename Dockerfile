# Base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Run the application
EXPOSE 3000
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "3000"]