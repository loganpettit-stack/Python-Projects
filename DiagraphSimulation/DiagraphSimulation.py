"""
Author: Logan Pettit
Date: September 2, 2019
Class: 4500 Introduction to the Software Profession
Description: This program is a game that will create a Digraph based on the given input file provided, The first line
of the file will describe the amount of nodes that will be in the game, the game will require between 2 and 20 nodes.
The second line describes the direction of the arrows. 3 1 would represent an arrow that has a tail at node 3 and a head
at 1. The game will play choosing random paths to traverse each node until each node has been visited at least once. For
every node to be visited at least once the graph will need to be described as a strongly connected graph. This means that
every node must have an arrow to visit and also an arrow to leave the node, so our program does not get stuck. The input
 file for this program must be set up in a specific way to get it to run. Every node must have an arrow going to and from
the node, meaning the graph must be strongly connected. The number of arrows listed in line 2, must match the number of
arrows being described in the lines after with each line being formatted "head" "space" "tail". The game will run for 10
simulations of the game taking different paths each time a new game is started, statistics on all the games that took place
are then output to an output file. The Structures used in this program was mostly lists. A dictionary of lists stores
 the node value and the tails associated with that node we then choose a random path to traverse too incrementing a second
list the size of the total nodes. Each element in the second list represents a node and once each element in that list
 is greater than 0 the game will end and calculate some results based on how it was played. Go ahead play the game, just
 make sure your input file is correctly set up!
Here is an example input file format:
4
5
1 2
2 3
3 4
4 1
2 3
"""

import random
from collections import defaultdict


# Function taken from numpy import
def trim_zeros(filt, trim='fb'):
    first = 0
    trim = trim.upper()
    if 'F' in trim:
        for i in filt:
            if i != 0.:
                break
            else:
                first = first + 1
    last = len(filt)
    if 'B' in trim:
        for i in filt[::-1]:
            if i != 0.:
                break
            else:
                last = last - 1
    return filt[first:last]


# This function checks the file to make sure the format is set up properly
def check_file_format():
    line_count = 0
    try:
        with open("HW2PettitOutfile.txt", "w") as outFile1:
            try:
                with open("HW2infile.txt") as checkFile:
                    n = checkFile.readline()
                    k = checkFile.readline()
                    try:
                        if n == "\n" or len(n) < 1:
                            outFile1.write("Input File formatting Error: Line 1 in the input file represents the number of nodes, you should have 2 - 11 nodes")
                            print("Input File formatting Error: Line 1 in the input file represents the number of nodes, you should have 2 - 11 nodes")
                            exit(1)
                        if k == "\n":
                            outFile1.write("Input File formatting Error: Line 2 in the input file represents the number of arrows in the game please enter "
                                           "the pairs for the edges as well as the number of pairs there are on line 2, the pairs"
                                           "will come after line 2.")
                            print("Input File formatting Error: Line 2 in the input file represents the number of arrows in the game please enter the pairs for "
                                  "the edges as well as the number of pairs there are on line 2, the pairs"
                                  "will come after line 2.")
                            exit(1)
                        for lines in checkFile:
                            line_count += 1
                        if line_count != int(k):
                            outFile1.write("Input File formatting Error: The number of edge pairs does not match the number of edge pairs declared, there may"
                                           "be a blank line at the end of the file.")
                            print("Input File formatting Error: The number of edge pairs does not match the number of edge pairs declared, there may be a blank"
                                  "line at the end of the file.")
                            exit(1)
                        if int(n) < 2 or int(n) >= 21:
                            outFile1.write("Input File formatting Error: Please enter a number on line 1 for the nodes between 2 and 20")
                            print("Input File formatting Error: Please enter a number on line 1 for the nodes between 2 and 20")
                            exit(1)
                    except ValueError:
                        print("Input File formatting Error: Check line 1 and line 2 to make sure they are integers in the input"
                              " file for the number of circles and number of arrows")
                        outFile1.write("Input File formatting Error: Check line 1 and line 2 to make sure they are integers in "
                                       "the input file for the number of circles and number of arrows")
                        exit(1)
            except FileNotFoundError:
                print("File does not exist!")
                exit(1)
    except FileNotFoundError:
        print("File does not exist!")
        exit(1)


# This function checks to make sure every node is visited and checks
# to make sure there are no pairs that are larger than the nodes declared
def check_pairs(edge_list, node):
    check_array = []

    # check for an edge head going to a node
    for pair in edge_list:

        # check for the file to contain all pairs
        if len(pair) >= 2:
            edge_head = pair[1]
            tail = pair[0]
            if node == int(edge_head):

                # check for a tail leaving the node
                for pair2 in edge_list:
                    edge_tail = pair2[0]
                    if edge_tail == node:
                        check_array.append(int(edge_tail))

            # Check that heads and tails are not larger than nodes being used
            with open("HW2PettitOutfile.txt", "w") as outF:
                if edge_head > int(N):
                    outF.write("Input File formatting Error: There is an edge that traverses to a nonexistent node")
                    print("Input File formatting Error: There is an edge that traverses to a nonexistent node")
                    exit(1)
                if tail > int(N):
                    outF.write("Input File formatting Error: There is an edge that traverses to a nonexistent node")
                    print("Input File formatting Error: There is an edge that traverses to a nonexistent node")
                    exit(1)
        else:
            print("Input File formatting Error: One of the lines in the file does not represent a pair.")
            with open("HW2PettitOutfile.txt", "w") as outF:
                outF.write("Input File formatting Error: One of the lines in the file does not represent a pair.")
            exit(1)


def check_graph():
    # node_check = [0] * int(N)
    node_check = []
    n = 1

    # store nested lists of nodes visited in node_check array
    while n <= int(N):
        # node_check[int(n - 1)] = check_traversal(graph, n)
        node_check.append(check_traversal(graph, n))
        n += 1

    # check if each nested list is the size of the total nodes
    i = 1
    while i < int(N):
        if len(node_check[i]) < int(N):
            with open("HW2PettitOutfile.txt", "w") as outFile1:
                outFile1.write("Graph Format Error: Your graph is not a strongly connected graph, make sure every node can be visited"
                      " and be exited.")
                print("Graph Format Error: Your graph is not a strongly connected graph, make sure every node can be visited"
                      " and be exited.")
                exit(1)
        i += 1


def check_traversal(graph, n):
    visited = []
    check_array = [n]
    i = 0

    # Traverse the path starting from node n,
    # as it comes to new nodes store them in the visited array
    while check_array:

        node = check_array.pop(0)
        if node not in visited:
            visited.append(node)
            options = graph[node]

            for option in options[i]:
                check_array.append(option)
                check_array = trim_zeros(check_array)
    return visited


# Check to see if the array has no zeros in it
# this indicates the game is complete
def node_array_check(node_array):
    zero_count = 0
    for x in node_array:
        if x == 0:
            zero_count += 1
    if zero_count == 0:
        return False
    else:
        return True


# Obtain a random element from traversal options
def get_random_array_element(k):

    # use trim zeros to get rid of trailing zeros
    for x in graph[k]:
        return random.choice(trim_zeros(x))


# Graph traversal function
def traversal():
    nodes_visited_array = [0] * int(N)
    get_random_array_element(1)
    nodes_visited_array[0] += 1
    location = 1
    traversal_check = 0

    while node_array_check(nodes_visited_array):
        location = get_random_array_element(location)
        current_node = location
        nodes_visited_array[current_node - 1] += 1

        if traversal_check > 1000000:
            with open("HW2PettitOutfile.txt", "w") as outFile:
                print("Vsits exceeded 1,000,000")
                outFile.write("Visits exceeded 1,000,000")
                exit(1)
        traversal_check += 1

    return nodes_visited_array


# function to create digraph game structure
def create_graph(N):
    graph = defaultdict(list)

    # Set up a matrix to store the head of an edge that
    # contains a tail matching that nodes value
    w, h = int(N), int(N) + 1
    matrix = [[0 for x in range(w)] for y in range(h)]

    counter = 0
    i = 1
    j = 0

    # loop through pairs in edge list determining if the tail matches the
    # The node number if so store the head of the edge to the matrix to
    # gather the traversal options, append that to the node represented as a
    # key in the dictionary
    while i <= int(N):
        for pairs in edgeList:
            head = pairs[1]
            tail = pairs[0]

            if tail == i:
                matrix[i][j] = head
                j += 1
                counter += 1

        graph[i].append(matrix[i])
        j -= counter
        i += 1
        counter = 0

    return graph


# Function provides end game output information
def output_game_information():
    # with open("HW2PettitOutfile.txt", "w") as outFile:
    txt = "Circles used this game {}\n"
    print(txt.format(int(N)))
    # outFile.write(txt.format(int(N)))

    txt1 = "Arrows this game: {}\n"
    print(txt1.format(int(K)))
    # outFile.write(txt1.format(int(K)))

    txt2 = "Total checks on each circle this game: {}\n"
    array_sum = sum(nodes_visited_array)
    print(txt2.format(array_sum))
    # outFile.write(txt2.format(array_sum))

    average_total_checks = total_checks / game_simulations
    txt3 = "Average number of total checks per game: {}\n"
    print(txt3.format(average_total_checks))
    # outFile.write(txt3.format(average_total_checks))

    txt4 = "The max number of checks in a circle this game: {}\n"
    print(txt4.format(max(nodes_visited_array)))
    # outFile.write(txt4.format(max(nodes_visited_array)))

    txt5 = "The graph: {}"
    print(txt5.format(graph))

    txt6 = "Array storing node visits: {}\n"
    print(txt6.format(nodes_visited_array))


def end_sim_output():
    with open("HW2PettitOutfile.txt", "w") as outFile:
        print("End game simulations output: \n")
        outFile.write("End game simulations output: \n")

        average = total_checks / game_simulations
        txt7 = "The average number of total checks per game: {}\n"
        print(txt7.format(average))
        outFile.write(txt7.format(average))

        max_totalchecks = max(total_checks_each_game)
        txt8 = "The maximum number of total checks in a single game: {}\n"
        print(txt8.format(max_totalchecks))
        outFile.write(txt8.format(max_totalchecks))

        min_totalchecks = min(total_checks_each_game)
        txt9 = "The minimum number of total checks in a single game: {}\n"
        print(txt9.format(min_totalchecks))
        outFile.write(txt9.format(min_totalchecks))

        avg_checks = total_checks / game_simulations
        txt10 = "The average number of checks on a single circle over all the games: {}\n"
        print(txt10.format(avg_checks))
        outFile.write(txt10.format(avg_checks))

        txt11 = "The maximum number of single circle checks: {}\n"
        print(txt11.format(max_visits))
        outFile.write(txt11.format(max_visits))

        txt12 = "The minimum number of single circle checks: {}\n"
        print(txt12.format(min_visits))
        outFile.write(txt12.format(min_visits))


# Main
edgeList = []
c = 1

# check file for simple formatting errors
check_file_format()

# Open files for reading and writing
with open("HW2infile.txt") as inFile:
    N = inFile.readline()
    K = inFile.readline()

    try:
        for line in inFile:
            edges = [int(x) for x in line.split()]
            list(edges)
            edgeList.append(edges)
    except ValueError:
        with open("HW2PettitOutfile.txt", "w") as outFile:
            print("Input File formatting Error: The values in the file must be digits")
            outFile.write("Input File formatting Error: The values in the file must be digits")
        exit(1)


graph = create_graph(N)

# Check each node to make sure it gets visited and
# that no array out of bounds exception is possible
while c < int(N):
    check_pairs(edgeList, c)
    c += 1

# Check graph for strong connectivity
check_graph()

game_simulations = 10
game = 0
total_checks = 0
total_checks_each_game = []
max_visits = 0
min_visits = game_simulations

while game < game_simulations:
    nodes_visited_array = traversal()

    array_sum = sum(nodes_visited_array)
    total_checks_each_game.append(array_sum)
    total_checks += array_sum

    if max_visits < max(nodes_visited_array):
        max_visits = max(nodes_visited_array)

    if min_visits > min(nodes_visited_array):
        min_visits = min(nodes_visited_array)

    output_game_information()
    game += 1

end_sim_output()
