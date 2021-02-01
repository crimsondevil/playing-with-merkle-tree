import json, sys

def get_path(tree, node):
    search_node = node
    path = []
    while 1:
        prev_node = search_node
        for key in tree.keys():
            if search_node in key:
                search_node = tree[key]
                break
        if prev_node == search_node:
            break
        path.append(search_node)
    return path

if __name__ == "__main__":
    tree = json.load(open("merkle.tree"))
    if sys.argv[1] in tree.keys():
        print("Yes.", get_path(tree, sys.argv[1]))
    else:
        print ("No.")
