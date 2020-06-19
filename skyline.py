import random as rand
import numpy as np
import matplotlib.pyplot as plot


def s(r):
    return r[0]


def e(r):
    return r[2]


def h(r):
    return r[1]


def null(r):
    return r[2] <= r[0]


def generateRandomBuildings(n, h, w, xmin, xmax):
    buildings = []
    for i in range(0, n):
        hh = rand.randint(0, h)
        ww = rand.randint(1, w)
        ss = rand.randint(xmin, xmax-ww)
        if hh > 0:
            buildings.append((ss, hh, ss+ww))
    return buildings


def skylineFromBuildings(buildings):
    if len(buildings) == 0:
        return Skyline([])
    elif len(buildings) == 1:
        return Skyline(buildings)
    else:
        mid = len(buildings)//2
        return skylineFromBuildings(buildings[:mid]) + skylineFromBuildings(buildings[mid:])


class Skyline:

    def __init__(self, ranges):  # ranges are correct (not intersects)
        self.ranges = ranges

    def save(self, name):
        if not self.ranges:
            return (0, 0)
        else:
            ss = s(self.ranges[0])
            ee = e(self.ranges[-1])
            values = np.zeros(ee-ss)
            maxh, area = 0, 0
            for r in self.ranges:
                if h(r) > maxh:
                    maxh = h(r)
                area = area + (h(r)*(e(r)-s(r)))
                for i in range(s(r)-ss, e(r)-ss):
                    values[i] = h(r)
            plot.bar(range(ss, ee), values, width=1.0, align='edge')
            plot.title("Skyline")
            plot.savefig(name, bbox_inches='tight')
            plot.close()
            return (maxh, area)

    def __str__(self):
        string = ""
        for r in self.ranges:
            string = string + "|" + str(s(r)) + "\t*" + str(h(r)) + "*\t" + str(e(r)) + "|"
        return string

    def __add__(self, other):
        if isinstance(other, self.__class__):
            r1 = self.ranges
            r2 = other.ranges
            nr = []

            def addRange(r):
                if not nr:
                    nr.append(r)
                else:
                    if s(r) == e(nr[-1]) and h(r) == h(nr[-1]):
                        nr[-1] = (s(nr[-1]), h(r), e(r))  # stored = start stored - end new
                    else:
                        nr.append(r)

            c1, c2 = null, null
            try:
                i1, i2 = iter(r1), iter(r2)
                c1, c2 = next(i1), next(i2)
                ss, hh, ee = 0, 0, 0
                while True:
                    if s(c1) < s(c2):
                        ss = s(c1)
                        hh = h(c1)
                        if e(c1) <= s(c2):
                            ee = e(c1)
                            addRange((ss, hh, ee))
                            c1 = null
                            c1 = next(i1)
                        else:
                            ee = s(c2)
                            addRange((ss, hh, ee))
                            c1 = (s(c2), h(c1), e(c1))  # c1 = start c2 - end c1
                    elif s(c1) > s(c2):
                        ss = s(c2)
                        hh = h(c2)
                        if e(c2) <= s(c1):
                            ee = e(c2)
                            addRange((ss, hh, ee))
                            c2 = null
                            c2 = next(i2)
                        else:
                            ee = s(c1)
                            addRange((ss, hh, ee))
                            c2 = (s(c1), h(c2), e(c2))  # c2 = start c1 - end c2
                    else:
                        ss = s(c1)
                        hh = max(h(c1), h(c2))
                        if e(c1) < e(c2):
                            ee = e(c1)
                            addRange((ss, hh, ee))
                            c2 = (e(c1), h(c2), e(c2))  # c2 = end c1 - end c2
                            c1 = null
                            c1 = next(i1)
                        elif e(c1) > e(c2):
                            ee = e(c2)
                            addRange((ss, hh, ee))
                            c1 = (e(c2), h(c1), e(c1))  # c1 = end c2 - end c1
                            c2 = null
                            c2 = next(i2)
                        else:
                            ee = e(c1)
                            addRange((ss, hh, ee))
                            c1, c2 = null, null
                            c1 = next(i1)
                            c2 = next(i2)
            except StopIteration:
                if c1 != null:
                    addRange(c1)
                if c2 != null:
                    addRange(c2)
                nr.extend(i1)
                nr.extend(i2)
                return Skyline(nr)
        elif isinstance(other, int):
            nr = [(s(r)+other, h(r), e(r)+other) for r in self.ranges]
            return Skyline(nr)
        else:
            raise NotImplemented

    def __sub__(self, other):
        if isinstance(other, int):
            nr = [(s(r)-other, h(r), e(r)-other) for r in self.ranges]
            return Skyline(nr)
        else:
            raise NotImplemented

    def __neg__(self):
        if not self.ranges:
            return Skyline([])
        else:
            rs = self.ranges.copy()
            ini = s(rs[0])
            fin = e(rs[-1])
            rs.reverse()
            nr = []
            for r in rs:
                ss = ini+(fin-e(r))
                ee = ss+(e(r)-s(r))
                nr.append((ss, h(r), ee))
            return Skyline(nr)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            r1 = self.ranges
            r2 = other.ranges
            nr = []

            def addRange(r):
                if not nr:
                    nr.append(r)
                else:
                    if s(r) == e(nr[-1]) and h(r) == h(nr[-1]):
                        nr[-1] = (s(nr[-1]), h(r), e(r))  # stored = start stored - end new
                    else:
                        nr.append(r)

            try:
                i1, i2 = iter(r1), iter(r2)
                c1, c2 = next(i1), next(i2)
                ss, hh, ee = 0, 0, 0
                while True:
                    if s(c1) < s(c2):
                        if e(c1) <= s(c2):
                            c1 = next(i1)
                        else:
                            c1 = (s(c2), h(c1), e(c1))  # c1 = start c2 - end c1
                    elif s(c1) > s(c2):
                        if e(c2) <= s(c1):
                            c2 = next(i2)
                        else:
                            c2 = (s(c1), h(c2), e(c2))  # c2 = start c1 - end c2
                    else:
                        ss = s(c1)
                        hh = min(h(c1), h(c2))
                        if e(c1) < e(c2):
                            ee = e(c1)
                            addRange((ss, hh, ee))
                            c2 = (e(c1), h(c2), e(c2))  # c2 = end c1 - end c2
                            c1 = next(i1)
                        elif e(c1) > e(c2):
                            ee = e(c2)
                            addRange((ss, hh, ee))
                            c1 = (e(c2), h(c1), e(c1))  # c1 = end c2 - end c1
                            c2 = next(i2)
                        else:
                            ee = e(c1)
                            addRange((ss, hh, ee))
                            c1 = next(i1)
                            c2 = next(i2)
            except StopIteration:
                return Skyline(nr)
        elif isinstance(other, int):
            if not self.ranges:
                return Skyline([])
            else:
                rs = self.ranges
                nr = self.ranges.copy()
                total = e(rs[-1]) - s(rs[0])
                for i in range(1, other):
                    for r in rs:
                        if r == rs[0] and h(nr[-1]) == h(r):
                            nr[-1] = (s(nr[-1]), h(r), i*total+e(r))
                        else:
                            nr.append((i*total+s(r), h(r), i*total+e(r)))
                return Skyline(nr)
        else:
            raise NotImplemented
