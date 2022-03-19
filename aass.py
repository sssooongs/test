"""装饰器@check作用于plus函数时，plus函数本身作为参数func传入装饰器中。
在装饰器check的定义内部，定义了一个函数模板，描述了对输入的func如何处理
。可以看到，newfunc对func（也就是输入的plus）套用了判断数据类型的if语句，
 最后，再将套好的newfunc输出，替代原来的func 。
 这样，此时执行func就是在执行newfunc，执行plus就是在执行套上if语句的新函数。
 参数一般用不定长的*args,**kwargs来表示，args，kwargs这两个形参英文字母是什么无所谓可以自己定，
 关键是前面的单星号*和双星号**
 """


def 炼丹炉(func):#定义装饰器
  def 变身(*args, **kwargs):#定义函数模版，如何处理func
      aa = args[0] +1
      bb = args[1] +1
      #return func(aa,bb)
      cc = func(aa, bb)
      print(cc)
  return 变身 #将处理后的func作为新函数newfunc输出。注意，这里的wrapper没有打括号就证明是返回了函数体，而非函数运行结果


@炼丹炉  # 把下面的 ‘孙悟空’ 塞进炼丹炉，并把新的孙悟空复制给下面的函数
def 孙悟空(a ,b):
    return (a+b)

def xunhuan():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
             print(n, '等于', x, '*', n//x)
             break
        else:
            # 循环中没有找到元素
            print(n, ' 是质数11111111')



if __name__ == "__main__":
    孙悟空(3,2)
