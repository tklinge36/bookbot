import sys
from stats import number_words, get_chars_dict, sorted_chars

def get_book_text(filepath):
    with open(filepath) as file:
        file_content = file.read()
    return file_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]

    text = get_book_text(book)
    num_words = number_words(text)
    chars_dict = get_chars_dict(text)
    sorted_list = sorted_chars(text)
    print("============ BOOKBOT ============")
    print("Analysing book found at " + book + "... ")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count -------")
    
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()