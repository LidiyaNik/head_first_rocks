phrase = "Don't panic!"

plist = list(phrase)
print(phrase)
print(plist)
nlist = ''.join(plist[1:3])
nlist = nlist + ''.join([plist[5], plist[4], plist[7], plist[6]])
print(nlist)