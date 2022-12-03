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
    player_guide = row[2]
    score = score_round(opponent_move, player_guide)
    return score

def score_round(opponent_move, player_guide):
    opponent_points = convert_move_to_points(opponent_move)
    player_points = convert_guide_to_points(player_guide)
    score = player_points
    if player_points == 0:
        if opponent_points == 1:
            score += 3
        else:
            score += opponent_points - 1
    elif player_points == 3:
        score += opponent_points
    else:
        if opponent_points == 3:
            score += 1
        else:
            score += opponent_points + 1
    return score

def convert_move_to_points(move):
    if move == "A":
        return 1
    elif move == "B":
        return 2
    else:
        return 3

def convert_guide_to_points(guide):
    if guide == "X":
        return 0
    elif guide == "Y":
        return 3
    else:
        return 6

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
