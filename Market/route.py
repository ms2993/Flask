from Market import application
from flask import render_template,redirect, url_for,flash
from Market.models import Item,User
from Market.forms import Registrationform
from Market import db
@application.route('/')
@application.route('/home')
def home_page():
    return render_template('index.html')

@application.route('/market', methods = ['GET','POST'])
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@application.route('/register', methods = ["GET", "POST"])
def register_page():
    form = Registrationform()
    print(form.password1.data)
    print(form.password2.data)
    print(form.errors)
    if form.is_submitted():
        print("submitted")

    if form.validate():
        print("valid")
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print('--test 0 --')
        user_to_create = User(username=form.username.data,
                              email=form.email.data,
                              password=form.password1.data)
        print('--test1--')
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:
        print('hello')
        for err in form.errors.values():
            flash(f'error in creating user: {err}', category='danger')
    return render_template('register.html',form =form)