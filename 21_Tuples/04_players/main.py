players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

# TODO здесь писать код

data = []
for sublist, sublist2 in players.items():
    flat_list = []
    for item in sublist:
        flat_list.append(item)
    for item in sublist2:
        flat_list.append(item)
    data.append(tuple(flat_list))
print(data)