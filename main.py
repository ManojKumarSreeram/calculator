from add import sum
from sub import min
from mul import mul
from div import div

a=int(input("Enter a value"))
b=int(input("Enter b value"))

sum_value=sum(a,b)
min_value=min(a,b)
mul_value=mul(a,b)
div_value=div(a,b)
print(sum_value,"------",min_value,"------",mul_value,"--------",div_value)
