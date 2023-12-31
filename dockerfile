FROM python:3.10-bullseye

WORKDIR /app

COPY ./detectify/ /app/detectify/
COPY ./requirements.txt /app/
COPY ./setup.py /app/

RUN pip install -r requirements.txt
RUN pip install .

CMD ["python", "detectify/api.py"]