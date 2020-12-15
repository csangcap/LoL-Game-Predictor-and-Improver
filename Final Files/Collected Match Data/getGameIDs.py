import requests
import csv

region = "na1"
username = "Doublelift"
apiKey = "RGAPI-0033f1ea-daa5-4542-a8e8-b89f4bb8c244"

URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + username + "?api_key=" + apiKey

count = 0

accountID = "jrQCf2rSwHx8bFcImZremtX_-dOInnCuKb47o9t-DDtSbQ"


with open('gameIDs.csv', mode='a', newline='') as gameIDs:
	csvFileWriter = csv.writer(gameIDs, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	URL = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountID + "?queue=420&season=13&api_key=" + apiKey
	response = requests.get(URL)
	gameInfo = response.json()
	for game in gameInfo['matches']:
		# print(game['gameId'])
		with open('gameIDs.csv', mode='r') as readGameIDs:
			gameID_reader = csv.reader(readGameIDs)
			duplicateFound = False
			for gameId in gameID_reader:
				if(gameId == game['gameId']):
					duplicateFound = True
			if(not duplicateFound):
				print(game['gameId'])
				csvFileWriter.writerow([game['gameId']])