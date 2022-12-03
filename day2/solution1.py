def solve_problem():
    file = open("data.txt", "r")
    data = file.read()
    file.close()
    rows = convert_multiline_string_to_array(data)
    total = calculate_total_score(rows)
    return total

def calculate_total_score(rows):
    total = 0
    for row in rows:
        total += score_row(row)
    return total

def score_row(row):
    opponent_move = row[0]
    player_move = row[2]
    opponent_points = convert_move_to_points(opponent_move)
    player_points = convert_move_to_points(player_move)
    difference_between_points = opponent_points - player_points
    value_between_points = abs(difference_between_points)
    score = player_points
    if value_between_points == 0:
        score += 3
    elif value_between_points == 1:
        if player_points > opponent_points:
            score += 6
    else:
        if player_points == 1:
            score += 6
    return score

def convert_move_to_points(move):
    if move == "A" or move == "X":
        return 1
    elif move == "B" or move == "Y":
        return 2
    else:
        return 3

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
