def kinetic_energy():
    print("Kinetic Energy is given by 0.5 * mass * velocity:")
    m = float(input("Enter the value for mass in kilogram: "))
    v = float(input("Enter the value for velocity in metre per seconds: "))
    result = 0.5 * m * v**2
    print(f"The kinetic energy is {result}")

def potential_energy():
    print("Potential Energy is given by mass * acceleration due to gravity * height:")
    m = float(input("Enter the value for mass in kilogram: "))
    g = float(input("Enter the value for acceleration due to gravity in metre per seconds square: "))
    h = float(input("Enter the value for height in metres: "))
    result = m * g * h
    print(f"The potential energy is {result}")

def youngs_modulus():
    print("Youngs Modulus is given by (force/area) / (extension/length):")
    force = float(input("Enter the value for force in Newton: "))
    area = float(input("Enter the value for area in metres square: "))
    extension = float(input("Enter the value for extension in metres: "))
    length = float(input("Enter the value for the original length: "))
    result = (force/area) / (extension/length)
    print(f"The youngs Modulus is {result}")

def pressure():
    print("Pressure is given by density * height * acceleration due to gravity:")
    density = float(input("Enter the value for density in kilogram per metres cube: "))
    height = float(input("Enter the value for height: "))
    g = float(input("Enter the value for acceleration due to gravity: "))
    result = density * height * g
    print(f"The pressure is {result} ")

def height_of_free_fall():
    print("The height of free falll is given by 0.5 * acceleration due to gravity * time squared: ")
    g = float(input("Enter the value for acceleration due to gravity: "))
    time = float(input("Enter the value for time in seconds: "))
    result = 0.5 * g * time**2
    print(f"The Height of free fall is {result}")

def user_selection():
    user_name = input("Hello there! Enter your name below:\n")
    print(f"Hi {user_name}, You can select a formula from the list below to work with:")
    print("1 - Kinetic Energy")
    print("2 - Potential Energy")
    print("3 - Young's Modulus")
    print("4 - Pressure")
    print("5 - Height of free fall")
    user_choice = int(input("Enter your choosen number: "))

    if user_choice == 1:
      kinetic_energy()
    elif user_choice == 2:
      potential_energy()
    elif user_choice == 3:
        youngs_modulus()
    elif user_choice == 4:
        pressure()
    elif user_choice == 5:
        height_of_free_fall()
    else:
        print("Invalid selection")
      
user_selection()

#kinetic_energy()

