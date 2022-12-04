def split_apart_assignments_from_pair(pair):
    assignments = pair.split(",")
    return assignments

def determine_endpoints_of_assignment_range(assignment):
    endpoints = assignment.split("-")
    return endpoints