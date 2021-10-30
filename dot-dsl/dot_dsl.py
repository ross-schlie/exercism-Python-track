"""exercism dot dsl module."""


NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    """Dot DSL Graph"""
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}
        if data is not None:
            if type(data) is not list:
                raise TypeError("Graph data malformed")

            for element in data:
                self.__add_element(element)

    def __add_element(self, element):
        self.__len_check(element, 3)

        if element[0] == NODE:
            self.__add_node(element)
        elif element[0] == EDGE:
            self.__add_edge(element)
        elif element[0] == ATTR:
            self.__add_attr(element)
        else:
            raise ValueError("Unknown item")

    def __len_check(self, element, expected):
        if len(element) < expected:
            raise TypeError("Graph item incomplete")

    def __len_match_check(self, element, expected, element_type):
        if len(element) != expected:
            raise ValueError(f"{element_type} is malformed")

    def __add_node(self, element):
        self.__len_match_check(element, 3, "Node")
        element_type, name, attrs = element
        # if type(name) is not str or type(attrs) is not dict:
        #      raise ValueError("Node is malformed")

        self.nodes.append(Node(name, attrs))

    def __add_edge(self, element):
        self.__len_match_check(element, 4, "Edge")
        element_type, src, dst, attrs = element
        # if type(src) is not str or type(dst) is not str or type(attrs) is not dict:
        #      raise ValueError("Edge is malformed")

        self.edges.append(Edge(src, dst, attrs))

    def __add_attr(self, element):
        self.__len_match_check(element, 3, "Attribute")
        element_type, key, value = element
        # if type(key) is not str:
        #      raise ValueError("Attribute is malformed")

        self.attrs[key] = value
