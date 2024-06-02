pos=-1
def search(list,ns):
    for i in range(len(list)):
        if ns==list[i]:
            globals()['pos']=i
            return True
    else:
        return False
list=[5,9,8,2,7,4,10]
ns=int(input("enter the number to be searched"))
if search(list,ns):
    print("Found at position",pos+1)
else:
    print("Not Found")
    
