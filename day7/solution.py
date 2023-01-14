class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def __repr__(self):
        return f"{self.name}: {self.size}"

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False
    
    def __hash__(self):
        return hash((self.name, self.size))

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = set()
        self.directories = set()
        self.parent_directory = None
    
    def __repr__(self):
        hierarchy = f"- {self.name} (dir)\n"
        for file in self.files:
            hierarchy += f"  - {file.name} (file)\n"
        for directory in self.directories:
            hierarchy += f"  {directory}\n"
        hierarchy = hierarchy[:-1]
        return hierarchy
    
    def __eq__(self, other):
        if isinstance(other, Directory):
            if self.name == other.name:
                return True
            else:
                return False
        else:
            return False
    
    def __hash__(self):
        return hash((self.name, self.parent_directory))

    def add_file(self, file):
        self.files.add(file)
    
    def add_directory(self, other_directory):
        self.directories.add(other_directory)
        other_directory.parent_directory = self
    
    def find_subdirectory_by_name(self, name):
        for directory in self.directories:
            if directory.name == name:
                return directory
    
    def list_all_subdirectories(self):
        subdirectories = []
        for directory in self.directories:
            name = directory.name
            size = directory.calculate_size()
            subdirectories.append((name, size))
            if directory.directories:
                subdirectories.extend(directory.list_all_subdirectories())
        return subdirectories
    
    def calculate_size(self):
        total = 0
        for file in self.files:
            total += file.size
        for directory in self.directories:
            total += directory.calculate_size()
        return total

class Terminal:
    def __init__(self, history):
        self.output = history.split("\n")
        self.root_directory = None
        self.current_directory = None
    
    def __repr__(self):
        return f"OUTPUT: {len(self.output)}"
    
    def set_current_directory(self, directory):
        self.current_directory = directory
    
    def read_output_to_create_directories(self):
        for line in self.output:
            parts = line.split(" ")
            if line[0:4] == "$ cd":
                name = parts[2]
                if name != "..":
                    if self.current_directory != None:
                        found_directory = self.current_directory.find_subdirectory_by_name(name)
                        self.set_current_directory(found_directory)
                    else:
                        new_directory = Directory(name)
                        self.root_directory = new_directory
                        self.set_current_directory(new_directory)
                else:
                    self.set_current_directory(self.current_directory.parent_directory)
            elif line[0:4] == "$ ls":
                continue
            elif line[0:3] == "dir":
                name = parts[1]
                new_directory = Directory(name)
                self.current_directory.add_directory(new_directory)
            else:
                size = int(parts[0])
                name = parts[1]
                new_file = File(name, size)
                self.current_directory.add_file(new_file)
    
    def list_all_directories(self):
        root_directory_name = self.root_directory.name
        root_directory_size = self.root_directory.calculate_size()
        root = (root_directory_name, root_directory_size)
        all_directories = self.root_directory.list_all_subdirectories()
        all_directories.append(root)
        return all_directories
    
    def trim_excessive_directories(self):
        directories = self.list_all_directories()
        trimmed = []
        for _, size in directories:
            if size <= 100000:
                trimmed.append(size)
        return trimmed
    
    def calculate_total_size_of_small_directories(self):
        sizes = self.trim_excessive_directories()
        total = 0
        for size in sizes:
            total += size
        return total
    
    def calculate_space_to_delete_in_order_to_upgrade(self):
        total_diskspace = 70000000
        required_space = 30000000
        used_space = self.root_directory.calculate_size()
        unused_space = total_diskspace - used_space
        needed_space = required_space - unused_space
        return needed_space

    def determine_directories_large_enough_to_free_up_enough_space_for_upgrade(self):
        needed_space = self.calculate_space_to_delete_in_order_to_upgrade()
        all_directories = self.list_all_directories()
        large_enough_directories = []
        for _, size in all_directories:
            if size >= needed_space:
                large_enough_directories.append(size)
        return large_enough_directories
    
    def determine_smallest_directory_to_delete_to_upgrade(self):
        directories = self.determine_directories_large_enough_to_free_up_enough_space_for_upgrade()
        directories.sort()
        return directories[0]

def solve_problem():
    data = extract_data_from_file(7, False)
    terminal = Terminal(data)
    terminal.read_output_to_create_directories()
    size = terminal.determine_smallest_directory_to_delete_to_upgrade()
    return size

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

# Idea to use classes from Patrick Clements
# Idea to organize classes around File and Directory:
# https://aoc.just2good.co.uk/2022/7
