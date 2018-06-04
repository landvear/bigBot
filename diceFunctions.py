import random
import re
import discord
regexRollnum = '(\d+[dD]\d+)'
testCase = '(4d6 + 4d5) + 3'


# lance un dé pour un couple nombre de lancé et taille du dé
def rollDice(diceToRoll):
    # identification du nombre de lancés puis de la taille du dé
    rollNumber = re.search("^(\d+)", diceToRoll).group()
    diceRange = re.search("(\d+)$", diceToRoll).group()

    # calcul du lancé de dé
    if rollNumber == 0 and diceRange == 0:
        return '0'
    result = 0
    for i in range(0, int(rollNumber)):
        temp = random.randint(1, int(diceRange))
        result = result + temp
    return str(result)


# enlève les esapces, lance les dés, retourne la valeur totale
def dice(operation):
    operationArray = []
    resultArray = []
    # enlève les espaces
    operation = str(operation.replace(" ", ""))
    rollParameters = re.findall(regexRollnum, operation)

    # lance les dés, stock les opérations et leurs résultats dans un tableau
    operation = buildDiceArrays(operation, operationArray, resultArray, rollParameters)

    # Construit un embed à partir des tableaux d'opération et de résultat
    try:
        embed = buildEmbed(operation, operationArray, resultArray)
        return embed
    except:
        return 'Commande incorecte'


def buildEmbed(operation, operationArray, resultArray):
    embed = discord.Embed(title='Dice roll result')
    for index in range(len(operationArray)):
        embed.add_field(name=operationArray[index], value=resultArray[index], inline=True)
    embed.add_field(name='Total', value=str(eval(operation)), inline=False)
    return embed


def buildDiceArrays(operation, operationArray, resultArray, rollParameters):
    for diceToRoll in rollParameters:
        operationArray.append(diceToRoll)
        resultDiceRoll = rollDice(str(diceToRoll))
        operation = operation.replace(diceToRoll, resultDiceRoll, 1)
        resultArray.append(resultDiceRoll)
    print('operation ' + operation)
    return operation
