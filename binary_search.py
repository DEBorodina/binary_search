class Search:
      @staticmethod
      def binary_search(arr, x):
        l = 0
        r = len(arr) 
        while l < r: 
               k = int((l + r) / 2)
               if x == arr[k]: 
                     return 1
               elif x < arr[k]: 
                     r = k 
               else: 
                     l = k + 1 
                     
        return 0
  
      @staticmethod
      def left(arr, x):
        l = 0
        r = len(arr) 
        while l < r: 
               k = int((l + r) / 2)
               if x <= arr[k]: 
                     r = k 
               else:
                     l = k + 1 
        return l 
      
      @staticmethod
      def right(arr, x):
        l = 0
        r = len(arr) 
        while l < r: 
               k = int((l + r) / 2)
               if x < arr[k]: 
                     r = k 
               else:
                     l = k + 1 
        return l 


n = int(input())

arr = input().split(" ")

k = int(input())

to_find = input().split(" ")

for i in range(0,n):
    arr[i]=int(arr[i])

for i in range(0,k):
    to_find[i]=int(to_find[i])
    
srch = Search()    
for el in to_find:
    print(srch.binary_search(arr, el), srch.left(arr,el), srch.right(arr,el))