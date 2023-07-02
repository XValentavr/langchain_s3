FROM python:3.10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# set argument vars in docker-run command
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION
ARG AWS_S3_BUCKET_NAME


ENV AWS_ACCESS_KEY_ID $AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY $AWS_SECRET_ACCESS_KEY
ENV AWS_DEFAULT_REGION $AWS_DEFAULT_REGION
ENV AWS_S3_BUCKET_NAME $AWS_S3_BUCKET_NAME

# install dependencies
RUN pip install --upgrade pip
COPY src/requirements.txt .
RUN pip install -r requirements.txt

# copy project

COPY . /app
WORKDIR /app/src

EXPOSE 5000
CMD ["python", "application.py"]
