f = open('Exercise.csv', 'r')
header = f.readline()
 
lineslist = []
for line in f:
    lineslist.append(line.strip().split(','))
f.close()
 
session = {}
averages = {}
for li in lineslist:
    try: 
        dur, cal = int(li[0]), float(li[-1]) # changing duration and calories to int and float
    except ValueError:
        continue
    if not session.get(dur): # if not in dictionary add to it as a key 
        session[dur] = [cal] # add list as value
    else:
        session[dur].append(cal) # if key already in list append value to list of values

# top and lowest 20 sessions for duration of 45 and 60:
session[60].sort() # sorting these lists to find the top and lowest values
session[45].sort()
tav60 = round(sum(session[60][-20:]) / 20, 2)
tav45 = round(sum(session[45][-20:]) / 20, 2)
lav60 = sum(session[60][:20]) / 20
lav45 = round(sum(session[45][:20]) / 20, 2)

# comparing these values and the value of all other averages:
averages['tav60'] = tav60
averages['tav45'] = tav45 # making dictionary with all top and lowest averages
averages['lav60'] = lav60
averages['lav45'] = lav45

total = {} # dictionary with the averages and their durations

print('Duration(m)\tAverage Calories') # print table of answers
for k in sorted(session):
    avg = round(sum(session[k]) / len(session[k]), 2)
    total[k] = avg # dictionary of all averages and their durations
    print(f'{int(k)}\t\t{avg}') # average of calories for each duration type
    

print('\nDuration(m)\tAverage cals burned in TOP 20 sessions')
print(f'60\t\t{tav60}\n45\t\t{tav45}')
print('\nDuration(m)\tAverage cals burned in LOWEST 20 sessions')
print(f'60\t\t{lav60}\n45\t\t{lav45}')

print('\nDuration:\t60m top 20\t45m top 20\t60m lowest 20\t45m lowest 20') # header
print('Averages: ', end='\t') # making a table to display the differences
for v in averages:
    print(averages[v], end='\t\t')
print()
# print('\tDifference:')

# getting percentage difference of all values and the top and lowest values for 45 and 60
for duration in total:
    t = total[duration] # value
    print(duration, end='\t') # printing the durations(keys)
    print(t, end='\t') # printing the averages (values)
    for avg in averages:
        if averages[avg] > t:
            diff = (averages[avg] - t) / ((averages[avg] + t) / 2) * 100
            print(round(diff, 3), end='\t\t') # percentage difference
        else:
            diff = (t - averages[avg]) / ((averages[avg] + t) / 2) * 100
            print(round(diff, 3), end='\t\t')
    print()

while True: 
    duration = int(input('Enter the duration of you session in minutes: ')) # asking for user data
    calsb = int(input('Enter the number of calories burned: '))
    if total.get(duration): # if it is a valid session type (from dictionary)
        averagecals = total[duration]
        if averagecals > calsb:
            off = averagecals - calsb # getting difference
            print(f'You are {round(off,4)} calories away from the average number of calories burned in {duration} mins')
        else:
            off = calsb - averagecals
            print(f'You are {round(off,4)} calories above the average number of calories burned in {duration} mins!!')
        break
    if not total.get(duration):
        print('That is not a valid session duration!') # allowence for error
        continue
    
    
