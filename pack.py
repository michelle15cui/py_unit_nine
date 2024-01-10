class Dog:
    def __init__(self,name):
        self.name = name
        self.trick_list = []
    def get_name(self):
        return self.name
    def sit(self):
        print(f"{self.name} sits.")
        self.trick_list.append("sit")
    def lay_down(self):
        print(f"{self.name} lays down.")
        self.trick_list.append("lay_down")
    def write_python_program(self):
        print(f"{self.name} writes a python program.")
        self.trick_list.append("write_a_python_project")
    def print_trick_list(self):
        if not self.trick_list:
            print(f"{self.name} did not perform any tricks yet.")
        else:
            print(f"{self.name} did perform the following tricks:")
            for trick in self.trick_list:
                print(f"- {trick}")
from dog import Dog
class Pack:
    def __init__(self, leader):
        self.members = [leader]
        self.leader_index = 0
    def get_leader_name(self):
        return self.members[self.leader_index].get_name()
    def add_member(self, new_member):
        self.members.append(new_member)
    def print_pack(self):
        print("The pack contains:")
        for member in self.members:
            print(f"\t{member.get_name()}")
    def new_leader(self, new_leader_index):
        if 0 <= new_leader_index < len(self.members) and new_leader_index != self.leader_index:
            old_leader_name = self.get_leader_name()
            self.leader_index = new_leader_index
            print(f"{self.get_leader_name()} takes the leader's spot instead of {old_leader_name}.")
        else:
            print("This dog leader is not valid.")
    def all_sit(self):
        for member in self.members:
            member.sit()
    def all_print_tricks(self):
        for member in self.members:
            member.print_trick_list()
    def __str__(self):
        return f"the new leader's name: {self.get_leader_name()}"
if __name__ == "__main__":
    dog1 = Dog("Fido")
    dog2 = Dog("Spot")
    dog3 = Dog("Rover")
    pack = Pack(dog1)
    pack.add_member(dog2)
    pack.add_member(dog3)
    pack.print_pack()
    pack.all_sit()
    pack.all_print_tricks()
    pack.new_leader(2)
    print(pack)
    print(dog1)
