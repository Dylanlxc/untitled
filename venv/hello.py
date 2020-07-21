names = ['Michael', 'Bob', 'Tracy']
for name in names:
    if name == "Michael":
        print("指定名字：%s" %(name))
    else:
        print(name)



name1 = "liuxinchi"
name2 = "liuxinchi"
if name1 == name2:
    print(True)
else:
    print(False);
d = {};
d['Jack'] = 90

if 'Jacka' in d:
    print(d['Jacka'])
else:
    print("Jacka不存在！")

if d.get("Jacka",False):
    print(d['Jack'])
else:
    print("Jacka不存在！")