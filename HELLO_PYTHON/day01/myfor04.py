#enumerate 방법1
arr = ["홍길동", "전우치", "이순신"]
for idx,i in enumerate(arr):
    print(idx,i)

#방법2
cnt = 0
for i in arr:
    print(cnt,i)
    cnt+=1