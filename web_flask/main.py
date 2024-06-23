#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask , render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', title='MarketMate')

@app.route('/aboutus')
def aboutus():
    return render_template('About Us HTML.html', title='About Us')

@app.route('/contactus')
def contactus():
    return render_template('Contact Form HTML.html', title='Contact Us')

@app.route('/feedback')
def feedback():
    return render_template('Feedback Form HTML.html', title='FeedBack')

@app.route('/feedbacksubmit')
def feedbacksubmit():
    return render_template('Feedback Form Confirm HTML and CSS.html', title='FeedBack')



@app.route('/login')
def login():
    return render_template('Login And Registration HTML.html', title='Login')

@app.route('/signup')
def signup():
    return render_template('Login And Registration HTML.html', title='About Us')

@app.route('/wishlist')
def wishlist():
    return render_template('Wishlist HTML.html', title='Wish List')

@app.route('/cart')
def cart():
    return render_template('Shopping Cart HTML.html', title='Shopping Cart')

@app.route('/profile')
def profile():
    return render_template('Profile HTML.html', title='Profile')


@app.route('/checkoutdetails')
def checkoutdetails():
    return render_template('Details For Checkout HTML.html', title='Checkout Details')

@app.route('/payment')
def payment():
    return render_template('Payment HTML.html', title='Payment')

@app.route('/paymentconfirm')
def paymentconfirm():
    return render_template('Payment Confirmation HTML and CSS.html', title='Payment Confirmation')







if __name__ == "__main__":
    """ Main Function """
    app.run(debug=True, port=5001)