class Students:
    def student_info(self, stu_name, ID, cgpa):
        print(f"Name: {stu_name}\nID: {ID}\nCGPA: {cgpa}")


class Nasif(Students):
    def university(self):
        print("University: GUB")


class Zisha(Students):
    def university(self):
        print("University: AIUB")


name_nasif = Nasif()
name_zisha = Zisha()
name_nasif.student_info("Nasif", 211015006, 3.694)
name_nasif.university()
name_zisha.student_info("Zisha", 211015000, 3.95)
name_zisha.university()
