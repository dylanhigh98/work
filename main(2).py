costperfoot = float(.87)
print("Hello")
name = input("please enter the name of your company; ")
print(f"\nHello, {name}!")
feet = float ( input("How many feet of fiber optic cable do you need?; ")  )
totalCost = .87 * feet
print("\nThe total cost for installing fiber coptic cable for the company",name,"is",totalCost)
def cost(feet):
  cost = .87
  if feet >= 100:
    cost = cost(feet * .8)
  elif feet >= 250:
    cost = cost(feet * .7)
  elif feet >= 500:
    cost = cost(feet * .5)
  return feet * cost