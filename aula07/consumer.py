from kafka import KafkaConsumer
from json import loads

from flask import Flask, escape, request

app = Flask(__name__)

consumer = KafkaConsumer(
    'page_views-page_views-changelog',
     bootstrap_servers=['kafka:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group')

@app.route('/')
def hello():
    output = ""
    for message in consumer:
        message = message.value
        print('{} received'.format(message))
        output = output + str(message) + "\n"
    return f'{output}'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')