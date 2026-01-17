def calculate_average(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    return average

def add_tax(bill_total):
    total = bill_total + bill_total * 0.10 
    return total

def greet_user(name):
    return "Hello " + name

test_avg = calculate_average(1,2,3)
print(test_avg)
print(greet_user(input("What's your name?: ")))