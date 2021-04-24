class Item(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(100), nullable = False, unique = True)
    barcode = db.Column(db.String(length=10), nullable = False, unique = True)
    price = db.Column(db.Integer())
    description = db.Column(db.String(length = 1024), nullable = False)
    
    def __repr__(self):
        return f'{self.name} - {self.price}'