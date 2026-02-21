# agents/safety_agent.py

import csv

def load_medicine_data(file_path="backend/data/medicines.csv"):
    medicines = {}

    with open(file_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            medicines[int(row["id"])] = {
                "name": row["name"],
                "stock": int(row["stock"]),
                "prescription_required": row["prescription_required"].lower() in ["true", "yes"]
            }

    return medicines


def check_order(order):

    medicines = load_medicine_data()

    med_id = order.get("medicine_id")

    if med_id is None:
        return {
            "approved": False,
            "reason": "Medicine not recognized",
            "order": order
        }

    if med_id not in medicines:
        return {
            "approved": False,
            "reason": "Medicine not found in inventory",
            "order": order
        }

    med_data = medicines[med_id]

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
        "reason": "Stock available",
        "order": order
    }
       