# Playoff Portfolio Creator
A Python script that utilizes the following to create a stock portfolio based off of teams that win throughout the NHL playoffs
- Alpaca Markets Trading API
- AWS Lambda
- Data from: https://sports.yahoo.com/nhl/scoreboard/

## How it Works
Using AWS Lambda, the script is run once a day to scrape scores and team names for all games played. This information is parsed and a winner is decided for each game. Each team has an assigned ticker that is somehow associated with the organization (helmet sponsor, jersey sponsor, arena sponsor). When a team wins, 1 share of the corresponding ticker is purchased using the Alpaca Trading API. Below are the corresponding tickers for each NHL team. Upon completion of the NHL playoffs this script will have created a diverse portfolio consisting of equity from a range of sectors.

## Team Tickers
|Western Conference|Eastern Conference|
|--|--|
|<table> <tr><th>Team</th><th>Ticker</th></tr><tr><td>Dallas Stars</td><td>SVNDY</td></tr> <tr><td>Colorado Avalanche</td><td>BALL</td></tr> <tr><td>Winnipeg Jets</td><td>BCE</td></tr> <tr><td>Nashville Predators</td><td>BRDCY</td></tr> <tr><td>St Louis Blues</td><td>EPD</td></tr> <tr><td>Minnesota Wild</td><td>TM</td></tr> <tr><td>Arizona Coyotes</td><td>SVV</td></tr> <tr><td>Chicago Blackhawks</td><td>UAL</td></tr> <tr><td>Vancouver Canucks</td><td>NXE</td></tr> <tr><td>Edmonton Oilers</td><td>RCI</td></tr> <tr><td>Vegas Golden Knights</td><td>TMUS</td></tr> <tr><td>LA Kings</td><td>ELV</td></tr> <tr><td>Seattle Kraken</td><td>AMZN</td></tr> <tr><td>Calgary Flames</td><td>BNS</td></tr> <tr><td>Anaheim Ducks</td><td>HMC</td></tr> <tr><td>San Jose Sharks</td><td>SAP</td></tr> </table>| <table> <tr><th>Team</th><th>Ticker</th></tr><tr><td>Boston Bruins</td><td>TD</td></tr> <tr><td>Florida Panthers</td><td>AMTB</td></tr> <tr><td>Toronto Maple Leafs</td><td>PAHC</td></tr> <tr><td>Tampa Bay Lightning</td><td>XOM</td></tr> <tr><td>Detroit Red Wings</td><td>MYE</td></tr> <tr><td>Buffalo Sabres</td><td>KEY</td></tr> <tr><td>Ottawa Senators</td><td>CM</td></tr> <tr><td>Montreal Canadiens</td><td>RY</td></tr> <tr><td>New York Rangers</td><td>BRK.B</td></tr> <tr><td>Carolina Hurricanes</td><td>MODG</td></tr> <tr><td>Philadelphia Flyers</td><td>WFC</td></tr> <tr><td>Washington Capitals</td><td>COF</td></tr> <tr><td>New York Islanders</td><td>UBS</td></tr> <tr><td>Pittsburgh Penguins</td><td>MSA</td></tr> <tr><td>New Jersey Devils</td><td>PRU</td></tr> <tr><td>Columbus Blue Jackets</td><td>BFH</td></tr> </table>|

# Final Portfolio
![image](https://github.com/tbbovest/playoff_portfolio/assets/74005237/8f535feb-896b-4eab-a0f7-21bf18a78004)
