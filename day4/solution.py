def solve_problem():
    data = extract_data_from_file(4)
    pairs = convert_multiline_string_to_array(data)
    complete_overlaps = calculate_total_of_all_complete_overlaps(pairs)
    partial_overlaps = calculate_total_of_all_partial_overlaps(pairs)
    return {
        "complete": complete_overlaps,
        "partial": partial_overlaps
    }

def calculate_total_of_all_partial_overlaps(pairs):
    total = 0
    for pair in pairs:
        assignments = split_apart_assignments_from_pair(pair)
        first_assignment = assignments[0]
        second_assignment = assignments[1]
        first_interval = find_endpoints_of_assignment_range(first_assignment)
        second_interval = find_endpoints_of_assignment_range(second_assignment)
        overlap = determine_if_one_interval_overlaps_with_other_interval(first_interval, second_interval)
        if overlap:
            total += 1
    return total

def calculate_total_of_all_complete_overlaps(pairs):
    total = 0
    for pair in pairs:
        assignments = split_apart_assignments_from_pair(pair)
        first_assignment = assignments[0]
        second_assignment = assignments[1]
        first_interval = find_endpoints_of_assignment_range(first_assignment)
        second_interval = find_endpoints_of_assignment_range(second_assignment)
        overlap = determine_if_one_interval_contains_other_interval(first_interval, second_interval)
        if overlap:
            total += 1
    return total

def determine_if_one_interval_overlaps_with_other_interval(first_interval, second_interval):
    first_set = create_set_of_integers_over_range(first_interval[0], first_interval[1])
    second_set = create_set_of_integers_over_range(second_interval[0], second_interval[1])
    overlap = first_set.intersection(second_set)
    overlapped_list = list(overlap)
    if len(overlapped_list):
        return True
    else:
        return False

def determine_if_one_interval_contains_other_interval(first_interval, second_interval):
    if (first_interval[0] <= second_interval[0] and first_interval[1] >= second_interval[1]) or (second_interval[0] <= first_interval[0] and second_interval[1] >= first_interval[1]):
        return True
    else:
        return False

def split_apart_assignments_from_pair(pair):
    assignments = pair.split(",")
    return assignments

def find_endpoints_of_assignment_range(assignment):
    endpoints = []
    string_values = assignment.split("-")
    for value in string_values:
        endpoints.append(int(value))
    return endpoints

def create_set_of_integers_over_range(lower_endpoint, upper_endpoint):
    ranged_list = [item for item in range(lower_endpoint, upper_endpoint + 1)]
    ranged_set = set(ranged_list)
    return ranged_set

def extract_data_from_file(day_number):
    file = open(f"day{day_number}/data.txt", "r")
    data = file.read()
    file.close()
    return data

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

result = solve_problem()
print(result)
