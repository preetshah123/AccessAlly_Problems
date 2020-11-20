def getSQCount(index):
    #hard coded array of the arth sq totals within each hour... hard coded since this is known and is always constant
    #assuming the clock is a normal LED clock

    arrayOfArthSQInEachHour = [1, 5, 5, 4, 4, 3, 3, 2, 2, 1, 0, 1]
    total = 0

    #get total for all the hours that have passed since 12pm
    for i in range(index):
        total += arrayOfArthSQInEachHour[i]
    return total

def getSumOfSQInHour(hour, minutesLeft, smallestCommonDiff, largestCommonDiff):
    total = 0
    #this check will get the last digit of the hour hand if 11, or 12 since the common difference is added to the last digit
    if hour > 10:
        hour = hour - 10
    for i in range(smallestCommonDiff, largestCommonDiff +1):
        firstDigit = hour + i
        secondDigit = firstDigit + i
        minuteCount = (firstDigit*10) + secondDigit
        if minuteCount <= minutesLeft:
            total += 1
        else:
            break
    return total


def main(D):
    hour = D//60 #the numbers of hours past 12pm
    minutesLeft = D - (hour*60) #the number of minutes left in the hour

    if hour > 0:
        currentSumOfArthSQ = getSQCount(hour)
    else: #if 0, then no hour has passed since 12pm so the current sum is 0
        currentSumOfArthSQ = 0

    smallestCommonDiff = 0
    largestCommonDiff = 0

    #determine what the max and min difference can be used for this hour so the "end time" is still a valid time
    if hour < 10 and hour > 0:
        smallestCommonDiffSetup = (hour-0)//2
        smallestCommonDiff = 0-smallestCommonDiffSetup
        largestCommonDiff = 5 - hour
    else:
        if hour == 0 or hour == 12:
            smallestCommonDiff, largestCommonDiff = 1,1

    if hour != 10:
        sumOfArthSQInHour = getSumOfSQInHour(hour, minutesLeft, smallestCommonDiff, largestCommonDiff)
    else:
        sumOfArthSQInHour = 0

    return currentSumOfArthSQ + sumOfArthSQInHour



#pick a number for D between 0 and 10^9
#link to question1: https://accessally.com/careers/coding-assessment/
print('Input number of minutes past 12pm: ')
D = int(input())
additionalSum = 0
totalSumPossibleIn12Hrs = 31

if D >= 720:
    additionalSum = (D//720)*totalSumPossibleIn12Hrs #the total arth sq in 24 are known, so find out how many 12hours fit into minutes given and multiply by the known sum to get additional count
    D = D%720 #get the leftover minutes

#D must be less than or equal to 720 before entering here
print('the total number of arithmetic sequences are: ')
print(main(D) + additionalSum)
