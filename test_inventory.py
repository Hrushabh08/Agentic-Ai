# test_inventory_alerts.py

from agents.inventory_agent import check_refill_alerts

# Check medicines with stock <= 50
alerts = check_refill_alerts(threshold=50)
print("Low Stock Alerts:", alerts)
