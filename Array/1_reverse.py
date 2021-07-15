# Write a program to reverse an array or string


def reverseWord(s):

    # return s[::-1]
    
    st=0
    e=len(s)-1
    s=list(s)
    while st < e:
        s[st],s[e]=s[e],s[st]
        st+=1
        e-=1
    return "".join(s)

print(reverseWord("Geeks"))