list = [9, 80, 16, 67, 35]

list_len = len(list)

for i in range(list_len):
    item = list[i]
    

    next_item = list[(i + 1) % list_len]

    result = item + next_item
    print(f"{result}")
