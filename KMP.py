
def KMP(pat,txt):

    i=0
    j=0
    n=len(txt)
    m=len(pat)

    lps=[0]*m
    
    calculatelps(pat,m,lps)

    while i<n:
        if pat[j]==txt[i]:
            i+=1
            j+=1

        if j==m:
            print(i-j)
            j=lps[j-1]

        elif i<n and pat[j]!=txt[i]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1

def calculatelps(pat,m,lps):

    len=0
    i=1

    while i<m:

        if pat[i]==pat[len]:
            len+=1
            lps[i]=len
            i+=1

        else:
            if len!=0:
                len=lps[len-1]
            else:
                lps[i]=0
                i+=1

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMP(pat, txt) 
