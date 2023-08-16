# 수식으로 풀기

a, b, c, d, e, f = map(int, input().split())

# ax + by = c
# dx + ey = f

# ax + b*(f-dx)/e = c
# ax + bf/e - bdx/e = c
# aex + bf - bdx = ec
# (ae-bd)x = ec-bf
# x = (ec-bf)/(ae-bd)

# a(f-ey)/d + by = c
# af/d - aey/d + by = c
# af - aey + bdy = cd
# (bd-ae)y = cd-af
# y = (cd-af)/(bd-ae)

print((e*c-b*f)//(a*e-b*d), (c*d-a*f)//(b*d-a*e))