import time
import random


def text_pause(text):
    print(text)
    time.sleep(2)


allTeams = ["Team1", "Team2", "Team3", "Team4", "Team5"]

team1Score = random.randrange(0, 100)
team2Score = random.randrange(0, 100)
team3Score = random.randrange(0, 100)
team4Score = random.randrange(0, 100)
team5Score = random.randrange(0, 100)

team1Check = int()
team1Type = "abc"
team1Names = []

allCompetitions = []


def team2_get_info():
    text_pause("Team 2 Printed")


def team1_get_info():
    text_pause("Welcome our events")
    text_pause("Teams can be single or team of five people")

    global allCompetitions
    allCompetitions = ["MAth", "Physics", "Programming", "Networking", "Help_deck"]

    print("\n The competition that can be joined are:", allCompetitions)

    global team1Type
    team1Type = input("\n Team 1 are 'team = t' or single 'person = p' ?")
    while team1Type != 't' and team1Type != 'p':
        team1Type = input("\n You can only choose 't for team' or single 'p = person'.")

    global team1Names
    team1Names = []
    if team1Type == "p":
        text_pause('Team1 is a person')
        team1Names = input("Please enter your name")
    elif team1Type == "t":
        text_pause('Team1 is a team')
        team1Names = input("Please enter all five name, separate by commas or spaces..")
    print("team names are", team1Names)

    global team1Check
    team1Check = int(input("Are we okay to continue '1', or '2' to make changes"))
    while team1Check != 1 and team1Check != 2:
        text_pause("Sorry you enter invalid value")
        team1Check = int(input("Press '1' to continue or '2' to change"))
    if team1Check == 2:
        team1_get_info()
    elif team1Check == 1:
        team2_get_info()


team1_get_info()

print("Team 1 Check Value:", team1Check)
time.sleep(2)
print("Team 1 Type Value:", team1Type)
time.sleep(2)
print("Team 1 Names Value:", team1Names)
time.sleep(2)
print("Number Of Events:", len(allCompetitions))
time.sleep(2)
print(allCompetitions)

############################################

event1choice = random.randrange(0, len(allCompetitions))
print(event1choice)
time.sleep(2)
print("Event 1 is:", allCompetitions[event1choice])
time.sleep(2)
del allCompetitions[event1choice]

print("All Teams", allCompetitions)
time.sleep(2)
random.shuffle(allCompetitions)
print("All Teams", allCompetitions)
time.sleep(2)

print("Team1 Score:", team1Score)
time.sleep(2)
print("Team2 Score:", team2Score)
time.sleep(2)
print("Team3 Score:", team3Score)
time.sleep(2)
print("Team4 Score:", team4Score)
time.sleep(2)
print("Team5 Score:", team5Score)
time.sleep(2)

text_pause(allCompetitions)
print("Number of events:", len(allCompetitions))
