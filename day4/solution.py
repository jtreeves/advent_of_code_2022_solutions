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

# print(determine_if_one_interval_contains_other_interval([2, 4], [6, 8]))
# print(determine_if_one_interval_contains_other_interval([2, 8], [3, 7]))
# print(determine_if_one_interval_contains_other_interval([6, 6], [4, 6]))
# print(find_endpoints_of_assignment_range("2-8"))
# print(find_endpoints_of_assignment_range("172-893"))
print(calculate_total_of_all_complete_overlaps(["2-4,6-8","2-3,4-5","5-7,7-9","2-8,3-7","6-6,4-6","2-6,4-8"]))