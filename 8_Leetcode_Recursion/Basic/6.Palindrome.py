

def rev(n):
    if n==0:
        return ''

    f=str(n%10)+rev(n//10)
    return f

n=515

if n==int(rev(n)):
    print(True)

