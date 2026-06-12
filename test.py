import models

burger = models.FoodItem("Smash Burger", 5.99, "Entree", 4.5)

print(burger.getName())
print(burger.getPrice())
print(burger.getCategory())
print(burger.getRating())