FROM ubuntu:latest
LABEL authors="gega"

ENTRYPOINT ["top", "-b"]


# Use an official Python runtime as a parent image
FROM python:3.10.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Django runs on
EXPOSE 8000

# Run Django when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
