
import math

def mathTest():

    # 向大取整：math.ceil()
    print(f"ceil(-0.5) 向大取整: {math.ceil(-0.5)}") #0
    print(f"ceil(0.5) 向大取整: {math.ceil(0.5)}")   #1

    # 向小取整：math.floor() 以及 //

    print(f"floor(-0.3) 向小取整: {math.floor(-0.3)}") #-1
    print(f"floor(0.5) 向小取整: {math.floor(0.5)}")   #0

    print(f"-3 // 10 向小取整: {math.floor(-3 // 10)}") #-1
    print(f"5 // 10 向小取整: {math.floor(5 // 10)}")   #0


    # 向0取整 : int()

    print(f"int(-0.3) 向0取整: {int(-0.3)}") #0
    print(f"int(0.3) 向0取整: {int(0.3)}")   #0


    # 偶數捨入法 : round() 是取最接近的數值, 可是當往前與往後的數值等距時, 會取偶數, 它的用意是要解決多筆數字以四捨五入後加總平均會偏高的問題, 讓遇到中間值時捨位與進位的機率相等, 而非一律進位。

    print(f"round(-1.3) 偶數捨入法: {round(-1.3)}")
    print(f"round(1.3) 偶數捨入法: {round(1.3)}")
    print(f"round(-1.6) 偶數捨入法: {round(-1.6)}")
    print(f"round(1.6) 偶數捨入法: {round(1.6)}")
    print(f"round(-2.5) 偶數捨入法: {round(-2.5)}")
    print(f"round(-1.5) 偶數捨入法: {round(-1.5)}")
    print(f"round(2.5) 偶數捨入法: {round(2.5)}")
    print(f"round(1.5) 偶數捨入法: {round(1.5)}")


if __name__ == '__main__':
    mathTest()