import csv

DATA_FILE_PATH = "data.csv"
DATA_HEADER = ["id", "title", "user_story", "acceptance_criteria", "business_value", "estimation", "status"]
STATUSES = ["planning", "todo", "in progress", "review", "done"]


def read_data():
    with open(DATA_FILE_PATH, "r") as file:
        data = list(csv.DictReader(file, delimiter=','))
    return data


def save_data(data):
    with open(DATA_FILE_PATH, "w") as file:
        writer = csv.DictWriter(file, fieldnames=DATA_HEADER, delimiter=',', lineterminator='\n')
        file.write(",".join(DATA_HEADER)+"\n")
        for i in data:
            writer.writerow(i)


def save_user_story(story):
    data = read_data()
    with open(DATA_FILE_PATH, "r") as file:
        story["id"] = len(file.readlines()) - 1
        story["status"] = "planning"
        data.append(story)
    save_data(data)


def update_user_story(story):
    data = read_data()
    for line in data:
        if int(line["id"]) == story["id"]:
            data[story["id"]] = story
    save_data(data)


def delete_user_story(id):
    data = read_data()
    for line in data:
        if int(line["id"]) == id:
            data.remove(line)
    for line in data:
        if int(line["id"]) > id:
            line["id"] = int(line["id"])-1
    save_data(data)
