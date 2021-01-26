maleOrFemale = input("are you a male or female? (m/f)     ")

tWeight = float(input("what's your total weight?   "))
waist = float(input("what's your waist measurement?   "))
wrist = float(input("what's your wrist measurement? (press 0 if male)   "))
forearm = float(input("what's your forearm measurement? (press 0 if male)   "))
hip = float(input("what's your hip measurement? (press 0 if male)   "))

def calculateBFP(maleOrFemale, tWeight, waist, wrist, forearm, hip):
    if maleOrFemale.lower() == "f":
        formulaLean = (0.732 * tWeight) - (0.157 * waist) - (0.249 * hip) + (0.434 * forearm) + (wrist / 3.14) + 8.987
        leanBodyMass = "your lean body mass is " + str(formulaLean) + " lbs"
        fatBodyMass = tWeight - formulaLean
        fatBodyMassStatement = "your fat body mass is " + str(fatBodyMass) + " lbs"
        bodyFatPercent = (fatBodyMass / tWeight) * 100
        bodyFatPercentStatement = "your fat body percentage is " + str(bodyFatPercent)
        
        return (leanBodyMass, fatBodyMassStatement, bodyFatPercentStatement)

x = calculateBFP(maleOrFemale, tWeight, waist, wrist, forearm, hip)
print(x)

def calculateBFPforM(maleOrFemale, tWeight, waist):
    if maleOrFemale.lower() == "m":
        leanFormula = (1.082 * tWeight) - (4.15 * waist) + 94.42
        leanFormulaStatement = "your lean body mass is " + str(leanFormula) + " lbs"
        fatBody = tWeight - leanFormula
        fatBodyStatement = "your fat body mass is " + str(fatBody) + " lbs"
        percentage = (fatBody / tWeight) * 100
        percentageStatement = "your fat body percentage is " + str(percentage)
         
        return (leanFormulaStatement, fatBodyStatement, percentageStatement)

y = calculateBFPforM(maleOrFemale, tWeight, waist)
print(y)