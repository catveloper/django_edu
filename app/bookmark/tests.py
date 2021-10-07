import itertools
from pprint import pp
from typing import List, Set, Tuple, Any, Optional

from django.test import TestCase


# Create your tests here.
class Member:
    name: str
    grouped: Optional[List[Any]]

    def __init__(self, name):
        self.name = name
        self.grouped = [self]

    def __repr__(self):
        return self.name

members: List[Member] = [Member('동욱'), Member('보배'), Member('다혜'), Member('서현'), Member('세현'), Member('성민'),
                         Member('명성'), Member('길수'), Member('서연'), Member('예린'), Member('영현'), Member('재훈')]
groups = []
for member1 in members:
    for member2 in members:
        if member2 in member1.grouped:
            continue
        member1.grouped.append(member2)
        member2.grouped.append(member1)
        for member3 in members:
            if member3 in member1.grouped or member3 in member2.grouped:
                continue
            member1.grouped.append(member3)
            member3.grouped.append(member1)
            member2.grouped.append(member3)
            member3.grouped.append(member2)

            groups.append([member1, member2, member3])
pp(groups)