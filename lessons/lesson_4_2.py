class User:
    class_names = ['M', 'F']
    count = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        User.count += 1

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def get_user_count(cls):
        return cls.count

maksat = User("Max", "Smith")
print(maksat.full_name)
print(User.get_user_count())
print(User.count)
User.class_names += ['X']