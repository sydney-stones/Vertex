FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app_deploy.py app.py
COPY virtual_tryon.py .
COPY config.py .

# Create directories
RUN mkdir -p output_images input_images/person input_images/clothing

# Set environment variables
ENV PORT=8080
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 8080

# Run the application
CMD python app.py
