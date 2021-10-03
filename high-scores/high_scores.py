"""exercism high scores module."""


def latest(scores):
    """
    Get the most recent score.

    :param scores list - List of scores
    :return int - Most recent score.
    """
    return scores[len(scores) - 1]

def personal_best(scores):
    """
    Get the best (personal) score.

    :param scores list - List of scores
    :return int - Best score.
    """
    scores.sort(reverse=True)
    return scores[0]

def personal_top_three(scores):
    """
    Get the top 3 scores.

    :param scores list - List of scores
    :return list - Best 3 scores.
    """

    scores.sort(reverse=True)
    topc = 3
    top = []
    if len(scores) < topc:
        topc = len(scores)

    for i in range(0, topc):
        top.append(scores[i])

    return top
