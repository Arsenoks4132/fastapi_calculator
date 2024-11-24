FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY first_main.py /code/first_main.py

CMD ["fastapi", "run", "first_main.py", "--port", "8001"]