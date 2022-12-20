class Description:
    def __init__(self, text):
        self.bullets = text.split("\n")
        self.name = self.extract_name()
        self.items = self.extract_items()
        self.operation = self.extract_operation()
        self.divisible = self.extract_divisible()
        self.true_throw_name = self.extract_true_throw_name()
        self.false_throw_name = self.extract_false_throw_name()
    
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
        sign = operation_bullet[24]
        final_element = operation_bullet.split(f" {sign} ")[1]
        return {
            "sign": sign,
            "element": final_element
        }
    
    def extract_divisible(self):
        divisibility_bullet = self.bullets[3]
        number_to_test = divisibility_bullet[22:]
        return int(number_to_test)

    def extract_true_throw_name(self):
        true_throw_bullet = self.bullets[4]
        index = true_throw_bullet[-1]
        name = "m" + index
        return name

    def extract_false_throw_name(self):
        false_throw_bullet = self.bullets[5]
        index = false_throw_bullet[-1]
        name = "m" + index
        return name

class Monkey:
    def __init__(self, text):
        description = Description(text)
        self.name = description.name
        self.current_items = description.items
        self.operation = description.operation
        self.divisible = description.divisible
        self.true_throw_name = description.true_throw_name
        self.false_throw_name = description.false_throw_name
        self.inspected_items = 0

def solve_problem():
    data = extract_data_from_file(11)
    monkey_descriptions = list_all_monkey_descriptions(data)
    monkeys = []
    for description in monkey_descriptions:
        new_monkey = Monkey(description)
        print(f"NAME: {new_monkey.name}")
        monkeys.append(new_monkey)
    return monkeys

def list_all_monkey_descriptions(instructions):
    monkeys = instructions.split("\n\n")
    return monkeys

def extract_data_from_file(day_number):
    file = open(f"day{day_number}/data.txt", "r")
    data = file.read()
    file.close()
    return data

result = solve_problem()
print(result)
