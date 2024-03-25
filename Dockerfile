FROM python:3.9.10

WORKDIR /code

COPY ./req.txt /code/req.txt

RUN pip install --no-cache-dir --upgrade -r /code/req.txt

COPY ./fine_tuned_model ./code/fine_tuned_model

COPY ./model.py /code/model.py

COPY ./main.py /code/main.py


EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
