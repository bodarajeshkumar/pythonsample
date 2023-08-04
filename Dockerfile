# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Flask application code into the container
COPY app.py /app

# Install required dependencies
RUN pip install Flask

# Expose the port that the Flask app will be running on
EXPOSE 5000

# Start the Flask app when the container starts
CMD ["python", "app.py"]