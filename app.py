import settings_dev

from os import environ
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(settings_dev)


@app.route('/')
def chackout():
    return render_template('checkout.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=environ.get("PORT", 5000))
