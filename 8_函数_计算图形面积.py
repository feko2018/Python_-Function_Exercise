# -*- encoding:utf-8 -*-


# 写函数，专门计算图形的面积
# 其中嵌套函数，计算圆的面积，正方形的面积和长方形的面积
# 调用函数area(‘圆形’,圆半径) 返回圆的面积
# 调用函数area(‘正方形’,边长) 返回正方形的面积
# 调用函数area(‘长方形’,长，宽) 返回长方形的面积
# 代码模板 def area(): def 计算长方形面积(): pass
# def 计算正方形面积(): pass
# def 计算圆形面积(): pass
def count():
    def area(graph, *args):
        if graph == "圆形":
            return 3.14 * (args[0] ** 2)
        if graph == "正方形":
            return args[0] ** 2
        if graph == "长方形":
            return args[0] * args[1]
    return area


area = count()
print(area("圆形",2))
print(area("正方形",2))
print(area("长方形",2,3.1))