def file_reader(file: str):
    with open(file, encoding="utf-8") as f:
        cookbook = {}
        for txt in f.read().split('\n\n'):
            food, q_i, *ingredients = txt.split('\n')
            info = []
            for arg in ingredients:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                info.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cookbook[food] = info
        return print(cookbook)


file_reader("cookbook.txt")
