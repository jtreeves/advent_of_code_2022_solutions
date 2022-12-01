file = open("data.txt", "r")
read_file = file.read()
calorie_chunks = []
total_calories = []

def create_strings_for_each_elf(data):
    while len(data):
        first_line_break = data.find("\n\n")
        if first_line_break != -1:
            file_before = data[0:first_line_break]
            calorie_chunks.append(file_before)
            data = data[first_line_break+2:]
        else:
            calorie_chunks.append(data)
            data = []
    print(f"FINAL DATA: {data}")

create_strings_for_each_elf(read_file)

# def count_total_calories_for_each_elf(chunks):
#     return

print(calorie_chunks)
file.close()