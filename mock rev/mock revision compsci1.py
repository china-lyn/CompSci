def mean(nums):
    total = 0
    for n in range(0, len(nums)):
        total += nums[n]
        #print(nums[n])
    mean = total / len(nums)
    return round(mean, 2)

def median(nums):
    nums.sort()
    if len(nums) % 2 != 0: #odd
        val = len(nums) // 2
        median = nums[val]
    else: # even
        val = (len(nums) // 2)
        median = ((nums[val] + nums[val + 1]) / 2) - 1
    return(median)

def mode(nums):
    count = {}
    for n in nums:
        if not count.get(n):
            count[n] = 1
        else:
            count[n] += 1
    
    for num, c in count.items():
        if c == c:
            mode = 'There is no mode'
        else:
            mode = max(count, key=count.get)

    return mode
        
def mini(nums):
    m = 0
    for n in nums:
        if m >= n:
            m = n
            return m
        else:
            return n
                
def maxi(nums):
    m = 0
    for n in nums:
        if n > m:
            m = n
    return m

def ranges(nums):
    high = max(nums)
    low = min(nums)
    finalrange = high - low
    return finalrange

def frequency(nums):
    print('''
    ===================
         FREQUENCY
    ===================
    ''')
    freq = {}
    for n in nums:
        if not freq.get(n):
            freq[n] = 1
        else:
            freq[n] += 1
    for num, count in freq.items():
        print(f'{num} --> {count} time(s)')
    return '\n'

def placeVal(nums, place):
    UNITS = 0
    TENS = 1
    HUNDREDS = 2
    
    units = []
    tens = []
    huns = []
    
    if place[0] == 'u':
        number = place[-1]
        for n in nums:
            new = str(n)
            try:
                if new[UNITS] == number:
                    units.append(n)
            except IndexError:
                continue
        return units
    if place[0] == 't':
        number = place[-1]
        for n in nums:
            new = str(n)
            try:
                if new[TENS] == number:
                    tens.append(n)
            except IndexError:
                continue
        return tens
    if place[0] == 'h':
        number = place[-1]
        for n in nums:
            new = str(n)
            try:
                if new[HUNDREDS] == number:
                    huns.append(n)
            except IndexError:
                continue
        return huns
    
    
nums = []
while True:
    num = input('Enter a number between 0-999 inclusive, and a letter (a-z) to finish: ')
    if num.isalpha() == True:
         break
    nums.append(int(num))

print(f'Mean: {mean(nums)}')
print(f'Median: {median(nums)}')
print(f'Mode: {mode(nums)}')
print(f'Min: {mini(nums)}')
print(f'Max: {maxi(nums)}')
print(f'Range: {ranges(nums)}')
print(frequency(nums))

question = input('Would you like to print numbers with a particular place value? (y/n): ')
if question.lower() == 'y':
    placeval = input('''Enter a place value to filter the inputs (u, t, h):
    -------------------------------------------------
    Example: Enter u8 to list all nums with 8 in units column
             Enter h5 to list all nums with 5 in hundreds column
    ''')
    print(f'{placeval} = {placeVal(nums, placeval)}')
