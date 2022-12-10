def extract_contents_of_directories(lines):
    sections = lines.split("$ ls\n")
    contents = []
    for section in sections:
        section_array = convert_multiline_string_to_array(section)
        contents.append(section_array)
    return contents

def convert_directory_array_to_object(directory_array):
    directory_object = {}
    for element in directory_array:
        if not check_if_command(element):
            if not check_if_directory(element):
                file = get_file_name_and_size(element)
                directory_object[file["name"]] = file["size"]
            else:
                new_directory = get_directory_name(element)
                directory_object[new_directory] = {}
    return directory_object

def get_directory_name(line):
    partition = line.split(" ")
    name = partition[1]
    return name

def get_file_name_and_size(line):
    partition = line.split(" ")
    name = partition[1]
    size = partition[0]
    return {
        "name": name,
        "size": size
    }

def check_if_command(line):
    first_character = line[0]
    is_command = first_character == "$"
    return is_command

def check_if_directory(line):
    first_characters = line[0:3]
    is_directory = first_characters == "dir"
    return is_directory

def determine_directory_name(line):
    return line[5:]

def convert_multiline_string_to_array(multiline_string):
    rows = []
    while len(multiline_string):
        first_line_break = multiline_string.find("\n")
        if first_line_break != -1:
            content_before = multiline_string[0:first_line_break]
            rows.append(content_before)
            multiline_string = multiline_string[first_line_break+1:]
        else:
            rows.append(multiline_string)
            multiline_string = ""
    return rows

def extract_data_from_file(day_number):
    file = open(f"day{day_number}/data.txt", "r")
    data = file.read()
    file.close()
    return data

# print(check_if_command("$ ls"))
# print(check_if_directory("234 a"))
# print(extract_contents_of_directories("$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k"))
# print(determine_directory_name("$ cd bcd"))
print(convert_directory_array_to_object(['dir e', '29116 f', '2557 g', '62596 h.lst', '$ cd e']))