from ..config import db

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurantpizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))

    restaurant = db.relationship('Restaurant', back_populates='restaurantpizzas')
    pizza = db.relationship('Pizza', back_populates='restaurantpizzas')

    def __repr__(self):
        return f"<RestaurantPizza {self.price}>"
    
    @db.validates('price')
    def validate_price(self, key, price):
        if not 1 <= price <= 30:
            raise ValueError ("price must be between 1 and 30")
        return price