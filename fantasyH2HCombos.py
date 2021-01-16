import json
import requests
import datetime
from datetime import datetime
import urllib, json

def teamDictionaryGenerator():
    for team in fantasyData_leagueTeams:
        leagueTeams[team["id"]] = team
    for member in fantasyData_leagueMembers:
        members[member["id"]] = member

def playerLookup(playerName):
    print(playerMapping[playerName])

def teamLookup (teamLabel):
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
            team = str(game["v"]["tid"])+","+game["v"]["tc"]+" "+game["v"]["tn"]
            nbateams.append(team)
            team = str(game["h"]["tid"])+","+game["h"]["tc"]+" "+game["h"]["tn"]
            nbateams.append(team)
    #print(nbateams)

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
            tempPlayer["stats"] = player["playerPoolEntry"]["player"]["stats"]
            tempPlayer["fantasyTeamID"] = team["id"]
            tempTeam[tempPlayer["name"]] = tempPlayer
            playerMapping[tempPlayer["name"]] = tempPlayer
        teamMapping[team["id"]] = tempTeam

#This is the main function that understands user input.
def parseInput(inputVal):
    if inputVal == 1:
        teamLabel=int(input ("\n What team should I lookup? = "))
        teamLookup(teamLabel)
        print("done collecting schedule...\n")
        for player in teamMapping[teamLabel]:
            print(player)
    elif inputVal == 2:
        playerName =input ("\n What player should I lookup? = ")
        playerLookup(playerName)
    elif inputVal == 3:
        print("computing H2H matchup")
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
nbateams = []
testteams = []
leagueTeams = {}
members = {}
mySchedule = []
#builds initial team data
teamDictionaryGenerator()
leagueBeginning = datetime.strptime('22 Dec 2020', '%d %b %Y')

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
