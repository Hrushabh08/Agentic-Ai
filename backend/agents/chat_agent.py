# agents/chat_agent.py
from agents.conversational_agent import extract_order
from agents.safety_agent import check_order
from agents.inventory_agent import update_inventory, check_refill_alerts

def chat_with_pharmacy(user_message):
    # Step 1: Extract order
    order = extract_order(user_message)
    
    # Step 2: Safety & policy check
    result = check_order(order)
    
    if result["approved"]:
        # Step 3: Update inventory
        update_inventory(order)
        response = f"✅ Order approved: {order['quantity']} units of {order['medicine_name']} ({order['dosage']})"
    else:
        response = f"❌ Order rejected: {result['reason']}"

    # Step 4: Check low stock alerts
    alerts = check_refill_alerts(threshold=10)
    if alerts:
        response += "\n⚠️ Refill Alerts for low stock medicines:\n"
        for alert in alerts:
            response += f"- {alert['medicine_name']}: {alert['stock']} left\n"

    return response
