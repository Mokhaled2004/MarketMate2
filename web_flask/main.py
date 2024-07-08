#!/usr/bin/python3
""" Starts a Flask Web Application """
from flask import Flask, render_template, request, redirect, url_for, flash,session, jsonify    
from hashlib import md5
from models import storage
from models.user import User
from models.product import Product
from models.order   import Order
from models.review import Review
from models.payment import Payment
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

#----------------------------Index Page (Home)-----------------------------------------------

@app.route('/')
def home():
    users = storage.all(User)  # Retrieve all users from storage
    total_ratings = 0
    for u in users.values():
        total_ratings   += u.rating
                             
    num_users = len(users)
    if num_users > 0:
        average_rating = total_ratings / num_users
        average_rating = round(average_rating, 1)
    else:
        average_rating = 0  # Handle case where there are no users or ratings
    return render_template('index.html', title='MarketMate', average_rating=average_rating)



#----------------------------Process-Payment-----------------------------------------------

@app.route('/process_payment', methods=['POST'])
def process_payment():
    if request.method == 'POST':
        user_id = session.get('user_id')
        if not user_id:
            flash('Please log in to complete payment.', 'danger')
            return redirect(url_for('login'))
        
        all_orders = storage.all(Order)
        latest_order = None

        # Find the latest order for the logged-in user
        for order in all_orders.values():
            if order.user_id == user_id:
                if latest_order is None or order.created_at > latest_order.created_at:
                    latest_order = order

        if not latest_order:
            return jsonify({'error': 'No orders found for the user'}), 404

        order_id = latest_order.id # Update status to 'Delivered'
        storage.save()  # Save the updated order

        card_number = request.form['card_number']
        card_name = request.form['card_name']
        expiry_month = request.form['expiry_month']
        expiry_year = request.form['expiry_year']
        cvv = request.form['cvv']
        payment_type = request.form['payment_type']

        # Create a new Payment object
        payment = Payment(
            order_id=order_id,
            user_id=user_id,
            card_number=card_number,
            card_name=card_name,
            expiry_month=expiry_month,
            expiry_year=expiry_year,
            cvv=cvv,
            payment_type=payment_type,
            
        )

        # Assuming storage handles file-based storage
        storage.new(payment)
        storage.save()

        flash('Payment processed successfully!', 'success')
        return redirect(url_for('track'))  # Redirect to track page 

    
    return redirect(url_for('home'))  # Redirect to home page if method is not POST
    
#----------------------------Update-Market-Name-----------------------------------------------
 
@app.route('/update_market_name', methods=['POST'])
def update_market_name():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'User not logged in'}), 401

    # Fetch all orders for the logged-in user
    all_orders = storage.all(Order)
    latest_order = None

    # Find the latest order for the logged-in user
    for order in all_orders.values():
        if order.user_id == user_id:
            if latest_order is None or order.created_at > latest_order.created_at:
                latest_order = order

    if not latest_order:
        return jsonify({'error': 'No orders found for the user'}), 404

    # Update the market_name, address, and date in the latest order
    latest_order.market_name = request.form.get('market_name')
    latest_order.address = request.form.get('address')
    latest_order.date = request.form.get('date')

    # Save the updated order to storage
    storage.save()

    return redirect(url_for('payment'))

#----------------------------Submit-Contact-Form-----------------------------------------------

@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    if 'user_id' not in session:
        flash('Please log in to submit the contact form.', 'danger')
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    subject = request.form['subject']
    message = request.form['message']
    
    # Create a new Review object
    new_review = Review(user_id=user_id, subject=subject, text=message)
    storage.new(new_review)
    storage.save()
    
    flash('Contact form submitted successfully!', 'success')
    return redirect(url_for('contactus'))

#----------------------------Feedback-----------------------------------------------

@app.route('/feedsubmit', methods=['POST'])
def feedsubmit():
    if 'user_id' not in session:
        flash('Please log in to submit feedback.', 'danger')
        return redirect(url_for('login'))

    user_id = session['user_id']
    rating = request.form.get('rating')

    if rating:
        try:
            rating = int(rating)
            if 1 <= rating <= 5:
                user = storage.get(User, user_id)
                if user:
                    user.rating = rating
                    storage.save()
                    flash('Feedback submitted successfully!', 'success')
                else:
                    flash('User not found.', 'danger')
            else:
                flash('Invalid rating value.', 'danger')
        except ValueError:
            flash('Invalid rating value.', 'danger')
    else:
        flash('Please select a rating.', 'danger')

    return redirect(url_for('feedbacksubmit'))


#----------------------------Mark-Delivered-----------------------------------------------

@app.route('/mark_delivered', methods=['PUT'])
def mark_latest_delivered():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'User not logged in'}), 401

    all_orders = storage.all(Order)
    latest_order = None

    # Find the latest order for the logged-in user
    for order in all_orders.values():
        if order.user_id == user_id:
            if latest_order is None or order.created_at > latest_order.created_at:
                latest_order = order

    if not latest_order:
        return jsonify({'error': 'No orders found for the user'}), 404

    latest_order.delivered = 'Delivered'  # Update status to 'Delivered'
    storage.save()  # Save the updated order

    return jsonify({'message': 'Latest order marked as Delivered'}), 200

#----------------------------Mark-Cancelled-----------------------------------------------

@app.route('/mark_cancelled', methods=['PUT'])
def mark_cancelled():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'User not logged in'}), 401

    all_orders = storage.all(Order)
    latest_order = None

    # Find the latest order for the logged-in user
    for order in all_orders.values():
        if order.user_id == user_id:
            if latest_order is None or order.created_at > latest_order.created_at:
                latest_order = order

    if not latest_order:
        return jsonify({'error': 'No orders found for the user'}), 404

    latest_order.delivered = 'Cancelled'  # Update status to 'Delivered'
    storage.save()  # Save the updated order

    return jsonify({'message': 'Latest order marked as Delivered'}), 200

#----------------------------Add to Cart -----------------------------------------------
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

#----------------------------Remove from Cart-----------------------------------------------

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

#----------------------------Checkout-----------------------------------------------

@app.route('/checkout', methods=['POST'])
def checkout():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'User not logged in'}), 401

    # Fetch all products belonging to the user
    products_to_delete = []
    products = []
    total_price = 0.0
    delivered = "not delivered"

    all_products = storage.all(Product)  
    for product in all_products.values():
        if product.user_id == user_id:
            products_to_delete.append(product)
            products.append({
                'title': product.title,
                'price': product.price,
                'quantity': product.quantity  
            })
            total_price += product.price 

    # Create a new Order object
    order = Order(
        delivered=delivered,
        user_id=user_id,
        products=products,
        total_price=total_price,
        created_at=datetime.now(),
        market_name= ""
    )

    # Save the order to file-based storage
    storage.new(order)
    storage.save()

    # Delete all products that belong to the user
    for product in products_to_delete:
        storage.delete(product)
    storage.save()
    return jsonify({'message': 'Order placed successfully'}), 200

#----------------------------Display Order Details-----------------------------------------------

@app.route('/order_details', methods=['GET'])
def order_details():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'User not logged in'}), 401

    # Fetch all orders for the logged-in user
    user_orders = []
    all_orders = storage.all(Order)
    for order in all_orders.values():
        if order.user_id == user_id and order.delivered == "not delivered":
            user_orders.append(order.to_dict())

    return jsonify(user_orders), 200

#----------------------------Login-----------------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Hash the entered password
        hashed_password = md5(password.encode()).hexdigest()
        user = None
        for u in storage.all(User).values():
            if u.email == email or u.password == hashed_password  :
                user = u
                break
        if user:
            
            session['user_id'] = user.id
            session['user_email'] = user.email
            session['user_first_name'] = user.first_name
            session['user_last_name'] = user.last_name
            session['user_address'] = user.address
            session['user_password'] = user.password
            session['user_photo'] = user.photo
            flash('Logged in successfully!', 'success')
            return redirect(url_for('logged'))
        else:
            flash('Invalid credentials, please try again.', 'danger')
            return redirect(url_for('login'))
    return render_template('Login And Registration HTML.html')

#----------------------------Sign-up-----------------------------------------------

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        address = request.form.get('address', '')
        phone = request.form.get('phone')  
        # Check if email already exists
        for u in storage.all(User).values():
            if u.email == email:
                flash('Email already exists. Please log in.', 'warning')
                return redirect(url_for('signup'))
        # Create a new user
        hashed_password = md5(password.encode()).hexdigest()
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password, address=address, phone=phone,rating = 0)
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

#----------------------------View Profile-----------------------------------------------

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
            user.photo = request.form['photo']
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
        'photo': session.get('user_photo')
    }

    

    return render_template('Profile HTML.html', title='Profile', user=user_details)

#----------------------------Order-History-----------------------------------------------

@app.route('/fetch_order_history', methods=['GET'])
def fetch_order_history():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'User not logged in'}), 401

    # Fetch all orders for the logged-in user
    user_orders = []
    all_orders = storage.all(Order)
    for order in all_orders.values():
        if order.user_id == user_id:
            user_orders.append(order.to_dict())

    return jsonify(user_orders)




#----------------------------Filter Order History-----------------------------------------------

@app.route('/fetch_filtered_orders', methods=['GET'])
def fetch_filtered_orders():
    filter_type = request.args.get('filter', 'all')
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'error': 'User not logged in'}), 401

    if filter_type == 'all':
        # Fetch all orders for the logged-in user
        user_orders = [order.to_dict() for order in storage.all(Order).values() if order.user_id == user_id]
        filtered_orders = user_orders
    elif filter_type == 'delivered':
        user_orders = [order.to_dict() for order in storage.all(Order).values() if order.user_id == user_id and order.delivered == 'Delivered']
        filtered_orders = user_orders
    elif filter_type == 'cancelled':
        user_orders = [order.to_dict() for order in storage.all(Order).values() if order.user_id == user_id and order.delivered == 'Cancelled']
        filtered_orders = user_orders
    elif filter_type == 'not-delivered':
        user_orders = [order.to_dict() for order in storage.all(Order).values() if order.user_id == user_id and order.delivered == 'not delivered']
        filtered_orders = user_orders
    else:
        return jsonify({'error': 'Invalid filter type'}), 400

    return jsonify(filtered_orders)

#----------------------------Carttest page (BIM Store)-----------------------------------------------

@app.route('/carttest')
def carttest():
    if 'user_id' not in session:
        flash('Please log in to view your profile.', 'danger')
        return redirect(url_for('login'))

    user_id = session['user_id']
    user = storage.get(User,user_id)
    if not user:
        flash('User not found.', 'danger')
        return redirect(url_for('login'))

    first_name = user.first_name
    if user.photo and user.photo != "None":
            photo_url = user.photo 
   
    else:
            photo_url = "https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o="
    return render_template('Cart Test HTML.html', title='carttest',first_name=first_name, photo_url=photo_url)

#----------------------------Check-out Detals Page-----------------------------------------------

@app.route('/checkoutdetails')
def checkoutdetails():
    return render_template('Details For Checkout HTML.html', title='Checkout Details')

#----------------------------Track Order Page-----------------------------------------------

@app.route('/track')
def track():
    return render_template('track.html', title='track order')

#----------------------------Contact Confirm Page-----------------------------------------------

@app.route('/Contact Form Confirm HTML and CSS')
def Contact():
    return render_template('Contact Form Confirm HTML and CSS.html', title='Contact Form Confirm HTML and CSS')

#----------------------------About-Us Page-----------------------------------------------

@app.route('/aboutus')
def aboutus():
    if 'user_id' not in session:
        flash('Please log in to view your profile.', 'danger')
        return redirect(url_for('login'))

    user_id = session['user_id']
    user = storage.get(User,user_id)
    if not user:
        flash('User not found.', 'danger')
        return redirect(url_for('login'))

    first_name = user.first_name
    if user.photo and user.photo != "None":
            photo_url = user.photo  
   
    else:
            photo_url = "https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o="
    return render_template('About Us HTML.html', title='About Us',first_name=first_name, photo_url=photo_url)

#----------------------------Contact Form Page-----------------------------------------------

@app.route('/contactus')
def contactus():
    if 'user_id' not in session:
        flash('Please log in to view your profile.', 'danger')
        return redirect(url_for('login'))

    user_id = session['user_id']
    user = storage.get(User,user_id)
    if not user:
        flash('User not found.', 'danger')
        return redirect(url_for('login'))

    first_name = user.first_name
    if user.photo and user.photo != "None":
            photo_url = user.photo 
   
    else:
            photo_url = "https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o="
    return render_template('Contact Form HTML.html', title='Contact Us',first_name=first_name, photo_url=photo_url)

#----------------------------Feedback Page-----------------------------------------------

@app.route('/feedback')
def feedback():
    return render_template('Feedback Form HTML.html', title='FeedBack')

#----------------------------Feedback Submit Page-----------------------------------------------

@app.route('/feedbacksubmit')
def feedbacksubmit():
    return render_template('Feedback Form Confirm HTML and CSS.html', title='FeedBack')

#----------------------------Orders History Page-----------------------------------------------

@app.route('/history')
def history():
    if 'user_id' not in session:
        flash('Please log in to view your profile.', 'danger')
        return redirect(url_for('login'))

    user_id = session['user_id']
    user = storage.get(User,user_id)
    if not user:
        flash('User not found.', 'danger')
        return redirect(url_for('login'))

    first_name = user.first_name
    if user.photo and user.photo != "None":
            photo_url = user.photo 
   
    else:
            photo_url = "https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o="
    return render_template('History HTML.html', title='History',first_name=first_name, photo_url=photo_url)

#----------------------------Payment Page---------------------------------------------------

@app.route('/payment')
def payment():
    return render_template('Payment HTML.html', title='Payment')

#----------------------------Payment Confirmation Page-----------------------------------------------

@app.route('/paymentconfirm')
def paymentconfirm():
    return render_template('Payment Confirmation HTML and CSS.html', title='Payment Confirmation')

#----------------------------Raya Page (RAYA Store)-----------------------------------------------

@app.route('/raya')
def raya():
    if 'user_id' not in session:
        flash('Please log in to view your profile.', 'danger')
        return redirect(url_for('login'))

    user_id = session['user_id']
    user = storage.get(User,user_id)
    if not user:
        flash('User not found.', 'danger')
        return redirect(url_for('login'))

    first_name = user.first_name
    if user.photo and user.photo != "None":
            photo_url = user.photo  
   
    else:
            photo_url = "https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o="
    return render_template('RAYA HTML.html', title='Raya Store',first_name=first_name, photo_url=photo_url)

#----------------------------Ragab-Sons Page (RAGAB-SONS Store)-----------------------------------------------

@app.route('/ragabsons')
def ragabsons():
    if 'user_id' not in session:
        flash('Please log in to view your profile.', 'danger')
        return redirect(url_for('login'))

    user_id = session['user_id']
    user = storage.get(User,user_id)
    if not user:
        flash('User not found.', 'danger')
        return redirect(url_for('login'))

    first_name = user.first_name
    if user.photo and user.photo != "None":
            photo_url = user.photo 
   
    else:
            photo_url = "https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o="
    return render_template('WELADRAGAB HTML.html', title='Ragab sons Store',first_name=first_name, photo_url=photo_url)

#----------------------------Walmart Page (WALMART Store)-----------------------------------------------

@app.route('/walmart')
def walmart():
    if 'user_id' not in session:
        flash('Please log in to view your profile.', 'danger')
        return redirect(url_for('login'))

    user_id = session['user_id']
    user = storage.get(User,user_id)
    if not user:
        flash('User not found.', 'danger')
        return redirect(url_for('login'))

    first_name = user.first_name
    if user.photo and user.photo != "None":
            photo_url = user.photo 
   
    else:
            
            photo_url = "https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o="

    return render_template('WALMART HTML.html', title='Walmart Store',first_name=first_name, photo_url=photo_url)

#----------------------------SEOUDI Page (SEOUDI Store)-----------------------------------------------

@app.route('/seoudi')
def seoudi():
    if 'user_id' not in session:
        flash('Please log in to view your profile.', 'danger')
        return redirect(url_for('login'))

    user_id = session['user_id']
    user = storage.get(User,user_id)
    if not user:
        flash('User not found.', 'danger')
        return redirect(url_for('login'))

    first_name = user.first_name
    if user.photo and user.photo != "None":
            photo_url = user.photo  
   
    else:
            photo_url = "https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o="
    return render_template('SEOUDI HTML.html', title='Seoudi Store',first_name=first_name, photo_url=photo_url)

#----------------------------Logged Home Page-----------------------------------------------

@app.route('/logged')
def logged():
    if 'user_id' not in session:
        flash('Please log in to view your profile.', 'danger')
        return redirect(url_for('login'))

    user_id = session['user_id']
    user = storage.get(User,user_id)
    if not user:
        flash('User not found.', 'danger')
        return redirect(url_for('login'))

    first_name = user.first_name
    if user.photo and user.photo != "None":
            photo_url = user.photo  
   
    else:
            photo_url = "https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o="


    users = storage.all(User)  # Retrieve all users from storage
    total_ratings = 0
    count_positive_ratings = 0

    for u in users.values():
        if u.rating > 0:
            total_ratings += u.rating
            count_positive_ratings += 1
                             
    #num_users = len(users)
    if count_positive_ratings > 0:
        average_rating = total_ratings / count_positive_ratings
        average_rating = round(average_rating, 1)
    else:
        average_rating = 0  # Handle case where there are no users or ratings
    return render_template('Logged Home Page HTML.html', title='Logged Home Page', first_name=first_name, photo_url=photo_url, average_rating=average_rating)

#----------------------------Main-----------------------------------------------

if __name__ == "__main__":
    """ Main Function """
    app.run(debug=True, port=5001)