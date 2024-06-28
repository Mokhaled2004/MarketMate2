#!/usr/bin/python3
""" Starts a Flask Web Application """
import os
from flask import Flask, render_template, request, redirect, url_for, flash,session, jsonify    
from hashlib import md5
from models import storage
from models.user import User
from models.product import Product
from models.order   import Order
import json
from datetime import datetime, timedelta


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


from flask import session, jsonify, request

@app.route('/process_cart', methods=['POST'])
def process_cart():
    if request.method == 'POST':
        cart_data = request.json.get('cart')
        
        if cart_data:
            user_id = session.get('user_id')  # Retrieve the logged-in user ID from the session
            
            if not user_id:
                return jsonify({'error': 'User not logged in'}), 401

            for item in cart_data:
                # Extract product details from cart data
                title = item.get('title')
                image = item.get('image')
                price = item.get('price')

                # Check if the product with the same title and user ID already exists in storage
                existing_product = None
                for product in storage.all(Product).values():
                    if product.title == title and product.user_id == user_id:
                        existing_product = product
                        break
                
                if existing_product is None:
                    # Create Product object with quantity set to 1 and save to storage
                    new_product = Product(title=title, image=image, price=price, quantity=1, user_id=user_id)
                    storage.new(new_product)
                    storage.save()
                else:
                    # Increment the existing product's quantity by 1
                    existing_product.quantity += 1
                    existing_product.price = price * existing_product.quantity

                    storage.save()

            return jsonify({'message': 'Cart processed successfully'}), 200
        else:
            return jsonify({'error': 'No cart data received'}), 400
    else:
        return jsonify({'error': 'Method not allowed'}), 405


@app.route('/remove_item_by_title/<string:product_title>', methods=['DELETE'])
def remove_item_by_title(product_title):
    user_id = session.get('user_id')  # Assume you store user_id in the session

    if not user_id:
        return jsonify({'error': 'User not logged in'}), 401

    product_to_remove = None

    # Find the product in storage that matches the product_title and belongs to the logged-in user
    for product in storage.all(Product).values():
        if product.title == product_title and product.user_id == user_id:
            product_to_remove = product
            break

    if product_to_remove:
        if product_to_remove.quantity > 1:
            product_to_remove.quantity -=1 
            product_to_remove.price = product_to_remove.price * product_to_remove.quantity / (product_to_remove.quantity + 1)

        else:
            storage.delete(product_to_remove)

        storage.save()
        return jsonify({'message': 'Item removed successfully'}), 200
    else:
        return jsonify({'error': 'Product not found or does not belong to the user'}), 404


@app.route('/checkout', methods=['POST'])
def checkout():
    
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'error': 'User not logged in'}), 401

        # Fetch all products belonging to the user
        products = []
        total_price = 0.0

        all_products = storage.all(Product)  # Adjust according to your storage implementation
        for product in all_products.values():
            if product.user_id == user_id:
                products.append({
                    
                    'title': product.title,
                    'price': product.price,
                    'quantity': product.quantity  # Assuming quantity is already correct
                })
                total_price += product.price * product.quantity

                # Adjust product quantity in storage if needed
                # Note: This part depends on your storage implementation

        # Create a new Order object
        order = Order(
            user_id=user_id,
            products=products,
            total_price=total_price,
            created_at=datetime.now()
        )

        # Save the order to storage (assuming your storage handles SQLAlchemy sessions or file-based storage)
        storage.new(order)
        storage.save()

        return jsonify({'message': 'Order placed successfully'}), 200

  



@app.route('/logged')
def logged():
    return render_template('Logged Home Page HTML.html', title='Logged Home Page')




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


from flask import session
@app.route('/carttest')
def carttest():
    return render_template('Cart Test HTML.html', title='carttest')

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
            # Store user details in session
            session['user_id'] = user.id
            session['user_email'] = user.email
            session['user_first_name'] = user.first_name
            session['user_last_name'] = user.last_name
            session['user_address'] = user.address
            session['user_password'] = user.password
            flash('Logged in successfully!', 'success')
            return redirect(url_for('logged'))
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




@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        flash('Please log in to view your profile.', 'danger')
        return redirect(url_for('login'))

    if request.method == 'POST':
        user_id = session['user_id']
        user = storage.get(User, user_id)
        if user:
            user.first_name = request.form['first_name']
            user.last_name = request.form['last_name']
            user.email = request.form['email']
            if request.form['password']:
                user.password = md5(request.form['password'].encode()).hexdigest()
            user.address = request.form['address']
            storage.save()
            flash('Profile updated successfully!', 'success')
        else:
            flash('User not found.', 'danger')
    
    user_details = {
        'email': session.get('user_email'),
        'first_name': session.get('user_first_name'),
        'last_name': session.get('user_last_name'),
        'address': session.get('user_address'),
        'password': session.get('user_password'),
    }

    return render_template('Profile HTML.html', title='Profile', user=user_details)





@app.route('/wishlist')
def wishlist():
    return render_template('Wishlist HTML.html', title='Wish List')
@app.route('/cart')
def cart():
    return render_template('Shopping Cart HTML.html', title='Shopping Cart')

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