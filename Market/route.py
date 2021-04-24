@application.route('/')
@application.route('/home')
def home_page():
    return render_template('index.html')

@application.route('/market', methods = ['GET','POST'])
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)