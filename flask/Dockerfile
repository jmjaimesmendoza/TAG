FROM python:3.11
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
ENV FLASK_APP main.py
COPY ./main.py /code/main.py

EXPOSE 5420

CMD [ "python", "main.py"]