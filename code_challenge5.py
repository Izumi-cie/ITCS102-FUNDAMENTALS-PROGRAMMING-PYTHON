print("Welcome to Manga Reader Recommender!!")
print("Please answer these questions first")
genre = input("What genre do you want? (action/isekai/romcom/sci-fi)").lower()
duration = input("How long do you want it to be? (short/medium/long)").lower()
year = input("What year is it? (2000s/2010s)")

#Action
if genre == "action":
    if duration == "short":
        if year == "2000s":
            print("These are the manga recommendations:\n1. Rurouni Kenshin \n2. Black Lagoon \n3. Hellsing")
        elif year == "2010s":
            print("These are the manga recommendations:\n1. Dead Tube\n2. Ajin: Demi-Human\n3. Dorohedoro")
    elif duration == "medium":
        if year == "2000s":
            print("These are the manga recommendations:\n1. Katekyo Hitman Reborn!\n2. Hunter x Hunter \n3. Shaman King")
        elif year == "2010s":
            print("These are the manga recommendations:\n1. Kimetsu no Yaiba\n2. One Punch Man\n3. The Promised Neverland")
    elif duration == "long":
        if year == "2000s":
            print("These are the manga recommendations:\n1. One Piece \n2. Dragon Ball \n3. Naruto \n4. Bleach")
        elif year == "2010s":
            print("These are the manga recommendations:\n1. Black Clover \n2. Toriko\n3. The Seven Deadly Sins\n4. Boku no Hero Academia")

#Romcom
elif genre == "romcom":
    if duration == "short":
        if year == "2000s":
            print("These are the manga recommendations:\n1. Ouran High School Host Club\n2. Lovely★Complex\n3. Kare Kano")
        elif year == "2010s":
            print("These are the manga recommendations:\n1. Wotakoi: Love is Hard for Otaku\n2. Aho Girl\n3. Tonikaku Kawaii")
    elif duration == "medium":
        if year == "2000s":
            print("These are the manga recommendations:\n1. Special A\n2. Nodame Cantabile\n3. Skip Beat!")
        elif year == "2010s":
            print("These are the manga recommendations:\n1. Yamada-kun and the Seven Witches\n2. Tonikaku Kawaii\n3. Kimi ni Todoke")
    elif duration == "long":
        if year == "2000s":
            print("These are the manga recommendations:\n1. Kimi ni Todoke\n2. Skip Beat!\n3. Nodame Cantabile")
        elif year == "2010s":
            print("These are the manga recommendations:\n1. Kaguya-sama: Love Is War\n2. Komi Can't Communicate\n3. Nisekoi")

#Isekai
elif genre == "isekai":
    if duration == "short":
        if year == "2000s":
            print("These are the manga recommendations:\n1. Inuyasha\n2. The Twelve Kingdoms\n3. Ascendance of a Bookworm")
        elif year == "2010s":
            print("These are the manga recommendations:\n1. Re:Zero\n2. No Game No Life\n3. Konosuba")
    elif duration == "medium":
        if year == "2000s":
            print("These are the manga recommendations:\n1. .Hack//Sign\n2. Sword Art Online (beginning)\n3. Log Horizon")
        elif year == "2010s":
            print("These are the manga recommendations:\n1. The Rising of the Shield Hero\n2. That Time I Got Reincarnated as a Slime\n3. The Saga of Tanya the Evil")
    elif duration == "long":
        if year == "2000s":
            print("These are the manga recommendations:\n1. The Rising of the Shield Hero\n2. The Twelve Kingdoms\n3. Inuyasha")
        elif year == "2010s":
            print("These are the manga recommendations:\n1. Overlord\n2. That Time I Got Reincarnated as a Slime\n3. The Saga of Tanya the Evil")

#Sci-fi
elif genre == "sci-fi":
    if duration == "short":
        if year == "2000s":
            print("These are the manga recommendations:\n1. Pluto\n2. Ghost in the Shell: The New Movie\n3. Battle Angel Alita")
        elif year == "2010s":
            print("These are the manga recommendations:\n1. Promised Neverland\n2. Blame!\n3. Knights of Sidonia")
    elif duration == "medium":
        if year == "2000s":
            print("These are the manga recommendations:\n1. Neon Genesis Evangelion\n2. Planetes\n3. Space Brothers")
        elif year == "2010s":
            print("These are the manga recommendations:\n1. No. 6\n2. Golden Kamuy\n3. To Your Eternity")
    elif duration == "long":
        if year == "2000s":
            print("These are the manga recommendations:\n1. 20th Century Boys\n2. Nausicaä of the Valley of the Wind\n3. Gunnm (Battle Angel Alita)")
        elif year == "2010s":
            print("These are the manga recommendations:\n1. Attack on Titan\n2. Akira\n3. Ajin: Demi-Human")


else:
    print("Sorry, we couldn't find any recommendations based on your input. Please try again.")






