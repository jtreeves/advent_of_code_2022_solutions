def determine_forest_length(forest):
    rows = forest.split("\n")
    length = len(rows)
    return length

def determine_forest_width(forest):
    rows = forest.split("\n")
    width = len(rows[0])
    return width

def create_rows_of_trees(forest):
    string_rows = forest.split("\n")
    list_rows = []
    for string_row in string_rows:
        list_row = []
        for string in string_row:
            list_row.append(int(string))
        list_rows.append(list_row)
    return list_rows

def create_columns_of_trees(forest):
    width = determine_forest_width(forest)
    rows = forest.split("\n")
    columns = []
    for i in range(width):
        column = []
        for row in rows:
            column.append(int(row[i]))
        columns.append(column)
    return columns

print(create_rows_of_trees("30373\n25512\n65332\n33549\n35390"))
print(create_columns_of_trees("30373\n25512\n65332\n33549\n35390"))
# print(determine_forest_width("30373\n25512\n65332\n33549\n35390"))