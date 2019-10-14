FROM python:3-slim

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["flask-app.py"]