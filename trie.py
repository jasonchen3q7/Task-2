class Node:
    def __init__(self):
        self.nexts = {}   # 用来存子节点
        self.end = False  # 用来是不是一个单词结尾


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.nexts:
                cur.nexts[ch] = Node()
            cur = cur.nexts[ch]
        cur.end = True

    def find(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.nexts:
                return False
            cur = cur.nexts[ch]
        return cur.end

    def hasPrefix(self, pre):
        cur = self.root
        for ch in pre:
            if ch not in cur.nexts:
                return False
            cur = cur.nexts[ch]
        return True


if __name__ == "__main__":
    t = Trie()
    words = ["cat", "car", "dog", "door"]

    for w in words:
        t.add(w)

    print("find cat:", t.find("cat"))
    print("find cap:", t.find("cap"))
    print("prefix ca:", t.hasPrefix("ca"))
    print("prefix do:", t.hasPrefix("do"))