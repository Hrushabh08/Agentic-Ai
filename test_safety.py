from agents.conversational_agent import extract_order
from agents.safety_agent import check_order

user_input = "I need 2 strips of Amlodipine"
order = extract_order(user_input)
result = check_order(order)
print(result)
