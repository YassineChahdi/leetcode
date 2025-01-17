from typing import List

def numRescueBoats(people: List[int], limit: int) -> int:
    boats = 0
    people.sort(reverse=True)

    for person in people:
        boats += 1
        if person + people[-1] <= limit:
            people.pop()

    return boats
