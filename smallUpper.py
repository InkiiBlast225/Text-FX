abLower = 'abcdefghijklmnopqrstuvwxyz'
abUpper = 'ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘꞯʀsᴛᴜᴠᴡxʏᴢ'
abDict = {}
for i in range(len(abLower)):
    abDict[abLower[i]] = abUpper[i]

inTxt = input('Enter Text To Make Small Caps: ').lower() # Does tHIs work?
outTxt = ''
for i in inTxt:
    if abDict.get(i) != None:
        outTxt += abDict.get(i)
    else:
        outTxt += i
print(outTxt)