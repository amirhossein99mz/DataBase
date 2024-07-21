def read_file(filename):
    try:
        with open(filename) as file1:
            file2 = file1.read()
    except OSError as err:
        print(err) 