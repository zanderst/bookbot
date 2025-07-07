from stats import num_words, num_characters, sort_on


#opens file and returns contents as string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents




def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]

    
    # print(get_book_text(path))
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}\n----------- Word Count ----------")

    print(num_words(path))
    print("--------- Character Count -------")
    char_count = num_characters(path)
    char_list = list(char_count.items())
    char_list.sort(reverse=True, key=sort_on)
    for char, count in char_list:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
    



main()
