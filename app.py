from player import Player
from playerdata import PlayerData
from rank import Rank
from stage import Stage
import json

# Create the game.

# init screen
stage = Stage()
stage.screen.title("Save Me If You Can")
stage.init_screen()
name = stage.screen.textinput(title="Player name", prompt="Enter your name: ")
data = PlayerData("data")

# Check specified name.
with open("data.json", "r") as f:
    name_data = json.load(f)

while name in name_data:
    check = stage.screen.textinput(title="Player name already exists",
                                   prompt="Record new score or try another name? (Start/New): ")
    if check.lower() == "start":
        player = Player(name, data)
        break
    elif check.lower() == "new":
        new_name = stage.screen.textinput(title="Player name", prompt="Enter your name: ")
        player = Player(new_name, data)
        break

player = Player(name, data)
rank = Rank()
start = False
if name:
    start = True

# Start the game.
while start:
    sort_rank = rank.player_rank()
    stage.init_screen()
    stage.add_coin()
    stage.check_collision(player)
    if player.lives <= -1:
        start = False
        stage.painter.goto(0, 200)
        stage.painter.write("GAME OVER", font=("VT323", 50, "normal"), move=True, align="center")

        n = 1
        x, y = 0, 100
        while n <= 3:
            stage.painter.goto(x, y)
            for name in sort_rank[f"Rank{n}"][0]["name"]:
                stage.painter.write(f"#Rank{n}# {name} collect: {sort_rank[f'Rank{n}'][1]['score']} $ ",
                                    font=("VT323", 25, "normal"), move=True, align="center")
                y -= 30
            n += 1
        stage.painter.goto(0, -75)
        stage.painter.write(f"Your Rank!", font=("VT323", 25, "normal"), move=True, align="center")
        stage.painter.goto(0, -100)
        stage.painter.write(f"#{rank.find_rank(player.player_name)}# {player.player_name} collect: {player.score} $",
                            font=("VT323", 25, "normal"), move=True, align="center")

stage.screen.exitonclick()
stage.screen.mainloop()