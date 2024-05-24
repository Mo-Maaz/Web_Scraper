# Use the official Python image from Docker Hub
FROM python:3.8-slim

# Set environment variables for Flask
ENV FLASK_APP=scraper_service.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host=files.pythonhosted.org -r requirement.txt

# Expose port 8080 to the outside world
EXPOSE 8080

# Expose port 9095 for metrics
EXPOSE 9095

# Run the scraper service
CMD ["python", "scraper_service.py"]