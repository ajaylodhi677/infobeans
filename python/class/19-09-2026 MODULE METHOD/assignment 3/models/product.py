class Product:
    def __init__(self,product_id,product_name,price,quantity):
        self.product_id=product_id
        self.product_name=product_name
        self.price=price
        self.quantity=quantity

    def display(products):
        for product in products:
            print(product.product_id,product.product_name,product.price,product.quantity)

    def total_values(products):
        for product in products:
            total=product.price*product.quantity
            print(product.product_name,"=",total)

    def low_stock(products):
        for product in products:
            if product.quantity<10:
                print(product.product_name)

    def highest_price(products):
        high=products[0]
        for product in products:
            if product.price>high.price:
                high=product
        print(high.product_name,"=",high.price)

    def total_inventory_value(products):
        total=0
        for product in products:
            total+=product.price*product.quantity
        print(total)

    def search_product(products,product_id):
        for product in products:
            if product.product_id==product_id:
                print(product.product_id,product.product_name,product.price,product.quantity)
                return
        print("Product not found")