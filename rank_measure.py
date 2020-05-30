from typing import Iterable, Dict
from mappings import twitter_mapping, release_mapping


def calc_inversions(sequence: Iterable[int], descending: bool) -> int:
    """ Calculate the number of inversions required for descending sequnece """
    if descending is not True:
        sequence = sequence[::-1]

    count = 0
    for i, val_i in enumerate(sequence):
        for val_j in sequence[i:]:
            if val_i < val_j:
                count += 1
    return count


def calc_points(n: int, inversions: int) -> int:
    """ Given n and inversions, calculate the awarded points """
    potential = (n * (n - 1) / 2)
    return potential - inversions


def score_answer(answer: str, mapping: Dict, descending: bool = True) -> int:
    """ Calculate the awarded number of points for supplied ranking """
    n = len(answer)

    sequence = [mapping.get(x).get('value') for x in answer]
    inversions = calc_inversions(sequence, descending=descending)

    return calc_points(n, inversions)


def score_twitter(answer: str, mapping=twitter_mapping, correction=2):
    full_score = score_answer(
        answer=answer,
        mapping=mapping,
        descending=True
    )
    return full_score / correction


def score_releases(answer: str, mapping=release_mapping, correction=4):
    full_score = score_answer(
        answer=answer,
        mapping=mapping,
        descending=False
    )
    return full_score / correction
