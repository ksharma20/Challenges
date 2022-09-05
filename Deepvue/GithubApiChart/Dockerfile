FROM python:bullseye
COPY requirements.txt /ksharma20/code/
WORKDIR /ksharma20/code
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD (python manage.py runserver 0.0.0.0:8000)