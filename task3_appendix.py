
from collections import defaultdict, Counter

# Student-specific inputs
LAST_NAME = "LANCION"
SEED_NUM = 7
FAVORITE_ARTIST = "CUP OF JOE"

# Customers
customers = [f"{LAST_NAME}_C{i}" for i in range(1, 6)]

# Products and fixed prices
prices = {
    "NOTEBOOK": 35,
    "PEN": 10,
    "USB": 250,
    "HEADPHONES": 500,
    "CALCULATOR": 300
}

products = list(prices.keys())

# Generate transaction records
transactions = []

for i, customer in enumerate(customers):
    for j, product in enumerate(products):
        char_position = ord(
            FAVORITE_ARTIST[(i + j) % len(FAVORITE_ARTIST)]
        )

        quantity = 1 + (
            char_position + SEED_NUM + i + j
        ) % 5

        transactions.append({
            "customer": customer,
            "product": product,
            "quantity": quantity,
            "price": prices[product],
            "total": quantity * prices[product]
        })

# Add one repeated customer-product purchase
transactions.append(transactions[0].copy())

# Organize transactions by customer and product
organized = defaultdict(lambda: defaultdict(int))

for t in transactions:
    organized[t["customer"]][t["product"]] += t["quantity"]

# Identify repeated customer-product purchases
purchase_counts = Counter(
    (t["customer"], t["product"]) for t in transactions
)

repeated = {
    key: count for key, count in purchase_counts.items()
    if count > 1
}

# Calculate overall transaction value
overall_total = sum(t["total"] for t in transactions)
total_quantity = sum(t["quantity"] for t in transactions)

print("=" * 65)
print("TRANSACTION HISTORY ANALYZER")
print("=" * 65)

# 1. Generated transaction records
print("\n1. GENERATED TRANSACTION RECORDS")

for t in transactions:
    print(
        f"{t['customer']:15} | {t['product']:12} | "
        f"Qty: {t['quantity']} | Price: P{t['price']} | "
        f"Total: P{t['total']}"
    )

# 2. Distinct customers and products
print("\n2. DISTINCT CUSTOMERS AND PRODUCTS")
print("Number of distinct customers:", len(set(t["customer"] for t in transactions)))
print("Number of distinct products:", len(set(t["product"] for t in transactions)))
print("Customers:", ", ".join(customers))
print("Products:", ", ".join(products))

# 3. Repeated purchases
print("\n3. REPEATED CUSTOMER-PRODUCT PURCHASES")

for (customer, product), count in repeated.items():
    print(f"{customer} - {product}: {count} transactions")

# 4. Customer summaries
print("\n4. CUSTOMER SUMMARY")

customer_totals = defaultdict(int)
customer_quantities = defaultdict(int)

for t in transactions:
    customer_totals[t["customer"]] += t["total"]
    customer_quantities[t["customer"]] += t["quantity"]

for customer in customers:
    print(
        f"{customer}: Total Spent = P{customer_totals[customer]}, "
        f"Items Purchased = {customer_quantities[customer]}"
    )

# 5. Product summaries
print("\n5. PRODUCT SUMMARY")

product_totals = defaultdict(int)
product_quantities = defaultdict(int)

for t in transactions:
    product_totals[t["product"]] += t["total"]
    product_quantities[t["product"]] += t["quantity"]

for product in products:
    print(
        f"{product}: Quantity Sold = {product_quantities[product]}, "
        f"Sales = P{product_totals[product]}"
    )

# 6. Ordered transactions: highest value first
print("\n6. ORDERED TRANSACTIONS (HIGHEST VALUE FIRST)")

ordered = sorted(
    transactions,
    key=lambda t: t["total"],
    reverse=True
)

for t in ordered:
    print(
        f"{t['customer']:15} | {t['product']:12} | "
        f"Qty: {t['quantity']} | Total: P{t['total']}"
    )

# 7. Overall transaction summary
print("\n7. OVERALL TRANSACTION SUMMARY")
print("Total transaction records:", len(transactions))
print("Total quantity sold:", total_quantity)
print(f"Overall sales: P{overall_total}")
print("Repeated customer-product combinations:", len(repeated))

print("\nREPORT COMPLETE")

# 7. TRANSACTION VALUES
print("\n7. TRANSACTION VALUES")

for t in transactions:
    print(
        f"{t['customer']} - {t['product']}: "
        f"{t['quantity']} x P{t['price']} = P{t['total']}"
    )

# 8. FINAL CONSOLIDATED TRANSACTION REPORT
print("\n" + "=" * 50)
print("FINAL CONSOLIDATED TRANSACTION REPORT")
print("=" * 50)

print("Total Transaction Records:", len(transactions))
print("Distinct Customers:", len(set(t["customer"] for t in transactions)))
print("Distinct Products:", len(set(t["product"] for t in transactions)))
print("Total Quantity Sold:", total_quantity)
print(f"Overall Transaction Value: P{overall_total:,.2f}")

print("\nCUSTOMER TOTALS")
for customer in customers:
    print(f"{customer}: P{customer_totals[customer]:,.2f}")

print("\nPRODUCT SALES")
for product in products:
    print(f"{product}: P{product_totals[product]:,.2f}")

print("\nREPEATED PURCHASES")
for (customer, product), count in repeated.items():
    print(f"{customer} - {product}: {count} purchases")

print("\nEND OF FINAL REPORT")
