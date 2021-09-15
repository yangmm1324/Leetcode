def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
    # bottom-up find the all the combinations, be cautious of the changing sets, use set
    allCombs = set(baseCosts)

    for top in toppingCosts:
        for cost in set(allCombs):
            allCombs.add(cost + top)
            allCombs.add(cost + top*2)


    dist = lambda x, y: abs(x-y)
    ans = float("inf")

    for cost in allCombs:
        if dist(cost, target) < dist(target, ans):
            ans = cost
        elif dist(cost, target) == dist(target, ans) and cost < ans:
            ans = cost

    return ans

# all possible combinations in the dfs call, TLE 
 def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
    dist = lambda x, y : abs(x-y)
    ans = [float("inf")]

    def dfs(topping, k):
        diff = dist(target, k)
        base = dist(target, ans[0])

        if diff < base or (diff == base and k <ans[0]):
            ans[0] = k

        for i, (price, val) in enumerate(topping):
            if val == 0: continue
            topping[i][1] -= 1
            dfs(topping, k+price)
            topping[i][1] += 1

    topping = [[price, 2] for price in toppingCosts]

    for base in baseCosts:
        dfs(topping, base)

    return ans[0]
