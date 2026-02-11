# agents/inventory_agent.py
import csv

MEDICINES_CSV = "data/medicines.csv"

def update_inventory(order):
    """
    Subtract ordered quantity from stock in medicines.csv
    """
    medicines = []
    with open(MEDICINES_CSV, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["name"].lower() == order["medicine_name"].lower():
                row["stock"] = str(int(row["stock"]) - order["quantity"])
            medicines.append(row)

    # Write back updated stock
    with open(MEDICINES_CSV, "w", newline='', encoding="utf-8") as csvfile:
        fieldnames = ["medicine_id","name","dosage","unit","stock","prescription_required"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(medicines)

def check_refill_alerts(threshold=10):
    """
    Return list of medicines where stock <= threshold
    """
    low_stock = []
    with open(MEDICINES_CSV, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row["stock"]) <= threshold:
                low_stock.append({
                    "medicine_name": row["name"],
                    "stock": int(row["stock"])
                })
    return low_stock
