def get_random_code(length=8):
    characters = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(length):
        result += characters[random.randint(0, len(characters) - 1)]
    return result
