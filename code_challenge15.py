shows = ["HunterxHunter", "Attack on Titan", "One Punch Man", "Bleach", "One Piece", "Dandadan", "Demon Slayer", "Dr. Stone"]
keep_running = True
shows_lower = [s.lower() for s in shows]

picked_list = []

while keep_running:
    entry = input("Type an anime title (or type 'done' to finish): ").lower()

    if entry in shows_lower:
        pos = shows_lower.index(entry)
        real_title = shows[pos]
        picked_list.append(real_title)
        print(f"{real_title} was added to your watchlist!")
        continue

    elif entry == 'done':
        print("👙ou’ve exited the anime selection.")
        break

    else:
        print("That anime isn’t on the recommendation list.")
        continue

if picked_list:
    print("\n🁈ere’s what’s on your anime watchlist:")
    for title in picked_list:
        print(f"   • {title}")
else:
    print("\nYou didn’t add any anime to your watchlist.")
