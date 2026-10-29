
print("=== Campus Event Financial Planning ===")
venue = float(input("Enter venue cost: ₹"))
equipment = float(input("Enter equipment cost: ₹"))
transport = float(input("Enter transport cost: ₹"))
sponsorship = float(input("Enter sponsorship amount: ₹"))
catering = float(input("Enter catering cost per participant: ₹"))
certificate = float(input("Enter certificate cost per participant: ₹"))
fee = float(input("Enter registration fee per participant: ₹"))
participants = int(input("Enter expected participants: "))
target_budget = float(input("Enter available budget excluding fees: ₹"))
fixed_cost = venue + equipment + transport
variable_cost = catering + certificate
total_cost = fixed_cost + variable_cost * participants
participant_contribution = fee * participants
total_funds = participant_contribution + sponsorship
shortfall = max(0, total_cost - total_funds)
surplus = max(0, total_funds - total_cost)
# Minimum registrations to break even
if fee > variable_cost:
    required = max(
        0, int((fixed_cost - sponsorship + fee - variable_cost - 1)
               // (fee - variable_cost))
    )
else:
    required = 0 if sponsorship >= fixed_cost else -1
print("\n--- Financial Report ---")
print(f"Fixed costs: ₹{fixed_cost:.2f}")
print(f"Variable cost per participant: ₹{variable_cost:.2f}")
print(f"Total event cost: ₹{total_cost:.2f}")
print(f"Participant contributions: ₹{participant_contribution:.2f}")
print(f"Sponsorship: ₹{sponsorship:.2f}")
print(f"Total funds: ₹{total_funds:.2f}")
print(f"Sponsorship/funding shortfall: ₹{shortfall:.2f}")
print(f"Surplus: ₹{surplus:.2f}")
if required == -1:
    print("Break-even is not possible at this registration fee.")
else:
    print(f"Minimum registrations to break even: {required}")

if total_cost <= target_budget + participant_contribution + sponsorship:
    print("Status: Event is within the available budget.")
else:
    print("Status: Additional funding is required.")

