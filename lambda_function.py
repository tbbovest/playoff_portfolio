from bs4 import BeautifulSoup
import requests
import re
import json
from config import *

url = "https://sports.yahoo.com/nhl/scoreboard/?confId=&schedState=2&dateRange=2024-03-22"
page = requests.get(url)
main = BeautifulSoup(page.content, 'html.parser')

team_tickers = {
    "Bruins": "TD",
    "Hurricanes": "MODG",
    "Blue Jackets": "BFH",
    "Devils": "PRU",
    "Islanders": "UBS",
    "Rangers": "BRK.B",
    "Flyers": "WFC",
    "Penguins": "MSA",
    "Capitals": "COF",
    "Sabres": "KEY",
    "Red Wings": "MYE",
    "Panthers": "AMTB",
    "Canadiens": "RY",
    "Senators": "CM",
    "Lightning": "XOM",
    "Maple Leafs": "PAHC",
    "Coyotes": "SVV",
    "Blackhawks": "UAL",
    "Avalanche": "BALL",
    "Stars": "SVNDY", 
    "Wild": "TM",
    "Predators": "BRDCY",
    "Blues": "EPD",
    "Jets": "BCE",
    "Ducks": "HMC",
    "Flames": "BNS",
    "Oilers": "RCI",
    "Kings": "ELV",
    "Sharks": "SAP",
    "Kraken": "AMZN",
    "Canucks": "NXE",
    "Golden Knights": "TMUS"
    }

# Scrape teams who played and scores for each
team_name_html = main.find_all("div", class_="Fw(n) Fz(12px)")
scores_html = main.find_all("span", class_="YahooSans Fw(700)! Va(m) Fz(24px)!")

team_name_str = str(team_name_html)
scores_str = str(scores_html)

# Remove all non-characters in the team name and scores list
team_names = re.findall(r'>(.*?)<', team_name_str)
scores = re.findall(r'>(.*?)<', scores_str)

# This is only used if a shootout occurs
final_scores = []
inside_parentheses = False
for s in scores:
    if s == '(':
        inside_parentheses = True
    elif s == ')':
        inside_parentheses = False
    elif not inside_parentheses:
        final_scores.append(s)

# Remove blank list elements
team_names_cleaned = [word for word in team_names if any (char.isalpha() for char in word)]
scores_cleaned = [num for num in final_scores if num.isdigit()]

# Ensure both lists are the same length
if len(team_names_cleaned) != len(scores_cleaned):
    raise ValueError("The number of team names and scores must be the same.")

#Identify a winner for each game
winners = []
for i in range(0, len(team_names_cleaned), 2):
    team1 = team_names_cleaned[i]
    team2 = team_names_cleaned[i+1]
    score1 = scores_cleaned[i]
    score2 = scores_cleaned[i+1]

    if score1 > score2:
        winners.append(team1)
    elif score2 > score1:
        winners.append(team2)

print(winners)

#Get associated ticker for each winner
winning_tickers = []
for i in winners:
    winning_tickers.append(team_tickers[i])

BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = 'https://paper-api.alpaca.markets/v2/account'
ORDERS_URL = 'https://paper-api.alpaca.markets/v2/orders'
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY }

def getAccount():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    
    return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)

    return json.loads(r.content)

print(winning_tickers)
for i in winning_tickers:
    #create_order(i, 1, "buy", "market", "gtc")
    print("Sending buy order for: " + i)
