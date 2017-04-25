from algorithms.Node import Node


def greedy(start_state, goal_state, forbidden):
    if start_state == goal_state:
        return start_state

    h = 0
    for i in range(len(start_state)):
        h += abs(int(start_state[i]) - int(goal_state[i]))

    current_node = Node(value=start_state, parent=None, heuristic=h)
    expanded_map = dict()
    expanded_list = []
    fringe = []

    while current_node.value != goal_state:
        # Expand node
        expanded_list.append(current_node.value)

        # expanded list is not permitted to exceed 1000
        if len(expanded_list) == 1000:
            return current_node, expanded_list

        # add to dict
        if current_node.value not in expanded_map.keys():
            # no nodes with this value previously expanded
            expanded_map[current_node.value] = []
            expanded_map[current_node.value].append(current_node.changed)
        else:
            expanded_map[current_node.value].append(current_node.changed)

        # generate children
        current_node.generate_children(goal_node=goal_state)

        # Add children of expanded node to fringe
        children = current_node.children
        while len(children) != 0:
            child = children.pop(0)
            if child.value not in forbidden:
                if child.value in expanded_map.keys():
                    if child.changed not in expanded_map[child.value]:
                        insert_element(child, fringe)
                else:
                    insert_element(child, fringe)
        # print([node.value for node in fringe])
        # print([node.heuristic for node in fringe])
        # If there is no solution
        if len(fringe) == 0:
            return current_node, expanded_list

        current_node = fringe.pop(0)
    expanded_list.append(current_node.value)
    return current_node, expanded_list


def insert_element(child, fringe):
    if len(fringe) != 0:
        for i in range(len(fringe)):
            if fringe[i].heuristic >= child.heuristic:
                fringe.insert(i, child)
                break
    else:
        fringe.append(child)
