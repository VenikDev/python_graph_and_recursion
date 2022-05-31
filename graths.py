import networkx as nx
import matplotlib.pyplot as plt


def task1():
    graph = nx.Graph()

    graph.add_edges_from([
        ("a", "b"), ("a", "c"), ("a", "f")
    ])
    graph.add_edges_from([
        ("b", "a"), ("b", "c"), ("b", "d")
    ])
    graph.add_edges_from([
        ("c", "b"), ("c", "e"), ("c", "d")
    ])
    graph.add_edges_from([
        ("d", "c"), ("d", "b"), ("d", "e"), ("d", "f")
    ])
    graph.add_edges_from([
        ("f", "a"), ("f", "d")
    ])
    graph.add_edges_from([
        ("e", "c"), ("e", "d")
    ])

    pos = nx.circular_layout(graph)
    nx.draw(graph, pos=pos, with_labels=True)
    plt.show()

def task2():
    graph = nx.Graph()

    graph.add_edge(1, 2, weight=7)
    graph.add_edge(1, 3, weight=9)
    graph.add_edge(1, 6, weight=14)

    graph.add_edge(4, 2, weight=15)
    graph.add_edge(4, 3, weight=11)
    graph.add_edge(4, 5, weight=6)

    graph.add_edge(5, 6, weight=9)
    graph.add_edge(5, 4, weight=6)

    graph.add_edge(6, 3, weight=2)
    graph.add_edge(6, 1, weight=14)

    pos = nx.circular_layout(graph)
    weights = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=weights)

    nx.draw(graph, pos, with_labels=True)

    plt.show()

def task3():
    START_PATH = 1
    END_PATH = 8
    diGraph = nx.DiGraph()

    diGraph.add_weighted_edges_from([
        (1, 3, 85), (1, 2, 32), (1, 4, 75), (1, 5, 57),
        (2, 3, 75), (2, 5, 23), (2, 8, 64),
        (3, 6, 6),
        (4, 3, 18),
        (5, 4, 10), (5, 6, 11), (5, 7, 20),
        (6, 4, 9), (6, 7, 7),
        (7, 8, 12),
        (8, 5, 2)
    ])

    predecessor, _ = nx.floyd_warshall_predecessor_and_distance(diGraph)
    short_path = nx.reconstruct_path(START_PATH, END_PATH, predecessor)

    edges_short_path = [(a, b) for a, b in zip(short_path, short_path[1:])]
    print(edges_short_path)

    pos = nx.circular_layout(diGraph)
    weights = nx.get_edge_attributes(diGraph, "weight")
    nx.draw_networkx_edge_labels(diGraph, pos, edge_labels=weights)
    nx.draw_networkx_edges(diGraph, pos=pos, edgelist=edges_short_path, edge_color='r', width=3)

    nx.draw(diGraph, pos, with_labels=True)

    plt.show()

def task4():
    diLetterGraph = nx.DiGraph()

    A, B, V, G, D, E, Z, J, I, K, L, M = "А", "Б", "В", "Г", "Д", "Е", "З", "Ж", "И", "К", "Л", "М"

    diLetterGraph.add_weighted_edges_from([
        (A, B, 1), (A, V, 1), (A, G, 1), (A, D, 1),
        (B, E, 1), (B, V, 1),
        (V, E, 1), (V, J, 1),
        (G, V, 1), (G, J, 1),
        (D, G, 1), (D, J, 1), (D, Z, 1),
        (E, I, 1), (E, J, 1),
        (J, I, 1),
        (Z, J, 1), (Z, I, 1),
        (I, K, 1), (I, M, 1), (I, L, 1),
        (K, M, 1),
        (L, M, 1)
    ])

    predecessor, _ = nx.floyd_warshall_predecessor_and_distance(diLetterGraph)
    short_path = nx.reconstruct_path(A, M, predecessor)

    edges_short_path = [(a, b) for a, b in zip(short_path, short_path[1:])]
    print(edges_short_path)

    pos = nx.circular_layout(diLetterGraph)
    weights = nx.get_edge_attributes(diLetterGraph, "weight")
    nx.draw_networkx_edge_labels(diLetterGraph, pos, edge_labels=weights)
    nx.draw_networkx_edges(diLetterGraph, pos=pos, edgelist=edges_short_path, edge_color='r', width=3)

    nx.draw(diLetterGraph, pos, with_labels=True)

    plt.show()

def task5():
    diGraph = nx.DiGraph()

    A, B, C, D, E, F, G = "A", "B", "C", "D", "E", "F", "G"

    diGraph.add_weighted_edges_from([
        (A, C, 1), (A, D, 5), (A, G, 3),
        (B, A, 2), (B, E, 10),
        (C, B, 1), (C, E, 8), (C, F, 6), (C, G, 3),
        (D, G, 4),
        (E, A, 6), (E, G, 3),
        (F, E, 4),
        (G, A, 2), (G, F, 2)
    ])

    predecessor, _ = nx.floyd_warshall_predecessor_and_distance(diGraph)
    short_path = nx.reconstruct_path(B, D, predecessor)

    edges_short_path = [(a, b) for a, b in zip(short_path, short_path[1:])]
    print(edges_short_path)

    pos = nx.circular_layout(diGraph)
    weights = nx.get_edge_attributes(diGraph, "weight")
    nx.draw_networkx_edge_labels(diGraph, pos, edge_labels=weights)
    nx.draw_networkx_edges(diGraph, pos=pos, edgelist=edges_short_path, edge_color='r', width=3)

    nx.draw(diGraph, pos, with_labels=True)

    plt.show()

def task6():
    diGraph = nx.DiGraph()
    A, B, C, D, E, F, G, H, I, J, K, L, M, N = \
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "j", "K", "L", "M", "N"
    START_PATH = A
    END_PATH = N

    diGraph.add_weighted_edges_from([
        (A, B, 1), (A, C, 1), (A, D, 1),
        (B, E, 1),
        (C, E, 1), (C, H, 1), (C, F, 1), (C, G, 1), (C, J, 1),
        (D, G, 1),
        (E, H, 1),
        (F, H, 1), (F, I, 1), (F, J, 1),
        (G, J, 1),
        (H, L, 1), (H, K, 1), (H, I, 1),
        (I, K, 1),
        (J, I, 1), (J, K, 1), (J, M, 1),
        (K, L, 1), (K, N, 1), (K, M, 1),
        (L, N, 1),
        (M, N, 1),
    ])

    predecessor, _ = nx.floyd_warshall_predecessor_and_distance(diGraph)
    short_path = nx.reconstruct_path(START_PATH, END_PATH, predecessor)
    path_fron_A_to_N = [path for path in nx.all_simple_paths(diGraph, source=A, target=N)]
    print(f"Кол-во путей из {START_PATH} в {END_PATH} = {len(path_fron_A_to_N)}")

    edges_short_path = [(a, b) for a, b in zip(short_path, short_path[1:])]
    print("Короткий путь:", edges_short_path)

    pos = nx.circular_layout(diGraph)
    nx.draw_networkx_edges(diGraph, pos=pos, edgelist=edges_short_path, edge_color='r', width=3)

    nx.draw(diGraph, pos, with_labels=True)

    plt.show()

def main():
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    task6()


if __name__ == "__main__":
    main()
