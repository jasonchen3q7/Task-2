def make_next(p):
    nxt = [0] * len(p)
    j = 0

    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = nxt[j - 1]

        if p[i] == p[j]:
            j += 1

        nxt[i] = j

    return nxt


def kmp(s, p):
    if not p:
        return 0

    nxt = make_next(p)
    j = 0

    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = nxt[j - 1]

        if s[i] == p[j]:
            j += 1

        if j == len(p):
            return i - j + 1

    return -1



if __name__ == "__main__":
    s = "ababcabcacbab"
    p = "abcac"

    pos = kmp(s, p)

    print("text:", s)
    print("pattern:", p)
    print("pos:", pos)