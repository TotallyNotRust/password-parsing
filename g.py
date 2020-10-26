import glob
import re
import time
import gc
import sys
import os


print("Ready!")

text = True
sql = False

if len(sys.argv) > 2:
    if "--no-txt" in sys.argv:
        text = False
        print("NO TXT")
    if "--no-sql" in sys.argv:
        sql = False
        print("NO SQL")

input()

path = os.getcwd()

# files = glob.glob("./*/*.*")

files = [i for i in glob.glob("./*/*.*")+glob.glob("./*/*/*.*") if not "exts" in i]

try:
    os.mkdir(os.getcwd()+"/exts")
except:
    pass

leng = len(files)

for file in files:
    if file.endswith(".txt") and text:
        if not file.endswith("output.txt"): 
            gc.collect()
            try:
                f = open(file, "r+", encoding="utf-8")
            except UnicodeDecodeError:
                try:
                    f = open(file, "r+", encoding="cp1252")
                except Exception as e:
                    print("Error at:", file); print(e)
                    continue
            except MemoryError:
                print(file, "is too big (MemoryError)")

            try:
                for i in f:
                    try:
                        if re.findall("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z].$", i.split(":")[0]):
                            #try:
                            ext = i.split(":")[0].split(".")[-1]
                            if not ext in os.listdir(os.getcwd()+"/exts/"):
                                os.mkdir(path+"/exts"+"/"+ext)
                            x = open("./exts/" + ext + "/output.txt", "a")
                            x.write(i + "\n")
                            x.close()
                            print(i, end="")
                            #print(time.process_time())
                            #except Exception as e: print("Can't write to ", file, e)
                    except Exception as e: print(file, e, i)
            except Exception as e: 
                print("Error at:", file); print(e)
    elif file.endswith(".sql") and sql:
        print(file)
        try:
            for f in open(file, "r", encoding="cp1251"):
                try:
                    for x in re.findall("[a-zA-Z0-9]+@[a-zA-Z0-9]+\."+ext, f):
                        try:
                            outputFile.write(x + "\n")
                            print("{: <20.20} | {}".format(x.split("@")[0], time.process_time()))
                            #print(time.process_time())
                        except Exception as e: print("Can't write to ", outputFile); print(e)
                except Exception as e: print(outputFile, e); print("REEE")
        except Exception as e:
            print("Error at", file);print(e)
    else:
        print(file)

print(time.process_time())  