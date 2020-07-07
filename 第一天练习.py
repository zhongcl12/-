# # 20,30,60,80  成绩不可修改
# #
# # "王大锤" "王二锤" "王小锤" 学生姓名清单，支持修改
# #
# # 姓名：王大锤  手机号：19989778898 身份证号: 21384028340982390482349
# #
# # 10001 10002 100003 100004 学号，支持修改，并且不能重复
# a = (20,30,60,80)
# s = ["王大锤" ,"王二锤", "王小锤"]
# d = {'姓名':'王大锤','手机号':19989778898,'身份证号':21384028340982390482349}
# z = {10001,10002,100003,100004}
# print(a)
# print(s)
# print(d)
# print(z)
#
#
# a = [1,2,3,4,5,6,]
# z,x,*n = a
# print(z)
# print(x)
# print(n)
#
#
# a = {'name':'小名','age':66}
# x,y = a
# print(x)
# print(y)
#

# a = '1234567'
# print(a[1:])
# print('c=',a[:5:-1])

#
#
# # # range()
'''第一个参数:起始数据 默认为0
 第二个参数:代便结束值 不包括边界值t = 1
# # for s in  range(50,0,-1):
# #     t = t * s
# # print(t)
# # # 第三个参数:步长(增量) 默认值为1
'''


# for q in range(1,100):
#     if (q % 3 == 0):
#         #continue
#         print(q)


# for q  in range(100,200):
#     if (q % 4 != 0 ):
#           continue
#     print(q)


'''# # 冒泡排序'''
# a = [1,2,5,496,54,5,145,14,1,1,21,2,554]
# s = len(a)
# print(s)
# for b in range(len(a)-1):
#     for c in range(len(a)-1-b):
#         if a[c]>a[c+1]:
#             a[c],a[c+1] = a[c+1],a[c]
# print(a)
'''排序'''
# a =[1,2,5,4,2,98,54,32,47,19]  # 排序从小到大
# a.sort()
# print(a)
'''# 乘法表'''
# for a in range(1,10):
#     for b in range(1,a+1):
#         print(a,'x',b,'=',a*b,end='\t')
#     print()

'''# # 输入4位数num，每位都加5,再%10后倒序输出'''
# print(type(c))a = input("请输入四位数")
# c = ""
# for i in a:
#     b = str((int(i)+5)%10)
#     print(b)
#     c = c+b
# print(c[::-1])

'''# 1.编写如下程序
# 尝试有数部分部分:I
# # a.用户输入1-7七个数字，分别代表周- .到周 日
# b.如果输入1~5，打印对应的“周."~“周五”， 如果输入的数字是6或7.打印输出“周末":
# c.如果输入0，退出循坏
# d.输入其他内容，提示:“输入有误，请重新输入!”
# 提示:本题可以使用if和Iwhile循坏， 同时需要校验用户的输入是否正确。不用考虑浮点数等情况。'''
# a = ['周一','周二','周三','周四','周五','周六','周日']
# while True:
#     b = int(input("请输入数字:"))
#     if 0<b<=7:
#         print(a[b-1])
#     elif b==0:
#         print("退出循环")
#         break
#     else:
#         print("输入有误，请重新输入!")

'''   输入账号和密码，若账号密码正确则显示登录成功，若账号密码错误，则显示登录失败。最多可以输入三次。'''
# a =0
# while a < 3:
#     mingzi = input('账户')
#     mima = input('密码')
#     if mingzi=='钟成林'and mima == '123456':
#         print('登录成功')
#         break
#     else:
#         a += 1
#         if a == 3:
#             print('密码错误超过3次')

'''#   有四位数1,2,3,4,能组成多少个三位数,'''
# class b:
#     a =[1,2,3,4]
#     b =len(a)
#     for i in range(b):
#         for s in range(b):
#             for c in range(b):
#                 if i != s and s != c and c!=i:
#                     print(a[i],a[s],a[c])
#
'''#封装'''
# class L():
#     qian=100000
#     fangzi=50
#     __neiku=20
#
#     def ji_neng(self):
#         print("偷电瓶")
''' 子承父业'''
# class b(L):
#     aihao ="花钱"
#
# a=L()
# print(b.aihao)
# print(a.ji_neng())
# print(a.fangzi)

''' 文件操作'''#  b  二进制写入
# t = open("zhong.txt",'w')  #open 文件  ,w 代替写入
# t.write("zhong cheng")     #写入
# t.close()                  #关闭
'''a 追加写入,换行'''
# t= open('zhong.txt','a')     #  a 追加写入
# t.write("wu yu\nhiajis\nshas")
# t.writelines('sad',"sf","dgsd")
# t.writable()       #判断是否可追加写入
# t.close()
'''r 读取数据'''
# t = open('zhong.txt', 'r')
# print(t.read())     #读取数据
# print(t.read(2))     #读取数据字符多少
# print(t.readline())    #读取数据一行
# print(t.readlines())     #读取数据全部行
# t.close()
'''字符串截取'''
# a = 'dscjhgvzschbzj'
# print(a[0])
# print(a[0:-1])
# print(a[1::2])
# print(a[1:-1:2])
# print(a[5:1:-1])
# print(a[4::-1])
''' with'''
# with open("zhong.txt",'r') as  a:   #with 使用一个上下文管理器
#     s = a.readlines()
#     print(s)
#     for d in s:
#         print(d.replace("\n",""),end='\t')   #print 默认带一个换行
'''格式化'''
#占位
# for z in range(1,10):
#     for j in range(1,z+1):
#         print("%d x %d = %d"%(j,z,j*z),end='\t')
#     print()
#  .format
# for z in range(1,10):
#     for j in range(1,z+1):
#         print("{} x {} = {}".format(j,z,j*z),end='\t')
#     print()
'''修改列表'''
# a = [1,5,49,4,2,1,5,84,36,4]
# # # a[0] = 5
# # # print(a)
# # # a[2:8] = 12,5,46,5,45,4
# # # print(a)
'''新增数据'''
# s = [1,5,4,9,54,6]
# s.append('王大锤')
# print(s)
# s.extend(["字符","那个"])
# print(s)
# s.insert(0,"第三方胡教授")
# print(s)
'''删除列表'''
# a= [1,5,1,77,8,5,15,16]
# print(a.pop(1))#根据下标删除
# print(a)
# a= [True,1,5,1,77,8,5,15,16]
# a.remove(1) # 根据内容删除,,True 代表1,false 代表0
# print(a)
# a.clear()   #全部删除
# print(a)
'''字典'''
a = {"名字":"小屁孩","年纪":"2","学历":"博士"}
# for key in a:
#     print(a[key])
# a['名字'] = "小朋友"
# print(a)

# a.update(身高=58)
# print(a)
# b = {'体重':"98",'爱好':"学习"}
# a.update(b)
# print(a)
# b.pop("爱好")#删除
# print(b)
# b.clear()# 清空
# print(b)

# try:
#     a = open("ffsdfdf.txt",'r')
#     print(a.read())
#     a.close()
# except:
#     print("文件不存在")

def a(s,d):
    try:
        return s/d
    except:
        return
print(a(5,0))



