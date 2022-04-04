def analyze(words: list[str], text: str) -> tuple[list, list, list]:
    exact, almost, unmatched = list(), list(), list()

    for word in words:
        korean, english = parse_word(word)
        if korean in text:
            exact.append(objectify(korean, english))
            continue

        subtext = text
        start = subtext.find(korean[0], 0, len(subtext))
        while start != -1:
            i = 0
            while (
                i < len(korean)
                and start + i < len(subtext)
                and korean[i] == subtext[start + i]
            ):
                i += 1
            if i > (len(korean) - korean.count(" ")) / 2:
                j = i + 1
                while not str.isspace(subtext[start + j]):
                    j += 1
                almost.append(objectify(korean, english, subtext[start : start + j]))
                break
            start = subtext.find(korean[0], start + 1, len(subtext))
        else:
            unmatched.append(objectify(korean, english))
    return exact, almost, unmatched


def parse_word(word: str) -> tuple[str, str]:
    korean, english = word.split("~")
    korean = (
        korean.replace("(가)")
        .replace("(이)")
        .replace("(", "")
        .replace(")", "")
        .replace("w", "")
        .replace("-", "")
        .replace("ㄹ", "")
        .strip()
    )
    return korean, english.strip()


def objectify(korean: str, english: str, original: str = "") -> dict:
    return {"korean": korean, "english": english, "original": original}
