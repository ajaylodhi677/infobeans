class Customer:
    def __init__(self,customer_id,customer_name,city,purchase_amount):
        self.customer_id=customer_id
        self.customer_name=customer_name
        self.city=city
        self.purchase_amount=purchase_amount

    def display(customers):
        for customer in customers:
            print(customer.customer_id,customer.customer_name,customer.city,customer.purchase_amount)

    def by_city(customers,city):
        for customer in customers:
            if customer.city==city:
                print(customer.customer_id,customer.customer_name,customer.purchase_amount)

    def purchase_greater_than_10000(customers):
        for customer in customers:
            if customer.purchase_amount>10000:
                print(customer.customer_id,customer.customer_name,customer.purchase_amount)

    def highest_purchase(customers):
        high=customers[0]
        for customer in customers:
            if customer.purchase_amount>high.purchase_amount:
                high=customer
        print(high.customer_id,high.customer_name,high.purchase_amount)

    def total_sales(customers):
        total=0
        for customer in customers:
            total+=customer.purchase_amount
        print(total)

    def average_purchase(customers):
        total=0
        for customer in customers:
            total+=customer.purchase_amount
        average=total/len(customers)
        print(f"{average:.0f}")

    def search(customers,customer_id):
        for customer in customers:
            if customer.customer_id==customer_id:
                print(customer.customer_id,customer.customer_name,customer.city,customer.purchase_amount)
                return
        print("Customer not found")