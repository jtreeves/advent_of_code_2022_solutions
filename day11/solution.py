class Description:
    def __init__(self, text):
        self.bullets = text.split("\n")
        self.name = self.extract_name()
        self.items = self.extract_items()
        self.operation = self.extract_operation()
    
    def extract_name(self):
        name_bullet = self.bullets[0]
        index = name_bullet[-2:-1]
        name = "m" + index
        return name
    
    def extract_items(self):
        items_bullet = self.bullets[1]
        stringed_items = items_bullet.split(": ")[1]
        items = stringed_items.split(", ")
        listed_items = []
        for item in items:
            listed_items.append(int(item))
        return listed_items

    def extract_operation(self):
        operation_bullet = self.bullets[2]

    def convert_integer_from_string(self, number):
        return int(number)

class Monkey:
    def __init__(self, text):
        description = Description(text)
        self.name = description.name
        self.current_items = description.items
        self.inspected_items = 0

def solve_problem():
    data = extract_data_from_file(11)
    monkeys = list_all_monkeys(data)
    return data

def list_all_monkeys(instructions):
    monkeys = instructions.split("\n\n")
    return monkeys

def extract_data_from_file(day_number):
    file = open(f"day{day_number}/data.txt", "r")
    data = file.read()
    file.close()
    return data