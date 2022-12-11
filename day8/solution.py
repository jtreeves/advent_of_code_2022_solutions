def count_all_visible_trees(forest):
    length = determine_forest_length(forest)
    width = determine_forest_width(forest)
    rows = create_rows_of_trees(forest)
    columns = create_columns_of_trees(forest)
    total = calculate_forest_perimeter(length, width)
    print(f"STARTING TOTAL WITH PERIMETER: {total}")
    for row_index in range(1, len(rows) - 1):
        for column_index in range(1, len(columns) - 1):
            visible = check_if_visible_at_all(rows[row_index], columns[column_index], row_index, column_index)
            if visible:
                print(f"VISIBLE TREE ROW {row_index}, COLUMN {column_index}")
                total += 1
    return total

def check_if_visible_at_all(row_list, column_list, row_index, column_index):
    top = check_if_visible_from_top(column_list, row_index)
    bottom = check_if_visible_from_bottom(column_list, row_index)
    left = check_if_visible_from_left(row_list, column_index)
    right = check_if_visible_from_right(row_list, column_index)
    visible = top or bottom or left or right
    return visible

def check_if_visible_from_left(row_list, column_index):
    tree_height = row_list[column_index]
    left_trees = row_list[:column_index]
    for tree in left_trees:
        if tree >= tree_height:
            return False
    return True

def check_if_visible_from_right(row_list, column_index):
    tree_height = row_list[column_index]
    right_trees = row_list[column_index:]
    for tree in right_trees:
        if tree >= tree_height:
            return False
    return True

def check_if_visible_from_top(column_list, row_index):
    tree_height = column_list[row_index]
    top_trees = column_list[:row_index]
    for tree in top_trees:
        if tree >= tree_height:
            return False
    return True

def check_if_visible_from_bottom(column_list, row_index):
    tree_height = column_list[row_index]
    bottom_trees = column_list[row_index:]
    for tree in bottom_trees:
        if tree >= tree_height:
            return False
    return True

def calculate_forest_perimeter(length, width):
    perimeter = 2 * (length + width)
    overlap = 4
    perimeter_without_overlap = perimeter - overlap
    return perimeter_without_overlap

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

# print(create_rows_of_trees("30373\n25512\n65332\n33549\n35390"))
# print(create_columns_of_trees("30373\n25512\n65332\n33549\n35390"))
# print(determine_forest_width("30373\n25512\n65332\n33549\n35390"))
# print(calculate_forest_perimeter(5, 7))
# print(check_if_visible_from_left([2, 5, 5, 1, 2], 1))
# print(check_if_visible_from_right([2, 5, 5, 1, 2], 1))
# print(check_if_visible_from_top([0, 5, 5, 3, 5], 1))
# print(check_if_visible_from_bottom([0, 5, 5, 3, 5], 1))
# print(check_if_visible_at_all([2, 5, 5, 1, 2], [0, 5, 5, 3, 5], 1, 1))
# print(check_if_visible_at_all([3, 3, 5, 4, 9], [0, 5, 5, 3, 5], 3, 1))
print(count_all_visible_trees("30373\n25512\n65332\n33549\n35390"))