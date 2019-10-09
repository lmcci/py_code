# with 不用try 不用close

f = open('res/hello')

try:
    t = f.read()
    print(t)
except Exception:
    print('Exception')

f.close()

with open('res/hello') as f:
    t = f.read()
    print(t)

