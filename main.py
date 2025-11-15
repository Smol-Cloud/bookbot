from stats import get_num_words, char_count, sorted_char_count
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    relative_file_path = sys.argv[1]
    text = get_book_text(relative_file_path)
    num_words = get_num_words(text)
    chars = char_count(text)
    sorted_chars = sorted_char_count(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")

main()