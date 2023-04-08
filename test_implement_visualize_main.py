import matplotlib.pyplot as plotter
from binarymaxheap import BinaryMaxHeap
import matplotlib as plt
from networkx import *
from ternarymaxheap import *
from random import randint as rt
def get_tree_levels(G, root):
    levels = {}
    for node in G.nodes():
        path_length = nx.shortest_path_length(G, root, node)
        if path_length in levels:
            levels[path_length].append(node)
        else:
            levels[path_length] = [node]
    # print("Please understand this, before continuing",levels)
    return levels
def hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    import networkx as nx
    import random

    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  # allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''

        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
def ternary_tree_positions(G, root,width, sep=2):
    pos = {root: (0, 0)}
    levels=get_tree_levels(G,root)
    parent=root
    for level in levels:
        level_nodes = [n for n in G.nodes() if nx.shortest_path_length(G, root, n) == level]


        n = len(level_nodes)

        for i, node in enumerate(level_nodes):
            if node not in pos:
                x = (i-(n - 1) // 2) * (2*sep+2)
                y = -level
                pos[node] = (x, y)

            if level:
                # print("\n\nThis is i:",i)

                children = list(nx.neighbors(G,node))[1:]
                parent = list(nx.neighbors(G,node))[0]
                # print("These are children:",children)
                for i,child in enumerate(children):
                    # print("Debug list:",list(nx.neighbors(G,node)),"parent:",parent,"Position of the parent:",pos[parent])
                    if i%3 == 0:
                        pos_left = (pos[node][0] - (sep/((level**level))), -level - 1)
                        pos[child] = pos_left
                    elif i%3 == 1:
                        pos_middle = (pos[node][0], -level - 1)
                        pos[child] = pos_middle
                    elif i%3 == 2:
                        pos_right = (pos[node][0]+ (sep/((level**level))), -level - 1)
                        pos[child] = pos_right
                    # print("Child:",child,"\nDescendants/Children(used somewhere):",list(nx.neighbors(G,node))[1:],"\nNode:",node)
                    # print(" The position: for the node above ",pos[node])

    return pos

def visualize(x):
    global figure
    if isinstance(x, BinaryMaxHeap):
        heap=x.heap_list[1:]
        if len(heap) == len(set(heap)):
            heap_viz = Graph()
            heap_viz.add_node(x.heap_list[1])
            for i in range(1, len(x.heap_list)):
                if i < len(x) // 2:
                    heap_viz.add_edge(x.heap_list[i], x.heap_list[i * 2])
                    heap_viz.add_edge(x.heap_list[i], x.heap_list[(i * 2) + 1])
            nodes = list(heap_viz.nodes)

            # print("This is what it might", nodes)


            pos = hierarchy_pos(heap_viz, root=nodes[0], width=0.5)



            # print("Dictionary: ", pos)
            # print("We could maybe tweak this and then get a possible representation:", pos)
            plt.rcParams['figure.figsize'] = (16, 10)
            mngr = plt.pyplot.get_current_fig_manager()
            mngr.window.geometry("+0+0")
            drawing.draw(heap_viz, pos, with_labels=True)
            figure=plotter.gcf()
            plotter.show()
        else:
            heap = x.heap_list[1:]
            heap_with_ids = [(val, idx) for idx, val in enumerate(heap)]

            # Create a NetworkX graph object
            G = Graph()

            # Add the nodes to the graph
            for node in heap_with_ids:
                G.add_node(node)

            # Add the edges to the graph
            for i, node in enumerate(heap_with_ids):
                left_child = heap_with_ids[2 * i + 1] if 2 * i + 1 < len(heap_with_ids) else None
                right_child = heap_with_ids[2 * i + 2] if 2 * i + 2 < len(heap_with_ids) else None
                if left_child is not None:
                    G.add_edge(node, left_child)
                if right_child is not None:
                    G.add_edge(node, right_child)

            # Calculate the node positions using the hierarchy_pos function
            pos = hierarchy_pos(G, heap_with_ids[0])
            # print(pos)
            labeler = list(pos.keys())
            labels = {}
            for i in range(len(labeler)):
                labels[labeler[i]] = labeler[i][0]
            # Draw the heap
            # print("FOCUS:",labeler,"Dict:",labels)
            plt.rcParams['figure.figsize'] = (16, 10)
            mngr = plotter.get_current_fig_manager()
            mngr.window.geometry("+0+0")
            draw(G, pos, with_labels=False)
            draw_networkx_labels(G, pos=hierarchy_pos(G, heap_with_ids[0]), labels=labels)
            figure=plotter.gcf()
            plotter.show()
    if isinstance(x, TernaryMaxHeap):
        heap = x.heap_list[1:]
        if len(heap) == len(set(heap)):
            heap_viz = Graph()
            heap_viz.add_node(x.heap_list[1])
            for i in range(1, len(x.heap_list)):
                if 3*i+1<len(x):
                    heap_viz.add_edge(x.heap_list[i], x.heap_list[(i * 3) - 1])
                    heap_viz.add_edge(x.heap_list[i], x.heap_list[i * 3])
                    heap_viz.add_edge(x.heap_list[i], x.heap_list[(i * 3) + 1])
                elif 3*i<len(x):
                    heap_viz.add_edge(x.heap_list[i], x.heap_list[(i * 3) - 1])
                    heap_viz.add_edge(x.heap_list[i], x.heap_list[i * 3])
                elif 3*i-1<len(x):
                    heap_viz.add_edge(x.heap_list[i], x.heap_list[(i * 3) - 1])



                # if i < math.floor((len(x) - 2) / 3) + 1:
                #     heap_viz.add_edge(x.heap_list[i], x.heap_list[(i * 3) - 1])
                #     heap_viz.add_edge(x.heap_list[i], x.heap_list[i * 3])
                #     heap_viz.add_edge(x.heap_list[i], x.heap_list[(i * 3) + 1])
                # print(i,x.heap_list[i])
            nodes = list(heap_viz.nodes)




            pos = ternary_tree_positions(heap_viz, root=nodes[0], width=0.5)




            plt.rcParams['figure.figsize'] = (16, 10)
            mngr = plotter.get_current_fig_manager()
            mngr.window.geometry("+0+0")
            drawing.draw(heap_viz, pos, with_labels=True)
            figure = plotter.gcf()
            plotter.show()
        else:
            import networkx as nx
            heap = x.heap_list[1:]
            G = Graph()
            heap = [(i, v) for i, v in enumerate(heap)]
            # Add the nodes to the graph
            for i, v in heap:
                G.add_node((i, v))

            # Add edges to the graph to represent the heap structure
            for i in range(len(heap)):
                if 3 * i + 1 < len(heap):
                    G.add_edge((i, heap[i][1]), (3 * i + 1, heap[3 * i + 1][1]))
                if 3 * i + 2 < len(heap):
                    G.add_edge((i, heap[i][1]), (3 * i + 2, heap[3 * i + 2][1]))
                if 3 * i + 3 < len(heap):
                    G.add_edge((i, heap[i][1]), (3 * i + 3, heap[3 * i + 3][1]))

            # Draw the graph
            node_list=list(G.nodes)

            pos = ternary_tree_positions(G,node_list[0],width=2)
            labeler = list(pos.keys())
            labels = {}
            for i in range(len(labeler)):
                labels[labeler[i]] = labeler[i][1]
            # Draw the heap

            plt.rcParams['figure.figsize'] = (16, 10)
            mngr = plotter.get_current_fig_manager()
            mngr.window.geometry("+0+0")
            draw(G, pos, with_labels=False)
            draw_networkx_labels(G, pos=ternary_tree_positions(G, node_list[0],width=2), labels=labels)

            # Show the plot

            figure = plotter.gcf()
            plotter.show()

n=50
range_tuple = (0, n)
def execute_binary_heap():
    global n

    test_binary = BinaryMaxHeap()
    test_binary.is_empty()
    #samples inserted sequentially individually
    for i in range(n+1):test_binary.insert(i)
    print(test_binary)
    print(len(test_binary))
    visualize(test_binary)
    figure.savefig("binary_max_heap_seq1.pdf")
    #samples inserted sequentially from list
    test_binary.build_heap([i for i in range(n+1)])
    print(test_binary)
    print(len(test_binary))
    visualize(test_binary)
    figure.savefig("binary_max_heap_seq2.pdf")
    #random samples inserted
    test_binary=BinaryMaxHeap()
    for i in range(n+1):test_binary.insert(rt(*range_tuple))
    print(test_binary)
    print(len(test_binary))
    visualize(test_binary)
    figure.savefig("binary_max_heap_rand1.pdf")
    test_binary.is_empty()
    #random sample from list
    test_binary.build_heap([rt(*range_tuple) for _ in range(n+1)])
    print(test_binary)
    print(len(test_binary))
    visualize(test_binary)
    figure.savefig("binary_max_heap_rand2.pdf")
    print("Is the binary heap empty?", test_binary.is_empty())
    #ordered insert heap
    test_binary=BinaryMaxHeap()
    for i in range(n+1):test_binary.insert(-i)
    print(test_binary)
    print(len(test_binary))
    visualize(test_binary)
    figure.savefig("binary_max_heap_ord1.pdf")
    #ordered build heap
    test_binary=BinaryMaxHeap()
    test_binary.build_heap([-i for i in range(n+1)])
    print(test_binary)
    print(len(test_binary))

    visualize(test_binary)
    figure.savefig("binary_max_heap_ord2.pdf")
    print("Is the binary heap empty?", test_binary.is_empty())
def execute_ternary_heap():
    global n
    test_ternary = TernaryMaxHeap()
    # samples inserted sequentially individually
    for i in range(n+1): test_ternary.insert(i)

    print(test_ternary)
    print(len(test_ternary))
    visualize(test_ternary)
    figure.savefig("ternary_max_heap_seq1.pdf")
    # samples inserted sequentially from list
    test_ternary = TernaryMaxHeap()
    test_ternary.build_heap([i for i in range(n+1)])

    print(test_ternary)
    print(len(test_ternary))

    visualize(test_ternary)
    figure.savefig("ternary_max_heap_seq2.pdf")
    #random samples inserted individually using a for loop
    test_ternary=TernaryMaxHeap()
    for i in range(n+1): test_ternary.insert(rt(*range_tuple))

    print(test_ternary)
    print(len(test_ternary))
    visualize(test_ternary)
    figure.savefig("ternary_max_heap_rand1.pdf")
    #random samples inserted from list
    test_ternary = TernaryMaxHeap()
    test_ternary.build_heap([rt(*range_tuple) for _ in range(n+1)])
    print(test_ternary)
    print(len(test_ternary))
    visualize(test_ternary)
    figure.savefig("ternary_max_heap_rand2.pdf")
    print("Is the ternary heap empty?",test_ternary.is_empty())
    test_ternary = TernaryMaxHeap()
    # samples inserted sequentially individually
    for i in range(n + 1): test_ternary.insert(-i)

    print(test_ternary)
    print(len(test_ternary))
    visualize(test_ternary)
    figure.savefig("ternary_max_heap_ord1.pdf")
    # samples inserted sequentially from list
    test_ternary = TernaryMaxHeap()
    test_ternary.build_heap([-i for i in range(n + 1)])

    print(test_ternary)
    print(len(test_ternary))

    visualize(test_ternary)
    figure.savefig("ternary_max_heap_ord2.pdf")
    
def main():
    execute_binary_heap()
    execute_ternary_heap()

if __name__ == '__main__':
    print(__name__)
    main()