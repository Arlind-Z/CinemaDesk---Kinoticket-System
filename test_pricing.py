import pricing

# ---------- User Story 1: Preis pro Ticket ----------

# Basispreis in allen Tests: CHF 15.00

assert pricing.calculate_ticket_price(15.00, "Erwachsener", "2D") == 15.00
assert pricing.calculate_ticket_price(15.00, "Erwachsener", "3D") == 18.00
assert pricing.calculate_ticket_price(15.00, "Kind", "2D") == 10.50
assert pricing.calculate_ticket_price(15.00, "Kind", "3D") == 12.60
assert pricing.calculate_ticket_price(15.00, "Student", "2D") == 12.75
assert pricing.calculate_ticket_price(15.00, "Student", "3D") == 15.30
assert pricing.calculate_ticket_price(0.00, "Kind", "2D") == 0.00

print("Tests User Story 1 bestanden.")
