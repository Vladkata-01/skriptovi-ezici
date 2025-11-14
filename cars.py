car1 = {
  "Brand": input ("Enter car 1 brand: "),
 "Model" : input ("Enter car 1 model: "),
 "Horsepower" : input ("Enter car 1 horsepower: ")
 }
car2 = {
  "Brand": input ("Enter car 2 brand: "),
 "Model" : input ("Enter car 2 model: "),
 "Horsepower" : input ("Enter car 2 horsepower: ")
 }
if car1["Horsepower"] > car2["Horsepower"]:
    print("Car 1 is more powerful")
elif car1["Horsepower"] < car2["Horsepower"]:
     print("Car 2 is more powerful")