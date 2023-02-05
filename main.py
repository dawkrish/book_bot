def countFx(char,data):
    count = 0
    for i in range(len(data)):
        if char == data[i] or char.upper() == data[i]:
            count += 1
    return count

path = 'books/frankenstein.txt'

with open(path) as f:
    file_contents = f.read()
    print(f"--- Begin report of {path} ---")
    print(f"{len(file_contents.split())} words found in the document")
    
    dictionary = {'a': countFx('a',file_contents),
                  'b': countFx('b',file_contents),
                  'c': countFx('c',file_contents),
                  'd': countFx('d',file_contents),
                  'e': countFx('e',file_contents),
                  'f': countFx('f',file_contents),
                  'g': countFx('g',file_contents),
                  'h': countFx('h',file_contents),
                  'i': countFx('i',file_contents),
                  'j': countFx('j',file_contents),
                  'k': countFx('k',file_contents),
                  'l': countFx('l',file_contents),
                  'm': countFx('m',file_contents),
                  'n': countFx('n',file_contents),
                  'o': countFx('o',file_contents),
                  'p': countFx('p',file_contents),
                  'q': countFx('q',file_contents),
                  'r': countFx('r',file_contents),
                  's': countFx('s',file_contents),
                  't': countFx('t',file_contents),
                  'u': countFx('u',file_contents),
                  'v': countFx('v',file_contents),
                  'x': countFx('x',file_contents),
                  'y': countFx('y',file_contents),
                  'z': countFx('z',file_contents),
                 }
    countList = []
    for i in dictionary:
        countList.append(dictionary[i])
    countList.sort(reverse=True)
    

    value_arr = list(dictionary.values())
    keys_arr = list(dictionary.keys())
    
    for i in countList:
        index = value_arr.index(i)
        print(f"The '{keys_arr[index]}' character was found {value_arr[index]} times")
    
    print("--- End report ---")
