import random, time

playlist = "Rock Paper Scissors".split()

def playerinput():
    print()
    print(playlist)
    while True:
        pl = int(input("Enter The number of your choice : "))
        if pl > len(playlist) or pl<0:
            continue
        else:
            break
    return playlist[pl-1]


def winner(player1,player2):
    if player1==player2:
        return None
    
    if (player1=="Rock" and player2=="Scissors") or (player1=="Paper" and player2=="Rock") or (player1=="Scissors" and player2=="Rock"):
        return 1
    else:
        return 2
def play():
    while True:
        player = playerinput()
        computer = playlist[random.randint(0,len(playlist)-1)]
        winnerp = winner(player,computer)
        if winner!=None:
            break
    time.sleep(1)
    print()
    print(f"PLAYER ==> {player} COMPUTER ==> {computer}")
    if winnerp == 1:
        print("PLAYER WIN")
    else:
        print("COMPUTER WIN")
    

play()


   
   
