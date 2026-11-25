orders = []
for i in range(1,6):
    foods = input(f"Enter Order {i}: ")
    orders.append(foods)

print(f"Orders: {orders}")
a_order =  input("Enter additional order: ")
orders.append(a_order)
print("Updated List: ")
print(f"Orders: {orders}")

p_order = input("Enter priority order: ")
orders.insert(0,p_order)
print("Updated List: ")
print(f"Orders: {orders}")

searches = input("Search for an order: ")
if searches not in orders:
    print("Order not found")

print(f"No. of occurrences: {orders.count(searches)}")
print(f"First Index: {orders.count(searches)-1}")

cancel = input("Enter order to cancel: ")
if cancel not in orders:
    print("Order not found")

orders.remove(cancel)
print("Updated List: ")
print(f"Orders: {orders}")

print(f"Last Order Removed: {orders.pop()}\n\nFinal Order Report")
print(f"Orders: {sorted(orders)}")
print(f"Total Remaining Orders: {len(orders)-1}")