txt = "curitiba pr"
x = 0
try:
    x = txt.index("-")
    print(txt[x+1:x+4])
except:
    pass
