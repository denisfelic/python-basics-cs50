#import 
from functions import square
#import functions 

num = int(input("Type a number: "))
max_range = int(input("Type a range: "))
max_range+= 1

for n in range(max_range):
    print(f"{num}^{n} = {square(num,n)}")
    # print(f"{num}^{n} = {functions.square(num,n)}")
