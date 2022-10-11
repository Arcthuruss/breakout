def highscoreWriting(username,highscore):
    if username == None: return "No username was entered, highscore will not be saved"
    else:
        with open("highscores.txt" ,"a") as username:#"a" argument is for append maybe "w" is better ?
            username.write(username,highscore) #Will keep it clear for now need to find reliable way to xor and read