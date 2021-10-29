"""exercism food chain module."""

START = "I know an old lady who swallowed a fly."
END = "I don't know why she swallowed the fly. Perhaps she'll die."
BAD_END = "She's dead, of course!"
ANIMALS = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]
SWALLOW = "She swallowed the fly to catch the fly."
SPIDER_APPEND = " that wriggled and jiggled and tickled inside her"
OTHER_LINE = [
    "I don't know why she swallowed the fly. Perhaps she'll die.",
    "It wriggled and jiggled and tickled inside her.",
    "How absurd to swallow a bird!",
    "Imagine that, to swallow a cat!",
    "What a hog, to swallow a dog!",
    "Just opened her throat and swallowed a goat!",
    "I don't know how she swallowed a cow!"
]

def recite(start_verse, end_verse):
    output = []
    for i in range(start_verse, end_verse + 1):
        output.extend(build_verse(i))
        if i < end_verse:
            output.append("")

    return output

def build_verse(verse):
    # 0-based indexes vs 1-based verse counts
    verse = verse - 1
    output = []
    output.append(START.replace("fly", ANIMALS[verse]))

    if verse == len(ANIMALS) - 1:
        output.append(BAD_END)
    else:
        output.append(OTHER_LINE[verse])

        tmp = verse
        while tmp >= 1:
            target_animal = ANIMALS[tmp - 1]
            if target_animal == "spider":
                target_animal += SPIDER_APPEND

            output.append(SWALLOW.replace("fly", ANIMALS[tmp], 1).replace("fly", target_animal, 1))
            tmp -= 1

        if verse > 0:
            output.append(OTHER_LINE[0])

    return output
