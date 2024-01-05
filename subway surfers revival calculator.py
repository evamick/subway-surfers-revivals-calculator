#calculate how many revivals you get out of your keys in subway surfers
keys = int(input('how many keys do you have? '))
def revivals(k):
    sum = 0
    n = 0
    while sum + 2**n <= k:
        sum = 2**n + sum
        n += 1
    return n

print(f'you can revive {revivals(keys)} times\n{revivals(keys)+10} times with ads')