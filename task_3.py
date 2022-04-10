def file_reader_sort(format):
    b = 1
    file_dict = {}
    for v in range(3):
        with open(f"{b}.{format}", encoding="utf-8") as file:
            i = 0
            data = []
            for line in file:
                i += 1
                data.append(line)
            file_dict[f"{b}.txt"] = [f"{i}", data]
        b += 1
    sorted_values = sorted(file_dict.values())
    new_sorted_dictionary = {}
    for i in sorted_values:

        for k in file_dict.keys():

            if file_dict[k] == i:
                new_sorted_dictionary[k] = file_dict[k]

                break

    return new_sorted_dictionary


def file_writer(name):
    with open(f"{name}.txt", "w", encoding="utf-8") as file:
        for k, v in new.items():
            file.write(k)
            file.write("\n")
            for i in v:
                if type(i) == str:
                    file.write(i)
                    file.write("\n")
                elif type(i) == list:
                    for b in i:
                        file.write(b)
                    file.write("\n")


new = file_reader_sort("txt")
file_writer("sorted")
