import copy

directory_names = []

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def __repr__(self):
        return f"{self.name}: {self.size}"

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.directories = []
        self.parent_directory = None
    
    def __repr__(self):
        return f"DIR {self.name}: {len(self.directories)}"
    
    def add_file(self, file):
        self.files.append(file)
    
    def add_directory(self, other_directory):
        self.directories.append(other_directory)
        other_directory.parent_directory = self
    
    def calculate_size(self):
        total = 0
        for file in self.files:
            total += file.size
        for directory in self.directories:
            for file in directory.files:
                total += file.size
        return total

def sum_all_directories(directories):
    total = 0
    for value in directories.values():
        total += value
    return total

def filter_out_too_large_directories(sizes):
    filtered_sizes = {}
    for key, value in sizes.items():
        if value <= 100000:
            filtered_sizes[key] = value
    return filtered_sizes

def determine_total_sizes_of_all_directories(structure):
    directory_names = list_all_directories(structure)
    sizes = {}
    for directory_name in directory_names:
        directory = find_nested_directory_by_name(structure, directory_name)
        size = calculate_directory_size(directory)
        sizes[directory_name] = size
    return sizes

def find_nested_directory_by_name(structure, name):
    this_copy = copy.deepcopy(structure)
    keys = []
    keys.extend(this_copy.keys())
    while len(keys) > 0:
        key = keys.pop(0)
        if key == name:
            return this_copy[key]
        if isinstance(this_copy[key], dict):
            nested = this_copy.pop(key)
            keys.extend(nested.keys())
            this_copy.update(nested)

def generate_unique_directory_name(name_to_validate):
    duplicate = check_names_for_duplicate(name_to_validate)
    if duplicate:
        incremented_name = name_to_validate + '0'
        return generate_unique_directory_name(incremented_name)
    else:
        return name_to_validate

def check_names_for_duplicate(name_to_check):
    for name in directory_names:
        if name == name_to_check:
            return True
    return False

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
        unique_next_name = generate_unique_directory_name(next_directory_name)
        directory_names.append(unique_next_name)
        next_directory_contents = directories[i+1]
        folders.append({
            unique_next_name: next_directory_contents
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
                unique_directory_name = generate_unique_directory_name(new_directory)
                directory_object[unique_directory_name] = {}
                directory_names.append(unique_directory_name)
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
    postpended_name = name + '0'
    return postpended_name

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

def solve_problem():
    data = extract_data_from_file(7, False)
    contents = extract_contents_of_directories(data)
    sizes = determine_total_sizes_of_all_directories(contents)
    filtered_sizes = filter_out_too_large_directories(sizes)
    total = sum_all_directories(filtered_sizes)
    return total

def extract_data_from_file(day_number, is_official):
    if is_official:
        name = "data"
    else:
        name = "practice"
    file = open(f"day{day_number}/{name}.txt", "r")
    data = file.read()
    file.close()
    return data

result = solve_problem()
print(result)
