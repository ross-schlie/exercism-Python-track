"""excersism grep module."""

# import io

def grep(pattern, flags, files):
    """
    Search file(s) for lines matching a regular expression pattern
        and return the line number and contents of each matching line.

    :param pattern string - pattern used to match lines in a file.
    :param flags string - Zero or more flags to customize the matching behavior.
    :param files list - One or more files in which to search for matching lines.
    :rturn string - line number and contents of each matching line
    """

    output = ""
    if flags.count("-i") > 0:
        pattern = pattern.lower()

    for file in files:
        with open(file) as f:
            line_number = 1
            for line in f:
                # regex?
                # Try to match (based on flags) the pattern in the line of a file.
                matched = False
                if flags.count("-x") > 0:
                    if flags.count("-i") > 0 and line.lower() == pattern + "\n":
                        matched = True
                    elif line == pattern + "\n":
                        matched = True
                elif flags.count("-i") > 0 and line.lower().count(pattern) > 0:
                    matched = True
                elif line.count(pattern) > 0:
                    matched = True

                # Invert matched and not matched (when -v is present)
                if flags.count("-v") > 0:
                    if matched:
                        matched = False
                    else:
                        matched = True

                # If it matches, append to output
                if matched:
                    # Output just the file name, and move on
                    if flags.count("-l") > 0:
                        output += file + "\n"
                        break

                    if len(files) > 1:
                        output += file + ":"

                    if flags.count("-n") > 0:
                        output += str(line_number) + ":"

                    output += line

                line_number += 1

    return output