def longest_word(sentence):
    if len(sentence) == 0:
        return ""

    anything = []
    text = ""

    for letter in range(len(sentence)):
        if sentence[letter].isalpha():
            text += sentence[letter]
        elif sentence[letter] == "-" and sentence[letter-1].isalpha() and sentence[letter+1].isalpha():
            text += sentence[letter]
        elif sentence[letter] == " ":
            anything.append(text)
            text = ""
        else:
            continue

    if text:
        anything.append(text)


    result = ""
    count = 0

    for word in anything:
        if len(word) > count:
            result = word
            count = len(word)

    return result



# bonus
def longest_words(sentence):
    if len(sentence) == 0:
        return []

    anything = []
    text = ""

    for letter in sentence:
        if letter.isalpha():
            text += letter
        elif letter == "-":
            text += letter
        elif letter == " ":
            if text:
                anything.append(text)
                text = ""
            continue
        else:
            continue

    if text:
        anything.append(text)


    count = 0

    for word in anything:
        if len(word) > count:
            count = len(word)

    result = []
    for word in anything:
        if len(word) == count:
            result.append(word)

    return result