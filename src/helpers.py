def serve_dish(dish, customer):
    customer.set_credit(customer.get_credit() - dish.get_menu_price())

