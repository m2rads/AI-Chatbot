from extract_data import extractData

# Populates the trainer data from the json file
def populateTrainerData(path, parameter1, parameter2):
    menu = []
    data = extractData(path)
    if data != 'failed':
        for i in data:
            for j in range(0, len(data[i])):
                menu.append(data[i][j][parameter1].lower())
                menu.append(data[i][j][parameter2].lower())
        return menu
    else:
        return 