def count_characters(text):
    result = {}
    letter = 0
    spaces = 0
    num = 0
    punct = 0
    for i in text:
        if i.isalpha():
            letter += 1
        elif i.isdigit():
            num += 1
        elif i == " ":
            spaces += 1
        else:
            punct += 1
    
    result["letters"] = letter
    result["numbers"] = num
    result["spaces"] = spaces
    result["special"] = punct

    return result