# http://www.runoob.com/python/python-100-examples.html
# test one
tup1 = (1,2,3,4)
count = 0;
for x in tup1:
    for y in tup1:
        for z in tup1:
            if(x != y) and (x != z) and (y != z):
                count+=1;
print('test on result: ' ,count);

# test two

#test three

#test five
'''
l = []
for i in range(3):
    x = int(input('i参数'));
    l.append(x);
l.sort();
print(l);
'''
#test six
sixl = []
def funcsix(n):
    for sixx in range(n):
        if sixx == 0:
            sixl.append(0);
        elif sixx == 1:
            sixl.append(1);
        else:
            sixl.append(sixl[sixx-1] + sixl[sixx-2]);
funcsix(10)

print(sixl)

#test 8

for eighti in range(9):
        eighti+=1
        eightilist = [];
        for eightj in range(eighti):
            eightj+=1
            product = eighti * eightj;
            content = str(eighti) +' * '+str(eightj)+' = '+str(product)
            eightilist.append(content);
        print(eightilist);