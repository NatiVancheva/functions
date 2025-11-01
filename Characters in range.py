def characters_in_range(char1,char2):
    start = ord(char1)
    end = ord(char2)
    if start > end:
        start, end = end, start
    result = [chr(i) for i in range(start + 1, end)]
    return " ".join(result)

character1 = input()
character2 = input()
print(characters_in_range(character1, character2))
