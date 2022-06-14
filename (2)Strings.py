# --> String to Integers/Float/Boolean
# birth_year = input('Birth Year: ')
# age = 2021 - int(birth_year)
# print(age)

# --> Convert weight(Pounds to KG)
# user_weight = input("What is your weight in pound? ")
# weight_kg = int(user_weight) * 0.453
# print(weight_kg)

# --> Srtings
# perag1 = "Nasif 'Shakt_Launda'"
# perag2 = 'Azam "Shakt_Launda"'
# perag3 = '''
# Hi Zisha,
# How are you?
# thankQ
# your loving hubby Nasif'''
# copy_perag1 = perag1[:]
# print(perag1, perag2, perag3)   # print(perag)
# print(perag2[0])
# print(perag2[-1])
# print(perag2[0:6])
# print(perag2[5:19])
# print(copy_perag1)

# --> Formatted Srtings
# first = "Nasif"
# last = "Azam"
# full_name = first + " {"+last + "} is a coder"
# full_name1 = f"{first} [{last}] is a coder"
# print(full_name1)

# -->Strings Methods<-- #
msg = 'XXNasif Azam is a Engineer  X'
# print(len(msg))
# print(msg.upper())
# print(msg.find('f'))
# print(msg.replace('Engineer', 'SCADA Engineer'))
# print(msg.strip("X"))  # Remove Space
# print('Nasif' in msg)  # Boolean Expression

# user = input('What is user name? ')
# color = input('What is ' + user + ' favourite color? ')
# print(user+" likes "+color)

# -->Strings Letter<-- #
# letter = '''
# Dear <|name|>,
# Good evening <|name|>.

# Date: <|date|>
# '''
# # print(letter)
# name = input("Name is: ")
# date = input("Date is: ")
# letter = letter.replace("<|name|>", name)
# letter = letter.replace("<|date|>", date)
# print(letter)

txt = "I am Nasif  Azam"
dblspc = txt.find("  ")
print(dblspc)
txt = txt.replace("  ", " ")
print(txt)
