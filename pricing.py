# ---------- User Story 1: Preis pro Ticket ----------

SURCHARGE_3D = 3.00
DISCOUNT_CHILD = 0.30
DISCOUNT_STUDENT = 0.15

CATEGORY_ADULT = "Erwachsener"
CATEGORY_CHILD = "Kind"
CATEGORY_STUDENT = "Student"


def calculate_ticket_price(base_price, category, movie_format):
    """Return the final price of one ticket in CHF."""
    price = base_price

    if movie_format == "3D":
        price = price + SURCHARGE_3D

    if category == CATEGORY_CHILD:
        price = price * (1 - DISCOUNT_CHILD)
    elif category == CATEGORY_STUDENT:
        price = price * (1 - DISCOUNT_STUDENT)

    price = round(price, 2)
    return price
