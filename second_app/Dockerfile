FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY second_main.py /code/second_main.py

CMD ["fastapi", "run", "second_main.py", "--port", "80"]