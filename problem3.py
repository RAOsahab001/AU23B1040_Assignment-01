def process_orders(order_queue):
    print("Preparing orders:")
    for i, order in enumerate(order_queue, start=1):
        print(f"Preparing Your Order -" ,order)
    print("\nThe following orders have been dispatched:")
    for order in order_queue:
        print(order)

# Get orders from the user
def get_orders():
    order_queue = []
    while True:
        order = input("Enter the name of the order from menu: ")
        if order.lower() == "bss etna hi":
            break
        order_queue.append(order)
    return order_queue

if __name__ == "__main__":
    orders = get_orders()
    process_orders(orders)
