# agents/conversational_agent.py
def extract_order(user_message: str):
    user_message = user_message.lower()

    # Update this DB to match your CSV medicines
    medicine_db = {
        "bp": {"medicine_name": "Amlodipine", "dosage": "5mg"},
        "amlodipine": {"medicine_name": "Amlodipine", "dosage": "5mg"},
        "paracetamol": {"medicine_name": "Paracetamol", "dosage": "500mg"},
        "metformin": {"medicine_name": "Metformin", "dosage": "500mg"},
        "cough syrup": {"medicine_name": "Cough Syrup", "dosage": "100ml"},
        "azithromycin": {"medicine_name": "Azithromycin", "dosage": "250mg"},
        "vitamin c": {"medicine_name": "Vitamin C", "dosage": "500mg"}
    }

    order = {"medicine_name": "Unknown", "dosage": "Unknown", "quantity": 30}

    for key, value in medicine_db.items():
        if key in user_message:
            order["medicine_name"] = value["medicine_name"]
            order["dosage"] = value["dosage"]

            import re
            match = re.search(r"(\d+)\s*(tablet|strip|unit|capsule|pcs|ml)?", user_message)
            if match:
                order["quantity"] = int(match.group(1))
            else:
                order["quantity"] = 30
            break

    return order
