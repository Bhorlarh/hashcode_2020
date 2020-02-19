inputFileName = "../e_also_big.in"


def main():

    # List of all lines of pizzas
    allPizzas = []
    result = []
    linesOfPizza = 0

    with open(inputFileName) as inputSet:
        currentPizzas = inputSet.readline()[:-1].split(" ")

        # create list of pizzas out of all lines
        while (currentPizzas[0]):
            linesOfPizza += 1
            allPizzas.append(currentPizzas)
            currentPizzas = inputSet.readline()[:-1].split(" ")


    maximumTotalPizzas = int(allPizzas[0][0])
    typesOfPizzas = int(allPizzas[0][1])

    # loop through all lines of pizzas from the last line
    for i in range(linesOfPizza - 1, 0, -1):
        currentLine = allPizzas[i]

        # check each pizza on line
        for j in range(len(currentLine) - 1, -1, -1):
            currentPizza = int(currentLine[j])

            # make sure result is less than total pizzas
            if (currentPizza + sum(result)) <= maximumTotalPizzas:
                result.insert(0, currentPizza)

#    print(f"Types of pizzas ordered: {len(result)}")
#    print(f"Max possible Score: {maximumTotalPizzas}")
#    print(f"Score gotten: {sum(result)}\n\n")
    createSubmission(result)

def createSubmission(answer):
    with open(f'./{inputFileName[2]}_submission.in', 'w') as outputFile:
        outputFile.write(f"{len(answer)} \n")
        for i in answer:
            outputFile.write(str(i) + " ")
main()
