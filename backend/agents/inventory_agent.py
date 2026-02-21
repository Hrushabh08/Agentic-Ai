import json

def update_inventory(order):
    with open("inventory.json", "r") as file:
        inventory = json.load(file)

    for item in inventory:
        if item["medicine_id"] == order["medicine_id"]:
            item["stock"] -= order["quantity"]

    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)


def check_refill_alerts(threshold=10):
    with open("inventory.json", "r") as file:
        inventory = json.load(file)

    alerts = []
    for item in inventory:
        if item["stock"] <= threshold:
            alerts.append(item)

    return alerts
