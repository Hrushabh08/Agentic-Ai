# agents/safety_agent.py
import csv

# Load medicines from CSV
def load_medicine_data(file_path="data/medicines.csv"):
    medicines = {}
    with open(file_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Use 'name' column from your CSV
            medicines[row["name"].lower()] = {
                "stock": int(row["stock"]),
                "prescription_required": row["prescription_required"].lower() in ["true", "yes"]
            }
    return medicines

def check_order(order):
    medicines = load_medicine_data()
    med_name = order["medicine_name"].lower()

    if med_name not in medicines:
        return {
            "approved": False,
            "reason": "Medicine not found in inventory",
            "order": order
        }

    med_data = medicines[med_name]

    if med_data["stock"] < order["quantity"]:
        return {
            "approved": False,
            "reason": "Insufficient stock",
            "order": order
        }

    if med_data["prescription_required"]:
        return {
            "approved": False,
            "reason": "Prescription required",
            "order": order
        }

    return {
        "approved": True,
        "reason": "Stock available, prescription not required",
        "order": order
    }
