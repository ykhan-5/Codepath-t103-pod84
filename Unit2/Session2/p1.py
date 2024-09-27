#U --> Should we use Dictionary? 
#


#M --> Prefix Sum, ORD() to get ASCII value
#P

# fix the shift amount
#iterate through letters, apply shift, check not going past z, if does, reset to a

#I
#R
#E         

#[3, 5, 9]
class Solution:
    
    def shiftLetters(self, s, shifts):
        #print(ord('a') - 97) # 0(a) -> 25(z) if modulo 26 == 0, reset to 0
        s = list(s)
        for i in range(len(shifts)-2,-1,-1):
            shifts[i]+=shifts[i+1] 

        for i in range(len(s)): # s = "abc           
            s[i] = chr(((ord(s[i])-97 + shifts[i]) % 26) + 97)
            
        return "".join(s)
        

# EXAMPLE  -->"gfd"


s = "abc"
shifts = [3, 5, 9]    #--> Output: "rpl"
solution = Solution()
print(solution.shiftLetters(s, shifts))



# explanation: We start with "abc".
# After shifting the first 1 letters of s by 3, we have "dbc".
# After shifting the first 2 letters of s by 5, we have "igc".
# After shifting the first 3 letters of s by 9, we have "rpl", the answer.