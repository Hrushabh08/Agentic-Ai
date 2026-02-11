# run_pharmacy_agent.py

from agents.conversational_agent import extract_order
from agents.safety_agent import check_order
from agents.inventory_agent import update_inventory, check_refill_alerts

print("=== Welcome to Agentic Pharmacy ===\n")

# Step 1: Show low stock alerts
alerts = check_refill_alerts(threshold=10)
if alerts:
    print("⚠️ Low Stock Alerts:")
    for alert in alerts:
        print(f"- {alert['medicine_name']}: {alert['stock']} left")
else:
    print("No low stock alerts at the moment.")

print("\nYou can now place your orders. Type 'exit' to quit.\n")

# Step 2: Order loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye! 👋")
        break

    # Step 3: Extract order from input
    order = extract_order(user_input)

    # Step 4: Safety check
    result = check_order(order)

    if result["approved"]:
        # Step 5: Update inventory
        update_inventory(order)
        response = f"✅ Order approved: {order['quantity']} units of {order['medicine_name']} ({order['dosage']})"
    else:
        response = f"❌ Order rejected: {result['reason']}"

    # Step 6: Show any refill alerts
    alerts = check_refill_alerts(threshold=10)
    if alerts:
        response += "\n⚠️ Refill Alerts for low stock medicines:\n"
        for alert in alerts:
            response += f"- {alert['medicine_name']}: {alert['stock']} left\n"

    print("Pharmacy Agent:", response)
