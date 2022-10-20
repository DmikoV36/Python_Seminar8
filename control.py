import json

data_base = []

def load():
    global data_base
    with open("student_data_base.json", "r", encoding="utf-8") as fh:
        data_base = json.load(fh)
    print("База учеников успешно была загружена")

def ent_stud(list):
    with open("student_data_base.json", "w", encoding="utf-8") as fh:
        data_base.append(list)
        fh.write(json.dumps(data_base,ensure_ascii=False))
    print (f"Инфомация: {ent_stud} добавлена в систему.")