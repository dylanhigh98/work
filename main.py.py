# Get their rate and Invest ammount from the user.
invest = float(input("What is your initial investment?: "))
rate = float(input("What is your annual rate?: "))

# Start the variables that are used in the loop
total = invest
double = 2 * invest
years = 0
# Loop until the total amount is double the principal amount \
while total < double:
  # Add the intrest rate to the total and increment the years
  total += total * rate
  years += 1

# Print the results
print(f"Your investment will take {years} years to double")
