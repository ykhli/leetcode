# Note: This version is corrected but takes a long time
# see wildcard_matching_imp.py

def isMatch(s,p):
    if len(s) != len(p):
        if p.strip('*').strip('?') == '':
            return True
        # length not the same, no wild card -> false
        if '*' not in p:
            return False
        else:
            return findWildPattern(s,p)
    else:
        # length the same
        if '*' not in p and '?' not in p:
            # when there is no wildcards, two strings are the same
            if s == p:
                return True
            else:
                return False
        else:
            # wildcards
            pos = []
            np = list(p)
            ns = list(s)
            for i in range(0,len(p)):
                if p[i] == '?' or p[i] == '*':
                    np[i] = s[i]
            if np == ns:
                return True
            else:
                return False


def findWildPattern(s, p):
    patterns = p.split('*')
    index = 0
    while len(patterns) > 0:
        p = patterns.pop(0)
        if len(s) == 0:
            if len(p) == 0:
                continue
            else:
                return False

        if p in s:
            # not efficient here. Takes n^2 worst case
            index = s.index(p)
            # found p in string
            s = s[index+1:]
            # cut out the found part, keep looking
        else:
            # can't find p in string
            return False
    return True



print isMatch('','*')
