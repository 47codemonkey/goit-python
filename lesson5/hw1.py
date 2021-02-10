import re


def normalize(strg):
    my_set = strg.maketrans("абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
                              "abvgdeëžzijklmnoprstufhcčššъyьèûâ")
    my_list = []
    
    for elem in strg:
        if elem == elem.lower():
            trans = elem.translate(my_set)
        elif elem == elem.upper():
            trans = elem.lower().translate(my_set).upper()
        my_list.append(trans)
        
    s = re.sub(r'(\W)', '_', ''.join(my_list))
    return s

strg = input("Введите строку: ")

print(normalize(strg))