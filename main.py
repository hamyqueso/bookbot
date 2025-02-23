from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents


def main():
    # filepath = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]

    num_words = count_words(get_book_text(filepath))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    num_characters = count_characters(get_book_text(filepath))
    # print(f"{num_words} words found in the document")
    pretty_print(num_characters)
    print("============= END ===============")

main()
