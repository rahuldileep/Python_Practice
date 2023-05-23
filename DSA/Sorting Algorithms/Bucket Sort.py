n=int(input().strip())
bucket={}
for _ in range(n):
    number=input().strip()
    length=len(number)
    if length not in bucket:
        bucket[length]=[]
    bucket[length].append(number)
print(bucket)
print(sorted(bucket))
for key in sorted(bucket):
    for value in sorted(bucket[key]):
        print(value)
