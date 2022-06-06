def read_file(filename):
    openfile = open('./story.txt', 'r')
    read_file = openfile.read()
    return read_file
    
def count_words():
    text = read_file("./story.txt")
    count = {} 

    text = text.split()
    #print(split_text)
   
    for word in text:
        count[word] = text.count(word)
    return count


print(count_words()) 