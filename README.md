# Playoff Portfolio Creator
A Python script that utilizes the following to create a stock portfolio based off of teams that win throughout the NHL playoffs
- Alpaca Markets Trading API
- AWS Lambda
- Data from: https://sports.yahoo.com/nhl/scoreboard/

## How it works
Scores and team names are scraped daily from the link above using AWS Lambda. This information is parsed and a winner is decided for each game. Each team has an assigned ticker that is somehow associated with the team (helmet sponsor, jersey sponsor, arena sponsor). When a team wins, 1 share of the corresponding ticker is purchased using the Alpaca API.
