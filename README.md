# espnfantasybball

Simple repo for a smart coach for fantasy basketball.

## Example API query
https://fantasy.espn.com/apis/v3/games/fba/seasons/2021/segments/0/leagues/<<INSERTLEAGUEID>>?view=mLiveScoring&view=mMatchupScore&view=mPendingTransactions&view=mPositionalRatings&view=mRoster&view=mSettings&view=mTeam&view=modular&view=mNav

## Documenting API responses
### Average Stats
0 = points
1 = blocks
2 = steals
3 = assist
6 = rebounds
11 = Turnovers
13 = fgm
14 = fga
15 = ftm
16 = fta
17 = 3pm
19 = fg%
20 = ft%

### Schedule
	away
		rosterForCurrentScoringPeriod
		rosterForMatchupPeriodDelayed
		teamId
		tiebreak
		totalPoints
	home
		rosterForCurrentScoringPeriod 
		rosterForMatchupPeriodDelayed
		teamId
		tiebreak
		totalPoints
	id
	matchupPeriodId
	playoffTierType
	winner

### Teams
	"id": int,
	"nickname": string
	"draftDayProjectedRank": int
	"roster": object
		"entries": array of player objects
			"playerPoolEntry": object
				"player": object
					"eligibleSlots": array of ints (places player can fit)
					"fullName": string
					"id": int
					"injured": binary
                                	"injuryStatus": string ("ACTIVE")
					"proTeamId": int (team name)
					"stats": array of objects
						0 - 2021 season
							"averageStats": object (see averageStats breakdown)
						1 - 2021 season (??)
						2 - 2020 season
						3 - 2021 season (??)
						4 - 2021 projections					
			
			

