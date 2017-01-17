def map(list, func):
   new_arr=[]
   for x in list:
       new_arr.append(func(x))
   return new_arr
print (map([1,2,3,4,5], lambda x: x*3))
