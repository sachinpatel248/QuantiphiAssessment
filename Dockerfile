FROM python:3.12.2-slim

RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc linux-libc-dev libc6-dev build-essential

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY ./requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

ARG ENVIRONMENT
ENV ENVIRONMENT=$ENVIRONMENT


WORKDIR /app
ARG PORT
ARG HOST
ARG GRADIOPORT

ENV PORT=$PORT
ENV HOST=$HOST
ENV GRADIOPORT=$GRADIOPORT


EXPOSE ${PORT}
CMD  uvicorn main:app --host ${HOST} --port ${PORT}

# EXPOSE ${GRADIOPORT}
# CMD python gradio_app.py
