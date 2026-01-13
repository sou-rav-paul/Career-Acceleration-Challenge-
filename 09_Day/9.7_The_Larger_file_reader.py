def file_reader(value):
    for i in range(value):
        line = f'line of {i}'
        yield line
        