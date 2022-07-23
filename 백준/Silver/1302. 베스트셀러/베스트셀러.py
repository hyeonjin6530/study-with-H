n = int(input())
dic={}
for i in range(n):
    book=input()
    if book in dic:
        dic[book] += 1
    else:
        dic[book] = 1
best= max(dic.values())
best_book_list=[]
for j in dic:
    if dic[j] == best:
        best_book_list.append(j)
best_book_list.sort()
print(best_book_list[0])