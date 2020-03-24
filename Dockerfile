FROM python:3.7.7

WORKDIR /app

COPY . .

RUN set -ex && \
    adduser --disabled-password --gecos '' app

RUN set -ex && \
    pip install -r requirements.txt

RUN chown -R app:app .

EXPOSE 1234

USER app

CMD python manage.py runserver 0.0.0.0:1234
