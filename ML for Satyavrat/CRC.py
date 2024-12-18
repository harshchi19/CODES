# CRC
def xor(a,b):
    result=[]
    for i in range(1,len(b)):
        if a[i]==b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)
    
def mod2div(dividend,divisor):
    pick=len(divisor)
    temp=dividend[0:pick]
    
    while pick<len(dividend):
        if temp[0]=='1':
            temp=xor(divisor,temp)+dividend[pick]
        else:
            temp=xor('0'*pick,temp)+dividend[pick]
        pick+=1
        
    if temp[0]=='1':
        temp=xor(divisor,temp)
    else:
        temp=xor('0'*pick,temp)
        
    checkword=temp
    return checkword
    
def encode(data,key):
    l_key=len(key)
    appended_data=data+'0'*(l_key-1)
    remainder=mod2div(appended_data,key)
    codeword=data+remainder
    print("Remainder ",remainder)
    print("Encoded data ",codeword)
    
data=input("Enter data")
key=input("Enter key")
encode(data,key)