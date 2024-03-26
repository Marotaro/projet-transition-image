import json
import os

# permet de stocker un int ou une liste dans un fichier donner (si le fichier
# n'existe pas il sera créer) si la liste contien des tuples, les tuples seront
# changés en des chaines de caractère avec les éléments séparer par une virgule


def store_in_file(value, name):
    with open(f'{name}.json', '+w') as f:
        if isinstance(value, list):
            object = [','.join(map(str, element)) if isinstance(
                element, tuple) else element for element in value]
            json_object = json.dumps(object, indent=len(object))
            f.write(json_object)
            f.close()
        else:
            json_object = json.dumps(value)
            f.write(json_object)
            f.close()


# supprime tous les fichier non nécessaire au fonctionnement initial du
# programme (fichier de stockage par exemple)
def remove_unnecessary_files():
    files_to_keep = ["main.py", "requirements.txt",
                     "store.py", "t.py", ".gitignore", ".git",]
    all_files = os.listdir(".")
    for file_name in all_files:
        if file_name not in files_to_keep:
            file_path = os.path.join(".", file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
    print(all_files)

# pour retransformer une ligne en tuple
def tup(element):
    pos = element.split(",")
    return (int(pos[0]), int(pos[1]))

# permet de récupérer les information d'un fichier, si le fichier contion un
# simple élément il retourera l'élément, si il contient une liste, il retournera
# une liste contenant les éléments, si ces éléments était des chaines de
# caractère ils sont convertis en tuples


def get_content(name):
    with open(f'{name}.json', 'r') as f:
        lines = json.load(f)
        if isinstance(lines, list):
            lines = [tup(element) if isinstance(element, str)
                     else element for element in lines]
        return lines
        # [(1,3),(3,2)]
        # [1,4,63,2]
        # 4


remove_unnecessary_files()
store_in_file([(1,3),(3,2)],"asud")
print(get_content("asud"))

# sources utilisées
# https://www.geeksforgeeks.org/read-json-file-using-python/
# https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
# https://www.geeksforgeeks.org/python-check-if-a-given-object-is-list-or-not/
# https://www.w3resource.com/python-exercises/python-basic-exercise-85.php
