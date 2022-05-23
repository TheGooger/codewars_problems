def reverse_words(original_text):
    """It reverses each word in the string."""
    result_string = []
    for word in original_text.split(" "):
        result_string.append(word[::-1])
    return " ".join(result_string)
