def sort_empty_slots(sorted_list):
    for i in range(len(sorted_list)-1):
        if sorted_list[i] == "Empty slot":
            if sorted_list[i+1] != "Empty slot":
                sorted_list[i], sorted_list[i+1] = sorted_list[i+1], sorted_list[i]
            elif sorted_list[i+1] == "Empty slot":
                k = 2
                while i+k != len(sorted_list):
                    if sorted_list[i + k] != "Empty slot":
                        sorted_list[i], sorted_list[i+k] = sorted_list[i+k], sorted_list[i]
                    k += 1
    return sorted_list


if __name__ == "__main__":
    lista = [1, 2, "Empty slot", 7, "Empty slot", "Empty slot", 6]
    print(lista)
    print(sort_empty_slots(lista))