FROM python:3.10.0

WORKDIR /home/

RUN echo "testing1"

RUN git clone https://github.com/lck1984/pragmatic.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRET_KEY=django-insecure-d8%%^#f*!ztn+_u!!s_9go20@)#(iyquvzd)o(wt3oj*do-^b+" > .env

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]