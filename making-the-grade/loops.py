"""exercism making the grade (loops) module."""

import math

def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """

    for index, score in enumerate(student_scores):
        student_scores[index] = round(score)

    return student_scores


def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """

    failing_students = 0
    for score in student_scores:
        if score <= 40:
            failing_students += 1

    return failing_students


def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """

    best_students = []
    for score in student_scores:
        if score >= threshold:
            best_students.append(score)

    return best_students


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    """

    #F (40) - A = B, C, D, E = 4 thresholds
    thresholds = []
    next_threshold = 41
    spread = (highest - next_threshold) / 4
    while next_threshold < highest:
        thresholds.append(math.ceil(next_threshold))
        next_threshold += spread

    return thresholds


def student_ranking(student_scores, student_names):
    """
    :param student_scores: list of scores in descending order.
    :param student_names: list of names in descending order by exam score.
    :return: list of strings in format ["<rank>. <student name>: <score>"].
    """

    ranked = []
    for index, score in enumerate(student_scores):
        ranked.append(f"{index + 1}. {student_names[index]}: {student_scores[index]}")

    return ranked


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: First [<student name>, 100] found OR "No perfect score."
    """

    result = "No perfect score."
    for student in student_info:
        if student[1] == 100:
            return student

    return result
