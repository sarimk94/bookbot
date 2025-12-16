from stats import get_num_words, get_chars, sorted_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        s = f.read()
        return s

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("Usage: python3 main.py <path_to_book>")
    book = get_book_text(sys.argv[1])
    num_words = get_num_words(book)
    print(f"Found {num_words} total words")
    chars = get_chars(book)
    sorted_values = sorted_dict(chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("------- Character Count -------")
    for item in sorted_values:
        print(f"{item['char']}: {item['num']}")

main()