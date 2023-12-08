import re

decimal_words = ["one", "two", "three", "four",
                 "five", "six", "seven", "eight", "nine"]


def convert_to_decimal(word):
    """Convert the given word to a decimal digit.
    If the word is already a decimal digit, return the word.
    If the word is not a decimal digit, but is a word for a decimal digit, return the decimal digit.
    Otherwise, return None.
    """
    if word.isdecimal():
        return word
    if word in decimal_words:
        return str(decimal_words.index(word) + 1)
    return None


def find_first_decimal(line):
    """Return the first decimal digit in the given string, or None if there is none."""
    regex = r'(\d|' + '|'.join(decimal_words) + ')'
    match = re.search(regex, line)
    if match:
        return convert_to_decimal(match.group(1))
    return None


def find_last_decimal(line):
    """Return the last decimal digit in the given string, or None if there is none."""
    # Reverse the line and the decimal words, then search for the first decimal digit or word.
    sdrow_lamiced = [word[::-1] for word in decimal_words]
    regex = r'(\d|' + '|'.join(sdrow_lamiced) + ')'
    match = re.search(regex, line[::-1])
    # If there is a match, reverse the match and convert it to a decimal digit.
    if match:
        return convert_to_decimal(match.group(1)[::-1])
    return None


def get_calibration_value(line):
    """Return the calibration value for the given line.
    The calibration value is the first decimal digit in the line concatenated with the last decimal digit in the line.
    If there is no decimal digit in the line, return 0.
    If there is only one decimal digit in the line, return that digit concatenated with itself.
    """
    first_decimal = find_first_decimal(line)
    if first_decimal is None:
        return 0
    last_decimal = find_last_decimal(line)
    return int(first_decimal + last_decimal)


def sum_calibration_values(lines):
    """Return the sum of the calibration values for the given lines.
    Lines can be any iterable of strings."""
    total = 0
    for line in lines:
        total += get_calibration_value(line)
    return total


def apply_to_file(filename, func):
    """Apply the given function to the contents of the given file.
    Return the result of the function.
    """
    with open(filename, "r") as f:
        return func(f)


def main():
    """Print the sum of the calibration values for the lines in the input file."""
    total = apply_to_file("resources/input.txt", sum_calibration_values)
    print(total)


if __name__ == "__main__":
    main()
