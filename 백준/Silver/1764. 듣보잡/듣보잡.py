n, m = map(int, input().split())
no_listen=set()
no_see=set()
for i in range(n):
    a=input()
    no_listen.add(a)
for i in range(m):
    b=input()
    no_see.add(b)
no_listen_see=(no_listen&no_see)
no_listen_see=sorted(list(no_listen&no_see))
print(len(no_listen_see))
for i in no_listen_see:
    print(i)
