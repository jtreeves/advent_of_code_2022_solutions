def extract_data_from_file():
    file = open("data.txt", "r")
    data = file.read()
    file.close()
    return data
