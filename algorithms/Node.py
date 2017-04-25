class Node(object):
    def __init__(self, value, parent, heuristic=None, changed=None, depth=0):
        self.value = value
        self.parent = parent
        self.children = []
        self.expanded = False
        self.heuristic = heuristic
        self.changed = changed
        self.depth = depth
        self.f_n = 0

    def siblings(self):
        if self.parent is None:
            return None
        else:
            return self.parent.children

    def iter_ancestors(self):
        a = self
        while a.parent is not None:
            a = a.parent
            yield a.value

    def ancestors(self):
        return list(self.iter_ancestors())

    def generate_children(self, goal_node=None):
        digits = [int(digit) for digit in str(self.value)]
        for i in range(len(digits)):
            # subtract 1 from 1-9
            if i != self.changed:
                if digits[i] in range(1, 10):
                    self.append_child(digits[i] - 1, i, digits, goal_node)
                # add 1 to digits 0-8
                if digits[i] in range(9):
                    self.append_child(digits[i] + 1, i, digits, goal_node)

    def append_child(self, child_value, index, digits, goal_node):
        # Create new child value in a very not-elegant way.
        if index == 0:
            new_value = '{0}{1}{2}'.format(child_value, digits[1], digits[2])
        if index == 1:
            new_value = '{0}{1}{2}'.format(digits[0], child_value, digits[2])
        if index == 2:
            new_value = '{0}{1}{2}'.format(digits[0], digits[1], child_value)

        new_child = Node(value=new_value, parent=self, changed=index, depth=(self.depth+1))
        if goal_node is not None:
            # Generate Manhattan heuristic
            h_n = 0
            for j in range(3):
                h_n += abs(int(new_child.value[j]) - int(goal_node[j]))
            new_child.heuristic = h_n
            cost = len(new_child.ancestors())
            new_child.f_n = new_child.heuristic + cost
        self.children.append(new_child)

