from flask import Flask, request, jsonify
import logging

app: Flask = Flask(__name__)
logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(message)s')


@app.route("/", methods=["GET"])
def test():
    return "Hello World"


if __name__ == '__main__':
    app.run()