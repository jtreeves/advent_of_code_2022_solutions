def determine_if_interval_contains_other_interval(first_interval, second_interval):
    if (first_interval[0] <= second_interval[0] and first_interval[1] >= second_interval[1]) or (second_interval[0] <= first_interval[0] and second_interval[1] >= first_interval[1]):
        return True
    else:
        return False

def split_apart_assignments_from_pair(pair):
    assignments = pair.split(",")
    return assignments

def determine_endpoints_of_assignment_range(assignment):
    endpoints = assignment.split("-")
    return endpoints

print(determine_if_interval_contains_other_interval([2, 4], [6, 8]))
print(determine_if_interval_contains_other_interval([2, 8], [3, 7]))
print(determine_if_interval_contains_other_interval([6, 6], [4, 6]))