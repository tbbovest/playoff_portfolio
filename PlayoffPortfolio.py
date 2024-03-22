from bs4 import BeautifulSoup
import requests
import re

url = "https://sports.yahoo.com/nhl/scoreboard/?confId=&schedState=2&dateRange=2024-03-17"
page = requests.get(url)
main = BeautifulSoup(page.content, 'html.parser')

team_tickers = {
    ""
}

team_name_html = main.find_all("div", class_="Fw(n) Fz(12px)")
scores_html = main.find_all("span", class_="YahooSans Fw(700)! Va(m) Fz(24px)!")

team_name_str = str(team_name_html)
scores_str = str(scores_html)

team_names = re.findall(r'>(.*?)<', team_name_str)
scores = re.findall(r'>(.*?)<', scores_str)

team_names_cleaned = [word for word in team_names if any (char.isalpha() for char in word)]
scores_cleaned = [num for num in scores if num.isdigit()]

# Ensure both lists are the same length
if len(team_names) != len(scores):
    raise ValueError("The number of team names and scores must be the same.")

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

