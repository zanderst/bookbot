#counts words in book
def num_words(filepath):
    with open(filepath) as f: 
        file_contents = f.read()
        split_file = file_contents.split()
        return f"Found {len(split_file)} total words"
    
#counts characters in book
def num_characters(filepath):
    with open(filepath) as f: 
        file_contents = f.read()
        split_file = file_contents.split()

        counter = {}
        for word in split_file:
            for char in word:
                char = char.lower()

                if char in counter:
                    counter[char] += 1
                else:
                    counter[char] = 1
        
        return counter


def sort_on(count_dict):
    return count_dict[1]