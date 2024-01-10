class Dog:
    def __init__(self, name):
        self.name = name
        self.trick_list = []
    def get_name(self):
        return self.name
    def sit(self):
        print(f"{self.name} sits.")
        self.trick_list.append("sit")
    def lay_down(self):
        print(f"{self.name} lays down.")
        self.trick_list.append("lay down")
    def write_python_program(self):
        print(f"{self.name} writes a python program.")
        self.trick_list.append("write a python project")
    def print_trick_list(self):
        if not self.trick_list:
            print(f"{self.name} did not perform any tricks yet.")
        else:
            print(f"{self.name} did perform the following tricks:")
            for trick in self.trick_list:
                print(f"- {trick}")

name = Dog("Wendy")
name.sit()
name.lay_down()
name.write_python_program()
name.print_trick_list()