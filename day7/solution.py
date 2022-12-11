def determine_total_sizes_of_all_directories(structure):
    sizes = {}
    for key, value in structure.items():
        if type(value) != int:
            sizes[key] = calculate_directory_size(value)
    return sizes

def find_nested_directory_by_name(structure, name):
    # if type(structure) != int:
    print(f"STRUCTURE: {structure}")
    items = structure.items()
    length = len(items)
    iterations = 0
    inner_directories = []
    for key, value in items:
        iterations += 1
        print(f"KEY: {key}")
        if key == name:
            return value
        elif type(value) != int and iterations >= length:
            return find_nested_directory_by_name(value, name)
        else:
            continue

def list_all_directories(structure):
    directories = []
    for key, value in structure.items():
        if isinstance(value, dict):
            directories.append(key)
            directories += list_all_directories(value)
        else:
            continue
    return directories

def calculate_directory_size(directory):
    total = 0
    for value in directory.values():
        if type(value) == int:
            total += value
        else:
            total += calculate_directory_size(value)
    return total

def extract_contents_of_directories(lines):
    sections = lines.split("$ ls\n")
    contents = []
    for section in sections:
        section_array = convert_multiline_string_to_array(section)
        contents.append(section_array)
    directories = []
    for content in contents:
        directory = convert_directory_array_to_object(content)
        directories.append(directory)
    folders = []
    for i in range(len(directories)-1):
        next_directory_name = directories[i]["NEXT"]
        next_directory_contents = directories[i+1]
        folders.append({
            next_directory_name: next_directory_contents
        })
    trimmed_folders = []
    for folder in folders:
        trimmed_folder = remove_next_flag(folder)
        trimmed_folders.append(trimmed_folder)
    result = trimmed_folders[0]
    no_empties = confirm_no_empty_subdirectories(result)
    while not no_empties:
        result = replace_empty_directories(result, trimmed_folders)
        no_empties = confirm_no_empty_subdirectories(result)
    return result

def replace_empty_directories(structure, directories):
    if type(structure) != int:
        for key, value in structure.items():
            if not bool(value):
                correct_directory = find_correct_directory_in_array(directories, key)
                structure[key] = correct_directory[key]
            else:
                structure[key] = replace_empty_directories(value, directories)
    return structure

def confirm_no_empty_subdirectories(structure):
    stringed_structure = str(structure)
    found_empty = stringed_structure.find("{}")
    if found_empty == -1:
        return True
    else:
        return False

def remove_next_flag(contents):
    contents_name = list(contents.keys())[0]
    contents[contents_name].pop("NEXT", None)
    return contents

def find_correct_directory_in_array(directories, name):
    for directory in directories:
        directory_name = list(directory.keys())[0]
        if directory_name == name:
            return directory

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
        else:
            next_directory = determine_current_directory_under_analysis(element)
            if next_directory != "..":
                directory_object["NEXT"] = next_directory
    return directory_object

def determine_current_directory_under_analysis(line):
    return line[5:]

def get_directory_name(line):
    partition = line.split(" ")
    name = partition[1]
    return name

def get_file_name_and_size(line):
    partition = line.split(" ")
    name = partition[1]
    size = int(partition[0])
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
# print(convert_directory_array_to_object(['dir e', '29116 f', '2557 g', '62596 h.lst', '$ cd e']))
# print(find_key_in_nested_objects({'a': 1}, 'a'))
# print(find_correct_directory_in_array([{'a': {}}, {'b': {}}], 'a'))
# print(confirm_no_empty_subdirectories({'a': {}}))
# print(calculate_directory_size({'a': 2, 'b': {'d': 7, 'e': 8}, 'c': 5}))
# print(list_all_directories({'/': {'a': {'e': {'i': 584}, 'f': 29116, 'g': 2557, 'h.lst': 62596}, 'b.txt': 14848514, 'c.dat': 8504156, 'd': {'j': 4060174, 'd.log': 8033020, 'd.ext': 5626152, 'k': 7214296}}}))
print(find_nested_directory_by_name({'/': {'a': {'e': {'i': 584}, 'f': 29116, 'g': 2557, 'h.lst': 62596}, 'b.txt': 14848514, 'c.dat': 8504156, 'd': {'j': 4060174, 'd.log': 8033020, 'd.ext': 5626152, 'k': 7214296}}}, 'e'))