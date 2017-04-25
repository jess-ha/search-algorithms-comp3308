from algorithms.Node import Node


def iterative_deepening_search(start_state, goal_state, forbidden):
    start_node = Node(value=start_state,
                      parent=None,
                      changed=1000)
    expanded_list = []
    list_limit = 1000
    depth = 0
    while len(expanded_list) < 1000:
        # conduct depth limited search
        obtained_node, obtained_list = depth_limited_search(start_node=start_node,
                                                            goal_state=goal_state,
                                                            forbidden=forbidden,
                                                            max_depth=depth,
                                                            limit=list_limit)
        expanded_list += obtained_list
        list_limit -= len(obtained_list)
        depth += 1
        # If goal state reached, or expanded list max reached, return
        if obtained_node.value == goal_state or list_limit == 0:
            return obtained_node, expanded_list
    return obtained_node, expanded_list


def depth_limited_search(start_node, goal_state, forbidden, max_depth, limit):
    expanded_list = [start_node.value]
    if max_depth == 0:
        return start_node, expanded_list
    current_node = start_node
    # Maps state value to previously changed digit index.
    expanded_map = dict()
    expanded_map[start_node.value] = [start_node.changed]
    fringe = []
    while current_node.value != goal_state:
        # When the solution is as large as possible
        if len(expanded_list) == limit:
            return current_node, expanded_list

        if current_node.value in forbidden:
            if len(fringe) != 0:
                current_node = fringe.pop(0)

        if current_node.value not in forbidden:
            if current_node.depth < max_depth:
                # generate children the node
                current_node.generate_children()
                children = current_node.children
                children = children[::-1]
                for child in children:
                    if child.value not in forbidden:
                        # If we haven't seen a node of this value before
                        if child.value not in expanded_map.keys():
                            fringe.insert(0, child)
                        else:
                            if child.changed not in expanded_map[child.value]:
                                fringe.insert(0, child)
        # print([node.value for node in fringe])

        for node in fringe:
            if node.value in expanded_map.keys():
                if node.changed in expanded_map[node.value]:
                    fringe.remove(node)

        # an instance where no solution is found.
        if len(fringe) == 0:
            return current_node, expanded_list

        # get the next node to expand
        current_node = fringe.pop(0)
        if current_node.value in expanded_map.keys():
            if current_node.changed not in expanded_map[current_node.value]:
                # Add current node to list of expanded nodes
                expanded_list.append(current_node.value)
                if current_node.value not in expanded_map.keys():
                    expanded_map[current_node.value] = [current_node.changed]
                else:
                    expanded_map[current_node.value].append(current_node.changed)
        else:
            # Add current node to list of expanded nodes
            expanded_list.append(current_node.value)
            if current_node.value not in expanded_map.keys():
                expanded_map[current_node.value] = [current_node.changed]
            else:
                expanded_map[current_node.value].append(current_node.changed)

    return current_node, expanded_list
