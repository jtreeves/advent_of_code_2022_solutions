def solve_problem():
    file = open("data.txt", "r")
    read_file = file.read()
    file.close()
    chunks = create_chunks_of_numbers(read_file)
    totals = sum_totals_of_each_chunk(chunks)
    largest = find_largest_total(totals)
    return largest

def create_chunks_of_numbers(data):
    chunks = []
    while len(data):
        first_empty_line = data.find("\n\n")
        if first_empty_line != -1:
            data_before = data[0:first_empty_line]
            chunks.append(data_before)
            data = data[first_empty_line+2:]
        else:
            chunks.append(data)
            data = ''
    return chunks

def sum_totals_of_each_chunk(chunks):
    total_values = []
    for chunk in chunks:
        values = []
        while len(chunk):
            first_line_break = chunk.find("\n")
            if first_line_break != -1:
                content_before = chunk[0:first_line_break]
                values.append(int(content_before))
                chunk = chunk[first_line_break+1:]
            else:
                values.append(int(chunk))
                chunk = ''
        total = sum(values)
        total_values.append(total)
    return total_values

def find_largest_total(totals):
    totals.sort()
    return totals[-1]

result = solve_problem()
print(result)
