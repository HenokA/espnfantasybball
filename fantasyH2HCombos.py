import json
import requests
import datetime
from datetime import datetime
import urllib, json
import csv
from itertools import combinations 

def teamDictionaryGenerator():
    for team in fantasyData_leagueTeams:
        leagueTeams[team["id"]] = team
    for member in fantasyData_leagueMembers:
        members[member["id"]] = member

def playerLookup(playerName):
    if bool(playerMapping[playerName]["stats"]):
        for stat in playerMapping[playerName]["stats"]:
            print(stat, "\n")
        # projected2021Stats = playerMapping[playerName]["stats"][4]
        # y2021Stats = playerMapping[playerName]["stats"][0]
        # y2020Stats = playerMapping[playerName]["stats"][2]
        # print(projected2021Stats)

#Looks up matchups for a given teamId
def matchUpLookUp (teamLabel):
    print("Schedule & Team Info for Team ", teamLabel, " - " + leagueTeams[teamLabel]["location"] + " " +leagueTeams[teamLabel]["nickname"], " - " + members[leagueTeams[teamLabel]["owners"][0]]["firstName"] +" "+ members[leagueTeams[teamLabel]["owners"][0]]["lastName"], "\n")
    my_date = datetime.today()
    year, week_num, day_of_week = my_date.isocalendar()
    lS_year, lS_week_num, lS_day_of_week = leagueBeginning.isocalendar()
    if week_num < 52:
        week_num += 53
    leagueWeek = week_num - lS_week_num +1 #positive number means 2021
    for matchup in leagueSchedule:
        tempUse = {}
        if matchup["away"]["teamId"] == teamLabel:
            opponentTeamId = int(matchup["home"]["teamId"])
            tempUse["teamId"] = opponentTeamId
            tempUse["matchupWeek"] = int(matchup["matchupPeriodId"]) - leagueWeek
            tempUse["opponentName"] = members[leagueTeams[opponentTeamId]["owners"][0]]["firstName"] +" "+ members[leagueTeams[opponentTeamId]["owners"][0]]["lastName"]
            tempUse["opponentTeam"] = leagueTeams[opponentTeamId]["nickname"]
            mySchedule.append(tempUse)
            print(tempUse)
        elif matchup["home"]["teamId"] == teamLabel:
            opponentTeamId = int(matchup["away"]["teamId"])
            tempUse["teamId"] = opponentTeamId
            tempUse["matchupWeek"] = int(matchup["matchupPeriodId"]) - leagueWeek
            tempUse["opponentName"] = members[leagueTeams[opponentTeamId]["owners"][0]]["firstName"] +" "+ members[leagueTeams[opponentTeamId]["owners"][0]]["lastName"]
            tempUse["opponentTeam"] = leagueTeams[opponentTeamId]["nickname"]
            mySchedule.append(tempUse)
            print(tempUse)

#This function calls the url to update the JSON of Fantasy info
def getAPIResponse():
    url = "https://fantasy.espn.com/apis/v3/games/fba/seasons/2021/segments/0/leagues/68361879?view=mLiveScoring&view=mMatchupScore&view=mPendingTransactions&view=mPositionalRatings&view=mRoster&view=mSettings&view=mTeam&view=modular&view=mNav"
    response = requests.get(url,
                 cookies={"swid": espnAuth["swid"],
                          "espn_s2": espnAuth["espn_s2"]})
    return response.json()

#This function parses the input Schedule JSON to understand the NBA Schedule
def parseSchedule():
    for month in scheduleData["lscd"]:
        for game in month["mscd"]["g"]:
            count = 1
            for key in fantasyWeeks.keys():
                date = datetime.strptime(game["gdte"], '%Y-%m-%d')
                if date >= fantasyWeeks[key]["date"][0]:
                    if date <= fantasyWeeks[key]["date"][1]:   
                        nbaGame = {}
                        nbaGame["date"] = date
                        nbaGame["ids"] = [str(schedule2Fantasy[game["v"]["tid"]]), str(schedule2Fantasy[game["h"]["tid"]])]
                        nbaGame["away"] = str(schedule2Fantasy[game["v"]["tid"]])+","+game["v"]["tc"]+" "+game["v"]["tn"]
                        nbaGame["home"] = str(schedule2Fantasy[game["h"]["tid"]])+","+game["h"]["tc"]+" "+game["h"]["tn"]
                        fantasyWeeks[key]["games"].append(nbaGame) 
    #print(fantasyWeeks[1]["games"])

#This function goes through each Fantasy team and builds team:roster mappings & a general player Dictionary
def parseTeams():
    for team in fantasyData_leagueTeams:
        tempTeam = {}
        #print(team["roster"]["entries"][0].items())
        for player in team["roster"]["entries"]:
            tempPlayer = {}
            tempPlayer["name"] = player["playerPoolEntry"]["player"]["fullName"]
            tempPlayer["nbaTeam"] = player["playerPoolEntry"]["player"]["proTeamId"]
            tempPlayer["eligibleSlots"] = player["playerPoolEntry"]["player"]["eligibleSlots"]
            tempPlayer["stats"] = remapStats(player["playerPoolEntry"]["player"]["stats"])
            tempPlayer["ownership"] = player["playerPoolEntry"]["player"]["ownership"]
            tempPlayer["fantasyTeamID"] = team["id"]
            tempTeam[tempPlayer["name"]] = tempPlayer
            playerMapping[tempPlayer["name"]] = tempPlayer
        teamMapping[team["id"]] = tempTeam

#Remaps the ambiguous keyValues for playerStats into readable form
def remapStats(stats):
    remappedStats = []
    toCheck = [4, 5]
    #print(stats[4]["averageStats"].keys())
    statMapping = {"0":"points","1":"blocks", "2":"steals", "3":"assist",
        "6":"rebounds", "11":"Turnovers", "13":"fgm", "14":"fga", "15":"ftm",
        "16":"fta", "17":"threePM", "19":"fg%", "20":"ft%"}
    for index in toCheck:
        tempStat = {}
        if index < len(stats) and bool(stats):
            for key in statMapping.keys():
                try:
                    if key in stats[index]["averageStats"].keys():
                        tempStat[statMapping[key]] = stats[index]["averageStats"][key]
                    else:
                        tempStat[statMapping[key]] = 0   
                except:
                    foo = 0
        remappedStats.append(tempStat)
    return remappedStats

def csvDict(filename):
    result_list=[]
    with open(filename) as file_obj:
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for row in reader:
            result_list.append(dict(row))
    return result_list

def gamesPerWeek(nbaTeam, fantasyWeek):
    games = fantasyWeeks[fantasyWeek]["games"]
    countGames = 0
    for game in games:
        #print(game["ids"])
        if str(nbaTeam) in game["ids"]:
            countGames += 1
    return countGames

def teamCombos(){
    
}

#This is the main function that understands user input.
def parseInput(inputVal):
    if inputVal == 1:
        teamLabel=int(input ("\n What team should I lookup? = "))
        matchUpLookUp(teamLabel)
        print("done collecting schedule...\n  ")#, teamMapping[teamLabel])
        #print(fantasyWeeks[1]["games"])
        for player in teamMapping[teamLabel]:
            print(teamMapping[teamLabel][player]["name"], ", ", gamesPerWeek(teamMapping[teamLabel][player]["nbaTeam"], 1))
    elif inputVal == 2:
        playerName =input ("\n What player should I lookup? = ")
        playerLookup(playerName)
    elif inputVal == 3:
        print("computing H2H matchup")
        gamesThisWeek()
    elif inputVal == 4:
        print("computing Trade matchup")   
#League starts week 52 of 2020

with open(r"C:\Users\Henok Addis\Documents\espn_auth.json") as f:
  espnAuth = json.load(f) 

fantasyData = getAPIResponse()

leagueSchedule = fantasyData["schedule"]
#with open(r"C:\Users\Henok Addis\Code\espnfantasybball\nbatestjson.json") as f:
#  fantasyData = json.load(f)

with open(r"C:\Users\Henok Addis\Code\espnfantasybball\nbaschedule.json") as f:
  scheduleData = json.load(f)


#initial variables set
leagueSchedule = fantasyData["schedule"]
fantasyData_leagueTeams = fantasyData["teams"]
fantasyData_leagueMembers = fantasyData["members"]
testteams = []
leagueTeams = {}
members = {}
mySchedule = []
#builds initial team data
teamDictionaryGenerator()
leagueBeginning = datetime.strptime('22 Dec 2020', '%d %b %Y')
fantasyWeeks = {
    #1: ['22 Dec 2020', '27 Dec 2020'],
    1: {"date": [datetime.strptime('22 Dec 2020', '%d %b %Y'), datetime.strptime('27 Dec 2020', '%d %b %Y')], "games": []},
    2: {"date": [datetime.strptime('2020-12-28', '%Y-%m-%d'), datetime.strptime('2021-01-03', '%Y-%m-%d')], "games": []},
    3: {"date": [datetime.strptime('2021-01-04', '%Y-%m-%d'), datetime.strptime('2021-01-10', '%Y-%m-%d')], "games": []},
    4: {"date": [datetime.strptime('2021-01-11', '%Y-%m-%d'), datetime.strptime('2021-01-17', '%Y-%m-%d')], "games": []},
    5: {"date": [datetime.strptime('2021-01-18', '%Y-%m-%d'), datetime.strptime('2021-01-24', '%Y-%m-%d')], "games": []},
    6: {"date": [datetime.strptime('2021-01-25', '%Y-%m-%d'), datetime.strptime('2021-01-31', '%Y-%m-%d')], "games": []},
    7: {"date": [datetime.strptime('2021-02-01', '%Y-%m-%d'), datetime.strptime('2021-02-01', '%Y-%m-%d')], "games": []},
    8: {"date": [datetime.strptime('2021-02-08', '%Y-%m-%d'), datetime.strptime('2021-02-14', '%Y-%m-%d')], "games": []},
    9: {"date": [datetime.strptime('2021-02-15', '%Y-%m-%d'), datetime.strptime('2021-02-21', '%Y-%m-%d')], "games": []},
    10: {"date": [datetime.strptime('2021-02-22', '%Y-%m-%d'), datetime.strptime('2021-02-28', '%Y-%m-%d')], "games": []},
    11: {"date": [datetime.strptime('2021-03-01', '%Y-%m-%d'), datetime.strptime('2021-03-14', '%Y-%m-%d')], "games": []},
    12: {"date": [datetime.strptime('2021-03-15', '%Y-%m-%d'), datetime.strptime('2021-03-21', '%Y-%m-%d')], "games": []},
    13: {"date": [datetime.strptime('2021-03-22', '%Y-%m-%d'), datetime.strptime('2021-03-28', '%Y-%m-%d')], "games": []},
    14: {"date": [datetime.strptime('2021-03-29', '%Y-%m-%d'), datetime.strptime('2021-04-04', '%Y-%m-%d')], "games": []},
    15: {"date": [datetime.strptime('2021-04-05', '%Y-%m-%d'), datetime.strptime('2021-04-11', '%Y-%m-%d')], "games": []},
    16: {"date": [datetime.strptime('2021-04-12', '%Y-%m-%d'), datetime.strptime('2021-04-18', '%Y-%m-%d')], "games": []}
}

schedule2Fantasy = {1610612737: 1,1610612738: 2,1610612740: 3,1610612741: 4,1610612739: 5,1610612742: 6,1610612743: 7,1610612765: 8,1610612744: 9,1610612745: 10,1610612754: 11,1610612746: 12,1610612747: 13,1610612748: 14,1610612749: 15,1610612750: 16,1610612751: 17,1610612752: 18,1610612753: 19,
    1610612755: 20, 1610612756: 21, 1610612757: 22, 1610612758: 23, 1610612759: 24, 1610612760: 25, 1610612762: 26, 1610612764: 27, 1610612761: 28, 1610612763: 29, 1610612766: 30
}

#gets user schedules
parseSchedule()

#dict for team lookup
teamMapping = {}
#dict for player lookup
playerMapping = {}
parseTeams()

#further options
test_text = int(input ("\n Team Lookup          = 1\n Player Lookup        = 2\n Run H2H Analysis     = 3\n Trade Evaluation     = 4\n Waiver Wire Analysis = 5\n\n"))
parseInput(test_text)