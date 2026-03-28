from temperature import celcius, farenheit, kelvin

option = 0
while option != 7:
    option = float(input("""Choose the option from below: 
                   1. Celcius to Farenheit
                   2. Farenheit to Celcius
                   3. Kelvin to Celcius
                   4. Celcius to Kelvin
                   5. Farenheit to Kelvin
                   6. Kelvin to Farenheit 
                   7. Exit
                     Enter your option: """))

    if option == 1:
        c = float(input("Enter the temperature in Celcius: "))
        print(f"{c}°C is equal to {celcius.c_to_f(c)}°F")
    elif option == 2:
        f = float(input("Enter the temperature in Farenheit: "))
        print(f"{f}°F is equal to {farenheit.f_to_c(f)}°C")
    elif option == 3:
        k = float(input("Enter the temperature in Kelvin: "))
        print(f"{k}K is equal to {kelvin.k_to_c(k)}°C")
    elif option == 4:
        c = float(input("Enter the temperature in Celcius: "))
        print(f"{c}°C is equal to {celcius.c_to_k(c)}K")
    elif option == 5:
        f = float(input("Enter the temperature in Farenheit: "))
        print(f"{f}°F is equal to {farenheit.f_to_k(f)}K")
    elif option == 6:
        k = float(input("Enter the temperature in Kelvin: "))
        print(f"{k}K is equal to {kelvin.k_to_f(k)}°F")
    elif option == 7:
        print("Thank you for using the temperature converter!")
    else:
        print("Invalid option. Please choose a number between 1 and 7.")    
 
