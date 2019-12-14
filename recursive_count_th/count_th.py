'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC as proceed through word the length will decrease till final opportunity of occurence
    #at len 2 of final two indexs
    # Also if input length is less than 2 will return 0 by default 
    if len(word) < 2:
        return 0 #means no occurence of 'th' was found

    if word[0] == "t" and word[1] == "h":
        return 1 + count_th(word[1:]) #from index 1, not including 1 to rest of word 
        #but add 1 to occurence count
        #we are proceeding to our base case as we go through word left to right
    else:
        return count_th(word[1:]) #from index 1, not including 1 to rest of word 
        #but occurence count not increased
    
    print(count_th)
    


