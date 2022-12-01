file = open("data.txt", "r")
read_file = file.read()
blocks = []

def create_strings_for_each_elf(current_file):
    while len(current_file) > 4:
        find_first = current_file.find("\n\n")
        file_before = current_file[0:find_first]
        blocks.append(file_before)
        current_file = current_file[find_first+2:]

create_strings_for_each_elf(read_file)
print(blocks)
file.close()