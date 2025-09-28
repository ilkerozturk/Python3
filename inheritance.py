# Kalıtım (Inheritance), Miras Alma (Derivation) ve Polimorfizm (Polymorphism) kavramları nesne yönelimli 
# programlamanın temel taşlarındandır. Bu kavramlar, kodun yeniden kullanılabilirliğini artırır ve daha esnek, 
# bakımı kolay yazılımlar geliştirmeyi sağlar.

# Kalıtım (Inheritance)
# Kalıtım, bir sınıfın (class) başka bir sınıftan özellikleri ve davranışları (metotları) miras almasını sağlar. 


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
class Student(Person):
    def __init__(self, name, age, student_id):
        Person.__init__(self, name, age)  # Üst sınıfın yapıcı metodunu çağır
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying and his/her student ID is {self.student_id}."
    

student = Student("Alice", 20, "S12345")
print(student.greet())  # Person sınıfından miras alınan metot
print(student.study())  # Student sınıfına özgü metot

