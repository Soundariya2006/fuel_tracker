while True:
    Vehicle_type=input("Enter your vehicle type(car/bike/truck/bus):").lower()
    if Vehicle_type.isalpha():
        print("you have enter the valid vehicle type")
    else:
        print("you have not enter the valid vehicle type")
        continue

    Distance=input("Enter the distance in km:")
    try:
        distance=float(Distance)
        if distance < 0:
            print("Distance cannot be negative.please enter a valid distance.")
            continue

        else:
            print("you have enter the valid distance")
    except ValueError:
        print("please enter the distance in valid format(expected float)")
        continue

    Fuel = input("Enter the fuel in liters:")
    try:
        fuel=float(Fuel)
        if fuel < 0:
            print("fuel cannot be negative.please enter a valid fuel.")
            continue

        elif fuel==0:
            print("fuel cannot be zero.please enter a valid fuel.")
            continue
            
        else:
            print("you have enter the valid float")
    except ValueError:
        print("please enter the fuel in valid format(expected float)")
        continue

    mileage = distance/fuel
    if mileage>=0:
        if mileage>=45:
            print("Good Efficiency")
        elif mileage>25 and mileage<45:
            print("Good,but need to improve")
        else :
             print("Bad performance,need to check your vehicle condition like pressure in tyre,service your vehicle")
             print("your vehicle is using too much fuel.")
    else:
        print("invalid mileage,please check your input value.")
    user_choice=input("Do you want to log another trip?(yes/no):").lower()
    if user_choice != 'yes':
        break
print("thank you for using the fuel tracker.")