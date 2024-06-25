#!/usr/bin/python3
""" Starts a Flask Web Application """
from models.__init__ import storage
from models.user import User
from hashlib import md5
from flask import Flask, render_template, request, redirect, url_for, session, flash

from models.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def home():
    return render_template('index.html', title='MarketMate')

@app.route('/aboutus')
def aboutus():
    return render_template('About Us HTML.html', title='About Us')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password = md5(password.encode()).hexdigest()
        
        # Fetching user by email
        users = storage.all(User)
        user = None
        for u in users.values():
            if u.email == email:
                user = u
                break

        if user and user.password == hashed_password:
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('Login And Registration HTML.html', title='Login')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        address = request.form['address']
        
        # Checking if user already exists
        users = storage.all(User)
        for u in users.values():
            if u.email == email:
                flash('Email already registered.', 'danger')
                return render_template('Login And Registration HTML.html', title='Sign Up')

        # Creating new user
        user = User(email=email, password=password, first_name=first_name, last_name=last_name, address=address)
        storage.new(user)
        storage.save()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('Login And Registration HTML.html', title='Sign Up')

# Other routes...

if __name__ == "__main__":
    app.run(debug=True, port=5001)
