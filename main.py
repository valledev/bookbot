def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    number_of_words = count_words(book_text)
    count_of_chars = count_chars(book_text)
    sorted_list_of_chars = sort_report(count_of_chars)

    #print report
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document")
    #for char in count_of_chars:
    #    count = count_of_chars[char]
    #    print(f"The '{char}' character was found {count} times")
    for dict in sorted_list_of_chars:
        char = dict["letter"]
        count = dict["number"]
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")
    print(count_of_chars)
    print(sorted_list_of_chars)
    
def get_book_text(path):    
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_chars(text):
    count = {}
    for char in text:
        if char.isalpha():
            if char.lower() in count:
                count[char.lower()] += 1
            else:
                count[char.lower()] = 1
    return count

def sort_on_number(dictionary):
    return dictionary["number"]

def sort_on_letter(dictionary):
    return dictionary["letter"]

def sort_report(dictionary):
    list = []
    for key in dictionary:
        entry = {}
        entry["letter"] = key
        entry["number"] = dictionary[key]
        list.append(entry)
    #list.sort(reverse=True, key=sort_on_number)
    list.sort(reverse=False, key=sort_on_letter)
    return list

main()