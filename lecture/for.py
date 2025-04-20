lst = ["qwe", "asd", "zxc"]

lst2 = [565, 232, 767]

for i, string in enumerate(lst):
    print(i, string)



for i, tpl in enumerate(zip(lst, lst2), start=1):
    # print(trgt) # (1, ("qwe", 565))
    
    t_str, t_int = tpl
    print(i, t_str, t_int)
