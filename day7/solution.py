import copy

def solve_problem():
    data = extract_data_from_file(7)
    contents = extract_contents_of_directories(data)
    print(f"CONTENTS: {contents}")
    sizes = determine_total_sizes_of_all_directories(contents)
    filtered_sizes = filter_out_too_large_directories(sizes)
    total = sum_all_directories(filtered_sizes)
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

# result = solve_problem()
# print(result)


contents = {'/': {'btsgrbd': {'cmfdm': {'gldnjj': {'dvght': {'tfbzq': {'tcghw.srg': 276592}}, 'lwvtzd.pws': 93750, 'sdwnsgwv.mjm': 176529, 'vmpgqbcd': 100111}, 'vhf': {'hfm.rfp': 240217, 'nblfzrb': {'jhc': 160378}}}, 'cqd': {'bnddfgrb': 305358, 'dwqncqp': {'slpgmhv': 122570, 'zlnbcwr': 278461}, 'hnnfdtbh': {'gfprhn.rjj': 334830}, 'jhc': {'fgb.btb': 179593}, 'nblfzrb': {'jhc': 160378}, 'scnm.qbf': 327762, 'vmpgqbcd': 165080, 'vzgwwjq.zbp': 190041, 'zwv': {'jhc': 40349, 'pqwml': {'hbzvzwpr': 193573}, 'sdwnsgwv.mjm': 173804}}, 'gvwvs': {'gjslw': {'gzbm': {'fst': {'mqpg': 99806}, 'gpjz': {'dnsvsp': {'vmdbpwj': {'jhc': 258373}, 'zvspnvfr': {'vzgwwjq.zbp': 18241}}, 'jhc.dfd': 218828}, 'gzd': {'chdfwj': 20383, 'prrlv.rvn': 63309}, 'hfm': {'qhh': 291753}}}, 'gwz': {'hfm.hpn': 29042, 'mpc': 184043, 'sdwnsgwv.mjm': 230539, 'zlnbcwr': 803}, 'ljvrjp': {'pfltqw.zvc': 44312}, 'sltlpb': {'sdwnsgwv.mjm': 321945}, 'vbsnq': {'twbbg.ftq': 7774, 'zpqbp.cts': 109546}}, 'nblfzrb': {'jhc': 160378}, 'nfm': {'fwmfmtt.hdg': 327853, 'vdjs': 151272, 'wznwjfw': {'nblfzrb': {'jhc': 160378}, 'zvspnvfr': {'vzgwwjq.zbp': 18241}}, 'zlnbcwr': 75692}, 'qwnml.bqn': 293979, 'sdwnsgwv.mjm': 159220, 'vzgwwjq.zbp': 327978, 'zvspnvfr.zbc': 155479}, 'cprq.fmm': 3868, 'gcbpcf': {'gfprhn.rjj': 295086, 'ldwwls': {'sdwnsgwv.mjm': 175977}, 'nblfzrb': {'jhc': 160378}, 'zvspnvfr': {'vzgwwjq.zbp': 18241}, 'zwv': {'jhc': 40349, 'pqwml': {'hbzvzwpr': 193573}, 'sdwnsgwv.mjm': 173804}}, 'hfm': {'qhh': 291753}, 'lthcng.gnf': 324644, 'nblfzrb.mrr': 133181, 'sfrbjmmh.jnj': 140568, 'tfsh': {'fbrqvwgr': {'nrhm': 244821}}, 'vlsqgrw': {'dzdd': {'hjmv': {'hfm.qcd': 91558}}, 'fst.rjm': 18805, 'gfprhn.rjj': 50694, 'jlnrm': 55025, 'pnsbfz': {'bmgmh': {'dvh': {'jhc': {'fgb.btb': 179593}, 'jtp': {'clh': {'sdwnsgwv.mjm': 54117}}, 'rzlt.llb': 85638}, 'mwfbthpj': {'zwslwbr.chm': 75900}, 'swqbph': {'jrlljc.ntl': 307258}}, 'nblfzrb': {'jhc': 160378}, 'zvfg': {'zvspnvfr.dqj': 311338}}, 'qjjjgd': {'cdmwgn': {'bttff': {'nblfzrb': {'jhc': 160378}}}, 'fqmln': {'cjgh': 282233}, 'gfprhn.rjj': 285733, 'gswsc': {'ccjg.zml': 153758, 'cllgt': {'vmpgqbcd': 132862}, 'ctqdpq.clq': 257967, 'jhc': 117673, 'wqcz.tww': 258604, 'zvspnvfr.grb': 122135}, 'htpzdb': {'hfm': {'qhh': 291753}, 'mlplp': {'zhcq.gzj': 256802}, 'nblfzrb': 231759, 'pqpbjbqp': 159823, 'vzgwwjq.zbp': 25382}, 'jwc': 261929, 'lvzpqqv': {'cgj': {'nblfzrb.lcc': 74595}, 'mdb': {'zvspnvfr.ldc': 167891}, 'shpdtb': {'bvff.hsf': 45889, 'sdwnsgwv.mjm': 92447}}, 'mlc': {'mrblf': 7978}, 'mzbpmhf': {'jhbs': 38713}, 'sdwnsgwv.mjm': 329303, 'vmpgqbcd': 76120}, 'whrtnh': {'jbbwzd': {'jhc.qqw': 88613}, 'nblfzrb': {'jhc': 160378}}, 'zggjjcct.fsz': 28406}, 'vmpgqbcd': 202279}}

directory_names = list_all_directories(contents)
print(directory_names)

names = ['/', 'btsgrbd', 'cmfdm', 'gldnjj', 'dvght', 'tfbzq', 'vhf', 'nblfzrb', 'cqd', 'dwqncqp', 'hnnfdtbh', 'jhc', 'nblfzrb', 'zwv', 'pqwml', 'gvwvs', 'gjslw', 'gzbm', 'fst', 'gpjz', 'dnsvsp', 'vmdbpwj', 'zvspnvfr', 'gzd', 'hfm', 'gwz', 'ljvrjp', 'sltlpb', 'vbsnq', 'nblfzrb', 'nfm', 'wznwjfw', 'nblfzrb', 'zvspnvfr', 'gcbpcf', 'ldwwls', 'nblfzrb', 'zvspnvfr', 'zwv', 'pqwml', 'hfm', 'tfsh', 'fbrqvwgr', 'vlsqgrw', 'dzdd', 'hjmv', 'pnsbfz', 'bmgmh', 'dvh', 'jhc', 'jtp', 'clh', 'mwfbthpj', 'swqbph', 'nblfzrb', 'zvfg', 'qjjjgd', 'cdmwgn', 'bttff', 'nblfzrb', 'fqmln', 'gswsc', 'cllgt', 'htpzdb', 'hfm', 'mlplp', 'lvzpqqv', 'cgj', 'mdb', 'shpdtb', 'mlc', 'mzbpmhf', 'whrtnh', 'jbbwzd', 'nblfzrb']