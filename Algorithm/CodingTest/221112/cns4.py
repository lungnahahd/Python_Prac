edges = [[1, 3], [1, 2], [2, 4], [2, 5]]

roots = [2, 3]

parents = [0 for _ in range(len(edges)+2)]
result = [0 for _ in range(len(edges))]
parents[1] = 1
edge_dict = dict()
for idx, edge in enumerate(edges):
    parents[edge[1]] = edge[0]
    edge_dict[(min(edge), max(edge))] = idx

# print(edge_dict)
print(parents)
for change_root in roots:
    if parents[change_root] == change_root:
        continue
    next_node = parents[change_root]
    parents[change_root] = change_root

    while True:
        if next_node == parents[next_node]:
            parents[next_node] = change_root
            result[edge_dict[min(parents[next_node], next_node),
                             max(parents[next_node], next_node)]] += 1
            break
        temp = parents[next_node]
        parents[next_node] = change_root
        result[edge_dict[min(parents[next_node], next_node),
                         max(parents[next_node], next_node)]] += 1
        change_root = next_node
        next_node = temp


print(result)
