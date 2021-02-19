x= open('file.txt','r')
words_list=[]
y=x.read()
file=y.split('\n')
print(file)
for word in file:
    new_word=word.rsplit(' ')
    for words in new_word:
        if words not in words_list:
            words_list.append( words)
    
words_list.sort()
print(words_list)