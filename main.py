def temp():
 print("Temperature Convertor")
 h = float(input("\nEnter your choice to be performed :\n"
                    "press 1 for Fahrenheit to Celsius \n"
                    "press 2 for Celsius to Fahrenheit \n"
                    "press 3 for Quit \n"))

 def fahrenheit_to_celsius():
  celsius = (fahrenheit - 32) * 5 / 9
  print(celsius)

 def celsius_to_fahrenheit():
  fahrenheit = (celsius * 9 / 5) + 32
  print(fahrenheit)


 if h == 1:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    fahrenheit_to_celsius()
 elif h == 2:
            celsius = float(input("Enter temperature in Celsius: "))
            celsius_to_fahrenheit()
 elif h == 3:
    print("Thank You")

 else:
            print("Invalid choice. Please enter 1, 2, or 3.")

 m = int(input("\nDo you wish to do another conversion?\n Press 1 if yes\n Press 2 if no\n"))

 if m==1:
    temp()

 elif m==2:
        print("Thank you for using the Temperature Convertor")
 else:
  print("enter a valid choice")



temp()