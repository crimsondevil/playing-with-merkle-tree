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

if __name__ == "__main__":
    new_Tree = m_Tree()
    leaf = sys.argv[1:]
    new_Tree.steps = leaf
    new_Tree.creation()
    old_Steps = new_Tree.get_Steps()
    #print ('Root : ', new_Tree.get_Root())
    json.dump(old_Steps, open("merkle.tree", "w"))
