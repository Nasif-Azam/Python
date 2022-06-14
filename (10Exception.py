# try:
#     age = int(input("Age: "))
#     print(age)
# except ValueError:
#     print("Invalid Value")

try:
    age = int(input("Age: "))
    income = 31000
    risk = income/age
    print(risk)
except ValueError:
    print("Age always is numeric")
except ZeroDivisionError:
    print("Not Dividable by Zero")
