# student_info = {
#     "name": "Nasif Azam",
#     "ID": 211015006,
#     "CGPA": 3.694
# }
# student_info["name"] = "Zisha"
# print(student_info["name"])
# print(student_info.get("id"))

# digits = input("Type 1 to 5 any digits: ")
# for digit in digits:
#     if(int(digit) == 1):
#         print("One")
#     if(int(digit) == 2):
#         print("Two")
#     if(int(digit) == 3):
#         print("Three")
#     if(int(digit) == 4):
#         print("Four")
#     if(int(digit) == 5):
#         print("Five")

# digits = input("Type 1 to 5 any digits: ")
# digit_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five"
# }
# output = ""
# for digit in digits:
#     output += digit_mapping.get(digit, "Missing") + " "
# print(output)
# print(digit_mapping.get(digit, "Not in Dictionary"))

# Emoji Converter
# def emoji_converter(msg):
#     words = msg.split()
#     emoji = {
#         ":)": "😃",
#         ":(": "😞",
#         ":D": "😁"
#     }
#     # print(emoji[':)'])
#     output = ""
#     for word in words:
#         output += emoji.get(word, word) + " "
#     return output


# msg = input("-->")
# print(emoji_converter(msg))


myDict = {
    "Name": "Nasif",
    "ID": 211015006,
    "CGPA": 3.70,
    1: 2,
    "adressDict": {
        "Birth Place": "Rangpur Sadar",
        "IP": [120, 114, 00, 6]
    }
}
print(myDict["Name"])  # If wrong return error
print(myDict.get("Name"))  # If wrong return none
print(myDict["CGPA"])
print(myDict["adressDict"]["Birth Place"])
print(myDict["adressDict"]["IP"])
print(myDict.keys())  # Dictionary keys
print(myDict.values())  # Dictionary values
print(myDict.items())  # Dictionary (keys,values)

update = {
    "Name": "Zisha",
    "ID": 211015000,
    "CGPA": 3.90,
    2: 2,
    "adressDict": {
        "Birth Place": "Rangpur Sadar",
        "IP": [120, 114, 00, 77]
    }
}
myDict.update(update)  # Dictionary Update
print("\n", myDict)
