

class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Info:
    def __init__(self, city: str, street: str, zip_code: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

class Library(Info):

    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        super().__init__(city, street, zip_code, phone)
        self.open_hours = open_hours

    def __str__(self):
        return f"Library in {self.city} on {self.street} street, {self.zip_code}.\nOpen hours: {self.open_hours}.\nContact info: {self.phone}"

class Employee(Info):
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str, zip_code: str, phone: str):
        super().__init__(city, street, zip_code, phone)
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date

    def __str__(self):
        return f"Employee {self.first_name} {self.last_name}.\nHired on {self.hire_date}.\nBirthday:{self.birth_date}.\nLives in {self.city}, {self.street} street, {self.zip_code}.\nContact info: {self.phone}"

class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str, author_surname: str, number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book available in:\n{self.library.city}\nPublication date: {self.publication_date}, author: {self.author_name} {self.author_surname}. Number of pages: {self.number_of_pages}."

class Order:
    def __init__(self, library: Library, employee: Employee, student: Student, books: list, order_date: str):
        self.library = library
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f"Order for student {self.student} from: \n{self.library}.\nPrepared by employee {self.employee.first_name} {self.employee.last_name}.\nBooks ordered on {self.order_date}: {[x.author_name + ' ' + x.author_surname for x in self.books]}"


library1 = Library("Olkusz", "Francesco Nullo 29b", "32-300", "8:00-16:00", "32 643 06 19")
library2 = Library("Bukowno", "Wodąca 51", "32-332", "11:00-19:00", "32 642 32 65")

book1 = Book(library1, "April 30, 2015", "Joanne K.", "Rowling", 352)
book2 = Book(library1, "September 01, 2015", "Joanne K.", "Rowling", 384)
book3 = Book(library1, "July 26, 2018", "Holly", "Black", 400)
book4 = Book(library2, "June 02, 2016", "Leigh", "Bardugo", 512)
book5 = Book(library2, "November 29, 2008", "Diana Wynne", "Jones", 320)

employee1 = Employee("Anna", "Nowak", "04-26-2005", "08-30-1980", "Olkusz", "Jasna 134", "32-300", "604 800 518")
employee2 = Employee("Jan", "Nowak", "07-01-2015", "06-05-1991", "Olkusz", "Sławkowska 18", "32-300", "709 501 902")
employee3 = Employee("Kacper", "Kowalski", "09-01-1998", "01-06-1970", "Bukowno", "Wodąca 43", "32-332", "509 987 202")

student1 = Student("Adam", "Górski")
student2 = Student("Michał", "Anioł")
student3 = Student("Alicja", "Kowalska")

book_list1 = [book1, book2, book3]
book_list2 = [book4, book5]

order1 = Order(library1, employee1, student1, book_list1, "11-24-2021")
order2 = Order(library2, employee2, student3, book_list2, "11-21-2021")

print(order1)
print('\n')
print(order2)