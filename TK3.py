import sys

# Membuat fungsi untuk membaca input dari user
def input_reader():
    return map(str.strip, input().splitlines())

# 1. Membuat fungsi untuk memainkan level
def play_level(level, word, answers):
    score = 0
    print(f"\n=== Level {level} ===")
    print(" ".join(word).center(50, " "))

    try:
        pool_answer = []
        remaining_trials = 10  # menambahkan variable untuk melacak sisa kesempatan

        while remaining_trials > 0:  # loop sampai kesempatan habis
            answer = input(f"{11-remaining_trials}> Your Answer : ").strip()
            if len(answer) < 3 or len(answer) > 6:
                print("Input min 3 characters and max 6 character.")
            elif answer == word.replace(" ", ""):
                print("You may not use all the characters that have been given.")
            elif answer in pool_answer:
                print("You should not use the same answer as before.")
            else:
                remaining_trials -= 1  # mengurangi kesempatan setiap input yang valid
                if answer in answers:
                    pool_answer.append(answer)
                    score += 10
                    print(f"#Right. Score : {score}")

            # menambahkan kondisi untuk menampilkan jawaban yang benar
            if score >= 70 and remaining_trials == 0:
                print(f"\nYou had answered 10 times with {len(pool_answer)} right answers..")
                print("Correct Answers:")
                for i, answer in enumerate(answers):
                    if i % 10 == 0:
                        print("\n", end="")
                    print(answer.ljust(8), end="")
                return score

            elif score < 70 and remaining_trials == 0:
                print("\nYou had answered 10 times with", len(pool_answer), "right answers..")
                retry = input("Do you want to try again [y/n]? ").strip().lower() # menambahkan pilihan untuk mencoba lagi
                if retry == "y":
                    return play_level(level, word, answers) # memanggil kembali fungsi play_level untuk mencoba lagi
                else:
                    return 0
        return score

    # menambahkan exception untuk menghentikan program
    except KeyboardInterrupt:
        print("Program terminated.")
        sys.exit()
        

# 2. Membuat fungsi untuk memainkan level
def puzzle_game():
    print("Coepoe Word Puzzle")
    print("===================")
    print("\nRules :")
    print("1. Create a word using given characters, min 3 characters & max 6 characters.")
    print("2. Each Level, you have 10 chances to answer correctly.")
    print("3. To get through to the next level, you have to score 70 points each level.")

    # 3. Membuat data level
    level_data = [
        {"word": " d    e   t   t   l   i ", "answers": ["die", "led", "lei", "let", "lid", "lie", "lit", "tie", "deli", "diet", "edit", "idle", "lied", "tide", "tied", "tile", "tilt", "tilde", "tiled", "title", "tilted", "titled"]},
        {"word": " s    e   c   a   e   n ", "answers": ["sec", "can", "cane", "scan", "scene", "case", "cease", "see", "sea", "seen", "sac"]},
        {"word": " h    k   r   n   e   o ", "answers": ["honk", "honker", "roe", "ore", "her", "hen", "one", "neo", "krone", "hoe", "hone"]}
    ]

    final_score = 0

    # 4. Membuat loop untuk memainkan level
    for level, level_info in enumerate(level_data, start=1):
        score = play_level(level, level_info["word"], level_info["answers"])
        final_score += score

        if score < 70:
            print("You failed to complete this level.")
            break

        if final_score >= level * 70:
            print(f"\nCongratulations, you have completed level {level}!")
        else:
            print(f"Your current score: {final_score}")
            retry = input("Do you want to retry [y/n]? ").strip().lower()
            if retry == "n":
                print("Game Over")
                return
            final_score = 0

    print("\nOverall Score = ", final_score)
    if final_score >= 210:
        print("\nYou Win!!")
    else:
        print("\nYou Lose..")
    print("\nPress ENTER to exit..")
    input()

# 5. Memanggil fungsi puzzle_game
if __name__ == "__main__":
    puzzle_game()
