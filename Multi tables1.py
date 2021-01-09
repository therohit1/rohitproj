num=int(input("Enter your no:"))
rows=1
while rows<=10:# 1 to 10 rows
    column=1
    while column<=num:
        print(rows*column,end="\t")
        column+=1
    print("\t")
    rows+=1
