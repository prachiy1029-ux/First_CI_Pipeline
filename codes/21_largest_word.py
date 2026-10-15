def largest_word(sentence):
    words = sentence.split()
    largest = ""

    for word in words:
        cleaned_word = word.strip(".,!?;:\"'()[]{}")
        if len(cleaned_word) > len(largest):
            largest = cleaned_word

    return largest


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print("Largest word:", largest_word(sentence))