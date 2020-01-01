from flask import Flask, json

from service import PrimeNumberCheck

app = Flask(__name__)


@app.route('/isTwoSided/<int:num>')
def is_two_sided(num):
    return json.dumps(PrimeNumberCheck().is_two_sided_prime(num));


if __name__ == '__main__':
    app.run()
