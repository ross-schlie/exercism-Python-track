"""exercism smart game format parsing module."""

import re


class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other

def parse(input_string:str):
    if len(input_string) < 3:
        raise ValueError("No valid instructions to parse.")

    props = {}
    children = []

    offset = 0
    if input_string[0] == '(':
        offset += 1

    if input_string[offset] == ';':
        offset += 1

    last_property_name = ""
    property_name = ""
    property_value = ""
    is_propery_value = False
    for char in input_string[offset::]:
        offset += 1
        if char == '(':
            children = parse_children(offset, input_string, children)

            break
        elif char == ')':
            continue
        elif char == ';':
            child = parse(input_string[offset:])
            children.append(child)
            break
        elif char == '[':
            is_propery_value = True
        elif char == ']':
            if property_value[-1] == '\\':
                property_value = property_value[0:-1] + ']'
                continue

            if property_name == "":
                value = props.get(last_property_name)
                value.append(property_value)
                props[last_property_name] = value
            else:
                if not property_name.isupper():
                    raise ValueError("Property name not uppercased.")

                props[property_name] = [property_value]
                last_property_name = property_name

            property_name = ""
            property_value = ""
            is_propery_value = False
        elif is_propery_value:
            if char == '\t':
                property_value += ' '
            else:
                property_value += char
        else:
            property_name += char

    if property_name != "":
        raise ValueError("Property value not defined.")

    if len(children) == 0:
        children = None

    return SgfTree(props, children)

def parse_children(open_index, input_string, children):
    while open_index > 0:
        close_index = input_string.find(')', open_index)
        child = parse(input_string[open_index:close_index])
        children.append(child)
        open_index = input_string.find('(', open_index + 1)

    return children
