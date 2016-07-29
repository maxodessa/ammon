def calc_t(result, scale_arg):
    t = 50 + (10 * (result - scale_arg[0])) / scale_arg[1]
    return t

agr1 = [9.12, 2.22]
agr2 = [6.35, 3.00]
agr3 = [4.56, 2.06]
fea1 = [7.78, 2.21]
fea2 = [3.42, 1.98]
fea3 = [4.53, 2.20]
oli1 = [7.78, 2.23]
oli2 = [3.40, 1.65]
oli3 = [7.90, 2.23]
ili1 = [9.14, 2.06]
ili2 = [3.97, 1.65]
ili3 = [6.78, 2.49]
nar1 = [8.91, 2.08]
nar2 = [4.17, 1.98]
nar3 = [2.56, 2.03]
sex1 = [9.26, 2.86]
sex2 = [5.00, 2.58]
sex3 = [2.79, 2.14]
table = [agr1, agr2, agr3, fea1, fea2, fea3, oli1, oli2, oli3, ili1, ili2, ili3, nar1, nar2, nar3, sex1, sex2, sex3]
res = [7, 11, 7, 6, 7, 6, 6, 9, 6, 10, 3, 9, 4, 6, 7, 5, 6, 5]
# print (table)
i = 1
for item in table:
    # print item
    # result = float(raw_input("Enter result of test:"))
    print ("T", i, "=", round(calc_t(res[i-1], item), 2))
    # print (i, round(calc_T(res[i-1], item),2)
    i = i + 1