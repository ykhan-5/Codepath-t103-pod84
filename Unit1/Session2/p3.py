#U --> Understanding
  
  #map needs to contain subtraction cases as well (ex. 4 , 9, 40, 90, 400, 900)      
#M --> Match #use a map
#P --> Pseudo Code
#I --> Implementation map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}


#R 
#E

class Solution:
    
  def intToRoman(self, num: int) -> str:
      map = {1:"I", 4: "IV", 5: "V", 9: "IX", 10: "X", 
             40: "XL", 50: "L", 90: "XC",100: "C", 400: "CD", 500: "D", 900:"CM", 1000: "M"}
      res = ""
      
      #XLIX
      #[9, 4, 7, 3]
      # 9*(i+1) 
      #keep going Dosbol
      
      for i in [1000,900,500,400,100,90,50,40,10,5,4,1]:
         print("hello")
        
      return res
      

num = 3749
solution = Solution()
print(solution.longest(num))

    