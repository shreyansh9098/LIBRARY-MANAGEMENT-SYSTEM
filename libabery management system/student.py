class Student:
    students = {}

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    @classmethod
    def register(cls, name, username, password):
        if username in cls.students:
            print(f"Username '{username}' is already taken. Try another.")
        else:
            cls.students[username] = Student(name, username, password)
            print(f"Registration successful for {name}!")

    @classmethod
    def login(cls, username, password):
        if username in cls.students:
            if cls.students[username].password == password:
                print(f"Login successful! Welcome {cls.students[username].name}.")
                return cls.students[username]
            else:
                print("Incorrect password.")
        else:
            print("Username not found.")
        return None