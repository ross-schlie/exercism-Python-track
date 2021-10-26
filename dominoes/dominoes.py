"""exercism dominoes module."""


def can_chain(dominoes):
    """
    Return a list of dominoes in a chain if they can be chained or None.

    :param dominoes list[(tuple),...] - Original list of dominoes (unmutated).
    :return list[(tuple),...] | None - The ordered dominoes in a chain or None
    """
    if len(dominoes) == 0:
        return dominoes

    if len(dominoes) == 1:
        if dominoes[0][0] == dominoes[0][1]:
            return dominoes
        else:
            return None

    ordered_dominoes = build_chains(dominoes, [], dominoes.copy())
    if ordered_dominoes is None or ordered_dominoes[0][0] != ordered_dominoes[len(ordered_dominoes) - 1][1]:
        return None

    return ordered_dominoes

def build_chains(dominoes, ordered_chain, domino_rest):
    """
    Recursively build the domino chain by shirnking the remaining dominoes.

    :param dominoes list[(tuple),...] - Original list of dominoes (unmutated).
    :param ordered_chain list[(tuple),...] - The ordered dominoes in a chain.
    :param domino_rest list[(tuple),...] - The 'rest' of the dominoes which should be shrunk per recursion.
    """
    last_length = len(domino_rest)
    while len(domino_rest) > 0:
        # IF the chain is empty, pop the first domino and use it as the base
        if len(ordered_chain) == 0:
            current_domino = domino_rest.pop()
            ordered_chain.append(current_domino)

        # Find the 'open' side to try and find a domino to attach
        side = ordered_chain[len(ordered_chain) - 1][1]

        # Find dominors that could be attached to this one.
        candidates = []
        for domino in domino_rest:
            if domino[0] == side or domino[1] == side:
                candidates.append(domino)

        # If it's impossible to add any dominoes, give up
        if len(candidates) == 0:
            return None

        for domino in candidates:
            index = domino_rest.index(domino)
            next_domino = domino_rest.pop(index)
            if side == next_domino[1]:
                # flip domino
                next_domino = (next_domino[1], next_domino[0])

            ordered_chain.append(next_domino)
            # Try and see if we can build it
            chain = build_chains(dominoes, ordered_chain, domino_rest)
            if chain is None:
                # reverse adding domino to ordered chain (to try next candidate)
                ordered_chain.pop(len(ordered_chain) - 1)
                domino_rest.append(next_domino)
            else:
                return ordered_chain

        # If not decreasing, then give up
        if len(domino_rest) == last_length:
            return None

        last_length = len(domino_rest)

    return ordered_chain
