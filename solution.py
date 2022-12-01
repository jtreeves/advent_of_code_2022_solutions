file = open("data.txt", "r")
read_file = file.read()
calorie_chunks = []
total_calories = []

def create_strings_for_each_elf(data):
    while len(data):
        first_empty_line = data.find("\n\n")
        if first_empty_line != -1:
            file_before = data[0:first_empty_line]
            calorie_chunks.append(file_before)
            data = data[first_empty_line+2:]
        else:
            calorie_chunks.append(data)
            data = ''

create_strings_for_each_elf(read_file)

def count_total_calories_for_each_elf(chunks):
    for chunk in chunks:
        calories = []
        while len(chunk):
            first_line_break = chunk.find("\n")
            if first_line_break != -1:
                content_before = chunk[0:first_line_break]
                calories.append(int(content_before))
                chunk = chunk[first_line_break+1:]
            else:
                calories.append(int(chunk))
                chunk = ''
        total = sum(calories)
        total_calories.append(total)

count_total_calories_for_each_elf(calorie_chunks)
print(total_calories)

total_calories.sort()
print(total_calories)
first_total = total_calories[0]
last_total = total_calories[-1]
print(first_total)
print(last_total)
file.close()