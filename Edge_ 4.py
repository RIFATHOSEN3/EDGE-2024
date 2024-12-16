def capitalize_alternate():
    word = input("Enter a word: ")
    result = ''.join(
        letter.upper() if i % 2 == 1 else letter.lower()
        for i, letter in enumerate(word)
    )
    print("Result:", result)
capitalize_alternate()