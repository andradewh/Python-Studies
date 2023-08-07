def solution (a: list):
    it = 0
    cost = 0
    for i in a:
        it += 1
        if len(i) == 1:
            item = int(i)
        else:
            item = len(i)
        if i == 1:
            cost = item
        if cost < item:
            cost = item
    return cost


print(solution(list('123123123132')))