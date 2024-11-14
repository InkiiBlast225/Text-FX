inTxt = input('Enter text to space out: ')
spaceNo = int(input('Enter how many spaces: '))
ignoreWs = (input('Space out white space in given text? ').lower() == 'no')

outTxt = ''
for i in range(len(inTxt)):
        outTxt += inTxt[i]
        if not(ignoreWs and (inTxt[i] == ' ')):
            outTxt += ' ' * spaceNo
print(outTxt)