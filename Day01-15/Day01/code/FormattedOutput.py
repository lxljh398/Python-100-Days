
# print("i am {0}, i am {1}d years old".format('Jeck',26))         #采用位置参数来索引
# print("i am {name}, i am {age}d years old".format(**{'name':'jeck','age':26}))   #采用自定义key来缩影,此时**表示将字典的k/v取出
# print("--{name:*^10s}--   =={age:<10.2f}==".format(name='Jeck',age=26.457))   #将name的宽度设置为10,空余的使用*号不全,并居中显示,age类型设置为浮点型,宽度为10.并左对齐
# print("原数:{:d}  二进制:{:b}, 八进制:{:o}, 十六进制x:{:x},十六进制X:{:X}".format(15, 15, 15, 15, 15))   #进制转换
# print("原数:{:d}, 科学计数法e:{:e}, 科学计数法E:{:E}" .format(1000000000,1000000000,1000000000))    #科学计数法表示
# print("原数:{:2F}, 百分号表示{:.2%},  原数:{:d},自动分割表示:{:,}".format(0.75,0.7584,10000000,10000000 ))  #百分号表示及自动分割



# a=('{0}{1}'.format('lx',30))
# a='{name}{age}'.format(**{'name':'lx','age':30})

a='{name:*^10s}{age:<10.2f}'.format(name='lx',age=25)
# a="--{name:*^10s}--   =={age:<10.2f}==".format(name='Jeck',age=26.457)

# print("原数:{:d}  二进制:{:b}, 八进制:{:o}, 十六进制x:{:x},十六进制X:{:X}".format(15, 15, 15, 15, 15))   #进制转换
# print('{:.2%}'.format(15.021556))
# print("原数:{:2F}, 百分号表示{:.2%},  原数:{:d},自动分割表示:{:,}".format(0.75,0.7584,10000000,10000000 ))  #百分号表示及自动分割
# print(a)

# print('%20s' %('fdsafd'))

# print('Age:%20.2f' %(25.51245))

print("--{name:*^10s}--   =={age:<10.2f}==".format(name='Jeck',age=26.457))