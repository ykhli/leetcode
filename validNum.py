class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        numCt = False
        spCt = 0
        ct = 0
        dotCt = 0
        eCt = 0
        # eof character
        s += "@"
        ps = ["."," "]
        nums = "0123456789"
        for i in s:
            if (ct == 0 and i == " "):
                continue

            if i == "@":
                if numCt == False:
                    return False
                return True

            if i == "e":
                if numCt == False or prev=="0" or (s[ct+1] not in nums):
                    return False
                eCt += 1
                if eCt > 1:
                    return False

            if i.isalpha() and i != "e":
                return False

            if i == ".":
                dotCt += 1
                if dotCt > 1 or ((s[ct+1] not in nums) and (s[ct+1] != "@") and (s[ct+1] != " ")):
                    return False

            if i in nums and numCt == False:
                numCt = True
            
            if i == " ":
                if ct > 0:
                    if prev in nums and s[ct+1] in nums:
                        return False
                    if prev not in nums and s[ct+1] in nums:
                        return False

                if s[ct+1] != " " and s[ct+1] != "@" and s[ct+1] not in nums:
                    return False
            prev = i

if __name__ == "__main__":
    x = Solution()
    print x.isNumber(" .9")
