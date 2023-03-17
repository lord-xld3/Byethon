def palin(InputText):
    inputLength = len(InputText)
    reverseArray = [None] * (inputLength)
    for i,j in enumerate(InputText):
        reverseArray[inputLength-i-1] = j
    reverseText = ""
    for x in reverseArray:
        reverseText = reverseText + x
    if InputText == reverseText:
        return True
    else: return False

# get the input => inputText
InputText = input("Enter in text: ")

if palin(InputText)==True:
     print(InputText + " Is a palindrome!")
else:
    print(InputText + " Is not a palindrome!")