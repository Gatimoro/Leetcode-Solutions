class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        qus = set(wordlist)
        def transformed(word):
            return word.lower().replace('a','$').replace('e','$').replace('i','$').replace('o','$').replace('u','$')
        # tran = dict()
        caps = dict()
        coresps = dict()
        for word in reversed(wordlist):
            # tran[transformed(word)] = word
            caps[word.lower()] = word
            coresps[transformed(word)] = word
            # print(transformed(word), word.lower(), transformed(word).lower(), word)
        #return [word if transformed(word) not in coresps else coresps[transformed(word)] for word in queries]
        ans = []
        for word in queries:
            # print(transformed(word).lower())
            if word in qus:
                ans.append(word)
                continue
            capi = word.lower()
            if capi in caps:
                # print('capitalization')
                ans.append(caps[capi])
                continue
            tran = transformed(word)
            if tran in coresps:
                # print('both')
                ans.append(coresps[tran])
                continue
            # print('nothing')
            ans.append("")
        return ans
