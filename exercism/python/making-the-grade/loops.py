"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    new_list = []
    for score in student_scores:
        new_list.append(round(score))
    return new_list


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    value_of_failed = 0
    for score in student_scores:
        if score <= 40:
            value_of_failed += 1
    return value_of_failed


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    best_scores_list = []
    for score in student_scores:
        if score >= threshold:
            best_scores_list.append(score)
    return best_scores_list


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55 
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    #step = (highest - 40) // 4
    # score_list = []
    
    # for i in range(41, highest, step):
    #     score_list.append(i)

    return list(range(41, highest, (highest - 40) // 4))


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    lst = []
    for number, combo in enumerate(zip(student_names, student_scores), start=1):
        combo_name, combo_score = combo
        lst.append(f'{number}. {combo_name}: {combo_score}')
        
    return lst


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for name_and_score in student_info:
        name, score = name_and_score
        if score == 100:
            return [name, score]
    return []
