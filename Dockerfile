# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /root

# Install system dependencies for psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Define environment variable
ENV FLASK_APP=app.py
# ENV PYTHONPATH=/root

# Copy everything from the root directory into the container at /root
COPY . /root

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py using gunicorn when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--reload", "app.app:application"]
