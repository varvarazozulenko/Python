from datetime import datetime
from sqlalchemy.orm import Session
from models import Base, engine, User, Product, Order

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with Session(engine) as session:
    user = User(name="Eero", is_admin=True, created_at=datetime.now())
    
    product1 = Product(name="Ноутбук", price=85000.0, description="ноут", created_by=user)
    product2 = Product(name="Мышка", price=3500.0, description="мышь", created_by=user)
    product3 = Product(name="Наушники", price=12000.0, description="беспроводные", created_by=user)
    
    order1 = Order(total_price=88500.0, user=user)
    order2 = Order(total_price=15500.0, user=user)
    
    order1.products.append(product1)
    order1.products.append(product2)
    
    order2.products.append(product2)
    order2.products.append(product3)
    
    session.add_all([user, product1, product2, product3, order1, order2])
    session.commit()
    print("se toimii tietokannassa!!")
    
#чтенние в обе стороны
    current_user = session.get(User, 1)
    print(f"Пользователь: {current_user.name}")
    
    for order in current_user.orders:
        print(f"Заказ {order.id} стоимостью {order.total_price} руб.")
        
        current_order = session.get(Order, 1)
    print(f"Заказ {current_order.id} пользователя: {current_order.user.name} (c ID: {current_order.user.id})")
    
    
    order_test = session.get(Order, 1)
    print(f"В заказе {order_test.id} лежат товары:")
    for prod in order_test.products:
        print(f"{prod.name} ({prod.price} руб.)")
        
    mouse_product = session.get(Product, 2)
    print(f"Товар '{mouse_product.name}' в заказах:")
    for order in mouse_product.orders:
        print(f"Заказ {order.id} (сумма заказа: {order.total_price} руб.)")
        
    