def latest(scores):
    """Get the most recent score from a list of high-scores."""
    return scores[- 1]

def personal_best(scores):
    """Get the highest score from a list of high-scores."""
    return max(scores)

def personal_top_three(scores):
    """Get the top 3 best scores from a list of high-scores."""
    scores.sort(reverse=True)
    return scores[:3]
