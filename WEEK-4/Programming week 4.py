# Qno.1
def is_in_range(number):
    return 0 <= number <= 100
result1 = is_in_range(23)
print(result1)

# Qno.2
def case_checker(current_string):
    for char in current_string:
        print(char)
case_checker("hYAAaaaa")

# Qno.3 
def greetings(name):
    return name[0].upper() + name[1:].lower()
chosen_name = input("Hi, What's your name?")
print(f"Hi, {greetings(chosen_name)}. Have a great day!")

# Qno.4 
def slicer(string_value):
    if len(string_value) > 1:
        return string_value[:-1]
    else:
        return string_value
user_value = input("Enter a string value: ")
output = slicer(user_value)
print(f"New string after removing the last character: {output}")

# Qno.5
def celsius(temp):
    con_temp = (temp - 32) * 5/9
    return print(f"Temperature in Celsius: {con_temp}")
def fahrenheit(temp):
    con_temp = temp * 9/5 + 32
    return print(f"Temperature in Fahrenheit: {con_temp}")
final_temp = float(input('Enter the temperature: '))
celsius(final_temp)
fahrenheit(final_temp)

# Qno.6
def fahrenheit(temp):
    con_temp = float(temp[:-1])
    return print(f"{temp} Temperature converted to Fahrenheit is: {con_temp * 9/5 + 32}F")
final_temp = input("Enter your temperature: ")
fahrenheit(final_temp)

# Qno.7
def celsius(temp):
    con_temp = (temp - 32) * 5/9
    return con_temp
def fahrenheit(temp):
    con_temp = temp * 9/5 + 32
    return con_temp
temperatures = []
for i in range(6):
    temp = float(input(f"Enter temperature {i + 1}: "))
    temperatures.append(temp)
celsius_temps = [celsius(temp) for temp in temperatures]
fahrenheit_temps = [fahrenheit(temp) for temp in temperatures]
max_temp = max(temperatures)
min_temp = min(temperatures)
mean_temp = sum(temperatures) / len(temperatures)

print(f"\nMaximum Temperature: {max_temp}")
print(f"Minimum Temperature: {min_temp}")
print(f"Mean Temperature: {mean_temp}")

# Qno.8
def celsius(temp):
    return (temp - 32) * 5/9
def fahrenheit(temp):
    return temp * 9/5 + 32
temperatures = []
while True:
    temp_input = input("Enter a temperature (press Enter to finish): ")
     if temp_input == "":
    break
    
    try:
        temp = float(temp_input)
        temperatures.append(temp)
    except ValueError:
        print("Invalid input. Please enter a valid temperature.")

if not temperatures:
    print("No temperatures entered.")
else:
    celsius_temps = [celsius(temp) for temp in temperatures]
    fahrenheit_temps = [fahrenheit(temp) for temp in temperatures]
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)

    print(f"\nMaximum Temperature: {max_temp}")
    print(f"Minimum Temperature: {min_temp}")
    print(f"Mean Temperature is : {mean_temp}")
