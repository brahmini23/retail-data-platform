from faker import Faker
from pathlib import Path
import pandas as pd
import utils
import random as rd

output_dir = Path(__file__).resolve().parent.parent / "data" / "raw"
NUM_CUSTOMERS = 20
NUM_ORDERS = 100
NUM_ORDER_ITEMS = 300
ORDER_STATUSES = [
    "Pending",
    "Processing",
    "Shipped",
    "Delivered",
    "Cancelled"
]

#Initialize Faker
fake = Faker()

def generate_customers():
    # generate fake records for customers table
    customers = [{
        'customer_id' : i,
        'first_name' : fake.first_name(),
        'last_name' : fake.last_name(),
        'email' : fake.unique.email(),
        'city' : fake.city(),
        'state' : fake.state(),
        'signup_date' : fake.date_time_this_decade()
    } for i in range(1, NUM_CUSTOMERS + 1) ]

    # Load into a Pandas DataFrame
    df = pd.DataFrame(customers)
    utils.save_csv(df, "customers.csv")
    #print(df)

    #output
    # output_dir = Path(__file__).resolve().parent.parent / "data" / "raw"
    # output_dir.mkdir(parents=True, exist_ok=True)

    # output_file = output_dir / "customers.csv"
    # df.to_csv(output_file, index=False)

    # print(f"Generated {len(df)} customers")
    # print(f"Saved to {output_file}")

def generate_categories():
    #generate records for categories table
    categories = [
        {"category_id": 1, "category_name": "Electronics"},
        {"category_id": 2, "category_name": "Clothing"},
        {"category_id": 3, "category_name": "Home & Kitchen"},
        {"category_id": 4, "category_name": "Books"},
        {"category_id": 5, "category_name": "Sports & Outdoors"},
        {"category_id": 6, "category_name": "Beauty & Personal Care"},
        {"category_id": 7, "category_name": "Toys & Games"},
        {"category_id": 8, "category_name": "Grocery"},
        {"category_id": 9, "category_name": "Office Supplies"},
        {"category_id": 10, "category_name": "Pet Supplies"},
    ]

    # Load into a Pandas DataFrame
    df = pd.DataFrame(categories)
    utils.save_csv(df, "categories.csv")

def generate_products():
    #generate records for products tables
    products = [
        ("Wireless Mouse", 29.99, 1),
        ("Mechanical Keyboard", 89.99, 1),
        ("Gaming Monitor", 299.99, 1),
        ("Bluetooth Speaker", 49.99, 1),
        ("USB-C Hub", 39.99, 1),

        ("Women Summer Dress", 39.99, 2),
        ("Women Spring Top", 19.99, 2),
        ("Kids Back to School Top", 9.99, 2),

        ("Running Shoes", 79.99, 5),
        ("Yoga Mat", 24.99, 5),
        ("Dumbbells", 59.99, 5),

        ("Cookware Set", 149.99, 3),
        ("Coffee Maker", 89.99, 3),

        ("Atomic Habits", 10.00, 4),
        ("Life of Pi", 7.99, 4),

        ("Maybelline Foundation", 15.99, 6),
        ("Mac Ruby Lipstick", 55.00, 6),

        ("Lettuce", 3.99, 8),
        ("Organic Spinach", 5.99, 8),

        ("3inch Binder", 5.99, 9),

        ("Flower Lego Set", 13.99, 7),
        ("Barbie Holiday Doll", 50.99, 7),

        ("Dog Squeaky Toy", 8.99, 10),
    ]

    product_records = []

    for i, (name, price, category_id) in enumerate(products, start=1):
        product_records.append({
            "product_id": i,
            "category_id": category_id,
            "product_name": name,
            "price": price
        } )
    
    # Load into a Pandas DataFrame
    df = pd.DataFrame(product_records)
    utils.save_csv(df, "products.csv")

def generate_orders():
    # generate fake records for orders table
    orders = [{
        'order_id' : i,
        'customer_id' : rd.randint(1, NUM_CUSTOMERS),
        'order_date' : fake.date_time_between(start_date="-3y", end_date="now"),
        'status' : rd.choice(ORDER_STATUSES)
    } for i in range(1, NUM_ORDERS + 1)]

    # Load into a Pandas DataFrame
    df = pd.DataFrame(orders)
    utils.save_csv(df, "orders.csv")

def generate_order_items():
    # generate fake order item transactions
    products_df = pd.read_csv(output_dir / "products.csv")
    orders_df = pd.read_csv(output_dir / "orders.csv")
    order_items = []
    order_item_id = 1
    #for every order - choose between 1 and 5 products & for each product - create one order_item row
    for _, order in orders_df.iterrows():
            num_products = rd.randint(1,5)
            selected_product = products_df.sample(num_products)

            for _, product in selected_product.iterrows():
                order_items.append({
                    'order_item_id' : order_item_id,
                    'order_id' : order["order_id"],
                    'product_id' : product["product_id"],
                    'quantity' : rd.randint(1,5),
                    'unit_price' : product["price"]
                })
                order_item_id += 1
     # Load into a Pandas DataFrame
    df = pd.DataFrame(order_items)
    utils.save_csv(df, "order_items.csv")

#data validation logic
    order_items_df = pd.read_csv(output_dir / "order_items.csv")

    print("Number of order items:", len(order_items_df))
    print("Unique order items:", order_items_df["order_item_id"].nunique())
    print("Unique orders:", order_items_df["order_id"].nunique())
    print("Duplicate order items:", order_items_df["order_item_id"].duplicated().sum())

    valid_products = set(products_df["product_id"])

    invalid_products = set(order_items_df["product_id"]) - valid_products

    print("Invalid product IDs:", invalid_products)

if __name__ == "__main__":
    generate_customers()
    generate_categories()
    generate_products()
    generate_orders()
    generate_order_items()