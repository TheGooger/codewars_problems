def reverse_words(original_text):
    """It reverses each word in the string."""
    splitted_text = original_text.split(sep=" ")
    result_string = ""
    for word in splitted_text:
        word = list(word)
        word.reverse()
        for letter in word:
            result_string += letter
        result_string += " "
    return(result_stringr.rstrip())