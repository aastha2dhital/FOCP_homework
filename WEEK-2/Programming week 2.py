# Qno.1
name = input("Hello, what is your name? ")
print("Hello " + name + ".  It is good to meet you!")


# Qno.2 
celsius = int(input("Enter the Temperature in Celsius:\n"))
fahrenheit = (1.8 * celsius) + 32
print(str(celsius) + " is equivalent to " + str(fahrenheit) + " Fahrenheit.")


# Qno.3 
num_std = 113
req_size = 22
groups = num_std // req_size
remaining_students = num_std % req_size
print("There will be " + str(groups) + " groups and " + str(remaining_students) + " leftovers.")


# Qno.4 
sweets = 24
pupils = 4
sweets_per_pupil = sweets // pupils
sweets_left_over = sweets % pupils
print("Each pupil will get", sweets_per_pupil, "sweets.")
print("There will be", sweets_left_over, "sweets left over.")
