# (a) Make a stem-and-leaf plot for the number of defects per 100 vehicles for these 32 brands.
# (b) Make a dot plot of the defects data.

brand <- c("Acura", "Audi", "BMW", "Buick", "Cadillac", "Chevrolet", "Chrysler", "Dodge", "Ford", "GMC", "Honda", "Hyundai", "Infiniti", "Jaguar", "Jeep", "Kia", "Land Rover", "Lexus", "Lincoln", "Mazda", "Mercedes-Benz", "Mercury", "Mini", "Mitsubishi", "Nissan", "Porsche", "Ram", "Scion", "Subaru", "Toyota", "Volkswagen", "Volvo")
defects <- c(86, 111, 113, 114, 111, 111, 122, 130, 93, 126, 95, 102, 107, 130, 129, 126, 170, 88, 106, 114, 87, 113, 133, 146, 111, 83, 110, 114, 121, 117, 135, 109)

data.frame(brand, defects)

stem(defects)

dotchart(defects, labels = brand, cex = 0.5)
