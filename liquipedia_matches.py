import csv
import requests
from bs4 import BeautifulSoup

url = "https://liquipedia.net/counterstrike/Liquipedia:Matches"

headers = {"User-Agent": "Mozilla/5.0"}

respuesta = requests.get(url, headers=headers)

soup = BeautifulSoup(respuesta.text, "html.parser")

teamleft = soup.findAll("td",{"class":"team-left"})

teams1 = []

for teams in teamleft:
    teamsLeftName = teams.find("span", {"data-highlightingclass": True})
    if teamsLeftName:
        teams1.append(teamsLeftName.text.strip())

team_right = soup.findAll("td",{"class":"team-right"})

teams2 = []

for teamsr in team_right:
    teamsRightName = teamsr.find("span", {"data-highlightingclass": True})
    if teamsRightName:
        teams2.append(teamsRightName.text.strip())

campeonatos = soup.findAll("div",{"class":"text-nowrap"})

copas = []

for campeonato in campeonatos:
    camp_name = campeonato.find("a",{"href":True,"title":True})
    if camp_name:
        copas.append(camp_name.text.strip())



enlaces = soup.findAll("div",{"class":"text-nowrap"})     

enlace = []

for urls in enlaces:
    urltrip = urls.find("a",{"href":True})
    if urltrip:
        href = urltrip["href"]
        full_url = "https://liquipedia.net" + href
        enlace.append(full_url)
        
numero_matches = min(len(teamleft),len(team_right),len(copas))
        
with open("matches.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["team left", "team right", "campeonatos", "urls"])
    
    for i in range(numero_matches):
        writer.writerow([teams1[i],teams2[i],copas[i],enlace[i]])
        
print("datos guardados")
      
