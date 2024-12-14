import os
import django
import numpy

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Replace with your project settings module
django.setup()
import pandas as pd
from sales_management.models import Invoice

# Path to your CSV file
CSV_FILE_PATH = "E:/MyWork/LanmarkGroupTask/export_2019.csv"


def preprocess_data(file_path):
    """Read and preprocess the CSV data using Pandas."""
    # Load the CSV into a Pandas DataFrame
    df = pd.read_csv(file_path)
    
    
    # Parse the date column
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d", errors="coerce")
    
    # Remove commas and convert numeric fields
    numeric_fields = [
        "Bottle Volume (ml)", "State Bottle Cost", "State Bottle Retail",
        "Bottles Sold", "Sale (Dollars)", "Volume Sold (Liters)", "Volume Sold (Gallons)"
    ]
    for field in numeric_fields:
        df[field] = (
            df[field]
            .astype(str)  # Ensure all values are strings for replacement
            .str.replace(",", "", regex=False)  # Remove commas
            .replace("nan", None)  # Replace 'nan' (string) with None
            .astype(float)  # Convert to float
        )
    df.dropna(inplace=True)
    # Fill NaN with None to handle nulls in Django
    df = df.where(pd.notnull(df), None)
    
    return df


def import_invoices(file_path):
    """Import invoices into the database using bulk_create."""
    # Preprocess the data
    df = preprocess_data(file_path)
    
    # Map DataFrame columns to model fields
    records = df.to_dict(orient="records")
    
    # Convert dictionaries to model instances
    invoices = [
        Invoice(
            invoice_number=record["Invoice/Item Number"],
            date=record["Date"],
            store_number=record["Store Number"],
            store_name=record["store_name"],
            address=record["Address"],
            city=record["City"],
            zip_code=record["Zip Code"],
            store_location=record["Store Location"],
            county_number=record["County Number"],
            county=record["County"],
            category=record["Category"],
            category_name=record["category_name"],
            vendor_number=record["Vendor Number"],
            vendor_name=record["vendor_name"],
            item_number=record["Item Number"],
            item_desc=record["item_desc"],
            pack=record["Pack"],
            bottle_volume_ml=record["Bottle Volume (ml)"],
            state_bottle_cost=record["State Bottle Cost"],
            state_bottle_retail=record["State Bottle Retail"],
            bottles_sold=record["Bottles Sold"],
            sale_dollars=record["Sale (Dollars)"],
            volume_sold_liters=record["Volume Sold (Liters)"],
            volume_sold_gallons=record["Volume Sold (Gallons)"],
        )
        for record in records
    ]
    
    # Bulk create invoices
    Invoice.objects.bulk_create(invoices, batch_size=1000)
    print(f"Successfully imported {len(invoices)} invoices!")


if __name__ == "__main__":
    import_invoices(CSV_FILE_PATH)
