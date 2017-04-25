from algorithms.Node import Node


def breadth_first_search(start_state, goal_state, forbidden=[]):
    current_node = Node(parent=None, value=start_state)
    # Maps state value to previously changed digit index.
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
        current_node.generate_children()

        # Add children of expanded node to fringe
        children = []
        for child in current_node.children:
            if child.value not in forbidden:
                children.append(child)

        fringe += children

        # print([node.value for node in fringe])

        # select first node from the fringe to expand next.
        for unexpanded in fringe:
            # if we've expanded a node of similar value previously
            if unexpanded.value in expanded_map.keys():
                # check if it is the same node
                if unexpanded.changed in expanded_map[unexpanded.value]:
                    # remove it from the fringe if we've expanded this node before
                    del unexpanded
                else:
                    # otherwise make this the current node and stop iterating through the fringe
                    current_node = unexpanded
                    del unexpanded
                    break
            else:
                # this is a value we haven't seen before.
                current_node = unexpanded
                del unexpanded
                break

        # No solution found.
        if len(fringe) == 0 and current_node.value != goal_state:
            return current_node, expanded_list

    # We found the goal node!
    expanded_list.append(current_node.value)
    return current_node, expanded_list
