def file_reader(file: str):
    cookbook = {}
    with open(file, encoding="utf-8") as f:
        for txt in f.read().split('\n\n'):
            food, q_i, *ingredients = txt.split('\n')
            info = []
            for arg in ingredients:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                info.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure})
            cookbook[food] = info
            result = cookbook
    return result


def get_shop_list_by_dishes(dishes: list, person_count):
    shoplist = {}
    for food in dishes:
        for i in file_reader("cookbook.txt").get(food):
            if i["ingredient_name"] not in shoplist:
                shoplist[i["ingredient_name"]] = {"quantity": i["quantity"] * person_count, "measure": i["measure"]}
            elif i['ingredient_name'] in shoplist:
                shoplist[i["ingredient_name"]] = {"quantity": i["quantity"] * person_count * dishes.count(food),
                                                  "measure": i["measure"]}
    return shoplist


print(get_shop_list_by_dishes(["Омлет", "Запеченный картофель", "Омлет"], 5))
