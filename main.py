
def main():
    with open("./books/frankenstein.txt",'r') as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        chars_count_dict = count_chars(file_contents)
        print("---Begin reporrt of /books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")
        for char in chars_count_dict:
            print(f"The '{char}' character was found {chars_count_dict[char]} times ")
        print("--- End report ---")




def count_words(text):
    words = text.split()
    return len(words) 

def count_chars(text):
    chars_dict={}
    for char in text:
        if( char.isalpha()):
            char = char.lower()
            if char in chars_dict:
                chars_dict[char]+=1
            else:
                chars_dict[char]=1
    return chars_dict


main()