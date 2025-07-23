# Use a lightweight Python base image
FROM python:3.9-slim

# Set a directory for the app
WORKDIR /app

# Copy only the requirements file initially to leverage Docker cache
COPY production/requirements.txt .

# Install the necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY production/ /app/

# Set environment variables for model and data paths
ENV MODEL_PATH /app/model.h5
ENV DATA_PATH /app/data/input.csv

# Specify a non-root user for security
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Command to run the main process
CMD ["python", "main_process.py"]