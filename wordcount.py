# put your code here.

# Pseudocode:
# Open file 
# creat an empty dictionary 
# For loop that splits using spaces 
# for each word create a key and then starts counting 
# return dictionary

def word_count(file_name):
    poem = open(file_name)

    word_count = {}

    for line in poem:
        # print line 
        line = line.rstrip()
        individual_words = line.split(" ")
     
        # print individual_words

        for words in individual_words:
            '''option 1 is super slow'''
            # if words not in word_count.iterkeys():
            #     word_count[words] = 1
            # elif words in word_count.iterkeys():
                # word_count[word_count] += 1
            """option 2 is super fast"""
            word_count[words] = word_count.get("words", 0) + 1
            

    for word, count in word_count.iteritems():
        print "%s %d" % (word, count)

    poem.close()

word_count("twain.txt")