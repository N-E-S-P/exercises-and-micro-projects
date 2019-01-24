########## PROCESS DATA

def process_data(source_csv_file_path):
    import csv
    with open(source_csv_file_path, 'r', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [dict(x) for x in reader]
    return data

########## COMPLETENESS

def completeness(data):
    null_counter = 0
    value_counter = 0
    for row in data:
        for value in row:
            value_counter += 1
            if row[value] == ' ' or row[value] == '':
                null_counter += 1
    if null_counter == 0:
        print('Completeness: 100%')
        return
    else:
        c = (null_counter / value_counter) * 100
        percentage_c = 100 - c
        print("Completeness:", round(percentage_c, 2), "%")
    print('Total values:', value_counter)
    print('Null values:', null_counter)
    return

