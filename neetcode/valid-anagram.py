class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fmap1 = self.fmap(s)
        fmap2 = self.fmap(t)

        return fmap1.items() == fmap2.items()

    def fmap(self,stri):
        fmap = dict()
        for ch in stri:
            if ch not in fmap:
                fmap[ch] = 0
            fmap[ch] +=1
        return fmap
