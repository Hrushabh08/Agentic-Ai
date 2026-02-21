# agents/conversational_agent.py

import re

medicine_db = {
    "bp": {"id": 1, "medicine_name": "Amlodipine", "dosage": "5mg"},
    "amlodipine": {"id": 1, "medicine_name": "Amlodipine", "dosage": "5mg"},
    "paracetamol": {"id": 2, "medicine_name": "Paracetamol", "dosage": "500mg"},
    "metformin": {"id": 3, "medicine_name": "Metformin", "dosage": "500mg"},
    "cough syrup": {"id": 4, "medicine_name": "Cough Syrup", "dosage": "100ml"},
    "azithromycin": {"id": 5, "medicine_name": "Azithromycin", "dosage": "250mg"},
    "vitamin c": {"id": 6, "medicine_name": "Vitamin C", "dosage": "500mg"}
}

def extract_order(user_message: str):

    user_message = user_message.lower()

    # Default order response
    order = {
        "medicine_id": None,
        "medicine_name": None,
        "dosage": None,
        "quantity": None,
        "status": "not_found"
    }

    # Extract quantity first
    quantity_match = re.search(r"\b(\d+)\b", user_message)
    quantity = int(quantity_match.group(1)) if quantity_match else 1

    # Detect medicine
    for key, value in medicine_db.items():
        if key in user_message:
            order["medicine_id"] = value["id"]
            order["medicine_name"] = value["medicine_name"]
            order["dosage"] = value["dosage"]
            order["quantity"] = quantity
            order["status"] = "found"
            break

    return order
