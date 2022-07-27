# Pull base image
FROM python:3.8-slim

# Set environment variables 
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1 

# Set work directory
ENV APP_HOME=/app/web
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# Install dependencies
COPY requirements.txt $APP_HOME
RUN pip install -r requirements.txt

# Copy project
COPY . $APP_HOME

# django
RUN python $APP_HOME/manage.py makemigrations
RUN python $APP_HOME/manage.py migrate
RUN python $APP_HOME/manage.py collectstatic