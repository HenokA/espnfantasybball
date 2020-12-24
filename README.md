# espnfantasybball

Simple repo for a smart coach for fantasy basketball.

## How to query APIs
### Fantasy
The following URL will provide access to Fantasy data if the correct league ID is provided
```
https://fantasy.espn.com/apis/v3/games/fba/seasons/2021/segments/0/leagues/68361879?view=mLiveScoring&view=mMatchupScore&view=mPendingTransactions&view=mPositionalRatings&view=mRoster&view=mSettings&view=mTeam&view=modular&view=mNav
```
## Accessing the Schedule Data
The full JSON file for an NBA season schedule (_2015 or later_) can be accessed through the URL:
```
https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/{YEAR}/league/00_full_schedule.json
```

## Schedule API Documentation
+ lscd
    + mscd
        + mon
        + g
            - gid
            - gcode
            - seri
            - is
            - gdte
            - htm
            - vtm
            - etm
            - an
            - as
            - st
            - stt
            + bd
                + b ...
            + v
                - tid
                - re
                - ta
                - tn
                - tc
                - s
            + h
                - tid
                - re
                - ta
                - tn
                - tc
                - s
            - gdtutc
            - utctm
            - ppdst
            + ptsls ...
    + mscd 
    + mscd
    ...
               

## JSON Breakdown

Name | Description | Value Type | Example
------------ | ------------ | ------------ | ------------ 
| `lscd` | League Schedule | _Array of JSON Objects_ | 
| `mscd` | Month Schedule | _Array of JSON Objects_ |
| `mon` | Month | _String_ | `"June"`
| `g` | Games | _Array of JSON Objects_ |
| `gid` | Game ID | _String_ | `"0041500407"`
| `gcode` | Game Code | _String_ | `"20160619/CLEGSW"`
| `seri` | Playoff Series Summary | _String_ | `"CLE wins series 4-3"`
| `gdte` | Game Date | _String_ | `"2016-06-19"`
| `an` | Arena | _String_ | `"ORACLE Arena"`
| `ac` | Arena City | _String_ | `"Oakland"`
| `as` | Arena State | _String_ | `"CA"`
| `stt` | Game Status | _String_ | `"Final"`
| `bd` | Broadcast Information | _JSON Object_ |
| `b` | Broadcasters | _Array of JSON Objects_ |
| `v` | Visiting Team Information | _JSON Object_ |
| `h` | Home Team Information | _JSON Object_ | 
| `tid` | Team ID | _Integer_ | `1610612739`
| `re` | W-L Record | _String_ | `"16-5"`
| `ta` | Team Abbreviation | _String_ | `"CLE"`
| `tn` | Team Name | _String_ | `"Cavaliers"`
| `tc` | Team City | _String_ | `"Cleveland"`
| `s` | Team Score | _String_ | `"93"`
| `gdtutc` | Game Date UTC | _String_ | `"2016-06-20"`
| `utctm` | UTC Time | _String_ | `"00:00"`


## Fantasy API Documentation
### Average Stats
* 0 = points
* 1 = blocks
* 2 = steals
* 3 = assist
* 6 = rebounds
* 11 = Turnovers
* 13 = fgm
* 14 = fga
* 15 = ftm
* 16 = fta
* 17 = 3pm
* 19 = fg%
* 20 = ft%

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
			
			

