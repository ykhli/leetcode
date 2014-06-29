def isMatch(s, p):
    s_cur = 0;
    p_cur= 0;
    match = 0;
    star = -1;
    while s_cur<len(s):
        # If match found
        if p_cur< len(p) and (s[s_cur]==p[p_cur] or p[p_cur]=='?'):
            s_cur += 1
            p_cur += 1
        # * found
        elif p_cur<len(p) and p[p_cur]=='*':
            match = s_cur
            star = p_cur
            p_cur += 1
        # Match not found, but there is a star before 
        elif (star != -1):
            p_cur = star + 1
            match += 1
            s_cur = match
        else:
            return False

    # In case there are more letters after going through s
    while p_cur<len(p) and p[p_cur]=='*':
        p_cur = p_cur+1

    if p_cur==len(p):
        return True
    else:
        return False

print isMatch('abcdefgh','a*e*h')
