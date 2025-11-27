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
    

