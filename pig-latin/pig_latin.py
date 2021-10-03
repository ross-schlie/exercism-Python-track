"""exercism pig latin module."""


def translate(text):
    """
    Translate text into pig latin.

    :param text string - text to translate.
    :return string = translated text.
    """

    translated = ""
    vowels = "aeiou"
    vowel_sounds = ["xr", "yt"]
    for word in text.split(" "):
        translated_word = ""
        if word[0] in vowels or word[0:2] in vowel_sounds:
            translated_word = word + "ay"
        else:
            for index, char in enumerate(word):
                if index == 0:
                    continue

                if char == "u" and word[index - 1] == "q":
                    translated_word = word[index + 1::] + word[0:index + 1] + "ay"
                    break
                elif char in vowels or char == "y":
                    translated_word = word[index::] + word[0:index] + "ay"
                    break

        translated += " " + translated_word

    return translated.strip()
