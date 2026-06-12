# ============================================================
#   AI-Based Movie Recommendation System
#   Python for AI & Data Science — Monthly Assessment Project
# ============================================================

# ── Movie Dataset ────────────────────────────────────────────
# Each record: (Movie Name, Genre, Rating, Min Age, Mood Tags)
movies = [
    ("Inception",            "Sci-Fi",   9.0, 13, "mind-bending"),
    ("Interstellar",         "Sci-Fi",   8.6, 13, "adventure"),
    ("The Matrix",           "Sci-Fi",   8.7, 16, "action"),
    ("Avengers: Endgame",    "Action",   8.4, 13, "adventure"),
    ("Spider-Man: No Way Home", "Action",8.3, 10, "fun"),
    ("John Wick",            "Action",   7.4, 18, "intense"),
    ("The Dark Knight",      "Action",   9.0, 13, "intense"),
    ("Toy Story",            "Animation",8.3,  0, "fun"),
    ("The Lion King",        "Animation",8.5,  0, "adventure"),
    ("Coco",                 "Animation",8.4,  0, "emotional"),
    ("The Pursuit of Happyness", "Drama",8.0, 10, "emotional"),
    ("Forrest Gump",         "Drama",    8.8, 13, "inspiring"),
    ("Titanic",              "Romance",  7.9, 13, "emotional"),
    ("La La Land",           "Romance",  8.0, 13, "fun"),
    ("Get Out",              "Horror",   7.7, 18, "intense"),
]

# ── Welcome Interface ────────────────────────────────────────
print("=" * 55)
print("   Welcome to the AI-Based Movie Recommendation System")
print("=" * 55)
print()

# ── User Input ───────────────────────────────────────────────
user_name = input("Enter your name           : ").strip()
user_age  = int(input("Enter your age            : "))

print()
print("Available genres:")
genres = []
for movie in movies:
    if movie[1] not in genres:
        genres.append(movie[1])

for i in range(len(genres)):
    print(f"  {i + 1}. {genres[i]}")

print()
preferred_genre = input("Enter your preferred genre: ").strip().title()

print()
print("Mood options: fun / adventure / intense / emotional / inspiring / mind-bending")
user_mood = input("Enter your mood (optional, press Enter to skip): ").strip().lower()

# ── Recommendation Logic ─────────────────────────────────────
print()
print("=" * 55)
print(f"  🎬  Recommended Movies for {user_name}:")
print("=" * 55)

recommended = []

for movie in movies:
    movie_name   = movie[0]
    movie_genre  = movie[1]
    movie_rating = movie[2]
    movie_min_age = movie[3]
    movie_mood   = movie[4]

    # Condition 1 — filter by age restriction
    if user_age < movie_min_age:
        continue

    # Condition 2 — filter by preferred genre
    if movie_genre != preferred_genre:
        continue

    # Condition 3 — prioritize by rating (only 7.5+)
    if movie_rating < 7.5:
        continue

    # Bonus — mood match boosts priority (added first)
    if user_mood and user_mood in movie_mood:
        recommended.insert(0, (movie_name, movie_rating))
    else:
        recommended.append((movie_name, movie_rating))

# ── Display Recommendations ──────────────────────────────────
if len(recommended) == 0:
    print(f"\n  Sorry, no movies found for genre '{preferred_genre}'")
    print("  Try a different genre or check your age eligibility.")
else:
    # Sort remaining list by rating (highest first)
    for i in range(len(recommended)):
        for j in range(i + 1, len(recommended)):
            if recommended[j][1] > recommended[i][1]:
                recommended[i], recommended[j] = recommended[j], recommended[i]

    count = 0
    for rec in recommended:
        count += 1
        print(f"  {count}. {rec[0]}  (Rating: {rec[1]})")

print()
print(f"  Total recommendations: {len(recommended)}")
print("=" * 55)
print(f"\n  Enjoy your movie, {user_name}! 🍿")
print("=" * 55)
