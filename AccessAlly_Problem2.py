#time complexity: constant time gibven the input is always the same, otherwise it is n where n is the size of the input array


def main(unitBloodArray, patientCountArray, bloodTypeRelation):
    total = 0
    index = 0
    for bloodType in bloodTypeRelation:
        #take all from the same blood type before checking others
        if unitBloodArray[index] >= patientCountArray[index]:
            total += patientCountArray[index]
            unitBloodArray[index] -= patientCountArray[index]
            patientCountArray[index] = 0
        else:
            total += unitBloodArray[index]
            patientCountArray[index] -= unitBloodArray[index]
            unitBloodArray[index] = 0

        #if still patients left for blood type, check the relationship for more
        if patientCountArray[index] != 0:
            checkRest = bloodTypeRelation[bloodType]
            length = len(checkRest)
            while length > 0:
                length -= 1
                maximumBloodVal = -1
                maximumBloodValIndex = -1
                for i in checkRest:
                    if unitBloodArray[i] >= maximumBloodVal:
                        maximumBloodVal = unitBloodArray[i]
                        maximumBloodValIndex = i
                if unitBloodArray[maximumBloodValIndex] >= patientCountArray[index]:
                    total += patientCountArray[index]
                    unitBloodArray[maximumBloodValIndex] -= patientCountArray[index]
                    patientCountArray[index] = 0
                    break
                else:
                    total += unitBloodArray[maximumBloodValIndex]
                    patientCountArray[index] -= unitBloodArray[maximumBloodValIndex]
                    unitBloodArray[maximumBloodValIndex] = 0

        index += 1
    return total



failedTry = True

while failedTry:
    print("Please specify the input file name to test (must be located in same location as this file): ")
    inputFileName = str(input())
    try:
        f = open(inputFileName, "r")
        failedTry = False
    except FileNotFoundError:
        print('File was not found, try again')
        pass


unitBloodValues = f.readline()
patientCountValues = f.readline()
unitBloodArrayString = unitBloodValues.split()
patientCountArrayString = patientCountValues.split()
f.close()
unitBloodArray = []
patientCountArray = []

for i in range(len(unitBloodArrayString)):
    if i == 3:
        unitBloodArray.append(int(unitBloodArrayString[i+1]))
        patientCountArray.append(int(patientCountArrayString[i+1]))
    elif i == 4:
        unitBloodArray.append(int(unitBloodArrayString[i - 1]))
        patientCountArray.append(int(patientCountArrayString[i - 1]))
    else:
        unitBloodArray.append(int(unitBloodArrayString[i]))
        patientCountArray.append((int(patientCountArrayString[i])))



#relationship between the blood type and what it can receive excluding the same type
bloodTypeRelation = {
    'O-': [],
    'O+': [0],
    'A-': [0],
    'B-': [0],
    'A+': [0,1,2],
    'B+': [0,1,4],
    'AB-': [0,2,4],
    'AB+': [0,1,2,3,4,5,6]
}

#problem 2, link: https://accessally.com/careers/coding-assessment/
print(main(unitBloodArray, patientCountArray, bloodTypeRelation))

