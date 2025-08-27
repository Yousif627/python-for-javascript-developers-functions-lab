#Exercise 1
def calculate_area_triangle(base, height):
	return (base * height) / 2 
print('Exercise 1:', calculate_area_triangle(10, 5))

#Exercise 2
def simple_interest(principal, rate, time):
    return (principal * rate *time)/100
print("Exercise 2:", simple_interest(1000, 5, 2))

#Exercise 3
def apply_discount(price, discount_percent):
    return price * (1 - discount_percent /100)
print('Exercise 3:', apply_discount(100, 25))

#Exercise 4
def convert_temperature(temp, unit):
    if unit == 'C':
        return (temp * 9/5) + 32
    elif unit == 'F':
        return (temp - 32) * 5/9
    else:
        raise ValueError("Unit must be 'C' or 'F'")
    
print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F')) 


# Exercise 5
def sum_to(n):
    return sum(range(1, n + 1))

print('Exercise 5:', sum_to(6))

# Exercise 6
def largest(a, b, c):
    return max(a, b, c)

print('Exercise 6:', largest(1, 2, 3))


# Exercise 7
def calculate_tip(bill_amount, tip_percent):
    return bill_amount * tip_percent / 100

print('Exercise 7:', calculate_tip(50, 20))
