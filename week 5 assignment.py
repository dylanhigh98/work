# Hello, This program will convert miles to kilometers.

def main():
    # display the intro screen.
    intro()

    try:
  # please type in how many you miles you are travleing.
      miles_needed = int(input('Enter the number of miles driven: '))

  # Convert miles to kilometers.
      miles_to_kilometers(miles_needed)

    except:
      print('An exception occured, try again by entering only a number')
      print()
      main()

  # The intro function displays an introductory screen.
def intro():
    print("This program converts your distance, miles to kilometers'")
    print('refrence the formula to convert miles to kilometers is:')
    print(' 1 mile = 1.60934 kilometers')
    print()

  # The miles_to_kilometers fucntion accepts a number of
  #miles and displays the approximate distance in kilometers.
def miles_to_kilometers(miles):
    kilometers = miles * 1.60934
    print('The distance you have driven is', kilometers, 'kilometers', miles, 'miles')
                  
  # Call the main function.
main()
input('Press ENTER to exit')
