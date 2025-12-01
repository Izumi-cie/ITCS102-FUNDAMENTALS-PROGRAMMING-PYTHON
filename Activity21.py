isLove = True

while isLove == True:
    confirm = input("Mahal po pa ba ako? (oo / hindi)-->").lower()

    if confirm == "oo":
        print("Edi masaya ang buhay")
        continue
    elif confirm == "hindi":
        print("Ayos lang, hindi naman masakit:<")
        break
    else:
        print("Pinagsasabi mo?")
        continue