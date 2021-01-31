class Tree:
    def __init__(self, h):
        self.h = h
        self.left = None
        self.right = None
        self.number = 2 ** h - 1

        self.right = Node(self.number - 1, h - 1, self)
        self.left = Node((self.number - 1) / 2, h - 1, self)

    def find_parents(self, p):
        res = []
        for child_number in p:
            if self.number == child_number:
                res.append(-1)
            else:
                if self.left.find_number(child_number):
                    res.append(self.left.find_number(child_number))

                if self.right.find_number(child_number):
                    res.append(self.right.find_number(child_number))
        return res


class Node:
    def __init__(self, number, h, parent):
        self.right = None
        self.left = None
        self.h = h
        self.parent = parent
        self.number = int(number)

        if self.h > 1 and not self.right:
            self.right = Node(number - 1, self.h - 1, self)
        if not self.left and self.h > 1:
            self.left = Node(number - 2 ** (self.h - 1), self.h - 1, self)

    def find_number(self, n):
        if self.number == n:
            return self.parent.number
        if self.right and self.left.find_number(n):
            return self.left.find_number(n)
        if self.right and self.right.find_number(n):
            return self.right.find_number(n)


def solution(h, q):
    return Tree(h).find_parents(q)
