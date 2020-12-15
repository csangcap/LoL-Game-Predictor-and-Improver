import json
import requests
import csv
import time

def getChampionInfo():
    with open("champion.json", "r", encoding='utf8') as read_file:
        data = json.loads(read_file.read())
        for champion in data["data"]:
            print(data["data"][champion]["key"] + ": '" + data["data"][champion]["id"] + "', ")

champ_map = {266: 'Aatrox', 103: 'Ahri', 84: 'Akali',12: 'Alistar',32: 'Amumu',34: 'Anivia',1: 'Annie',523: 'Aphelios',22: 'Ashe',
    136: 'AurelionSol', 268: 'Azir',432: 'Bard',53: 'Blitzcrank',63: 'Brand',201: 'Braum',51: 'Caitlyn',164: 'Camille',
    69: 'Cassiopeia',31: 'Chogath',42: 'Corki',122: 'Darius',131: 'Diana',119: 'Draven',36: 'DrMundo',245: 'Ekko',
    60: 'Elise',28: 'Evelynn',81: 'Ezreal',9: 'Fiddlesticks',114: 'Fiora',105: 'Fizz',3: 'Galio',41: 'Gangplank',
    86: 'Garen',150: 'Gnar',79: 'Gragas',104: 'Graves',120: 'Hecarim',74: 'Heimerdinger',420: 'Illaoi',39: 'Irelia',
    427: 'Ivern',40: 'Janna',59: 'JarvanIV',24: 'Jax',126: 'Jayce',202: 'Jhin',222: 'Jinx',145: 'Kaisa',429: 'Kalista',
    43: 'Karma',30: 'Karthus',38: 'Kassadin',55: 'Katarina',10: 'Kayle', 141: 'Kayn',85: 'Kennen',121: 'Khazix',
    203: 'Kindred',240: 'Kled',96: 'KogMaw',7: 'Leblanc',64: 'LeeSin',89: 'Leona',876: 'Lillia',127: 'Lissandra',
    236: 'Lucian',117: 'Lulu',99: 'Lux',54: 'Malphite',90: 'Malzahar',57: 'Maokai',11: 'MasterYi',21: 'MissFortune',
    62: 'MonkeyKing',82: 'Mordekaiser',25: 'Morgana',267: 'Nami',75: 'Nasus',111: 'Nautilus',518: 'Neeko',76: 'Nidalee',
    56: 'Nocturne',20: 'Nunu',2: 'Olaf',61: 'Orianna',516: 'Ornn',80: 'Pantheon',78: 'Poppy',555: 'Pyke',246: 'Qiyana',
    133: 'Quinn',497: 'Rakan',33: 'Rammus',421: 'RekSai',526: 'Rell',58: 'Renekton',107: 'Rengar',92: 'Riven',
    68: 'Rumble',13: 'Ryze',360: 'Samira',113: 'Sejuani',235: 'Senna',147: 'Seraphine',875: 'Sett',35: 'Shaco',
    98: 'Shen',102: 'Shyvana',27: 'Singed',14: 'Sion',15: 'Sivir',72: 'Skarner',37: 'Sona',16: 'Soraka',50: 'Swain',
    517: 'Sylas',134: 'Syndra',223: 'TahmKench',163: 'Taliyah',91: 'Talon',44: 'Taric', 17: 'Teemo',412: 'Thresh',
    18: 'Tristana',48: 'Trundle',23: 'Tryndamere',4: 'TwistedFate',29: 'Twitch',77: 'Udyr',6: 'Urgot',110: 'Varus',
    67: 'Vayne',45: 'Veigar',161: 'Velkoz',254: 'Vi',112: 'Viktor',8: 'Vladimir',106: 'Volibear',19: 'Warwick',
    498: 'Xayah',101: 'Xerath',5: 'XinZhao',157: 'Yasuo',777: 'Yone',83: 'Yorick',350: 'Yuumi',154: 'Zac',238: 'Zed',
    115: 'Ziggs',26: 'Zilean',142: 'Zoe',143: 'Zyra',}

# with open('championMastery.csv', mode='a', newline='') as accountIDs:

def appendChampionKey():
    championKey = []

    with open("champion.json", "r", encoding='utf8') as read_file:
            data = json.loads(read_file.read())
            for champion in data["data"]:
                championKey.append(data["data"][champion]["key"])

    print(championKey)

    with open('championMastery.csv', mode='a', newline='') as championMastery:
        csvFileWriter = csv.writer(championMastery, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvFileWriter.writerow(championKey)

def UsernamesToChampionMastery():
    myChampionMastery = {}

    region = "na1"
    # username = "wizardstars"
    apiKey = "RGAPI-00b8500a-3c34-4f24-b28d-510f24503c88"

    with open('usernames.csv', mode='r') as usernames:
        csv_reader = csv.reader(usernames)
        for row in csv_reader:
            Get_SummonerInfo_URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + row[0] + "?api_key=" + apiKey
            response = requests.get(Get_SummonerInfo_URL)
            summonerInfo = response.json()
            summonerID = summonerInfo['id']
            Get_ChampionMastery_URL = "https://" + region + ".api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summonerID + "?api_key=" + apiKey
            response = requests.get(Get_ChampionMastery_URL)
            championMastery = response.json()

            highestChampionPoints = 0

            for champion in championMastery:
                # print(champion['championId'], champion['championPoints'])
                myChampionMastery[champion['championId']] = champion['championPoints']
                if(champion['championPoints'] > highestChampionPoints):
                    highestChampionPoints = champion['championPoints']

            # print(myChampionMastery)

            toAppend = []
            
            if highestChampionPoints > 0:
                for key in myChampionMastery:
                    toAppend.append(summonerID)
                    toAppend.append(key)
                    toAppend.append(round(myChampionMastery[key]/highestChampionPoints * 100))
                    print(toAppend)
                    with open('normalized_roster.csv', mode='a', newline='') as normalized_roster:
                        csvFileWriter = csv.writer(normalized_roster, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        csvFileWriter.writerow(toAppend)
                    toAppend.clear()

# print(round(1.23*100))
# UsernamesToChampionMastery()

def getMyInfo():
    region = "na1"
    apiKey = "RGAPI-00b8500a-3c34-4f24-b28d-510f24503c88"
    username = "wizardstars"
    Get_SummonerInfo_URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + username + "?api_key=" + apiKey
    response = requests.get(Get_SummonerInfo_URL)
    summonerInfo = response.json()
    summonerID = summonerInfo['id']
    Get_ChampionMastery_URL = "https://" + region + ".api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summonerID + "?api_key=" + apiKey
    response = requests.get(Get_ChampionMastery_URL)
    mastery_json = response.json()
    
    highestChampionPoints = 0

    for champion in mastery_json:
        # print(champion['championId'], champion['championPoints'])
        # myChampionMastery[champion['championId']] = champion['championPoints']
        if(champion['championPoints'] > highestChampionPoints):
            highestChampionPoints = champion['championPoints']
    
    myDict = {'summonerID': [], 'championID': [], 'rating': []}
    max_champs = 5
    
    for x in range(0, min(len(mastery_json), max_champs)):
        normalized_points = round(mastery_json[x]["championPoints"] / highestChampionPoints * 100)
        myDict['summonerID'].append(summonerID)
        myDict['championID'].append(mastery_json[x]["championId"])
        myDict['rating'].append(normalized_points)
    
    print(myDict)

def leaderboardToSummonerID():
    region = "na1"
    apiKey = "RGAPI-00b8500a-3c34-4f24-b28d-510f24503c88"
    leaderboard_URL = "https://americas.api.riotgames.com/lor/ranked/v1/leaderboards" + "?api_key=" + apiKey
    response = requests.get(leaderboard_URL)
    leaderboard_json = response.json()

    i = 0
    toAppend = []
    resumeAt = 90
    resume = False
    with open('leaderboard.csv', mode='a', newline='') as leaderboard_csv:
        leaderboardWriter = csv.writer(leaderboard_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for player in leaderboard_json["players"]:
            # print(player["name"])
            if(resume):
                if i > 90:
                    print("Waiting 2 minutes")
                    time.sleep(120)
                    i = 0
                    # break
                    
                Get_SummonerInfo_URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + player["name"] + "?api_key=" + apiKey
                response = requests.get(Get_SummonerInfo_URL)
                summonerInfo_json = response.json()
                if 'status' in summonerInfo_json:
                    print("skipping ", player["name"])
                    # skippedWriter.writerow(player["name"])
                else: 
                    toAppend.append(player["rank"])
                    toAppend.append(summonerInfo_json['id'])
                    print(player["rank"], summonerInfo_json['id'])
                    leaderboardWriter.writerow(toAppend)
                    toAppend.clear()
            else:
                if i is resumeAt - 1:
                    resume = True
                    i = 0
            i += 1
        
def SummonerIDToMastery():
    region = "na1"
    apiKey = "RGAPI-00b8500a-3c34-4f24-b28d-510f24503c88"
    
    with open('leaderboard_masteries.csv', mode='a', newline='') as masteries_csv:
        masteries_writer = csv.writer(masteries_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        with open('leaderboard_summonerIDs.csv', mode='r') as summonerIDs:
            summonerID_reader = csv.reader(summonerIDs)
            i = 1
            resumeAt = 1593
            resume = False
            
            for row in summonerID_reader:
                if(resume):
                    if i > 90:
                        print("Waiting 2 minutes")
                        time.sleep(120)
                        i = 1
                    
                    print(i, "Currently appending:", row[0])

                    Get_ChampionMastery_URL = "https://" + region + ".api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + row[1] + "?api_key=" + apiKey
                    response = requests.get(Get_ChampionMastery_URL)
                    championMastery = response.json()

                    highestChampionPoints = 0
                    ChampionMasteryDict = {}
                    
                    if len(championMastery) != 0:

                        for champion in championMastery:
                            # print(champion['championId'], champion['championPoints'])
                            ChampionMasteryDict[champion['championId']] = champion['championPoints']
                            if(champion['championPoints'] > highestChampionPoints):
                                highestChampionPoints = champion['championPoints']

                        # print(ChampionMasteryDict)

                        toAppend = []
                        
                        if highestChampionPoints > 0:
                            for key in ChampionMasteryDict:
                                toAppend.append(row[1])
                                toAppend.append(key)
                                toAppend.append(round(ChampionMasteryDict[key]/highestChampionPoints * 100))
                                masteries_writer.writerow(toAppend)
                                toAppend.clear()
                    else:
                        print("skipping")
                else:
                    # print(i, row[0], resumeAt, int(row[0]) > resumeAt)
                    if int(row[0]) == resumeAt:
                        resume = True
                        i = 0
                i += 1
            

def TestingSummonerIDToMastery():
    region = "na1"
    apiKey = "RGAPI-00b8500a-3c34-4f24-b28d-510f24503c88"
    summonerID = "PfhPRnpYVE1bB7B_LUq1xT4Fih263cCUvspAuiQncl2Mlhs"
    Get_ChampionMastery_URL = "https://" + region + ".api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summonerID + "?api_key=" + apiKey
    response = requests.get(Get_ChampionMastery_URL)
    championMastery = response.json()

    print(championMastery)
    
    highestChampionPoints = 0
    ChampionMasteryDict = {}

    if len(championMastery) != 0:
        for champion in championMastery:
            # print(champion['championId'], champion['championPoints'])
            ChampionMasteryDict[champion['championId']] = champion['championPoints']
            if(champion['championPoints'] > highestChampionPoints):
                highestChampionPoints = champion['championPoints']
    else:
        print("skipping")

    # print(ChampionMasteryDict)

    toAppend = []
    
    if highestChampionPoints > 0:
        for key in ChampionMasteryDict:
            toAppend.append(summonerID)
            toAppend.append(key)
            toAppend.append(round(ChampionMasteryDict[key]/highestChampionPoints * 100))
            print(toAppend)
            # masteries_writer.writerow(toAppend)
            toAppend.clear()

# TestingSummonerIDToMastery()
# SummonerIDToMastery()
def checkingNA1():
    region = "na1"
    apiKey = "RGAPI-3b7fd837-9c72-49a1-a831-c2f50c9e6fe4"
    with open('random_usernames.csv', mode='r') as randomUsernames:
        with open('checkedUsernames.csv', mode='a', newline='') as checkedUsernames:
        
            usernameReader = csv.reader(randomUsernames)
            checkedUsernamesWriter = csv.writer(checkedUsernames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            for username in usernameReader:
                # print(username[0])
                Get_SummonerInfo_URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + username[0] + "?api_key=" + apiKey
                response = requests.get(Get_SummonerInfo_URL)
                summonerInfo_json = response.json()
                
                if 'status' in summonerInfo_json:
                    print("skipping ", username[0])
                    # skippedWriter.writerow(player["name"])
                else: 
                    print("Appending", username[0])
                    checkedUsernamesWriter.writerow([username[0]])
checkingNA1()