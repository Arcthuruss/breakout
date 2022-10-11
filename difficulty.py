import classes

difficulty = "Normal" # Set as none by default ?
lives = 3 # Set as ? By default ?

match difficulty:
    case "Easy":
        lives = 5
        print("👽")
    case "Normal":
        lives = 3
        print("😐")
    case "Hard":
        lives = 1
        print("🗿")
    case "Lunatic":
        lives = 1
        print("Foolishness")