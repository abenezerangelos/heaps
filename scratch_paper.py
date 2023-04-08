# import heapq
# import networkx as nx
# import matplotlib.pyplot as plt
# from binarymaxheap import *
#
# # Define the heap with duplicate values
# heap = [10, 8, 7, 8, 4, 1, 1]
#
# # Add unique identifiers to each node value
# heap_with_ids = [(val, idx) for idx, val in enumerate(heap)]
#
# # Create a NetworkX graph object
# G = nx.Graph()
#
# # Add the nodes to the graph
# for node in heap_with_ids:
#     G.add_node(node)
#
# # Add the edges to the graph
# for i, node in enumerate(heap_with_ids):
#     left_child = heap_with_ids[2*i+1] if 2*i+1 < len(heap_with_ids) else None
#     right_child = heap_with_ids[2*i+2] if 2*i+2 < len(heap_with_ids) else None
#     if left_child is not None:
#         G.add_edge(node, left_child)
#     if right_child is not None:
#         G.add_edge(node, right_child)
#
# # Calculate the node positions using the hierarchy_pos function
# pos = hierarchy_pos(G, heap_with_ids[0])
# print(pos)
# labeler=list(pos.keys())
# labels={}
# for i in range(len(labeler)):
#     labels[labeler[i]]=labeler[i][0]
# # Draw the heap
# nx.draw(G, pos, with_labels=False)
# nx.draw_networkx_labels(G,pos=hierarchy_pos(G,heap_with_ids[0]),labels=labels)
#
# plt.show()
import networkx as nx
import math


# def get_tree_levels(G, root):
#     levels = {}
#     for node in G.nodes():
#         path_length = nx.shortest_path_length(G, root, node)
#         if path_length in levels:
#             levels[path_length].append(node)
#         else:
#             levels[path_length] = [node]
#     print("Please understand this, before continuing",levels)
#     return levels
# def ternary_tree_positions(G, root,width, sep=2):
#     pos = {root: (0, 0)}
#     levels=get_tree_levels(G,root)
#     parent=root
#     for level in levels:
#         level_nodes = [n for n in G.nodes() if nx.shortest_path_length(G, root, n) == level]
#
#
#         n = len(level_nodes)
#
#         for i, node in enumerate(level_nodes):
#             if node not in pos:
#                 x = (i-(n - 1) // 2) * (2*sep+2)
#                 y = -level
#                 pos[node] = (x, y)
#
#             if level:
#                 print("\n\nThis is i:",i)
#
#                 children = list(nx.neighbors(G,node))[1:]
#                 parent = list(nx.neighbors(G,node))[0]
#                 print("These are children:",children)
#                 for i,child in enumerate(children):
#                     print("Debug list:",list(nx.neighbors(G,node)),"parent:",parent,"Position of the parent:",pos[parent])
#                     if i%3 == 0:
#                         pos_left = (pos[node][0] - (sep/((level**level))), -level - 1)
#                         pos[child] = pos_left
#                     elif i%3 == 1:
#                         pos_middle = (pos[node][0], -level - 1)
#                         pos[child] = pos_middle
#                     elif i%3 == 2:
#                         pos_right = (pos[node][0]+ (sep/((level**level))), -level - 1)
#                         pos[child] = pos_right
#                     print("Child:",child,"\nDescendants/Children(used somewhere):",list(nx.neighbors(G,node))[1:],"\nNode:",node)
#                     print(" The position: for the node above ",pos[node])
#
#     return pos


# def ternary_heap_tree_positions(G, root, sep=1):
#     levels=get_tree_levels(G,root)
#     pos = {root: (0, 0)}
#     nodes = {}
#     for level in range(1, levels + 1):
#         level_nodes = [n for n in G.nodes() if nx.shortest_path_length(G, root, n) == level]
#         n = len(level_nodes)
#         for i, (key, value) in enumerate(level_nodes):
#             x = (i - (n - 1) / 2) * sep
#             y = -level
#             pos[(key, value)] = (x, y)
#
#             parent = list(G.predecessors((key, value)))[0]
#             if i == 0:
#                 pos_left = (x - sep, y - 1)
#                 nodes[(key, value)] = 'left'
#                 pos[parent] = pos_left
#             elif i == 1:
#                 pos_middle = (x, y - 1)
#                 nodes[(key, value)] = 'middle'
#                 pos[parent] = pos_middle
#             elif i == 2:
#                 pos_right = (x + sep, y - 1)
#                 nodes[(key, value)] = 'right'
#                 pos[parent] = pos_right
#
#     return pos, nodes
