from typing import List, Tuple, Set


def analyze(words: List[str], text: str) -> Tuple[Set[str], Set[str], Set[str]]:
    exact, almost, unmatched = set(), set(), set()

    for word in words:
        if word in text:
            exact.add(word)
            continue

        subtext = text
        start = subtext.find(word[0], 0, len(subtext))
        while start != -1:
            i = 1
            while word[i] == subtext[start + i]:
                i += 1
            if i > len(word) / 2:
                j = i + 1
                while not str.isspace(subtext[start + j]):
                    j += 1
                almost.add(
                    f"{subtext[start:start + j]} almost matches with {word}"
                )
                break
            start = subtext.find(word[0], start + 1, len(subtext))
        else:
            unmatched.add(word)
    return exact, almost, unmatched
