import requests
import json
import discord

with open('./bot.conf', 'r') as file:
    conf = json.load(file)

baseUrl = 'http://api.betaseries.com/'
key = conf['BSkey']
sizeLimit = '1'
testId = '469'


def searchTitle(title):
    return getMovieInfo(getTitleID(title))


def getTitleID(title):
    request = baseUrl + 'search/all?' + 'key=' + key + '&query=' + title + '&limit=' + sizeLimit
    result = requests.get(request).json()
    titleId = result['movies'][0]['id']
    print(request)
    print(titleId)
    return titleId


# affiche les infos du film selectionné par ID
def getMovieInfo(movieID):
    request = baseUrl + 'movies/movie?' + 'key=' + key + '&id=' + str(movieID)
    result = requests.get(request).json()
    movieTitle = result['movie']['title']
    print(request)
    print(movieTitle)

    embed = discord.Embed(title=movieTitle)
    embed.add_field(name='titre original :', value=result['movie']['original_title'])
    embed.set_image(url=result['movie']['poster'])
    return embed


# affiche les infos de la série sélectionnée par ID
def searchShows():
    return


# affiche les suggestions si la recherche renvois plusieurs résultats
def showSuggestion():
    return


# searchTitle('terminator')
result = requests.get("http://api.betaseries.com/search/all?key=16017317979f&query='terminator 2'").json()
print(result['movies'])
if len(result['movies']) > 1:
    print('more than one')