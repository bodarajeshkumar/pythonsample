# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Flask application code into the container
COPY . .

# Install required dependencies
RUN pip install Flask

RUN chmod -R 777 ./uploads

# Expose the port that the Flask app will be running on
EXPOSE 5000

# Start the Flask app when the container starts
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
