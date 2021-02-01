import hashlib, json, sys
from collections import OrderedDict

class m_Tree:

    def __init__(node, steps=None):
        node.steps = steps
        node.old_Steps = OrderedDict()

    def creation(node):
        steps = node.steps
        old_Steps = node.old_Steps
        tmp = []

        for i in range(0, len(steps),2):
            lnode = steps[i]
            if i+1 != len(steps):
                rnode = steps[i+1]
            else:
                rnode = ''
            lhash = hashlib.sha256(lnode.encode('utf-8'))
            if rnode != '':
                rhash = hashlib.sha256(rnode.encode('utf-8'))
            old_Steps[steps[i]] = lhash.hexdigest()
            if rnode != '':
                old_Steps[steps[i+1]] = rhash.hexdigest()
            if rnode != '':
                tmp.append(lhash.hexdigest()+rhash.hexdigest())
            else:
                tmp.append(lhash.hexdigest())

        if len(steps) != 1:
            node.steps = tmp
            node.old_Steps = old_Steps
            node.creation()

    def get_Steps(node):
        return node.old_Steps

    def get_Root(node):
        next = list(node.old_Steps.keys())[-1]
        return node.old_Steps[next]


def validate(old_root, new_root, new_Old_Steps):
    curr_node = old_root
    path = [curr_node]
    while curr_node != new_root:
        prev_node = curr_node
        for key, value in new_Old_Steps.items():
            if curr_node in key:
                curr_node = value
                path.append(curr_node)
                break
        if prev_node == curr_node:
            break
    if old_root == new_root:
        return "Yes", path
    elif len(path) == 1:
        return "No"
    else:
        return "Yes", path

def parse_input(args):
    s = "".join(args[1:])
    old, new, _ = s.split(']')
    old = old.split(',')
    new = new.split(',')
    old[0] = old[0][1:].strip() if old[0].startswith('[') else old[0]
    new[0] = new[0][1:].strip() if new[0].startswith('[') else new[0]
    return old, new

if __name__ == "__main__":
    old_input, new_input = parse_input(sys.argv)
    old_tree = m_Tree()
    old_leaf = old_input
    old_tree.steps = old_leaf
    old_tree.creation()
    old_Steps = old_tree.get_Steps()
    old_root = old_tree.get_Root()
    #print ('old_root : ', old_root)
    #print (json.dumps(old_Steps, indent=4))

    new_tree = m_Tree()
    new_leaf = new_input
    new_tree.steps = new_leaf
    new_tree.creation()
    new_Old_Steps = new_tree.get_Steps()
    new_root = new_tree.get_Root()
    #print ('new_root : ', new_root)
    #print (json.dumps(new_Old_Steps, indent=4))
    file_op = [old_Steps, new_Old_Steps]
    json.dump(file_op, open('merkle.trees', 'w'))
    print (validate(old_root, new_root, new_Old_Steps))
