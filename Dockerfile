# Base Image
FROM python:3.9-slim

# Work directory
WORKDIR /main

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install virtualenv
RUN virtualenv venv
RUN chmod +x venv/bin/activate
RUN venv/bin/activate
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy other project files
COPY . .

# Expose a port to Containers
EXPOSE 8080

# Command to run on server
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]