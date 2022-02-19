def analyze(words: list[str], text: str) -> tuple[set, set, set]:
    exact, almost, unmatched = set(), set(), set()

    for word in words:
        korean, english = parse_word(word)
        if korean in text:
            exact.add(objectify(korean, english))
            continue

        subtext = text
        start = subtext.find(korean[0], 0, len(subtext))
        while start != -1:
            i = 1
            while korean[i] == subtext[start + i]:
                i += 1
            if i > len(korean) / 2:
                j = i + 1
                while not str.isspace(subtext[start + j]):
                    j += 1
                almost.add(objectify(korean, english))
                break
            start = subtext.find(korean[0], start + 1, len(subtext))
        else:
            unmatched.add(objectify(korean, english))
    return exact, almost, unmatched


def parse_word(word: str) -> tuple[str, str]:
    korean, english = word.split("~")
    korean = korean.replace("(", "").replace(")", "").replace("w", "").strip()
    return korean, english


def objectify(korean: str, english: str) -> dict:
    return {"korean": korean, "english": english}
