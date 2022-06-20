"""
to_tree()

converts list of paired (parent, child) tuple
to dictionary tree
"""

source = [
    (None, 'a'),
    (None, 'b'),
    ('a2', 'a21'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a22'),
    (None, 'c'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}


def to_tree(source):
    """return a tree (dictionary)"""
    root = {}
    nested = dict()

    # generating tree
    for k, v in source:
        if k is None:
            # links between root and nested
            if nested.get(v) is None:
                nested[v] = dict()
            root[v] = nested[v]
            continue

        if nested.get(k) is None:
            nested[k] = dict()

        # links nested
        if nested.get(v) is None:
            nested[k][v] = dict()
            nested[v] = nested[k][v]
        else:
            nested[k][v] = nested[v]

    return root


if __name__ == '__main__':
    assert to_tree(source) == expected
    print('to_tree(source) == expected', to_tree(source) == expected)
    print()
    print('to_tree(source)')
    print(to_tree(source))
    print()
    print('expected')
    print(expected)
