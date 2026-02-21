# backend/agents/chat_agent.py

from agents.conversational_agent import extract_order
from agents.safety_agent import check_order
from agents.inventory_agent import update_inventory, check_refill_alerts

def chat_with_pharmacy(user_message):

    order = extract_order(user_message)

    if order["medicine_id"] is None:
        return "❌ Medicine not recognized. Please try again."

    result = check_order(order)

    if result["approved"]:
        update_inventory(order)
        response = f"✅ Order approved: {order['quantity']} units of {order['medicine_name']} ({order['dosage']})"
    else:
        response = f"❌ Order rejected: {result['reason']}"

    alerts = check_refill_alerts(threshold=10)

    if alerts:
        response += "\n\n⚠️ Low Stock Alerts:\n"
        for alert in alerts:
            response += f"- {alert['medicine_name']}: {alert['stock']} left\n"

    return response
