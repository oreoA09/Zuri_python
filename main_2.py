# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
     story = open(filename)
     file_list = story.read()
     story.close()
     return file_list
#try returning before close()

def count_words():
    text = read_file_content("./story.txt").split()
    # [assignment] Add your code here
    counts = {item:text.count(item) for item in text}
    return counts
    # return {"as": 10, "would": 20}

print(count_words())