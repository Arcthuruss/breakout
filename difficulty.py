import menu
difficulty = menu.difficulty # Set as none by default ?
lives = 3 # Normal settings by default
speed = 60 # ""      ""     ""    ""
music_timer = 0
match difficulty:
	case "Easy":
		lives = 5
		speed = 30
		print("👽")
	case "Normal":
		lives = 3
		speed = 60
		print("😐")
	case "Hard":
		lives = 1
		speed = 120
		print("🗿")
	case "Lunatic":
		music_timer = 100
		lives = 1
		speed = 240
		print("Foolishness")