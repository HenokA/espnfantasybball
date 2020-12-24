import json
import datetime
from datetime import datetime
import urllib, json


def teamDictionaryGenerator():
    for team in fantasyData_leagueTeams:
        leagueTeams[team["id"]] = team
    for member in fantasyData_leagueMembers:
        members[member["id"]] = member

def findMatchup ():
    my_date = datetime.today()
    year, week_num, day_of_week = my_date.isocalendar()
    lS_year, lS_week_num, lS_day_of_week = leagueBeginning.isocalendar()
    if week_num < 52: 
        week_num += 53
    leagueWeek = week_num - lS_week_num +1 #positive number means 2021
    for matchup in leagueSchedule:
        tempUse = {}
        if matchup["away"]["teamId"] == teamNumber:
            opponentTeamId = int(matchup["home"]["teamId"])
            tempUse["teamId"] = opponentTeamId
            tempUse["matchupWeek"] = int(matchup["matchupPeriodId"]) - leagueWeek
            tempUse["opponentName"] = members[leagueTeams[opponentTeamId]["owners"][0]]["firstName"] +" "+ members[leagueTeams[opponentTeamId]["owners"][0]]["lastName"]
            tempUse["opponentTeam"] = leagueTeams[opponentTeamId]["nickname"]
            mySchedule.append(tempUse)
            print(tempUse)
        elif matchup["home"]["teamId"] == teamNumber:
            opponentTeamId = int(matchup["away"]["teamId"])
            tempUse["teamId"] = opponentTeamId
            tempUse["matchupWeek"] = int(matchup["matchupPeriodId"]) - leagueWeek
            tempUse["opponentName"] = members[leagueTeams[opponentTeamId]["owners"][0]]["firstName"] +" "+ members[leagueTeams[opponentTeamId]["owners"][0]]["lastName"]
            tempUse["opponentTeam"] = leagueTeams[opponentTeamId]["nickname"]
            mySchedule.append(tempUse)
            print(tempUse)

def parseInput(inputVal):
    if inputVal == 1:
        findMatchup()
        print("done collecting schedule...\n")
    elif inputVal == 2:
        print("computing H2H matchup")
    elif inputVal == 3:
        print("computing Trade matchup")

def getAPIResponse():
    fantasyData = json.load(f)
    url = "https://fantasy.espn.com/apis/v3/games/fba/seasons/2021/segments/0/leagues/68361879?view=mLiveScoring&view=mMatchupScore&view=mPendingTransactions&view=mPositionalRatings&view=mRoster&view=mSettings&view=mTeam&view=modular&view=mNav"
    response = requests.get(url,
                 cookies={"swid": "{SWID-COOKIE-HERE}",
                          "espn_s2": "LONG_ESPN_S2_COOKIE_HERE"})
    fantasyData = json.loads(response.read())

def parseSchedule():
    for month in scheduleData["lscd"]:
        for game in month["mscd"]["g"]:
            team = str(game["v"]["tid"])+","+game["v"]["tc"]+" "+game["v"]["tn"]
            nbateams.append(team)
            team = str(game["h"]["tid"])+","+game["h"]["tc"]+" "+game["h"]["tn"]
            nbateams.append(team)
    print(nbateams)

def parseTeams():
    for team in fantasyData_leagueTeams:
        for player in team["roster"]["entries"]
            

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
# print(fantasyData["draftDetail"])
#League starts week 52 of 2020
with open(r"C:\Users\headdis\Code\espnfantasybball\nbatestjson.json") as f:
  fantasyData = json.load(f)

with open(r"C:\Users\headdis\Code\espnfantasybball\nbaschedule.json") as f:
  scheduleData = json.load(f)

leagueSchedule = fantasyData["schedule"]
fantasyData_leagueTeams = fantasyData["teams"]
fantasyData_leagueMembers = fantasyData["members"]

nbateams = []

testteams = []

leagueTeams = {}
members = {}
mySchedule = []
teamDictionaryGenerator()
leagueBeginning = datetime.strptime('22 Dec 2020', '%d %b %Y')
teamNumber = int(input (" Input team number: "))
test_text = int(input ("\n Find Opponent        = 1\n Run H2H Analysis     = 2\n Trade Evaluation     = 3\n Waiver Wire Analysis = 4\n\n"))

#parseInput(test_text)
parseSchedule()