from flask import render_template, request, redirect, url_for
from .models import db, Account
import random

def register_routes(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            password = request.form['password']
            account_id = str(random.randint(100000000000, 999999999999))
            new_account = Account(account_id=account_id, first_name=first_name, last_name=last_name, email=email, password=password)
            db.session.add(new_account)
            db.session.commit()
            return redirect(url_for('login'))
        return render_template('signup.html')

    @app.route('/devlogin')
    def devlogin():
        return render_template('devlogin.html')

    @app.route('/producerlogin')
    def producerlogin():
        return render_template('producerlogin.html')

    @app.route('/producers')
    def producers():
        return render_template('producers.html')

    @app.route('/products')
    def products():
        return render_template('products.html')

    @app.route('/orders')
    def orders():
        return render_template('orders.html')