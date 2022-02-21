def maxNumberOfBalloons(text: str) -> int:
    S = counter(text)
    return min(S['b'], S['a'], S['l'] // 2, S['o'] // 2, S['n'])

maxNumberOfBalloons(ballon)