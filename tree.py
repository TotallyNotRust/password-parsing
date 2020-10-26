import glob, re

def recur(dirr = "./*/"):
    for x in glob.glob(dirr):
        if re.search("\.[a-z-A-Z].$", x):
            yield ("File:", x)
        else:
            try:
                yield [[dirr.split("\\")[1:-1] + [(f:= x.split("\\")[-2])]], [i.split("\\")[-1] for i in glob.glob(dirr[:-2] + f + "/*.*")]]
            except: pass
            for i in recur(x + "*/"):
                yield i

[print(i) for i in recur()]

l = {}

for i in [[['exts', 'yu']],['okok.ok', 'output.txt']]:
    try:
        print("".join(["[\"{}\"]".format(i) for i in i[0][0]]))
    except Exception as e: print(e)

# for i in recur():
#     try:
#         eval("l"+"[{}]"*len(i[0]).format(*i[0]))
#     except:
#         l[i[0]]