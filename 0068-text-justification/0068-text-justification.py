class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        l = 0
        cnt = 0
        noWords = 0
        r = 0
        while r < len(words):
            if cnt + len(words[r]) < maxWidth:
                cnt += (len(words[r]) + 1)
                r += 1
                noWords += 1
            elif cnt + len(words[r]) == maxWidth:
                cnt += (len(words[r]) + 1)
                r += 1
                noWords += 1
                
                cnt -= noWords
                space = maxWidth - cnt
                noWords -= 1
                
                if noWords == 0:
                    string = words[l] + (" " * (maxWidth - len(words[l] )))
                    ans.append(string)
                elif (space) % noWords == 0:
                    need = space // noWords
                    string = ""
                    for i in range(l,r - 1):
                        string += words[i] + (" "* need)
                    string += words[r - 1]
                    ans.append(string)
                else:
                    rem = (space) % noWords
                    need = space // noWords
                    string = ""
                    for i in range(l,r - 1):
                        if rem:
                            string += words[i] + (" "* (need + 1))
                            rem -= 1
                        else:
                            string += words[i] + (" "* need)
                    string += words[r - 1]
                    ans.append(string)
                cnt = 0
                l = r
                noWords = 0
            else:
                cnt -= noWords
                space = maxWidth - cnt
                noWords -= 1
                
                if noWords == 0:
                    string = words[l] + (" " * (maxWidth - len(words[l] )))
                    ans.append(string)
                elif (space) % noWords == 0:
                    need = space // noWords
                    string = ""
                    for i in range(l,r - 1):
                        string += words[i] + (" "* need)
                    string += words[r - 1]
                    ans.append(string)
                else:
                    rem = (space) % noWords
                    need = space // noWords
                    string = ""
                    for i in range(l,r - 1):
                        if rem:
                            string += words[i] + (" "* (need + 1))
                            rem -= 1
                        else:
                            string += words[i] + (" "* need)
                    string += words[r - 1]
                    ans.append(string)
                cnt = 0
                l = r
                noWords = 0
                
        if noWords > 0:
            
            string = ""
            for i in range(l,r - 1):
                string += words[i] + (" ")
            string += words[r - 1]
            new = string + " " * (maxWidth  - len(string))
            ans.append(new)
        else:
        
            string = ans.pop()
            new = string.split(" ")
            string = ""
            for i in range(len(new) - 1):
                string += new[i] + (" ")
            string += new[-1]
            new = string + " " * (maxWidth  - len(string))
            ans.append(new)
            
        return ans