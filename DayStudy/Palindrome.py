'''
Find Palindrome(Using queue, stack)
input : string "s"
output : If "s" is palindrome display "true". not palindrome case "false".
'''

def palindrome(s):
    qu=[]    #Define a queue as a list
    st=[]    #Define a stack as a list
    for x in s:    #step 1. String alphabet insert to queue and stack (not space or special string)
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())
    while qu:    #stem 2. PPick up queue and stack string. compare to both string.
        if qu.pop(0) != st.pop():
            return False

    return True


print(palindrome("Wow"))    #true
print(palindrome("palindrome"))    #Flase
print(palindrome("Madam, I'm Adam."))    #true