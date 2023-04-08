
import sys, pip, subprocess



missing = 0
try:
    from matplotlib.pyplot import *

    missing = 1
    import pydot
    from networkx import *

except:
    try:
        if not missing:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pydot"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "networkx"])
            from matplotlib.pyplot import *
            import pydot
            from networkx import *
        else:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pydot"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "networkx"])
            import pydot
            from networkx import *


    except:
        if hasattr(pip, 'main'):
            if not missing:
                pip.main(['install', 'matplotlib'])
                pip.main(['install', 'pydot'])
                pip.main(['install', 'networkx'])
            else:
                pip.main(['install', 'pydot'])
                pip.main(['install', 'networkx'])
        else:
            if not missing:
                pip._internal.main(['install', 'matplotlib'])
                pip._internal.main(['install', 'pydot'])
                pip._internal.main(['install', 'networkx'])
            else:
                pip._internal.main(['install', 'pydot'])
                pip._internal.main(['install', 'networkx'])
        from matplotlib.pyplot import *
        import pydot
        from networkx import *
# def hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
#     import networkx as nx
#     import random
#
#     if not nx.is_tree(G):
#         raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')
#
#     if root is None:
#         if isinstance(G, nx.DiGraph):
#             root = next(iter(nx.topological_sort(G)))  # allows back compatibility with nx version 1.11
#         else:
#             root = random.choice(list(G.nodes))
#
#     def _hierarchy_pos(G, root, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
#         '''
#         see hierarchy_pos docstring for most arguments
#
#         pos: a dict saying where all nodes go if they have been assigned
#         parent: parent of this branch. - only affects it if non-directed
#
#         '''
#
#         if pos is None:
#             pos = {root: (xcenter, vert_loc)}
#         else:
#             pos[root] = (xcenter, vert_loc)
#         children = list(G.neighbors(root))
#         if not isinstance(G, nx.DiGraph) and parent is not None:
#             children.remove(parent)
#         if len(children) != 0:
#             dx = width / len(children)
#             nextx = xcenter - width / 2 - dx / 2
#             for child in children:
#                 nextx += dx
#                 pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
#                                      vert_loc=vert_loc - vert_gap, xcenter=nextx,
#                                      pos=pos, parent=root)
#         return pos
#
#     return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
# def visualize(x):
#     print("WTF is going on, please")
#     if isinstance(x, BinaryMaxHeap):
#         heap=x.heap_list[1:]
#         if len(heap) == len(set(heap)):
#             heap_viz = Graph()
#             heap_viz.add_node(x.heap_list[1])
#             for i in range(1, len(x.heap_list)):
#                 if i < len(x) // 2:
#                     heap_viz.add_edge(x.heap_list[i], x.heap_list[i * 2])
#                     heap_viz.add_edge(x.heap_list[i], x.heap_list[(i * 2) + 1])
#             nodes = list(heap_viz.nodes)
#
#             print("This is what it might", nodes)
#
#
#             pos = hierarchy_pos(heap_viz, root=nodes[0], width=0.5)
#
#
#
#             print("Dictionary: ", pos)
#             print("We could maybe tweak this and then get a possible representation:", pos)
#             plt.rcParams['figure.figsize'] = (16, 10)
#             mngr = plt.pyplot.get_current_fig_manager()
#             mngr.window.geometry("+0+0")
#             drawing.draw(heap_viz, pos, with_labels=True)
#             plotter.show()
#         else:
#             heap = x.heap_list[1:]
#             heap_with_ids = [(val, idx) for idx, val in enumerate(heap)]
#
#             # Create a NetworkX graph object
#             G = Graph()
#
#             # Add the nodes to the graph
#             for node in heap_with_ids:
#                 G.add_node(node)
#
#             # Add the edges to the graph
#             for i, node in enumerate(heap_with_ids):
#                 left_child = heap_with_ids[2 * i + 1] if 2 * i + 1 < len(heap_with_ids) else None
#                 right_child = heap_with_ids[2 * i + 2] if 2 * i + 2 < len(heap_with_ids) else None
#                 if left_child is not None:
#                     G.add_edge(node, left_child)
#                 if right_child is not None:
#                     G.add_edge(node, right_child)
#
#             # Calculate the node positions using the hierarchy_pos function
#             pos = hierarchy_pos(G, heap_with_ids[0])
#             print(pos)
#             labeler = list(pos.keys())
#             labels = {}
#             for i in range(len(labeler)):
#                 labels[labeler[i]] = labeler[i][0]
#             # Draw the heap
#             print("FOCUS:",labeler,"Dict:",labels)
#             plt.rcParams['figure.figsize'] = (16, 10)
#             mngr = plotter.get_current_fig_manager()
#             mngr.window.geometry("+0+0")
#             draw(G, pos, with_labels=False)
#             draw_networkx_labels(G, pos=hierarchy_pos(G, heap_with_ids[0]), labels=labels)
#
#             plotter.show()
    # if isinstance(x, TernaryMaxHeap):
    #     heap = x.heap_list[1:]
    #     if len(heap) == len(set(heap)):
    #         heap_viz = Graph()
    #         heap_viz.add_node(x.heap_list[1])
    #         for i in range(1, len(x.heap_list)):
    #             if 3*i+1<len(x):
    #                 heap_viz.add_edge(x.heap_list[i], x.heap_list[(i * 3) - 1])
    #                 heap_viz.add_edge(x.heap_list[i], x.heap_list[i * 3])
    #                 heap_viz.add_edge(x.heap_list[i], x.heap_list[(i * 3) + 1])
    #             elif 3*i<len(x):
    #                 heap_viz.add_edge(x.heap_list[i], x.heap_list[(i * 3) - 1])
    #                 heap_viz.add_edge(x.heap_list[i], x.heap_list[i * 3])
    #             elif 3*i-1<len(x):
    #                 heap_viz.add_edge(x.heap_list[i], x.heap_list[(i * 3) - 1])
    #
    #
    #
    #             # if i < math.floor((len(x) - 2) / 3) + 1:
    #             #     heap_viz.add_edge(x.heap_list[i], x.heap_list[(i * 3) - 1])
    #             #     heap_viz.add_edge(x.heap_list[i], x.heap_list[i * 3])
    #             #     heap_viz.add_edge(x.heap_list[i], x.heap_list[(i * 3) + 1])
    #             print(i,x.heap_list[i])
    #         nodes = list(heap_viz.nodes)
    #
    #         print("This is what it might", nodes)
    #         print("Sandwich debug:",len(nodes))
    #         print("Maybe this one as well", len(x.heap_list),x.heap_list,"interms of nodes, wtf",len(x),x)
    #
    #
    #         pos = ternary_tree_positions(heap_viz, root=nodes[0], width=0.5)
    #
    #
    #
    #         print("Dictionary: ", pos)
    #         print("We could maybe tweak this and then get a possible representation:", pos)
    #         plt.rcParams['figure.figsize'] = (16, 10)
    #         mngr = plotter.get_current_fig_manager()
    #         mngr.window.geometry("+0+0")
    #         drawing.draw(heap_viz, pos, with_labels=True)
    #         plotter.show()
    #     else:
    #         import networkx as nx
    #         heap = x.heap_list[1:]
    #         G = Graph()
    #         heap = [(i, v) for i, v in enumerate(heap)]
    #         # Add the nodes to the graph
    #         for i, v in heap:
    #             G.add_node((i, v))
    #
    #         # Add edges to the graph to represent the heap structure
    #         for i in range(len(heap)):
    #             if 3 * i + 1 < len(heap):
    #                 G.add_edge((i, heap[i][1]), (3 * i + 1, heap[3 * i + 1][1]))
    #             if 3 * i + 2 < len(heap):
    #                 G.add_edge((i, heap[i][1]), (3 * i + 2, heap[3 * i + 2][1]))
    #             if 3 * i + 3 < len(heap):
    #                 G.add_edge((i, heap[i][1]), (3 * i + 3, heap[3 * i + 3][1]))
    #
    #         # Draw the graph
    #         node_list=list(G.nodes)
    #         print("Node List:",node_list,"Initial node:",node_list[0])
    #         pos = ternary_tree_positions(G,node_list[0],width=2)
    #         labeler = list(pos.keys())
    #         labels = {}
    #         for i in range(len(labeler)):
    #             labels[labeler[i]] = labeler[i][1]
    #         # Draw the heap
    #
    #         plt.rcParams['figure.figsize'] = (16, 10)
    #         mngr = plotter.get_current_fig_manager()
    #         mngr.window.geometry("+0+0")
    #         draw(G, pos, with_labels=False)
    #         draw_networkx_labels(G, pos=ternary_tree_positions(G, node_list[0],width=2), labels=labels)
    #
    #         # Show the plot
    #         plotter.show()
class BinaryMaxHeap():
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def __str__(self):
        string = ""
        for ind, val in enumerate(self.heap_list):
            string += f"|{val}"
        return string + "|"

    def __len__(self):
        return len(self.heap_list)

    def __contains__(self, item):
        return item in self.heap_list

    def is_empty(self):
        return len(self.heap_list) - 1 == 0

    def find_max(self):
        if self.size > 0:
            return self.heap_list[1]
        return None

    def insert(self, item):
        self.heap_list.append(item)
        self.size += 1
        self.percolate_up(self.size)

    def del_max(self):
        max_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.heap_list.pop()
        self.size = self.size - 1
        self.percolate_down(1)
        return max_val

    def max_child(self, index):
        if index * 2 + 1 > self.size:
            return index * 2

        else:
            if self.heap_list[index * 2] > self.heap_list[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def build_heap(self, alist):
        self.heap_list = [0] + alist[:]
        self.size = len(alist)
        index = len(alist) // 2
        while (index > 0):
            self.percolate_down(index)
            index -= 1

    def percolate_up(self, index):
        while index // 2 > 0:

            if self.heap_list[index] > self.heap_list[index // 2]:
                temp = self.heap_list[index // 2]
                self.heap_list[index // 2] = self.heap_list[index]
                self.heap_list[index] = temp
            index //= 2

    def percolate_down(self, index):
        while (index * 2) <= self.size:
            mc = self.max_child(index)
            if self.heap_list[index] < self.heap_list[mc]:
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[mc]
                self.heap_list[mc] = temp
            index = mc


