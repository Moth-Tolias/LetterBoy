"""return a jumbled version of a string. eg, the lazy hamster is jumping becomes the lzay hmasetr si jmunipg

shuffles insides of words.
"""
import random
import string

#okay, so this will be the jmuble algorythim

#variables, passed
#string_to_jumble = "" #yeah
#jumble_mode =  true # do u switch words of two letters

def string_jumble(string_to_jumble, jumble_mode = True):
        #variables, internal
        string_to_return = "" #New string
        string_words = [""] #array containing the words of the string
        current_word = [] #array containing the letters of the current word
        punctuation_ = [] #array containing the punctuation
        i = 0
        j = 0
        
        #put the words in an array
        for char in string_to_jumble:
                #each space signifies a new word
                if char not in string.ascii_letters:
                        punctuation_.append(char)
                        i += 1
                        ##make sure there's something to put it in!
                        string_words.append("")
                else:
                        #otherwise add to the entry
                        string_words[i] += char
                        #print(string_words) THIS IS WORKING
        
        #put the letters of the word into an array, and then switch 'em
        for word in string_words:
                #if the word is two long and mode is true switch 'em
                if (len(word) >= 0) and (len(word) <= 3) :
                        if jumble_mode == True:
                                #
                                for char in word:
                                        current_word.append(str(char))
                                        #print(current_word)
                                random.shuffle(current_word)
                                #pop the word and a space into the return string
                                for char in current_word:
                                        string_to_return += char
                                string_to_return += punctuation_[string_words.index(word)]
                                #print(string_to_return)
                                current_word.clear()
                                #that's all for this word
                                continue
                #ok now for the REAL real deal
                #take  away the first letter and put it in string_to_return bc it souldn't be jumbled
                i = 0
                for char in word:
                        if i == 0:
                                string_to_return += char
                                #print(string_to_return)
                                i = 1
                                #assert bluh WORKING
                                continue
                        #then put almost all of the word in current_word[]
                        #current_word.append("")
                        if (i+1) < len(word):
                                current_word.append(str(char))
                                #print(current_word)
                                i +=1
                #we should be at the last character now
                #print(i)
                print(len(word)+100)
                #jumble it
                #random.shuffle(current_word)
                #add to the new string
                for char in current_word:
                        string_to_return += char
                #add the last lettr pus a space
                #if word[i]:
                string_to_return += word[i]
                #string_to_return += punctuation_[i]
                string_to_return += punctuation_[string_words.index(word)]
                print(punctuation_[string_words.index(word)])
                #flush the string
                current_word.clear()
                #next word!
        print(string_to_return)
        print(punctuation_)

#done
#string_jumble("a0boop1boop3boop4boop5hey")
string_jumble("I1think2my3dog4is5terribly6lazy;7I8-9I!mean,£he$-%is^really&quite*fat.")#looks like list.index won't work for us
#string_jumble("")#fix this too
