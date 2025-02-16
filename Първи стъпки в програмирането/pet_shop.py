"""
Write a program that calculates the costs required to purchase dog
and cat food. The food is purchased from a pet store,
with a package of dog food costing 2.50 lv and a package of
cat food costing 4 lv.
"""

DOG_FOOD = 2.50
CAT_FOOD = 4.00

dog_food_count = int(input())
cat_food_count = int(input())

sum = DOG_FOOD*dog_food_count + CAT_FOOD*cat_food_count

print(f"{sum} lv.")