def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            if url not in entry[1]:     #url ,keyword only apper once a time
                entry[1].append(url)
            return
    #not found, add a new entry
    index.append([keyword,[url]])
        
def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def split_string(source, splitlist):
    output = []
    atsplit = True #At a split point
    for char in source: #iterate through string by each letter
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                #add character to last word
                output[-1] = output[-1] + char
    return output