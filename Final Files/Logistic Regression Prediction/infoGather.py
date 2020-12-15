import requests
import csv
import time

region = "na1"
username = "Doublelift"
apiKey = "RGAPI-0033f1ea-daa5-4542-a8e8-b89f4bb8c244"

URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + username + "?api_key=" + apiKey

count = 0
currentRow = 0
resumeAt = 1015

# For turning usernames into their account IDs

# with open('accountIDs.csv', mode='a', newline='') as accountIDs:
#     csvFileWriter = csv.writer(accountIDs, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     with open('usernames.csv', mode='r') as usernames:
#         csv_reader = csv.reader(usernames)
#         for row in csv_reader:
#             URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + row[0] + "?api_key=" + apiKey
#             response = requests.get(URL)
#             playerInfo = response.json()
#             print(playerInfo['accountId'])
#             csvFileWriter.writerow([playerInfo['accountId']])

# Turns account IDs to game IDs

# with open('gameIDs.csv', mode='a', newline='') as gameIDs:
#     csvFileWriter = csv.writer(gameIDs, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     with open('accountIDs.csv', mode='r') as accountIDs:
#         csv_reader = csv.reader(accountIDs)
#         for row in csv_reader:
#             URL = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + row[0] + "?queue=420&season=13&api_key=" + apiKey
#             response = requests.get(URL)
#             gameInfo = response.json()
#             for game in gameInfo['matches']:
#                 # print(game['gameId'])
#                 with open('gameIDs.csv', mode='r') as readGameIDs:
#                     gameID_reader = csv.reader(readGameIDs)
#                     duplicateFound = False
#                     for gameId in gameID_reader:
#                         if(gameId == game['gameId']):
#                             duplicateFound = True
#                     if(not duplicateFound):
#                         print(game['gameId'])
#                         csvFileWriter.writerow([game['gameId']])

record = []
with open('gameInfo.csv', mode='a', newline='') as gameInfo:
    csvFileWriter = csv.writer(gameInfo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with open('gameIDs.csv', mode='r') as gameIDs:
        csv_reader = csv.reader(gameIDs)
        for row in csv_reader:
            currentRow += 1
            if(currentRow >= resumeAt):
                URL = "https://na1.api.riotgames.com/lol/match/v4/matches/" + row[0] + "?api_key=" + apiKey
                count += 1
                if(count == 30):
                    print("Waiting...")
                    time.sleep(120)
                    count = 0
                
                response = requests.get(URL)
                gameInformation = response.json()
                
                for participant in gameInformation["participants"]:
                    record.append(participant["championId"])
                if(gameInformation["teams"][0]["win"] == "Win"):
                    record.append(1)
                else:
                    record.append(0)
                csvFileWriter.writerow(record)
                record.clear()
                print("Row", currentRow, "Done")
