FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /teams
WORKDIR /teams
COPY requirements.txt /teams/
RUN pip install -r requirements.txt
COPY . /teams/
CMD python manage.py runserver --settings=senttings.production 0.0.0.0:8080
