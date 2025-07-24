#functions are called via main.py

def get_word_count(text):
    #print(text)
    word_count = len(text.split())
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    return word_count

def get_character_count(text):
    lowercase_text = text.lower()   #lowercase-conversion necessary for case insensitivity
    character_count = {}
    for char in lowercase_text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count [char] = 1
    print("--------- Character Count -------")
    return character_count

def sort_dictionary(dict):
    char_count = []
    for i in dict:
        char_count.append({"char": i, "num": dict[i]})
    def sort_on(char_list):
        return char_list["num"]
    char_count.sort(reverse=True, key=sort_on)
    #print(char_count)
    for entry in char_count:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    return char_count