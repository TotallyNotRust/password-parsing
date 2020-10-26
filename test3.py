import glob
import sys

search = True
argument = ""

if len(sys.argv) > 1:
    if "search" in sys.argv:
        try:
            ind = sys.argv.index("search")
            search = True
            argument = sys.argv[ind+1]
        except: pass

def passwordFrequency():
    password = {}
    longest = 0
    for i in glob.glob("./exts/*/*.txt"):
        for i in open(i, "r"):
            if not i == "\n":
                try:
                    x = password[i.split(":")[0]]
                    password[i.split(":")[0]] +=1
                except:
                    if len(i.split(":")[0]) > longest: longest = len(i.split(":")[0][:-2])
                    password[i.split(":")[0]] = 1

    for i in (x:= sorted(password.items(), key=lambda item: item[1])):
        print("{: <{longestn}} | {: <{longest}}".format(i[1], i[0], longest = longest, longestn = len(str(x[-1][1]))))
    print(str(x[-1][1]))

def searchWord():
    for file in glob.glob("./exts/*/*.txt"):
        for i in open(file, "r"):
            if argument in i: 
                print(i.strip("\n"))

print(argument)
if __name__ == "__main__":
    if search:
        searchWord()
    else: 
        passwordFrequency()