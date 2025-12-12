def update_inventory(inventory, shipment):
    inv = {}
    for item in inventory:inv[item[1]] = item[0]
    for item in shipment:
        if item[1] in inv:inv[item[1]] += item[0]
        else:inv[item[1]] = item[0]
    answer = []
    for item in inv:answer.append([inv[item], item])
    print(answer)
    return answer
