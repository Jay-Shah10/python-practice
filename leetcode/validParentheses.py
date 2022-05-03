



def isValid(s: str) -> bool :
    print(len(s))
    for i in range(0, len(s)-1):
        ob = s[i]
        cb = s[i+1]
        print(ob, cb)
        if (ob == '(' or ob == '{' or ob == '[') and (cb == ')' or cb == '}' or cb == ']'):
            return True


        

def main(): 
    s = "()[]"
    print(isValid(s=s))


if __name__ == '__main__':
    main()
