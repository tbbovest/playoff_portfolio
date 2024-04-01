# Playoff Portfolio Creator
A Python script that utilizes the following to create a stock portfolio based off of teams that win throughout the NHL playoffs
- Alpaca Markets Trading API
- AWS Lambda
- Data from: https://sports.yahoo.com/nhl/scoreboard/

## How it Works
Using AWS Lambda the script is run once a day and scores/team names for each game played are scraped and stored. This information is parsed and a winner is decided for each game. Each team has an assigned ticker that is somehow associated with the organization (helmet sponsor, jersey sponsor, arena sponsor). When a team wins, 1 share of the corresponding ticker is purchased using the Alpaca Trading API. Below are the corresponding tickers for each NHL team.

## Team Tickers
Boston Bruins: $TD 
Carolina Hurricanes: $MODG 
Columbus Blue Jackets: $BFH
New Jersey Devils: $PRU <br />
New York Islanders: $UBS <br />
New York Rangers: $BRK.B <br />
Philadelphia Flyers: $WFC <br />
Pittsburgh Penguins: $MSA <br />
Washington Capitals: $COF <br />
Buffalo Sabres: $KEY
Detroit Red Wings: $MYE
Florida Panthers: $AMTB
Montreal Canadiens: $RY
Ottawa Senators: $CM
Tampa Bay Lightning: $XOM
Toronto Maple Leafs: $PAHC
Arizona Coyotes: $SVV
Chicago Blackhawks: $UAL
Colorado Avalanche: $BALL
Dallas Stars: $SVNDY
Minnesota Wild: $TM
Nashville Predators: $BRDCY
St Louis Blues: $EPD
Winnipeg Jets: $BCE
Anaheim Ducks: $HMC
Calgary Flames: $BNS
Edmonton Oilers: $RCI
LA Kings: $ELV
San Jose Sharks: $SAP
Seattle Kraken: $AMZN
Vancouver Canucks: $NXE
Vegas Golden Knights: $TMUS
