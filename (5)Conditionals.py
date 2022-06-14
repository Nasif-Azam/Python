# -->If Statement<-- #
# is_hot = False
# is_cold = True
# if is_hot:
#     print("It's a hot day")
#     print("Need to drink much water")
# elif is_cold:
#     print("It's cold day")
# else:
#     print("It's a lovely day")

# price = 1000000
# is_good_credit = False
# if is_good_credit:
#     down_pay = price*(10/100)
# else:
#     down_pay = price*(20/100)
# print(f"Down Payment = {down_pay}")

# high_income = True
# good_credit = True
# if high_income and good_credit:
#     print("Eligable for loan")
# else:
#     print("Not Eligable")

# good_credit = True
# criminal_record = False
# if good_credit and not criminal_record:
#     print("Eligable for loan")
# else:
#     print("Not Eligable")

# -->Comperision Operator<-- #
# temperature = int(input("Tempperature is = "))
# if temperature > 30:
#     print("It's Hot Day")
# elif temperature < 10:
#     print("It's Cold Day")
# else:
#     print("Lovely Day")

# user = input("Wrirte your name: ")
# if len(user) > 10:
#     print(f"[{user}] is more than 10 characters")
# elif len(user) < 3:
#     print(f"[{user}] is less than 3 characters")
# else:
#     print(f"[{user}] is looks good")

# weight = int(input("What is your weight: "))
# units = input("Weight in lb(L) or kg(K): ").upper()
# if units == "L":
#     weight = weight * 0.45
#     print(f"You are {weight} kg")
# elif units == "K":
#     weight = weight * 2.20
#     print(f"You are {weight} pounds ")

age = 20
if 18 <= age <= 25:  # if age >= 18 and age <= 25:
    print("Eligible")
else:
    print("Not Eligible")
