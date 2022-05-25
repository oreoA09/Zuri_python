# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    if compare_char(word) == compare_char(anagram):
        return True
    else:
        return False

def compare_char(text):
    counts = {item:text.count(item) for item in text}
    return counts

print(find_anagrams("hello", "check"))
print(find_anagrams("below", "elbow"))

