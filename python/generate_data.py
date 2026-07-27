from faker import Faker
import pandas as pd
from pathlib import Path

#Initialize Faker
fake = Faker()

def generate_customers():
    NUM_CUSTOMERS = 20
# generate fake records for customers table
    customers = [{
        #'customer_id' : fake.unique.random_int(min=0, max=50),
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
    #print(df)

    #output
    output_dir = Path(__file__).resolve().parent.parent / "data" / "raw"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "customers.csv"
    df.to_csv(output_file, index=False)

    print(f"Generated {len(df)} customers")
    print(f"Saved to {output_file}")

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
    #print(df)

    #output
    output_dir = Path(__file__).resolve().parent.parent / "data" / "raw"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "categories.csv"
    df.to_csv(output_file, index=False)

    print(f"Generated {len(df)} categories")
    print(f"Saved to {output_file}")

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

        ("Dog squich toy", 8.99, 10),
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
    #print(df)

    #output
    output_dir = Path(__file__).resolve().parent.parent / "data" / "raw"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "products.csv"
    df.to_csv(output_file, index=False)

    print(f"Generated {len(df)} products")
    print(f"Saved to {output_file}")
    

if __name__ == "__main__":
    generate_customers()
    generate_categories()
    generate_products()