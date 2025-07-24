import sys

def main(filepath):

#print messages spread across functions, see stats.py
    print("============ BOOKBOT ============")
    file_contents = get_book_text(filepath)

    from stats import get_word_count
    get_word_count(file_contents)

    from stats import get_character_count
    char_count = get_character_count(file_contents)

    from stats import sort_dictionary
    sort_dictionary(char_count)
    print("============= END ===============")

def get_book_text(filepath):
    print(f"Analyzing book found at {filepath}...")
    with open(filepath) as f:
        file_contents = f.read()    #file's contents are accessed and returned as a string
        #print(file_contents)
    return file_contents

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])