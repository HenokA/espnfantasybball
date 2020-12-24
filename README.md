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
### JSON Architecture
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
               

### Schedule JSON Breakdown

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

### Schedule TeamID - to - ESPN Fantasy TeamID Mapping

| Schedule Data TeamID | Team Name | ESPN Fantasy TeamID 
| ------------ | ------------ | ------------ | ------------
| 1610612737	| Atlanta Hawks	         | 1
| 1610612738	| Boston Celtics	     | 2
| 1610612740	| New Orleans Pelicans	 | 3
| 1610612741	| Chicago Bulls	         | 4
| 1610612739	| Cleveland Cavaliers	 | 5
| 1610612742	| Dallas Mavericks   	 | 6
| 1610612743	| Denver Nuggets    	 | 7
| 1610612765	| Detroit Pistons	     | 8
| 1610612744	| Golden State Warriors	 | 9
| 1610612745	| Houston Rockets	     | 10
| 1610612754	| Indiana Pacers	     | 11
| 1610612746	| LA Clippers	         | 12
| 1610612747	| Los Angeles Lakers	 | 13
| 1610612748	| Miami Heat	         | 14
| 1610612749	| Milwaukee Bucks	     | 15
| 1610612750	| Minnesota Timberwolves | 16
| 1610612751	| Brooklyn Nets	         | 17
| 1610612752	| New York Knicks	     | 18
| 1610612753	| Orlando Magic	         | 19
| 1610612755	| Philadelphia 76ers	 | 20
| 1610612756	| Phoenix Suns	         | 21
| 1610612757	| Portland Trail Blazers | 22
| 1610612758	| Sacramento Kings	     | 23
| 1610612759	| San Antonio Spurs	     | 24
| 1610612760	| Oklahoma City Thunder	 | 25
| 1610612762	| Utah Jazz	             | 26
| 1610612764	| Washington Wizards	 | 27
| 1610612761	| Toronto Raptors	     | 28
| 1610612763	| Memphis Grizzlies	     | 29
| 1610612766	| Charlotte Hornets	     | 30


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
			
			

