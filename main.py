import bakery_utils as bu

print(f"Welcome to {bu.BAKERY_NAME}!")
cost = bu.calculate_total(price=3.50, quantity=3)
bu.print_receipt("Chocolate Croissant", cost)

import kitchen.ovens
from kitchen.refrigerator import get_frosting

print("--- Kitchen Inventory Check ---")

bread = kitchen.ovens.bake_bread()
print(f"Oven Status: {bread}")

frosting = get_frosting()
print(f"Fridge Status: Found {frosting}")

from kitchen.blender import make_smoothie as smoothie_maker

smoothie = smoothie_maker()
print(f"Blender Status: Made a {smoothie}")