from math import floor

# unequal(standard) variances formulas:
def sqrt_gen(sx,n,sy,m):
    return (sx**2/n + sy**2/m)**0.5
def degree(sx,n,sy,m):
    return floor((sx**2/n + sy**2/m)**2 / (sx**4/(n**2*(n-1)) + sy**4/(m**2*(m-1))))

def t_statistic_gen(xbar,ybar, d, sx,n,sy,m):
    return (xbar-ybar -d) / sqrt_gen(sx,n,sy,m)

# print(degree(0.38,22,0.47,22))
# print(degree(44.76,8,38.94,17))


# equal variances(pooled) formulas:
def common_variance_squared(sx,n,sy,m):
    return (sx**2*(n-1) + sy**2*(m-1)) / (n+m-2)

def sqrt_pool(n,m):
    return (1/n + 1/m) ** 0.5
def t_statistic_pool(xbar,ybar, d, sx,n,sy,m):
    return (xbar-ybar -d) / sqrt_pool(n,m)*common_variance_squared(sx,n,sy,m)**0.5

print(common_variance_squared(0.00128,13,0.00096,15))