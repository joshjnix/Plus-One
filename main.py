class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        newlist = []
        for x in digits:
            string += str(x)
        newstring = int(string)
        newstring += 1
        newnewstring = str(newstring)
        for i in range(len(newnewstring)):
            newlist.append(newnewstring[i])
        for i in range(len(newlist)):
            newlist[i] = int(newlist[i])
        return newlist
