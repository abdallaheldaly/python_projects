class Solution(object):
    def reverse(self, x):
        
      # print(str(x)[ : : -1])

        if x >= 2 ** 31 - 1 or x <= -2 ** 31: return 0
        else:
            strg = str(x)
            if x >= 0 :
                revst = strg[ : : -1]
            else:
                temp = strg[1 : ] 
                temp2 = temp[ : : -1] 
                revst = "-" + temp2
            if int(revst) >= 2 ** 31 - 1 or int(revst) <= -2 ** 31: return 0
            else: return int(revst)
