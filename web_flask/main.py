#!/usr/bin/python3
""" Starts a Flask Web Application """
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from hashlib import md5
from models import storage
from models.user import User
from models.product import Product
from models.order   import Order



app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

products = [
    {'id': 1, 'name': 'Apple', 'price': 30, 'image': '/images/images/apple.png'},
    {'id': 2, 'name': 'Chili', 'price': 20, 'image': '/images/images/chili.png'},
    # Add other products here
]

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if request.method == 'POST':
        product_id = request.form['product_id']
        user_id = request.form['user_id']  # Assuming you have user ID in the form data

        # Check if the product exists
        product = storage.get(Product, product_id)
        if product is None:
            flash('Product not found.', 'warning')
            return redirect(url_for('cart'))

        # Check if the user exists
        user = storage.get(User, user_id)
        if user is None:
            flash('User not found.', 'warning')
            return redirect(url_for('cart'))

        # Create a new order item
        new_order = Order(user_id=user_id, product_id=product_id, product_name=product.name, product_price=product.price)
        storage.new(new_order)
        storage.save()

        # Check if the order item was saved
        if storage.get(Order, new_order.id) is not None:
            print("Order saved successfully:", new_order)
        else:
            print("Failed to save order:", new_order)

        flash('Product added to cart successfully!', 'success')
        return redirect(url_for('cart'))
    return render_template('Shopping Cart HTML.html')



@app.route('/carttest')
def carttest():
    return render_template('Cart Test HTML.html', title='carttest')

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
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Hash the entered password
        hashed_password = md5(password.encode()).hexdigest()
        user = None
        for u in storage.all(User).values():
            if u.email == email and u.password == hashed_password:
                user = u
                break
        if user:
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials, please try again.', 'danger')
            return redirect(url_for('login'))
    return render_template('Login And Registration HTML.html')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        address = request.form.get('address', '')
        # Check if email already exists
        for u in storage.all(User).values():
            if u.email == email:
                flash('Email already exists. Please log in.', 'warning')
                return redirect(url_for('signup'))
        # Create a new user
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password, address=address)
        storage.new(new_user)
        storage.save()
        # Check if the user was saved
        if storage.get(User, new_user.id) is not None:
            print("User saved successfully:", new_user)
        else:
            print("Failed to save user:", new_user)
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('Login And Registration HTML.html')
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
@app.route('/fruits')
def fruits():
    return render_template('Fruits Category Page HTML.html', title='Fruits & Vegetables')
@app.route('/medicine')
def medicine():
    return render_template('Medicine Category Page HTML.html', title='Medicine')
@app.route('/babycare')
def babycare():
    return render_template('Baby Care Category Page HTML.html', title='Baby Care')
@app.route('/meat')
def meat():
    return render_template('Meat Category Page HTML.html', title='Meat')
@app.route('/bakery')
def bakery():
    return render_template('Bakery Category Page HTML.html', title='Bakery')
@app.route('/snacks')
def snacks():
    return render_template('Snacks Category Page HTML.html', title='Snacks')
@app.route('/dairy')
def dairy():
    return render_template('Dairy Category Page HTML.html', title='Dairy Products')
if __name__ == "__main__":
    """ Main Function """
    app.run(debug=True, port=5001)