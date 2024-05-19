def open_book_txt(filename: str) -> str:
    books_dir = "books"
    try:
        with open(f"{books_dir}/{filename}.txt") as f:
            file_contents = f.read()
    except Exception as e:
        print(f"File read error: {e}")
    return file_contents


def number_of_words(text: str) -> int:
    length = None
    try:
        words = text.split()
        length = len(words)
    except Exception as e:
        print(f"Text splitter error: {e}")
    return length


def count_chars_in_text(text: str) -> dict[str, int]:
    text_lower = text.lower()
    counts = {}
    for char in text_lower:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts


def convert_dict_into_list_of_dicts(dictionary: dict, key_one, key_two) -> list[dict[str, int]]:
    list_of_dictionaries = []
    for k, v in dictionary.items():
        new_dictionary = {key_one: k, key_two: v}
        list_of_dictionaries.append(new_dictionary)
    return list_of_dictionaries


def filter_dict(dictionary: dict) -> dict:
    for k, v in dictionary.copy().items():
        if not k.isalpha():
            dictionary.pop(k)
    return dictionary


def sort_on(dictionary: dict):
    return dictionary["count"]


def print_char_report(word_count: int, char_counts: list[dict[str, int]], book_name: str) -> None:
    header_line = '-------'
    print(f"{header_line} BEGIN char report of: {book_name} {header_line}")
    print(f"Number of words found in document: {word_count} \n ")
    print("Character counts sorted by counts in descending order:")
    for count in char_counts:
        print(f"The {count['letter']} character was found {count['count']} times")
    print(f"{header_line} END char report of: {book_name} {header_line}")


def main():
    frankenstein = "frankenstein"
    word_count = number_of_words(open_book_txt(frankenstein))
    counts = count_chars_in_text(open_book_txt(frankenstein))
    filtered = filter_dict(counts)
    list_of_dicts = convert_dict_into_list_of_dicts(filtered, "letter", "count")
    list_of_dicts.sort(reverse=True, key=sort_on)
    print_char_report(word_count, list_of_dicts, frankenstein)


if __name__ == '__main__':
    main()
