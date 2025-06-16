from server.app import app
from server.config import db
from server.models import Restaurant, Pizza, RestaurantPizza

with app.app_context():
    db.drop_all()
    db.create_all()

    restaurant1 = Restaurant()
    setattr(restaurant1, "name", "Pizza Place")
    setattr(restaurant1, "address", "Tom Mboya St")
    restaurant2 = Restaurant()
    setattr(restaurant2, "name", "Pasta Place")
    setattr(restaurant2, "address", "Kenyatta Ave")
    restaurant3 = Restaurant()
    setattr(restaurant3, "name", "Salad Place")
    setattr(restaurant3, "address", "Westalands")
    db.session.add_all([restaurant1, restaurant2, restaurant3])
    db.session.commit()


    pizza1 = Pizza()
    setattr(pizza1, "name", "Margherita")
    setattr(pizza1, "ingredients", "Tomato, Mozzarella, Basil")
    pizza2 = Pizza()
    setattr(pizza2, "name", "Pepperoni")
    setattr(pizza2, "ingredients", "Tomato, Mozzarella, Pepperoni")
    pizza3 = Pizza()
    setattr(pizza3, "name", "Vegetarian")
    setattr(pizza3, "ingredients", "Tomato, Mozzarella, Peppers, Onions, Olives")
    db.session.add_all([pizza1, pizza2, pizza3])
    db.session.commit()

    restaurant_pizza1 = RestaurantPizza()
    setattr(restaurant_pizza1, "price", 10)
    setattr(restaurant_pizza1, "restaurant_id", restaurant1.id)
    setattr(restaurant_pizza1, "pizza_id", pizza1.id)
    restaurant_pizza2 = RestaurantPizza()
    setattr(restaurant_pizza2, "price", 12)
    setattr(restaurant_pizza2, "restaurant_id", restaurant3.id)
    setattr(restaurant_pizza2, "pizza_id", pizza2.id)
    restaurant_pizza3 = RestaurantPizza()
    setattr(restaurant_pizza3, "price", 8)
    setattr(restaurant_pizza3, "restaurant_id", restaurant2.id)
    setattr(restaurant_pizza3, "pizza_id", pizza3.id)
    db.session.add_all([restaurant_pizza1, restaurant_pizza2, restaurant_pizza3])
    db.session.commit()

    print("Database seeded successfully!")