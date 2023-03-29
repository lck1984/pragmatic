FROM python:3.10.0

WORKDIR /home/

RUN git clone https://github.com/lck1984/pragmatic.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-d8%%^#f*!ztn+_u!!s_9go20@)#(iyquvzd)o(wt3oj*do-^b+" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]