# 作者：宁方笑
# 开发时间：2021/5/5 14:06
# def numWaterBottles(numBottles, numExchange):
#     count=0
#     count+=numBottles
#     empty_bottle=0
#     empty_bottle+=numBottles
#     tmp=0
#     while(empty_bottle>=numExchange):
#         tmp=empty_bottle//numExchange
#         empty_bottle=empty_bottle-tmp*numExchange
#         count+=tmp
#         empty_bottle+=tmp
#     return count

def numWaterBottles(a, b):
     count=0
     count = a
     while a//b>=0:

         count+=(a//b)

         a=a//b+a%b
         if a<b:
             break

     return count


numBottles = 2
numExchange = 3
print(numWaterBottles(numBottles,numExchange))