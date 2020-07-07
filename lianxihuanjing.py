
# #
# # a = 1545612
# # b = 15452555
# # print(a + b)
# #   #python 靠缩进识别代码块,一个代码块是一个整体
# #
# # a,b,c =[1,2,3]   #解包赋值
# #
# # print(a)
# # print(b)
# # print(c)
# #
# # z,x,*c = [1,2,3,4,5]
# #
# #
# # print('z =',z)
# # print('x =',x)
# # print('c =',c)
# #
# # zi = ['张三','25','p白',18000.00]
# # di = {'姓名':'张三','年龄':25,'课程':'p白','薪资':18000.00}
# # print(zi)
# # print(di)
# #
# # a = 1
# # b = 2
# # print(a**b)
# # print(a/b)
# # print(a//b)
# # print(a%b)
# # print(a==b)
# #
# #
# #
# # a=1456321385
# #
# #
# #
# # a//=10000
# #
# # print(a%10)
# # print(10%60)
# #
# # fen_1 =[1,11,44,5,22,88,8,56,18,59,67,97,68,255]
# # for fen in fen_1 :
# #  if (0 <= fen & fen < 60):
# #     print("不及格")
# #  elif (60<=fen<70):
# #     print("及格")
# #  elif (70 <= fen <80):
# #     print("良好")
# #  elif (80 <= fen <=100):
# #     print("优秀")
# #  else :
# #     print("请输入有效分数")
# # # 100以内数的和
# # s = 0
# # for i in range(100):
# #     s = s + i
# # print(s)
# # # range()
# # # 第一个参数:起始数据 默认为0
# # # 第二个参数:代便结束值 不包括边界值
# # # 第三个参数:步长(增量) 默认值为1

'''
乘法表
'''

# for i in range(1,10):
#     # print("i每次遍历的值为:",i)
#     for j in range(1,i+1):
#         # print("j每次遍历的值为:",j)
#         print(j,"*",i,"=",i*j,end="\t") # \t 空格
#     print(end="\n")  # \n换行





# #
# # s = 1
# # for i in range(10,0,-1):
# #     s = s * i
# # print(s)
# #
# #
# #
# # # 猜数字
# # #  flag(变量取名)
# # flag = True
# # a = 50
# # while flag:
# #     b = int(input('请输入数字'))
# #     if b > a :
# #         print('大了')
# #     elif b < a :
# #         print('小了')
# #     else :
# #         print("猜对了")
# #         flag = False


#
# for q in range(1,100):
#     if (q % 3 == 0):
#       print(q)
#
# for q  in range(100,200):
#     if (q % 4 != 0 ):
#           continue
#     print(q)

# def shang(a,b):
#     if(b == 0):
#         print('除数不能为0')
#     else:
#         print('商为',a // b,'余为',a % b)
#
# shang(10,0)



#
# def shang(a,b):  #(行参)
#     if(b == 0):   # 判断 b如果等于0直接执行return
#         return  None  #返回 None
#     else: #不满足if,执行以下操作
#         return (a // b ,a % b)  #将a和b的值 取余和取商
#
# res = shang(10, 5)  #(实参),将变量值赋值到res
#
# if res is None:  #判断res 是否为None
#     print("参数错误")
# else:
#     print("商为:", res[0], "余为:", res[1])


#
# def shang(a,b =5):
#     if(b == 0):
#         print('除数不能为0')
#     else:
#         print('商为',a + b,'余为',a - b)
#
# shang(a=15)
# #  面向对象
# class zhong():
#     a = None
#     b = None
#     res = None
#     def input(self,a,b):
#         self.a=a
#         self.b=b
#     def jia(self):
#         self.res = self.a + self.b
#     def cheng(self):
#         self.res = self.a * self.b
#     def abc(self):
#         print(self.res)
#
#
#
# A = zhong()
# A.input(10,20)
# A.input(10,20)
# A.jia()
# A.abc()
#
# A.cheng()
# A.abc()


#
# class zhong():
#     res = None
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def jia(self):
#         self.res = self.a + self.b
#     def cheng(self):
#         self.res = self.a * self.b
#     def abc(self):
#         print(self.res)
# A = zhong(12,40)
#
# A.jia()
# A.abc()
#
# A.cheng()
# A.abc()
#
#





'''
# # 乘法口诀表
'''
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'x',i ,'=',j*i,end='\t')  #end默认值"\n"换行,"\t" tab空格
#     print()

#
# for z in range(1,20):
#     for i in range(1,z+1):
#         print(z,'x',i,'=',z*i,end='\t')
#     print()








'''# # 冒泡排序'''
# i= [1,5,4,6,2,145,85,45,45,4,25,1,5,4,5,4,5,5,]
# b = len(i)
# print(b)
# for d in range(b-1,0,-1):
#     for j in range(d):
#         if i[j]>i[j+1]:
#             i[j],i[j+1] =i[j+1],i[j]
# print(i)
#
#








# a = [8,1.2,5,54.44,89,89,9,8.4,6,4,961,6.16,4.846,48,41,96.84]
#
# print(a)

#
#
# a =[1,2,5,4,2,98,54,32,47,19]  # 排序从小到大
# a.sort()
# print(a)



# 冒泡排序
# a=[1,5,4,6,2,3,8,4,5,4,54,1,25,45,4,65,56,54,541,]
# lens= len(a)  #长度19位
# print(lens)
# for z in range(lens-1,0,-1):  #z 取长度倒序值
#     for j in range(z): #将z的值命名在j  里
#         if a[j]>a[j+1]: #相邻两个数值比较大小
#             a[j],a[j+1] =a[j+1],a[j]  #换位置
# print(a)

# 乘法口诀表
# for z in range(1,10):
#     for j in range(1,z+1):
#         print(z,'x',j,'=',z*j,end='\t')
#     print()


# a ="546"
# b =123
# print(int(a)+b)
# print(str(b)+a)
#
# print(list(a))
# print(set(a))
#
# t = open("zhong.txt",'w')  #open 文件  ,w 代替写入
# t.write("zhong cheng")     #写入
# t.close()                  #关闭
# t= open('zhong.txt','a')     #  a 追加写入
# t.write("wu yu")             #  b  二进制写入
# t.close()
