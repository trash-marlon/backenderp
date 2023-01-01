# Pull the official base image
FROM python:3.9.15-alpine

# Update and install dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev build-base linux-headers pcre-dev jpeg-dev zlib-dev

# Set work directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# Copy project
COPY . /usr/src/app

EXPOSE 8000

# Make migrations
RUN python manage.py makemigrations

# Migrate
RUN python manage.py migrate

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]