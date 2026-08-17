"""
7.

A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

Tuple Format:

(player_id, player_name, runs_scored)

Requirements:

Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.

Test Case:

Input:

Enter number of players: 5

101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76

Expected Output:

All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)

Highest Scorer:
(103, 'Gill', 120)

Lowest Scorer:
(104, 'Hardik', 38)

Total Runs:
361

Average Runs:
72.2

Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
(103, 'Gill', 120)
(105, 'SKY', 76)
"""
n=int(input("Enter number of players :"))
player=[]
for i in range(n):
    print("Enter details of player",i+1)
    id=int(input("Enter player id:"))
    name=input("Enter playee name :")
    run=int(input("Enter runs :"))
    player.append((id,name,run))
print("=="*20)
print("All playes details ")
low=player[0]
high=player[0]
total=0
more50=[]
for x in player:
    print(x)
    if x[2]>high[2]:
        high=x
    if x[2]<low[2]:
        low=x
    total+=x[2]
    if x[2]>50:
      more50.append(x)
print("=="*20)
print("hightest scorer :")
print(high)
print("=="*20)
print("lowest scorer :")
print(low)
print("=="*20)
print("Total runs :")
print(total)
print("=="*20)
print("average run")
print(total/n)
print("=="*20)
print("players coring more than 50")
for x in more50:
  print(x)