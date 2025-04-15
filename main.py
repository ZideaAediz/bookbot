from stats import get_num_words
from stats import get_character_count
from stats import get_sorted_character_count

import sys

def get_book_text(filepath):
    contents = None
    with open(filepath) as f:
        contents = f.read()

    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    contents = get_book_text(book)
    num_words = get_num_words(contents)
    chars = get_sorted_character_count(get_character_count(contents))
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in chars:
        print(f"{c["char"]}: {c["count"]}")
    print("============= END ===============")

main()