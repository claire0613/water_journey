class A:
    def __init__(self, name):
        self.name = name


class AList:
    def __init__(self, a_list: list[A]):
        self.a_list = a_list

    def print_all_name(self):
        print(self.name)

    def get_a_list(self):
        return self.a_list

    def get_a_list2(self):
        return iter(self.a_list)


a1 = A("1")
a2 = A("2")
a3 = A("3")

a_list = AList([a1, a2, a3])

# print(a_list.a_list)
print(a_list.get_a_list)
print(a_list.get_a_list2)
for i in a_list.a_list:
    print(i)
    
user_input = input("Please input your username (a/b): \n ")
print(user_input.strip())
