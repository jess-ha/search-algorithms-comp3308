import sys
from algorithms.DFS import depth_first_search
from algorithms.BFS import breadth_first_search
from algorithms.IDS import iterative_deepening_search
from algorithms.Greedy import greedy
from algorithms.A_Star import a_star
from algorithms.Hill_Climbing import hill_climbing


def parse_input_file(filename):
    """
    Parses input file and returns start-state, goal-state and forbidden states.
    :param filename:
    :return:
    """
    with open(filename, "r") as infile:
        lines = infile.read().splitlines()
        if len(lines) == 3:
            forbid = lines.pop().split(",")
            goal = lines.pop()
            start = lines.pop()
        else:
            goal = lines.pop().strip()
            start = lines.pop()
            forbid = []
    return start, goal, forbid


def h_climbing():
    result_node, expanded_nodes = hill_climbing(start_state=start_state,
                                                goal_state=goal_state,
                                                forbidden=forbidden)

    print_solution(result_node=result_node,
                   expanded_nodes=expanded_nodes)


def A_star():
    result_node, expanded_nodes = a_star(start_state=start_state,
                                         goal_state=goal_state,
                                         forbidden=forbidden)

    print_solution(result_node=result_node,
                   expanded_nodes=expanded_nodes)


def Greedy():
    result_node, expanded_nodes = greedy(start_state=start_state,
                                         goal_state=goal_state,
                                         forbidden=forbidden)

    print_solution(result_node=result_node,
                   expanded_nodes=expanded_nodes)


def IDS():
    result_tree, expanded_nodes = iterative_deepening_search(start_state=start_state,
                                                             goal_state=goal_state,
                                                             forbidden=forbidden)

    print_solution(result_node=result_tree,
                   expanded_nodes=expanded_nodes)


def DFS():
    result_tree, expanded_nodes = depth_first_search(start_state=start_state,
                                                     goal_state=goal_state,
                                                     forbidden=forbidden)

    print_solution(result_node=result_tree,
                   expanded_nodes=expanded_nodes)


def BFS():
    search_tree, expanded_list = breadth_first_search(start_state=start_state,
                                                      goal_state=goal_state,
                                                      forbidden=forbidden)

    print_solution(result_node=search_tree,
                   expanded_nodes=expanded_list)


def print_solution(result_node, expanded_nodes):
    if result_node.value != goal_state:
        solution_path = 'No solution found.'
    else:
        reversed_path = result_node.ancestors()
        solution_path = reversed_path[::-1]
        solution_path.append(goal_state)

    if 'No solution' in solution_path:
        print(solution_path)
    else:
        path = ''
        for value in solution_path:
            if path == '':
                path = '{0}'.format(value)
            else:
                path = '{0},{1}'.format(path, value)
        print(path)
    expanded = ''
    for value in expanded_nodes:
        if expanded == '':
            expanded= '{0}'.format(value)
        else:
            expanded = '{0},{1}'.format(expanded, value)
    print(expanded)

if __name__ == '__main__':
    f_name = sys.argv[2]
    # Get details from input file.
    start_state, goal_state, forbidden = parse_input_file(f_name)

    keyword_to_search_map = dict(
        D=DFS,
        B=BFS,
        I=IDS,
        G=Greedy,
        A=A_star,
        H=h_climbing
    )

    keyword = sys.argv[1]
    try:
        keyword_to_search_map[keyword]()
    except KeyError:
        pass
        if keyword not in keyword_to_search_map.keys():
            print('You need to add an argument from your shell '
                  'which matches one of these: {}'.format(keyword_to_search_map.keys()))
            sys.exit()
