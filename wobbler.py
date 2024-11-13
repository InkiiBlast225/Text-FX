def xor(a,b):
    if not(a) and not(b):
        return(False)
    elif a and b:
        return(False)
    return(True)

inTxt = input('Enter text to wobble: ') # Test Case: Does tHIs work?
inWblStart = input('Start w/ uppercase (default) or lowercase: ') # & Means 'input of starting wobble'
startLower = (inWblStart.lower() == 'lowercase') # & Means 'should i start w/ lower or upper?'

outTxt = ''
for i in range(len(inTxt)):
    if xor(not(startLower),(i % 2 == 0)):
        outTxt += inTxt[i].lower()
    else:
        outTxt += inTxt[i].upper()
print(outTxt)