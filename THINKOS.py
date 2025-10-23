import os
import time
import datetime
import json
import random
from pathlib import Path


class ThinkOS:
    def __init__(self):
        self.current_user = None
        self.user_files = {}
        self.password = "CHANGEME"  # Change this to your desired password
        self.data_file = "think_os_data.json"
        self.game_stats = {}
        self.load_data()

    def load_data(self):
        """Load saved user files from disk"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.user_files = data.get('user_files', {})
                    self.game_stats = data.get('game_stats', {
                        'tic_tac_toe': {'wins': 0, 'losses': 0, 'draws': 0},
                        'chess': {'games_played': 0},
                        'monopoly': {'games_played': 0, 'money_record': 0},
                        'oregon_trail': {'games_completed': 0, 'best_score': 0}
                    })
        except:
            self.user_files = {}
            self.game_stats = {
                'tic_tac_toe': {'wins': 0, 'losses': 0, 'draws': 0},
                'chess': {'games_played': 0},
                'monopoly': {'games_played': 0, 'money_record': 0},
                'oregon_trail': {'games_completed': 0, 'best_score': 0}
            }

    def save_data(self):
        """Save user files to disk"""
        try:
            data = {
                'user_files': self.user_files,
                'game_stats': self.game_stats
            }
            with open(self.data_file, 'w') as f:
                json.dump(data, f)
        except:
            pass

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def boot_screen(self):
        """Main login screen"""
        while True:
            self.clear_screen()
            print("=" * 50)
            print("        THINK OS - BOOT SEQUENCE")
            print("=" * 50)
            print()
            password = input("Password: ")

            if password == self.password:
                self.current_user = "Admin"
                self.desktop()
                break
            else:
                self.boot_screen_two()

    def boot_screen_two(self):
        """Screen shown after wrong password"""
        self.clear_screen()
        print("~That was the wrong password~")
        print()
        print("1) Admin Login!")
        print("2) Guest login!")
        print()

        choice = input("Select option: ")

        if choice == "1":
            return  # Return to boot_screen
        elif choice == "2":
            self.current_user = "guest"
            self.ltd_desktop()

    def desktop(self):
        """Main desktop for admin users"""
        while True:
            self.clear_screen()
            print("=" * 50)
            print("████████╗██╗░░██╗██╗███╗░░██╗██╗░░██╗░░░░░░░█████╗░░██████╗")
            print("╚══██╔══╝██║░░██║██║████╗░██║██║░██╔╝░░░░░░██╔══██╗██╔════╝")
            print("░░░██║░░░███████║██║██╔██╗██║█████═╝░█████╗██║░░██║╚█████╗░")
            print("░░░██║░░░██╔══██║██║██║╚████║██╔═██╗░╚════╝██║░░██║░╚═══██╗")
            print("░░░██║░░░██║░░██║██║██║░╚███║██║░╚██╗░░░░░░╚█████╔╝██████╔╝")
            print("░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░░░░░░░╚════╝░╚═════╝░")
            print("                          1.0.9                            ")
            print("=" * 50 )
            print()
            print("Welcome to THINK OS 1.0! <c> HBREW Inc.")
            print()
            print("=" * 50)
            print(f"Date: {datetime.date.today()}")
            print(f"Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
            print()
            print("1) Write text file      2) Documents...")
            print("3) Calculator...        4) Games...")
            print("5) Terminal...          6)System Info..")
            print("             7) Logout")
            print("=" * 50) 
            print()

            choice = input("Select option: ")

            if choice == "1":
                self.write_application()
            elif choice == "2":
                self.browse_documents()
            elif choice == "3":
                self.calculator()
            elif choice == "4":
                self.games_folder()
            elif choice == "5":
                self.terminal_ide()
            elif choice == "6":  # Update other numbers accordingly
                self.system_info()
            elif choice == "7":
                self.logout()
                break
                

    def games_folder(self):
        """Games folder menu"""
        while True:
            self.clear_screen()
            print("=" * 50)
            print("        THINK OS - GAMES FOLDER")
            print("=" * 50)
            print()
            print("🎮 Welcome to the Games Collection! 🎮")
            print()
            print("Available Games:")
            print("1) Tic Tac Toe")
            print("2) Chess")
            print("3) Monopoly")
            print("4) The Oregon Trail")
            print("5) Game Statistics")
            print("6) Back to Desktop")
            print()

            choice = input("Select game: ")

            if choice == "1":
                self.tic_tac_toe()
            elif choice == "2":
                self.chess()
            elif choice == "3":
                self.monopoly()
            elif choice == "4":
                self.oregon_trail()
            elif choice == "5":
                self.game_statistics()
            elif choice == "6":
                break

    def tic_tac_toe(self):
        """Tic Tac Toe game"""
        self.clear_screen()
        print("=" * 50)
        print("        TIC TAC TOE")
        print("=" * 50)
        print()

        # Initialize board
        board = [' ' for _ in range(9)]
        player = 'X'
        computer = 'O'

        def print_board():
            print(f" {board[0]} | {board[1]} | {board[2]} ")
            print("-----------")
            print(f" {board[3]} | {board[4]} | {board[5]} ")
            print("-----------")
            print(f" {board[6]} | {board[7]} | {board[8]} ")
            print()
            print("Positions:")
            print(" 1 | 2 | 3 ")
            print("-----------")
            print(" 4 | 5 | 6 ")
            print("-----------")
            print(" 7 | 8 | 9 ")

        def check_winner():
            win_patterns = [
                [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
                [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
                [0, 4, 8], [2, 4, 6]  # diagonals
            ]

            for pattern in win_patterns:
                if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != ' ':
                    return board[pattern[0]]

            if ' ' not in board:
                return 'Draw'
            return None

        def computer_move():
            available = [i for i, spot in enumerate(board) if spot == ' ']
            return random.choice(available)

        print("You are X, Computer is O")
        print()

        while True:
            self.clear_screen()
            print("=" * 50)
            print("        TIC TAC TOE")
            print("=" * 50)
            print()
            print_board()
            print()

            # Player move
            try:
                move = int(input("Enter position (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] == ' ':
                    board[move] = player
                else:
                    print("Invalid move! Try again.")
                    time.sleep(1)
                    continue
            except ValueError:
                print("Please enter a number!")
                time.sleep(1)
                continue

            # Check if player won
            winner = check_winner()
            if winner:
                self.clear_screen()
                print("=" * 50)
                print("        GAME OVER")
                print("=" * 50)
                print_board()
                print()
                if winner == 'X':
                    print("🎉 You WIN! 🎉")
                    self.game_stats['tic_tac_toe']['wins'] += 1
                elif winner == 'O':
                    print("💻 Computer WINS!")
                    self.game_stats['tic_tac_toe']['losses'] += 1
                else:
                    print("🤝 It's a DRAW!")
                    self.game_stats['tic_tac_toe']['draws'] += 1

                self.save_data()
                input("Press Enter to return to games...")
                break

            # Computer move
            comp_move = computer_move()
            board[comp_move] = computer

            # Check if computer won
            winner = check_winner()
            if winner:
                self.clear_screen()
                print("=" * 50)
                print("        GAME OVER")
                print("=" * 50)
                print_board()
                print()
                if winner == 'X':
                    print("🎉 You WIN! 🎉")
                    self.game_stats['tic_tac_toe']['wins'] += 1
                elif winner == 'O':
                    print("💻 Computer WINS!")
                    self.game_stats['tic_tac_toe']['losses'] += 1
                else:
                    print("🤝 It's a DRAW!")
                    self.game_stats['tic_tac_toe']['draws'] += 1

                self.save_data()
                input("Press Enter to return to games...")
                break

    def chess(self):
        """Simplified Chess game"""
        self.clear_screen()
        print("=" * 50)
        print("        CHESS")
        print("=" * 50)
        print()

        # Initialize chess board
        board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

        def print_board():
            print("   a b c d e f g h")
            for i, row in enumerate(board):
                print(f"{8 - i}  {' '.join(row)}")
            print()
            print("Uppercase = Your pieces")
            print("Lowercase = Computer pieces")
            print("Legend: K/k=King, Q/q=Queen, R/r=Rook")
            print("        B/b=Bishop, N/n=Knight, P/p=Pawn")

        moves_made = 0

        while moves_made < 10:  # Simplified game - 10 moves each
            self.clear_screen()
            print("=" * 50)
            print("        CHESS")
            print("=" * 50)
            print()
            print_board()
            print()
            print(f"Move {moves_made + 1}/10")
            print()

            # Player move
            move = input("Enter your move (e.g., 'e2 e4') or 'quit': ")
            if move.lower() == 'quit':
                break

            print("Move processed! Computer is thinking...")
            time.sleep(2)

            # Simple computer move simulation
            print("Computer moves a piece...")
            moves_made += 1

        self.clear_screen()
        print("=" * 50)
        print("        CHESS GAME FINISHED")
        print("=" * 50)
        print()
        print("Thanks for playing chess!")
        print("This is a simplified version.")
        print()
        self.game_stats['chess']['games_played'] += 1
        self.save_data()
        input("Press Enter to return to games...")

    def monopoly(self):
        """Simplified Monopoly game"""
        self.clear_screen()
        print("=" * 50)
        print("        MONOPOLY")
        print("=" * 50)
        print()

        properties = [
            "GO", "Mediterranean Ave", "Community Chest", "Baltic Ave",
            "Income Tax", "Reading Railroad", "Oriental Ave", "Chance",
            "Vermont Ave", "Connecticut Ave", "Jail", "St. Charles Place",
            "Electric Company", "States Ave", "Virginia Ave", "Pennsylvania Railroad",
            "St. James Place", "Community Chest", "Tennessee Ave", "New York Ave",
            "Free Parking", "Kentucky Ave", "Chance", "Indiana Ave",
            "Illinois Ave", "B&O Railroad", "Atlantic Ave", "Ventnor Ave",
            "Water Works", "Marvin Gardens", "Go To Jail", "Pacific Ave",
            "North Carolina Ave", "Community Chest", "Pennsylvania Ave", "Short Line",
            "Chance", "Park Place", "Luxury Tax", "Boardwalk"
        ]

        player_money = 1500
        player_position = 0
        computer_money = 1500
        computer_position = 0

        print("🏠 Welcome to Monopoly! 🏠")
        print(f"You start with ${player_money}")
        print()
        input("Press Enter to start the game...")

        for turn in range(20):  # 20 turns simplified game
            self.clear_screen()
            print("=" * 50)
            print(f"        MONOPOLY - TURN {turn + 1}")
            print("=" * 50)
            print()
            print(f"💰 Your money: ${player_money}")
            print(f"📍 Your position: {properties[player_position]}")
            print()

            input("Press Enter to roll dice...")

            # Player turn
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            roll = dice1 + dice2

            print(f"🎲 You rolled: {dice1} + {dice2} = {roll}")

            player_position = (player_position + roll) % len(properties)
            current_property = properties[player_position]

            print(f"📍 You landed on: {current_property}")

            # Simple money transactions
            if "Ave" in current_property or "Place" in current_property:
                cost = random.randint(50, 200)
                print(f"💸 Pay rent: ${cost}")
                player_money -= cost
            elif current_property == "GO":
                print("💰 Collect $200 for passing GO!")
                player_money += 200
            elif "Railroad" in current_property:
                cost = 200
                print(f"🚂 Railroad rent: ${cost}")
                player_money -= cost

            print(f"💰 Your money: ${player_money}")

            if player_money <= 0:
                print("💸 You're bankrupt! Game Over!")
                break

            time.sleep(3)

            # Computer turn (simplified)
            comp_roll = random.randint(2, 12)
            computer_position = (computer_position + comp_roll) % len(properties)
            computer_money += random.randint(-100, 150)

        self.clear_screen()
        print("=" * 50)
        print("        MONOPOLY GAME FINISHED")
        print("=" * 50)
        print()
        print(f"Final Money: ${player_money}")

        if player_money > self.game_stats['monopoly']['money_record']:
            print("🏆 NEW MONEY RECORD! 🏆")
            self.game_stats['monopoly']['money_record'] = player_money

        self.game_stats['monopoly']['games_played'] += 1
        self.save_data()
        print()
        input("Press Enter to return to games...")

    def oregon_trail(self):
        """The Oregon Trail game - faithful recreation"""
        import random

        # Game state variables
        money = 0
        oxen = 0
        food = 0
        ammunition = 0
        clothing = 0
        miscellaneous = 0

        # Party members
        party_names = []
        party_health = []

        # Game progress
        miles_traveled = 0
        total_miles = 2040  # Miles from Independence to Oregon
        current_date = [3, 1, 1848]  # March 1, 1848
        weather = "fair"

        # Landmarks
        landmarks = [
            (102, "Kansas River crossing"),
            (185, "Big Blue River crossing"),
            (304, "Fort Kearney"),
            (555, "Chimney Rock"),
            (635, "Fort Laramie"),
            (725, "Independence Rock"),
            (987, "South Pass"),
            (1067, "Green River crossing"),
            (1155, "Fort Bridger"),
            (1395, "Soda Springs"),
            (1505, "Fort Hall"),
            (1675, "Snake River crossing"),
            (1722, "Fort Boise"),
            (1869, "Blue Mountains"),
            (1950, "The Dalles"),
            (2040, "Oregon City - You made it!")
        ]

        # Profession selection
        self.clear_screen()
        print("=" * 60)
        print("        THE OREGON TRAIL")
        print("=" * 60)
        print()
        print("Many kinds of people made the trip to Oregon.")
        print()
        print("You may:")
        print("1. Be a banker from Boston")
        print("2. Be a carpenter from Ohio")
        print("3. Be a farmer from Illinois")
        print("4. Find out the differences between these choices")
        print("5. Ask for advice")
        print()

        while True:
            choice = input("What is your choice? ")
            if choice == "1":
                money = 1600
                profession = "banker"
                difficulty_multiplier = 1.0
                break
            elif choice == "2":
                money = 2500
                profession = "carpenter"
                difficulty_multiplier = 1.3
                break
            elif choice == "3":
                money = 2500
                profession = "farmer"
                difficulty_multiplier = 1.6
                break
            elif choice == "4":
                print("\nTraveling to Oregon isn't easy! But if you're a")
                print("banker, you'll have more money for supplies")
                print("and services than a carpenter or a farmer.")
                print("\nHowever, the harder you have it, the more")
                print("points you deserve! Farmers get 3 times the")
                print("points that bankers get.")
                print()
            elif choice == "5":
                print("\nDon't spend all your money before leaving")
                print("Independence. You need to save money to buy")
                print("supplies along the way.")
                print()
            else:
                print("That isn't a choice.")

        # Get party member names
        self.clear_screen()
        print("=" * 60)
        print("        THE OREGON TRAIL")
        print("=" * 60)
        print()
        print("What are the names of the four other members")
        print("in your party?")
        print()

        for i in range(4):
            name = input(f"What is the name of the {i + 1}. person? ")
            party_names.append(name.strip())
            party_health.append("Good")

        # Shopping in Independence
        self.clear_screen()
        print("=" * 60)
        print("        INDEPENDENCE GENERAL STORE")
        print("=" * 60)
        print()
        print("Before leaving Independence you should buy")
        print("equipment and supplies. You have $" + str(money))
        print("for the trip.")
        print()

        while True:
            print("=" * 40)
            print("Matt's General Store")
            print("Independence, Missouri")
            print(f"March 1, 1848")
            print("=" * 40)
            print()
            print("1. Oxen                   $200-300 each")
            print("2. Food                   $0.20 per pound")
            print("3. Ammunition             $2.00 per box")
            print("4. Clothing               $10.00 per set")
            print("5. Miscellaneous supplies $5.00 per part")
            print("6. Review purchases")
            print("7. Leave store")
            print()
            print(f"Amount you have: ${money}")
            print()

            choice = input("Which item would you like to buy? ")

            if choice == "1":  # Oxen
                print("\nThere are 2 oxen in a yoke; I recommend at")
                print("least 3 yoke. I charge $200-300 per ox.")
                while True:
                    try:
                        num_oxen = int(input("How many oxen? "))
                        cost = num_oxen * random.randint(200, 300)
                        if cost <= money:
                            money -= cost
                            oxen += num_oxen
                            print(f"You bought {num_oxen} oxen for ${cost}")
                            break
                        else:
                            print("You don't have enough money.")
                            break
                    except ValueError:
                        print("Please enter a number.")

            elif choice == "2":  # Food
                print("\nI recommend you take at least 200 pounds of")
                print("food for each person in your family. I sell")
                print("food for 20 cents a pound.")
                while True:
                    try:
                        pounds = int(input("How many pounds of food? "))
                        cost = int(pounds * 0.20)
                        if cost <= money:
                            money -= cost
                            food += pounds
                            print(f"You bought {pounds} pounds of food for ${cost}")
                            break
                        else:
                            print("You don't have enough money.")
                            break
                    except ValueError:
                        print("Please enter a number.")

            elif choice == "3":  # Ammunition
                print("\nI sell ammunition in boxes of 20 bullets.")
                print("Each box costs $2.00.")
                while True:
                    try:
                        boxes = int(input("How many boxes? "))
                        cost = boxes * 2
                        if cost <= money:
                            money -= cost
                            ammunition += boxes * 20
                            print(f"You bought {boxes} boxes for ${cost}")
                            break
                        else:
                            print("You don't have enough money.")
                            break
                    except ValueError:
                        print("Please enter a number.")

            elif choice == "4":  # Clothing
                print("\nYou'll need warm clothing in the mountains.")
                print("I recommend taking at least 2 sets of clothes")
                print("per person. Each set is $10.00.")
                while True:
                    try:
                        sets = int(input("How many sets? "))
                        cost = sets * 10
                        if cost <= money:
                            money -= cost
                            clothing += sets
                            print(f"You bought {sets} sets of clothing for ${cost}")
                            break
                        else:
                            print("You don't have enough money.")
                            break
                    except ValueError:
                        print("Please enter a number.")

            elif choice == "5":  # Miscellaneous
                print("\nMiscellaneous supplies include such things as")
                print("medicine, bandages, soap, cookware, etc.")
                print("Everything is $5 per part.")
                while True:
                    try:
                        parts = int(input("How many parts? "))
                        cost = parts * 5
                        if cost <= money:
                            money -= cost
                            miscellaneous += parts
                            print(f"You bought {parts} parts for ${cost}")
                            break
                        else:
                            print("You don't have enough money.")
                            break
                    except ValueError:
                        print("Please enter a number.")

            elif choice == "6":  # Review
                print("\n" + "=" * 40)
                print("YOUR PURCHASES:")
                print(f"Oxen: {oxen}")
                print(f"Food: {food} pounds")
                print(f"Ammunition: {ammunition} bullets")
                print(f"Clothing: {clothing} sets")
                print(f"Miscellaneous: {miscellaneous} parts")
                print(f"Money left: ${money}")
                print("=" * 40)
                input("\nPress Enter to continue...")

            elif choice == "7":  # Leave
                if oxen < 6:
                    print("\nYou should have at least 6 oxen to pull")
                    print("your wagon.")
                    continue
                break

            self.clear_screen()
            print("=" * 60)
            print("        INDEPENDENCE GENERAL STORE")
            print("=" * 60)
            print()

        # Main game loop
        days_traveled = 0

        def advance_date(days):
            current_date[1] += days
            if current_date[1] > 30:
                current_date[0] += current_date[1] // 30
                current_date[1] = current_date[1] % 30
                if current_date[0] > 12:
                    current_date[2] += 1
                    current_date[0] = 1

        def get_date_string():
            months = ["", "January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"]
            return f"{months[current_date[0]]} {current_date[1]}, {current_date[2]}"

        def check_landmarks():
            for mile, landmark in landmarks:
                if miles_traveled >= mile and miles_traveled - 15 < mile:
                    return landmark
            return None

        def random_event():
            events = [
                ("wagon_break", 0.1),
                ("illness", 0.08),
                ("bad_weather", 0.15),
                ("thief", 0.05),
                ("injured", 0.06),
                ("lost", 0.04),
                ("find_food", 0.03),
                ("indian_help", 0.02)
            ]

            if random.random() < 0.4:  # 40% chance of event
                event_type = random.choices([e[0] for e in events],
                                            weights=[e[1] for e in events])[0]
                return event_type
            return None

        # Main travel loop
        while miles_traveled < total_miles:
            landmark = check_landmarks()

            self.clear_screen()
            print("=" * 60)
            print("        THE OREGON TRAIL")
            print("=" * 60)
            print()
            print(get_date_string())
            print(f"Weather: {weather}")
            print(f"Health: Good")  # Simplified for this version
            print(f"Food: {food} pounds")
            print(f"Bullets: {ammunition}")
            print(f"Clothing: {clothing}")
            print(f"Money: ${money}")
            print()
            print(f"Miles traveled: {miles_traveled}")
            print(f"Miles to Oregon: {total_miles - miles_traveled}")
            print()

            if landmark:
                print(f"🏛️  You have reached: {landmark}")
                print()

            print("You may:")
            print("1. Continue on trail")
            print("2. Rest")
            print("3. Trade")
            print("4. Hunt")
            print("5. Buy supplies")
            print("6. Check map")
            print()

            choice = input("What is your choice? ")

            if choice == "1":  # Continue
                # Travel for the day
                if oxen <= 0:
                    print("You cannot continue without oxen!")
                    input("Press Enter to continue...")
                    continue

                miles_today = random.randint(12, 25)
                miles_traveled += miles_today
                food -= 8  # Food consumption per day
                days_traveled += 1
                advance_date(1)

                # Weather changes
                weather_options = ["fair", "rainy", "cloudy", "hot", "cold"]
                weather = random.choice(weather_options)

                # Random events
                event = random_event()
                if event == "wagon_break":
                    print("\nYour wagon axle broke!")
                    if miscellaneous > 0:
                        print("You use spare parts to fix it.")
                        miscellaneous -= 1
                    else:
                        print("You have no spare parts. You lose 3 days.")
                        advance_date(3)
                    input("Press Enter to continue...")

                elif event == "illness":
                    sick_person = random.choice(party_names)
                    print(f"\n{sick_person} has become ill!")
                    if miscellaneous > 0:
                        print("You use medicine to help them recover.")
                        miscellaneous -= 1
                    else:
                        print("You have no medicine. They will recover slowly.")
                        advance_date(2)
                    input("Press Enter to continue...")

                elif event == "bad_weather":
                    if weather == "rainy":
                        print("\nHeavy rains! You lose a day waiting for weather to clear.")
                        advance_date(1)
                    elif weather == "cold":
                        print("\nVery cold weather! You use extra clothing.")
                        if clothing > 0:
                            clothing -= 1
                    input("Press Enter to continue...")

                elif event == "thief":
                    stolen = random.randint(10, 50)
                    if food >= stolen:
                        food -= stolen
                        print(f"\nThieves stole {stolen} pounds of food!")
                    else:
                        print("\nThieves tried to steal food but you had none!")
                    input("Press Enter to continue...")

                elif event == "find_food":
                    found = random.randint(20, 80)
                    food += found
                    print(f"\nYou found {found} pounds of wild food!")
                    input("Press Enter to continue...")

                if food <= 0:
                    print("\nYou are out of food! Your party is starving!")
                    # In original game, party members would die
                    print("You must hunt or buy food immediately!")
                    input("Press Enter to continue...")

            elif choice == "2":  # Rest
                print("\nHow many days would you like to rest?")
                try:
                    rest_days = int(input("Days: "))
                    if rest_days > 0:
                        advance_date(rest_days)
                        food -= rest_days * 8
                        print(f"You rested for {rest_days} days.")
                        print("Your party's health improves.")
                        input("Press Enter to continue...")
                except ValueError:
                    print("Please enter a number.")

            elif choice == "3":  # Trade
                print("\nYou meet another wagon train.")
                print("They are willing to trade.")
                print()
                print("1. Trade food for ammunition")
                print("2. Trade ammunition for food")
                print("3. Trade clothing for food")
                print("4. Don't trade")

                trade_choice = input("Your choice: ")
                if trade_choice == "1" and food >= 50:
                    food -= 50
                    ammunition += 25
                    print("You traded 50 pounds of food for 25 bullets.")
                elif trade_choice == "2" and ammunition >= 25:
                    ammunition -= 25
                    food += 30
                    print("You traded 25 bullets for 30 pounds of food.")
                elif trade_choice == "3" and clothing >= 2:
                    clothing -= 2
                    food += 40
                    print("You traded 2 sets of clothing for 40 pounds of food.")
                input("Press Enter to continue...")

            elif choice == "4":  # Hunt
                if ammunition <= 0:
                    print("You have no ammunition for hunting!")
                    input("Press Enter to continue...")
                    continue

                print("\nYou go hunting...")
                print("Type BANG when you see an animal!")
                print()

                # Simple hunting mini-game
                animals = ["rabbit", "deer", "buffalo", "squirrel"]
                animal = random.choice(animals)

                print(f"You see a {animal}!")
                hunt_input = input("Type BANG: ").upper()

                if hunt_input == "BANG":
                    success = random.random() < 0.7  # 70% success rate
                    if success:
                        if animal == "buffalo":
                            meat = random.randint(200, 400)
                        elif animal == "deer":
                            meat = random.randint(100, 200)
                        else:
                            meat = random.randint(50, 100)

                        food += meat
                        ammunition -= 10
                        print(f"You shot the {animal}!")
                        print(f"You got {meat} pounds of meat!")
                    else:
                        ammunition -= 5
                        print("You missed!")
                else:
                    print("You were too slow!")

                input("Press Enter to continue...")

            elif choice == "5":  # Buy supplies (at landmarks)
                if landmark and "Fort" in landmark:
                    print(f"\n{landmark} - Trading Post")
                    print("1. Food - $0.50 per pound")
                    print("2. Ammunition - $3.00 per box")
                    print("3. Clothing - $15.00 per set")
                    print("4. Don't buy anything")

                    buy_choice = input("What would you like to buy? ")
                    if buy_choice == "1":
                        try:
                            pounds = int(input("Pounds of food: "))
                            cost = int(pounds * 0.5)
                            if cost <= money:
                                money -= cost
                                food += pounds
                                print(f"You bought {pounds} pounds of food.")
                        except ValueError:
                            pass
                    elif buy_choice == "2":
                        try:
                            boxes = int(input("Boxes of ammunition: "))
                            cost = boxes * 3
                            if cost <= money:
                                money -= cost
                                ammunition += boxes * 20
                                print(f"You bought {boxes} boxes of ammunition.")
                        except ValueError:
                            pass
                else:
                    print("There are no trading posts here.")
                input("Press Enter to continue...")

            elif choice == "6":  # Check map
                print("\n" + "=" * 50)
                print("MAP OF THE OREGON TRAIL")
                print("=" * 50)
                progress = int((miles_traveled / total_miles) * 40)
                map_line = "Independence" + "-" * progress + "*" + "-" * (40 - progress) + "Oregon"
                print(map_line)
                print(f"\nYou are {miles_traveled} miles from Independence")
                print(f"You have {total_miles - miles_traveled} miles to go")
                print("\nLandmarks:")
                for mile, name in landmarks:
                    if mile <= miles_traveled + 100:
                        status = "PASSED" if mile <= miles_traveled else f"{mile - miles_traveled} miles ahead"
                        print(f"{name}: {status}")
                input("\nPress Enter to continue...")

            # Check for game over conditions
            if miles_traveled >= total_miles:
                break

        # End game
        self.clear_screen()
        print("=" * 60)
        print("        CONGRATULATIONS!")
        print("=" * 60)
        print()
        print("🎉 You have successfully reached Oregon City! 🎉")
        print()
        print(f"You traveled {miles_traveled} miles in {days_traveled} days.")
        print(f"You arrived on {get_date_string()}")
        print()
        print("Final supplies:")
        print(f"Food: {food} pounds")
        print(f"Ammunition: {ammunition} bullets")
        print(f"Clothing: {clothing} sets")
        print(f"Money: ${money}")
        print()

        # Calculate score (like original game)
        points = 0
        if profession == "banker":
            points = miles_traveled * 1
        elif profession == "carpenter":
            points = miles_traveled * 2
        else:  # farmer
            points = miles_traveled * 3

        print(f"Your score as a {profession}: {points} points")
        print()
        print("Thanks for playing The Oregon Trail!")
        print()

        # Update game stats
        if 'oregon_trail' not in self.game_stats:
            self.game_stats['oregon_trail'] = {'games_completed': 0, 'best_score': 0}

        self.game_stats['oregon_trail']['games_completed'] += 1
        if points > self.game_stats['oregon_trail']['best_score']:
            self.game_stats['oregon_trail']['best_score'] = points

        self.save_data()
        input("Press Enter to return to games...")

    def game_statistics(self):
        """Display game statistics"""
        self.clear_screen()
        print("=" * 50)
        print("        GAME STATISTICS")
        print("=" * 50)
        print()

        print("🎯 Tic Tac Toe:")
        print(f"   Wins: {self.game_stats['tic_tac_toe']['wins']}")
        print(f"   Losses: {self.game_stats['tic_tac_toe']['losses']}")
        print(f"   Draws: {self.game_stats['tic_tac_toe']['draws']}")
        print()

        print("♟️  Chess:")
        print(f"   Games Played: {self.game_stats['chess']['games_played']}")
        print()

        print("🏠 Monopoly:")
        print(f"   Games Played: {self.game_stats['monopoly']['games_played']}")
        print(f"   Money Record: ${self.game_stats['monopoly']['money_record']}")
        print()

        print("🚂 The Oregon Trail:")
        print(f"   Games Completed: {self.game_stats.get('oregon_trail', {}).get('games_completed', 0)}")
        print(f"   Best Score: {self.game_stats.get('oregon_trail', {}).get('best_score', 0)}")
        print()

        input("Press Enter to return to games...")


    def write_application(self):
        """Text file creation application"""
        self.clear_screen()
        print("=" * 50)
        print("        THINK OS - WRITE APPLICATION")
        print("=" * 50)
        print()
        print("Welcome to Write, an application which lets you write text files...")
        print()

        filename = input("What will be the name of your text file? ")

        self.clear_screen()
        print(f"Creating file: {filename}")
        print("File created successfully!")
        print()
        input("Press Enter to continue...")

        self.clear_screen()
        print(f"Editing: {filename}")
        print("Enter your text (type 'SAVE' on a new line to finish):")
        print()

        content = []
        while True:
            line = input()
            if line.upper() == "SAVE":
                break
            content.append(line)

        # Save the file
        self.user_files[filename] = "\n".join(content)
        self.save_data()

        print()
        print("File saved successfully!")
        print("Redirecting to desktop...")
        time.sleep(2)

    def browse_documents(self):
        """Browse saved documents"""
        while True:
            self.clear_screen()
            print("=" * 50)
            print("        THINK OS - DOCUMENTS")
            print("=" * 50)
            print()

            if not self.user_files:
                print("No documents found. Create some files first!")
                print()
                input("Press Enter to return to desktop...")
                break

            print("Available documents:")
            file_list = list(self.user_files.keys())
            for i, filename in enumerate(file_list, 1):
                print(f"{i}) {filename}")

            print(f"{len(file_list) + 1}) Back to desktop")
            print()

            choice = input("Select document: ")

            try:
                choice_num = int(choice)
                if choice_num == len(file_list) + 1:
                    break
                elif 1 <= choice_num <= len(file_list):
                    selected_file = file_list[choice_num - 1]
                    self.view_document(selected_file)
                else:
                    print("Invalid choice!")
                    time.sleep(1)
            except ValueError:
                print("Please enter a number!")
                time.sleep(1)

    def view_document(self, filename):
        """View a specific document"""
        self.clear_screen()
        print("=" * 50)
        print(f"        VIEWING: {filename}")
        print("=" * 50)
        print()
        print(self.user_files[filename])
        print()
        input("Press Enter to return to documents...")

    def calculator(self):
        """Simple calculator application"""
        self.clear_screen()
        print("=" * 50)
        print("        THINK OS - CALCULATOR")
        print("=" * 50)
        print()
        print("Enter a mathematical expression:")
        print("(Examples: 2+2, 10*5, 100/4)")
        print()

        expression = input("Expression: ")

        try:
            # Safely evaluate mathematical expressions
            result = eval(expression, {"__builtins__": {}})
            print()
            print(f"Result: {result}")
        except:
            print()
            print("Error: Invalid expression!")

        print()
        input("Press Enter to return to desktop...")

    def system_info(self):
        """Display system information"""
        self.clear_screen()
        print("=" * 50)
        print("        THINK OS - SYSTEM INFO")
        print("=" * 50)
        print()
        print("  +==========================================+\n");
        print("  |                                          |\n");
        print("  |            T H I N K   O S               |\n");
        print("  |                                          |\n");
        print("  |              Version 1.0                 |\n");
        print("  |            (C) HBREW Inc.                |\n");
        print("  |                                          |\n");
        print("  +==========================================+\n\n");
        print()
        print(f"Operating System: Think OS v1.0")
        print(f"<c> HBREW INC.")
        print(f"User: {self.current_user}")
        print(f"Current Date: {datetime.date.today()}")
        print(f"Current Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
        print(f"Total Documents: {len(self.user_files)}")
        print(f"Version: 1.0.7 Python Port")
        print()
        input("Press Enter to return to desktop...")

    def ltd_desktop(self):
        """Limited desktop for guest users"""
        while True:
            self.clear_screen()
            print("=" * 50)
            print("        THINK OS - GUEST MODE")
            print("=" * 50)
            print()
            print("Hello there, you are logged in as a guest.")
            print("You do not have permission to create or browse through text files...")
            print()
            print("You can use the standard tools such as:")
            print("The calculator, clock, and games!")
            print()
            print("Have fun!")
            print()
            input("Press Enter to continue...")

            self.clear_screen()
            print("=" * 50)
            print("        GUEST MENU")
            print("=" * 50)
            print()
            print("1) Calculator!")
            print("2) Clock")
            print("3) Games...")
            print("4) Logout")
            print()

            choice = input("Select option: ")

            if choice == "1":
                self.ltd_calculator()
            elif choice == "2":
                self.clock()
            elif choice == "3":
                self.games_folder()
            elif choice == "4":
                self.logout()
                break

    def ltd_calculator(self):
        """Limited calculator for guest users"""
        self.calculator()  # Same as regular calculator

    def clock(self):
        """Display current date and time"""
        self.clear_screen()
        print("=" * 50)
        print("        THINK OS - CLOCK")
        print("=" * 50)
        print()
        print(f"Current Date: {datetime.date.today()}")
        print(f"Current Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
        print()
        input("Press Enter to return...")

    def logout(self):
        """Logout current user"""
        self.clear_screen()
        print("Logging out...")
        time.sleep(1)
        self.current_user = None

    def run(self):
        """Main run loop"""
        while True:
            self.boot_screen()

    def terminal_ide(self):
        """Terminal application"""
        current_program = []
        current_line = 10
        variables = {}

        self.clear_screen()
        print("=" * 60)
        print("        THINK OS - TERMINAL")
        print("=" * 60)
        print()
        print("THINK OS TERMINAL V1.0")
        print("<c> HBREW Inc. All rights reserved.")
        print("READY")
        print()
        print("Type HELP for available commands")
        print()

        while True:
            command = input("] ").strip().upper()

            if not command:
                continue

            # Split command and arguments
            parts = command.split()
            cmd = parts[0] if parts else ""
            args = parts[1:] if len(parts) > 1 else []

            if cmd == "HELP":
                print()
                print("AVAILABLE COMMANDS:")
                print("LIST - Display current program")
                print("RUN - Execute current program")
                print("NEW - Clear current program")
                print("LOAD [filename] - Load a program")
                print("SAVE [filename] - Save current program")
                print("AUTO [line] - Set auto line numbering")
                print("RENUM - Renumber program lines")
                print("DELETE [line] - Delete a line")
                print("CATALOG - Show saved programs")
                print("HOME - Clear screen")
                print("POKE [address] [value] - Set memory value")
                print("PEEK [address] - Read memory value")
                print("PRINT [expression] - Print value")
                print("HELLO - Display greeting")
                print("CALL -151 - Enter monitor mode")
                print("CONT - Continue program")
                print("NEOFETCH - about this system")
                print("EXIT - Return to desktop")
                print()
                print("PROGRAMMING:")
                print("10 PRINT \"HELLO WORLD\"")
                print("20 FOR I=1 TO 10")
                print("30 PRINT I")
                print("40 NEXT I")
                print()

            elif cmd == "LIST":
                if not current_program:
                    print("NO PROGRAM IN MEMORY")
                else:
                    print()
                    for line_num, line_code in sorted(current_program):
                        print(f"{line_num} {line_code}")
                print()

            elif cmd == "RUN":
                if not current_program:
                    print("NO PROGRAM TO RUN")
                    print()
                    continue

                print()
                self.execute_basic_program(current_program, variables)
                print()
                print("PROGRAM FINISHED")
                print()

            elif cmd == "NEW":
                current_program = []
                variables = {}
                current_line = 10
                print("PROGRAM CLEARED")
                print()

            elif cmd == "LOAD":
                if args:
                    filename = args[0]
                    if filename in self.user_files:
                        # Load program from file
                        content = self.user_files[filename]
                        current_program = []
                        for line in content.split('\n'):
                            if line.strip():
                                try:
                                    parts = line.split(' ', 1)
                                    line_num = int(parts[0])
                                    code = parts[1] if len(parts) > 1 else ""
                                    current_program.append((line_num, code))
                                except:
                                    pass
                        print(f"LOADED: {filename}")
                    else:
                        print(f"FILE NOT FOUND: {filename}")
                else:
                    print("SYNTAX: LOAD [FILENAME]")
                print()

            elif cmd == "SAVE":
                if args and current_program:
                    filename = args[0]
                    # Save program to file
                    content = []
                    for line_num, line_code in sorted(current_program):
                        content.append(f"{line_num} {line_code}")
                    self.user_files[filename] = '\n'.join(content)
                    self.save_data()
                    print(f"SAVED: {filename}")
                elif not current_program:
                    print("NO PROGRAM TO SAVE")
                else:
                    print("SYNTAX: SAVE [FILENAME]")
                print()

            elif cmd == "AUTO":
                if args:
                    try:
                        current_line = int(args[0])
                        print(f"AUTO LINE NUMBERING SET TO {current_line}")
                    except:
                        print("INVALID LINE NUMBER")
                else:
                    current_line = 10
                    print("AUTO LINE NUMBERING SET TO 10")
                print()

            elif cmd == "RENUM":
                if current_program:
                    new_program = []
                    line_num = 10
                    for _, code in sorted(current_program):
                        new_program.append((line_num, code))
                        line_num += 10
                    current_program = new_program
                    print("PROGRAM RENUMBERED")
                else:
                    print("NO PROGRAM TO RENUMBER")
                print()

            elif cmd == "DELETE":
                if args:
                    try:
                        del_line = int(args[0])
                        current_program = [(num, code) for num, code in current_program if num != del_line]
                        print(f"LINE {del_line} DELETED")
                    except:
                        print("INVALID LINE NUMBER")
                else:
                    print("SYNTAX: DELETE [LINE NUMBER]")
                print()

            elif cmd == "CATALOG":
                print()
                print("SAVED PROGRAMS:")
                basic_files = [f for f in self.user_files.keys() if f.upper().endswith('.BAS') or not '.' in f]
                if basic_files:
                    for filename in basic_files:
                        print(f"  {filename}")
                else:
                    print("  NO PROGRAMS SAVED")
                print()

            elif cmd == "HOME":
                self.clear_screen()
                print("SCREEN CLEARED")
                print()

            elif cmd == "POKE":
                if len(args) >= 2:
                    try:
                        address = int(args[0])
                        value = int(args[1])
                        print(f"POKE {address},{value}")
                        # Simulate memory operation
                        if address == 32:  # Text color
                            print("TEXT COLOR CHANGED")
                        elif address == 49200:  # Bell
                            print("BEEP!")
                    except:
                        print("INVALID POKE COMMAND")
                else:
                    print("SYNTAX: POKE [ADDRESS] [VALUE]")
                print()


        


            elif cmd == "NEOFETCH":
                print("                                        ,,╓▄▄██████████████████▄▄,,")
                print("                                   ,▄▄████████████████████████████████▄▄,")
                print("                               ▄▄██████████████████████████████████████████")
                print("                           ,▄██████████████████████████████████████████████████")
                print("                        ,▄█████████████████████████████████████████████████████")
                print("                      ,████████████████████████████████████████████████████████")
                print("                    ╓███████████████████████▀▀▀▀▀▀▀└└└└└╙▀█████████████████████")
                print("                   ███████████████████████▀`                ╙▀█████████████████")
                print("                ,▄███████████████████████╙                      ╙▀█████████████")
                print("        `      █████████████████████████                           ╙██████████▌")
                print("             ,████████████████████████▀                              ▀████████U")
                print("            ▄████████████████████████Ü         ]███`                   ▀██████U")
                print("           ████████████████████████▀            └└                      └▀████U")
                print("          ███████████████████████╜                                         ███U")
                print("         ▄████████████████████▀└                                            ╙█U")
                print("        ▐█████████████████████▄")
                print("       ╓████████████████████████▄")
                print("       ███████████████████████████▄")
                print("      j█████████████████████████████▄")
                print("      ████████████████████████████████▄")              
                print("      ██████████████████████████████████▄,")
                print("     ▐████████████████████████████████████▄")                
                print("     ▐██████████████████████████████████████▄")
                print("     ▐████████████████████████████████████████▄")                
                print("      ██████████████████████████████████████████r")
                print("      j██████████████████████████████████████████")                
                print("       ██████████████████████████████████████████")
                print("        ▀█████████████████████████████████████████")                
                print("         █████████████████████████████████████████")
                print("          ████████████████████████████████████████")
                print("           ████████████████████████████████████████")
                print(f"Operating System: Think OS v1.0.9")
                print(f"<c> HBREW INC.")
                print(f"Programmed By elian")
                print(f"Current Date: {datetime.date.today()}")
                print(f"Current Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
                print(f"Total Documents: {len(self.user_files)}")
                print(f"Version: 1.0.9 Python Port")
                print()
                
                
                
            elif cmd == "PEEK":
                if args:
                    try:
                        address = int(args[0])
                        # Simulate memory read
                        value = random.randint(0, 255)
                        print(f"PEEK({address}) = {value}")
                    except:
                        print("INVALID ADDRESS")
                else:
                    print("SYNTAX: PEEK [ADDRESS]")
                print()

            elif cmd == "PRINT":
                if args:
                    expression = ' '.join(args)
                    # Simple expression evaluator
                    try:
                        if '"' in expression:
                            # String literal
                            result = expression.strip('"')
                        else:
                            # Math expression
                            result = eval(expression, {"__builtins__": {}}, variables)
                        print(result)
                    except:
                        print("SYNTAX ERROR")
                else:
                    print("SYNTAX: PRINT [EXPRESSION]")
                print()

            elif cmd == "HELLO":
                print()
                print("HELLO, WELCOME TO THINK OS TERMINAL")
                print()

            elif command == "CALL -151":
                print()
                print("ENTERING MONITOR MODE...")
                self.monitor_mode()
                print("EXITING MONITOR MODE")
                print()

            elif cmd == "CONT":
                print("PROGRAM CONTINUED")
                print()

            elif cmd == "EXIT":
                break

            # Check if it's a program line (starts with number)
            elif cmd.isdigit():
                try:
                    line_num = int(cmd)
                    line_code = ' '.join(args)

                    if line_code:  # Add or replace line
                        # Remove existing line with same number
                        current_program = [(num, code) for num, code in current_program if num != line_num]
                        # Add new line
                        current_program.append((line_num, line_code))
                        print(f"LINE {line_num} ENTERED")
                    else:  # Delete line
                        current_program = [(num, code) for num, code in current_program if num != line_num]
                        print(f"LINE {line_num} DELETED")

                except:
                    print("SYNTAX ERROR")
                print()

            else:
                print(f"?SYNTAX ERROR: {command}")
                print()

    def execute_basic_program(self, program, variables):
        """Execute a BASIC program"""
        lines = dict(sorted(program))
        line_numbers = sorted(lines.keys())
        current_index = 0
        for_stack = []  # Stack for FOR loops

        while current_index < len(line_numbers):
            line_num = line_numbers[current_index]
            code = lines[line_num].strip()

            if not code:
                current_index += 1
                continue

            # Parse command
            parts = code.split()
            if not parts:
                current_index += 1
                continue

            cmd = parts[0].upper()

            try:
                if cmd == "PRINT":
                    # Handle PRINT statement
                    if len(parts) > 1:
                        content = ' '.join(parts[1:])
                        if content.startswith('"') and content.endswith('"'):
                            print(content[1:-1])
                        else:
                            # Try to evaluate as expression
                            try:
                                result = eval(content, {"__builtins__": {}}, variables)
                                print(result)
                            except:
                                print(content)
                    else:
                        print()

                elif cmd == "LET":
                    # Variable assignment: LET X = 5
                    if "=" in code:
                        var_part, val_part = code.split("=", 1)
                        var_name = var_part.split()[-1].strip()
                        try:
                            value = eval(val_part.strip(), {"__builtins__": {}}, variables)
                            variables[var_name] = value
                        except:
                            pass

                elif cmd == "FOR":
                    # FOR I = 1 TO 10
                    try:
                        parts = code.replace("=", " = ").split()
                        var_name = parts[1]
                        start_val = int(eval(parts[3], {"__builtins__": {}}, variables))
                        end_val = int(eval(parts[5], {"__builtins__": {}}, variables))

                        variables[var_name] = start_val
                        for_stack.append({
                            'var': var_name,
                            'end': end_val,
                            'line_index': current_index
                        })
                    except:
                        pass

                elif cmd == "NEXT":
                    # NEXT I
                    if for_stack:
                        loop_info = for_stack[-1]
                        var_name = loop_info['var']

                        if var_name in variables:
                            variables[var_name] += 1

                            if variables[var_name] <= loop_info['end']:
                                # Continue loop
                                current_index = loop_info['line_index']
                                continue
                            else:
                                # End loop
                                for_stack.pop()

                elif cmd == "GOTO":
                    # GOTO 100
                    if len(parts) > 1:
                        target_line = int(parts[1])
                        if target_line in line_numbers:
                            current_index = line_numbers.index(target_line)
                            continue

                elif cmd == "IF":
                    # IF X > 5 THEN PRINT "BIG"
                    if "THEN" in code.upper():
                        condition_part, then_part = code.upper().split("THEN", 1)
                        condition = condition_part[2:].strip()  # Remove "IF"

                        try:
                            if eval(condition, {"__builtins__": {}}, variables):
                                # Execute THEN part
                                then_command = then_part.strip()
                                if then_command.startswith("GOTO"):
                                    target = int(then_command.split()[1])
                                    if target in line_numbers:
                                        current_index = line_numbers.index(target)
                                        continue
                                elif then_command.startswith("PRINT"):
                                    content = then_command[5:].strip()
                                    if content.startswith('"') and content.endswith('"'):
                                        print(content[1:-1])
                        except:
                            pass

                elif cmd == "INPUT":
                    # INPUT X
                    if len(parts) > 1:
                        var_name = parts[1]
                        try:
                            value = input(f"{var_name}? ")
                            variables[var_name] = float(value) if '.' in value else int(value)
                        except:
                            variables[var_name] = value

                elif cmd == "REM":
                    # Comment - do nothing
                    pass

                elif cmd == "END":
                    break

            except Exception as e:
                print(f"ERROR IN LINE {line_num}: {e}")
                break

            current_index += 1

    def monitor_mode(self):
        """Monitor Mode simulation"""
        print("THINK OS MONITOR")
        print()

        while True:
            command = input("* ").strip().upper()

            if not command:
                continue

            if command in ["G", "CTRL-C"]:
                break
            elif command.startswith("L"):
                print("MEMORY LISTING:")
                for i in range(8):
                    addr = 2048 + i * 8
                    values = [f"{random.randint(0, 255):02X}" for _ in range(8)]
                    print(f"{addr:04X}: {' '.join(values)}")
                print()
            elif command.startswith("D"):
                print("DISASSEMBLY:")
                print("0800: A9 00    LDA #$00")
                print("0802: 8D 00 04 STA $0400")
                print("0805: 60       RTS")
                print()
            elif ":" in command:
                print("MEMORY SET")
                print()
            else:
                print("MONITOR COMMANDS:")
                print("L - List memory")
                print("D - Disassemble")
                print("ADDR:VALUE - Set memory")
                print("G - Go (exit monitor)")
                print()







# Run Think OS
if __name__ == "__main__":
    os_instance = ThinkOS()
    print("Starting Think OS...")
    time.sleep(2)
    os_instance.run()
