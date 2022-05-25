
def read_file_content(filename):
    # [assignment] Add your code here 
    file = open(filename, "r")
    print(file.read())
    return file.read();

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    asCount = text.count("as")
    wouldCount = text.count("would")
    print(asCount, wouldCount)

    return {"as": asCount, "would": wouldCount}

print(count_words())