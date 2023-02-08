ARG PYTHON_VERSION=3.10-slim-buster
ARG DJANGO_SUPERUSER_USERNAME
ARG DJANGO_SUPERUSER_EMAIL
ARG DJANGO_SUPERUSER_PASSWORD

RUN echo $DJANGO_SUPERUSER_USERNAME

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt

RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
RUN python -m pip install Pillow

COPY . /code/

RUN python manage.py makemigrations projet
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
RUN python manage.py createsuperuser --noinput --username DJANGO_SUPERUSER_USERNAME --email DJANGO_SUPERUSER_EMAIL --password DJANGO_SUPERUSER_PASSWORD

EXPOSE 8000

# replace demo.wsgi with <project_name>.wsgi
# CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "VReservation.wsgi"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
