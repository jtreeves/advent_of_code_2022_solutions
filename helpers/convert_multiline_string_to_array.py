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
