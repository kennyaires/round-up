import settings_dev
import math

from os import environ
from flask import Flask, render_template
from db import recset

app = Flask(__name__)
app.config.from_object(settings_dev)


class Produto:
    name = ''
    price = 0
    quantity = 0


class Donation:
    date = ''
    name = ''
    ngo = ''
    ecommerce = ''
    total = ''


@app.route('/')
def checkout():
    p1 = Produto()
    p1.name = 'Produto 1'
    p1.price = 10.15
    p1.quantity = 3
    p1.total = round(p1.price * p1.quantity, 2)

    p2 = Produto()
    p2.name = 'Produto 2'
    p2.price = 9.87
    p2.quantity = 2
    p2.total = round(p2.price * p2.quantity, 2)

    total_amount = p1.total + p2.total
    round_up_donation = round(math.ceil(total_amount) - total_amount, 2)

    products = [p1, p2]

    
    return render_template('checkout.html', products=products, total_amount=total_amount, round_up_donation=round_up_donation)

@app.route('/confirm')
def confirm():
    return render_template('confirm.html')

@app.route('/confirm/rounded/<donation_value>')
def confirm_donation(donation_value):
    print('donation value is: ', donation_value)
    # implement LinkAPI logic
    return render_template('confirm-rounded.html')

@app.route('/dashboard')
def dashboard():
    donations = []

    for rec in recset:
        d1 = Donation()
        d1.date = rec[6].isoformat()[:10]
        d1.name = rec[1]
        d1.ngo = rec[5]
        d1.ecommerce = rec[4]
        d1.total = rec[2]
        donations.append(d1)

    return render_template('dashboard.html', donations=donations)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=environ.get("PORT", 5000))
