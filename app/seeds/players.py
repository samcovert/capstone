from app.models import db, Player, environment, SCHEMA
from sqlalchemy.sql import text

def seed_players():
    team1 = [
        {'first_name': 'Keith', 'last_name': 'Tkachuk', 'position': 'C', 'number': 7, 'goals': 52, 'assists': 34, 'points': 86, 'pims': 228, 'plus_minus': -1, 'gp': 81, 'age': 24, 'team_id': 1},
        {'first_name': 'Jeremy', 'last_name': 'Roenick', 'position': 'C', 'number': 97, 'goals': 29, 'assists': 40, 'points': 69, 'pims': 115, 'plus_minus': -7, 'gp': 72, 'age': 27, 'team_id': 1},
        {'first_name': 'Mike', 'last_name': 'Gartner', 'position': 'R', 'number': 22, 'goals': 32, 'assists': 31, 'points': 63, 'pims': 38, 'plus_minus': -11, 'gp': 82, 'age': 37, 'team_id': 1},
        {'first_name': 'Oleg', 'last_name': 'Tverdovsky', 'position': 'D', 'number': 20, 'goals': 10, 'assists': 45, 'points': 55, 'pims': 30, 'plus_minus': -5, 'gp': 82, 'age': 20, 'team_id': 1},
        {'first_name': 'Craig', 'last_name': 'Janney', 'position': 'C', 'number': 15, 'goals': 15, 'assists': 38, 'points': 53, 'pims': 26, 'plus_minus': -1, 'gp': 77, 'age': 29, 'team_id': 1},
        {'first_name': 'Cliff', 'last_name': 'Ronning', 'position': 'C', 'number': 77, 'goals': 19, 'assists': 32, 'points': 51, 'pims': 26, 'plus_minus': -9, 'gp': 69, 'age': 30, 'team_id': 1},
        {'first_name': 'Dallas', 'last_name': 'Drake', 'position': 'R', 'number': 11, 'goals': 17, 'assists': 19, 'points': 36, 'pims': 52, 'plus_minus': -11, 'gp': 63, 'age': 28, 'team_id': 1},
        {'first_name': 'Teppo', 'last_name': 'Numminen', 'position': 'D', 'number': 27, 'goals': 2, 'assists': 25, 'points': 27, 'pims': 28, 'plus_minus': -3, 'gp': 82, 'age': 28, 'team_id': 1},
        {'first_name': 'Darrin', 'last_name': 'Shannon', 'position': 'L', 'number': 34, 'goals': 11, 'assists': 13, 'points': 24, 'pims': 41, 'plus_minus': 4, 'gp': 82, 'age': 27, 'team_id': 1},
        {'first_name': 'Bob', 'last_name': 'Corkum', 'position': 'C', 'number': 21, 'goals': 9, 'assists': 11, 'points': 20, 'pims': 40, 'plus_minus': -7, 'gp': 80, 'age': 29, 'team_id': 1},
        {'first_name': 'Dave', 'last_name': 'Manson', 'position': 'D', 'number': 23, 'goals': 3, 'assists': 17, 'points': 20, 'pims': 164, 'plus_minus': -25, 'gp': 66, 'age': 30, 'team_id': 1},
        {'first_name': 'Mike', 'last_name': 'Stapleton', 'position': 'C', 'number': 14, 'goals': 4, 'assists': 11, 'points': 15, 'pims': 36, 'plus_minus': -4, 'gp': 55, 'age': 30, 'team_id': 1},
        {'first_name': 'Deron', 'last_name': 'Quint', 'position': 'D', 'number': 5, 'goals': 3, 'assists': 11, 'points': 14, 'pims': 4, 'plus_minus': -4, 'gp': 27, 'age': 20, 'team_id': 1},
        {'first_name': 'Kris', 'last_name': 'King', 'position': 'L', 'number': 17, 'goals': 3, 'assists': 11, 'points': 14, 'pims': 185, 'plus_minus': -7, 'gp': 81, 'age': 30, 'team_id': 1},
        {'first_name': 'Norm', 'last_name': 'Maciver', 'position': 'D', 'number': 44, 'goals': 4, 'assists': 9, 'points': 13, 'pims': 24, 'plus_minus': -11, 'gp': 32, 'age': 31, 'team_id': 1},
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 4, 'assists': 8, 'points': 12, 'pims': 49, 'plus_minus': -3, 'gp': 63, 'age': 20, 'team_id': 1},
        {'first_name': 'Igor', 'last_name': 'Korolev', 'position': 'C', 'number': 23, 'goals': 3, 'assists': 7, 'points': 10, 'pims': 28, 'plus_minus': -5, 'gp': 41, 'age': 25, 'team_id': 1},
        {'first_name': 'Jim', 'last_name': 'Johnson', 'position': 'D', 'number': 8, 'goals': 3, 'assists': 7, 'points': 10, 'pims': 74, 'plus_minus': 5, 'gp': 55, 'age': 34, 'team_id': 1},
        {'first_name': 'Jeff', 'last_name': 'Finley', 'position': 'D', 'number': 26, 'goals': 3, 'assists': 7, 'points': 10, 'pims': 40, 'plus_minus': -8, 'gp': 65, 'age': 29, 'team_id': 1},
        {'first_name': 'Jim', 'last_name': 'McKenzie', 'position': 'L', 'number': 33, 'goals': 5, 'assists': 3, 'points': 8, 'pims': 200, 'plus_minus': -5, 'gp': 65, 'age': 27, 'team_id': 1},
        {'first_name': 'Chad', 'last_name': 'Kilger', 'position': 'C', 'number': 18, 'goals': 4, 'assists': 3, 'points': 7, 'pims': 13, 'plus_minus': -5, 'gp': 24, 'age': 19, 'team_id': 1},
        {'first_name': 'Jayson', 'last_name': 'More', 'position': 'D', 'number': 6, 'goals': 1, 'assists': 6, 'points': 7, 'pims': 37, 'plus_minus': 10, 'gp': 23, 'age': 27, 'team_id': 1},
        {'first_name': 'Brad', 'last_name': 'McCrimmon', 'position': 'D', 'number': 10, 'goals': 1, 'assists': 5, 'points': 6, 'pims': 18, 'plus_minus': 2, 'gp': 37, 'age': 37, 'team_id': 1},
        {'first_name': 'Nikolai', 'last_name': 'Khabibulin', 'position': 'G', 'number': 35, 'wins': 30, 'gaa': 2.83, 'svp': .908, 'gp': 72, 'age': 23, 'team_id': 1},
        {'first_name': 'Darcy', 'last_name': 'Wakaluk', 'position': 'G', 'number': 43, 'wins': 8, 'gaa': 2.99, 'svp': .899, 'gp': 16, 'age': 30, 'team_id': 1}
    ]
    team2 = [
        {'first_name': 'Keith', 'last_name': 'Tkachuk', 'position': 'C', 'number': 7, 'goals': 40, 'assists': 26, 'points': 66, 'pims': 147, 'plus_minus': 9, 'gp': 69, 'age': 25, 'team_id': 2},
        {'first_name': 'Jeremy', 'last_name': 'Roenick', 'position': 'C', 'number': 97, 'goals': 24, 'assists': 32, 'points': 56, 'pims': 103, 'plus_minus': 5, 'gp': 79, 'age': 27, 'team_id': 2},
        {'first_name': 'Cliff', 'last_name': 'Ronning', 'position': 'C', 'number': 77, 'goals': 11, 'assists': 44, 'points': 55, 'pims': 36, 'plus_minus': 5, 'gp': 80, 'age': 31, 'team_id': 2},
        {'first_name': 'Craig', 'last_name': 'Janney', 'position': 'C', 'number': 15, 'goals': 10, 'assists': 43, 'points': 53, 'pims': 12, 'plus_minus': 5, 'gp': 68, 'age': 29, 'team_id': 2},
        {'first_name': 'Teppo', 'last_name': 'Numminen', 'position': 'D', 'number': 27, 'goals': 11, 'assists': 40, 'points': 51, 'pims': 30, 'plus_minus': 25, 'gp': 82, 'age': 29, 'team_id': 2},
        {'first_name': 'Rick', 'last_name': 'Tocchet', 'position': 'R', 'number': 92, 'goals': 26, 'assists': 19, 'points': 45, 'pims': 157, 'plus_minus': 1, 'gp': 68, 'age': 33, 'team_id': 2},
        {'first_name': 'Dallas', 'last_name': 'Drake', 'position': 'R', 'number': 11, 'goals': 11, 'assists': 29, 'points': 40, 'pims': 71, 'plus_minus': 17, 'gp': 60, 'age': 28, 'team_id': 2},
        {'first_name': 'Mike', 'last_name': 'Gartner', 'position': 'R', 'number': 22, 'goals': 12, 'assists': 15, 'points': 27, 'pims': 24, 'plus_minus': -4, 'gp': 60, 'age': 37, 'team_id': 2},
        {'first_name': 'Bob', 'last_name': 'Corkum', 'position': 'C', 'number': 21, 'goals': 12, 'assists': 9, 'points': 21, 'pims': 28, 'plus_minus': -7, 'gp': 76, 'age': 29, 'team_id': 2},
        {'first_name': 'Oleg', 'last_name': 'Tverdovsky', 'position': 'D', 'number': 10, 'goals': 7, 'assists': 12, 'points': 19, 'pims': 12, 'plus_minus': 1, 'gp': 46, 'age': 21, 'team_id': 2},
        {'first_name': 'Gerald', 'last_name': 'Diduck', 'position': 'D', 'number': 4, 'goals': 8, 'assists': 10, 'points': 18, 'pims': 118, 'plus_minus': 14, 'gp': 78, 'age': 32, 'team_id': 2},
        {'first_name': 'Brad', 'last_name': 'Isbister', 'position': 'L', 'number': 16, 'goals': 9, 'assists': 8, 'points': 17, 'pims': 102, 'plus_minus': 4, 'gp': 66, 'age': 20, 'team_id': 2},
        {'first_name': 'John', 'last_name': 'Slaney', 'position': 'D', 'number': 26, 'goals': 3, 'assists': 14, 'points': 17, 'pims': 24, 'plus_minus': -3, 'gp': 55, 'age': 25, 'team_id': 2},
        {'first_name': 'Darrin', 'last_name': 'Shannon', 'position': 'L', 'number': 34, 'goals': 2, 'assists': 12, 'points': 14, 'pims': 26, 'plus_minus': 4, 'gp': 58, 'age': 27, 'team_id': 2},
        {'first_name': 'Juha', 'last_name': 'Ylonen', 'position': 'C', 'number': 36, 'goals': 1, 'assists': 11, 'points': 12, 'pims': 10, 'plus_minus': -3, 'gp': 55, 'age': 25, 'team_id': 2},
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 5, 'assists': 6, 'points': 11, 'pims': 35, 'plus_minus': -3, 'gp': 33, 'age': 20, 'team_id': 2},
        {'first_name': 'Deron', 'last_name': 'Quint', 'position': 'D', 'number': 5, 'goals': 4, 'assists': 7, 'points': 11, 'pims': 16, 'plus_minus': -6, 'gp': 32, 'age': 21, 'team_id': 2},
        {'first_name': 'Jayson', 'last_name': 'More', 'position': 'D', 'number': 31, 'goals': 5, 'assists': 5, 'points': 10, 'pims': 53, 'plus_minus': 0, 'gp': 41, 'age': 28, 'team_id': 2},
        {'first_name': 'Mike', 'last_name': 'Stapleton', 'position': 'C', 'number': 14, 'goals': 5, 'assists': 5, 'points': 10, 'pims': 36, 'plus_minus': -4, 'gp': 64, 'age': 31, 'team_id': 2},
        {'first_name': 'Norm', 'last_name': 'Maciver', 'position': 'D', 'number': 44, 'goals': 2, 'assists': 6, 'points': 8, 'pims': 38, 'plus_minus': -11, 'gp': 41, 'age': 32, 'team_id': 2},
        {'first_name': 'Jim', 'last_name': 'McKenzie', 'position': 'L', 'number': 33, 'goals': 3, 'assists': 4, 'points': 7, 'pims': 146, 'plus_minus': -7, 'gp': 64, 'age': 27, 'team_id': 2},
        {'first_name': 'Keith', 'last_name': 'Carney', 'position': 'D', 'number': 3, 'goals': 1, 'assists': 6, 'points': 7, 'pims': 18, 'plus_minus': 5, 'gp': 20, 'age': 27, 'team_id': 2},
        {'first_name': 'Michel', 'last_name': 'Petit', 'position': 'D', 'number': 24, 'goals': 4, 'assists': 2, 'points': 6, 'pims': 77, 'plus_minus': -4, 'gp': 32, 'age': 33, 'team_id': 2},
        {'first_name': 'Nikolai', 'last_name': 'Khabibulin', 'position': 'G', 'number': 35, 'wins': 30, 'gaa': 2.74, 'svp': .900, 'gp': 70, 'age': 24, 'team_id': 2},
        {'first_name': 'Jimmy', 'last_name': 'Waite', 'position': 'G', 'number': 28, 'wins': 5, 'gaa': 2.12, 'svp': .913, 'gp': 17, 'age': 30, 'team_id': 2}
    ]
    team3 = [
        {'first_name': 'Keith', 'last_name': 'Tkachuk', 'position': 'C', 'number': 7, 'goals': 36, 'assists': 26, 'points': 62, 'pims': 133, 'plus_minus': 6, 'gp': 78, 'age': 26, 'team_id': 3},
        {'first_name': 'Jeremy', 'last_name': 'Roenick', 'position': 'C', 'number': 97, 'goals': 24, 'assists': 48, 'points': 72, 'pims': 117, 'plus_minus': 10, 'gp': 80, 'age': 28, 'team_id': 3},
        {'first_name': 'Greg', 'last_name': 'Adams', 'position': 'L', 'number': 17, 'goals': 19, 'assists': 24, 'points': 43, 'pims': 26, 'plus_minus': -1, 'gp': 75, 'age': 35, 'team_id': 3},
        {'first_name': 'Teppo', 'last_name': 'Numminen', 'position': 'D', 'number': 27, 'goals': 10, 'assists': 30, 'points': 40, 'pims': 30, 'plus_minus': 3, 'gp': 82, 'age': 30, 'team_id': 3},
        {'first_name': 'Dallas', 'last_name': 'Drake', 'position': 'R', 'number': 11, 'goals': 9, 'assists': 22, 'points': 31, 'pims': 65, 'plus_minus': 17, 'gp': 53, 'age': 29, 'team_id': 3},
        {'first_name': 'Jyrki', 'last_name': 'Lumme', 'position': 'D', 'number': 20, 'goals': 7, 'assists': 21, 'points': 28, 'pims': 34, 'plus_minus': 5, 'gp': 60, 'age': 32, 'team_id': 3},
        {'first_name': 'Oleg', 'last_name': 'Tverdovsky', 'position': 'D', 'number': 10, 'goals': 7, 'assists': 18, 'points': 25, 'pims': 32, 'plus_minus': 11, 'gp': 82, 'age': 22, 'team_id': 3},
        {'first_name': 'Juha', 'last_name': 'Ylonen', 'position': 'C', 'number': 36, 'goals': 6, 'assists': 17, 'points': 23, 'pims': 20, 'plus_minus': 18, 'gp': 59, 'age': 26, 'team_id': 3},
        {'first_name': 'Daniel', 'last_name': 'Briere', 'position': 'C', 'number': 8, 'goals': 8, 'assists': 14, 'points': 22, 'pims': 30, 'plus_minus': -3, 'gp': 64, 'age': 20, 'team_id': 3},
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 6, 'assists': 16, 'points': 22, 'pims': 54, 'plus_minus': -5, 'gp': 79, 'age': 21, 'team_id': 3},
        {'first_name': 'Bob', 'last_name': 'Corkum', 'position': 'C', 'number': 21, 'goals': 9, 'assists': 10, 'points': 19, 'pims': 17, 'plus_minus': -9, 'gp': 77, 'age': 30, 'team_id': 3},
        {'first_name': 'Mike', 'last_name': 'Stapleton', 'position': 'C', 'number': 14, 'goals': 9, 'assists': 9, 'points': 18, 'pims': 34, 'plus_minus': -6, 'gp': 76, 'age': 32, 'team_id': 3},
        {'first_name': 'Keith', 'last_name': 'Carney', 'position': 'D', 'number': 3, 'goals': 2, 'assists': 14, 'points': 16, 'pims': 62, 'plus_minus': 15, 'gp': 82, 'age': 28, 'team_id': 3},
        {'first_name': 'Robert', 'last_name': 'Reichel', 'position': 'C', 'number': 16, 'goals': 7, 'assists': 6, 'points': 13, 'pims': 4, 'plus_minus': 2, 'gp': 13, 'age': 27, 'team_id': 3},
        {'first_name': 'Deron', 'last_name': 'Quint', 'position': 'D', 'number': 5, 'goals': 5, 'assists': 8, 'points': 13, 'pims': 20, 'plus_minus': -10, 'gp': 60, 'age': 22, 'team_id': 3},
        {'first_name': 'Brad', 'last_name': 'Isbister', 'position': 'L', 'number': 30, 'goals': 4, 'assists': 4, 'points': 8, 'pims': 46, 'plus_minus': 1, 'gp': 32, 'age': 21, 'team_id': 3},
        {'first_name': 'Jim', 'last_name': 'Cummins', 'position': 'R', 'number': 15, 'goals': 1, 'assists': 7, 'points': 8, 'pims': 190, 'plus_minus': 3, 'gp': 55, 'age': 28, 'team_id': 3},
        {'first_name': 'Cliff', 'last_name': 'Ronning', 'position': 'C', 'number': 32, 'goals': 2, 'assists': 5, 'points': 7, 'pims': 2, 'plus_minus': 3, 'gp': 7, 'age': 32, 'team_id': 3},
        {'first_name': 'J.J.', 'last_name': 'Daigneault', 'position': 'D', 'number': 33, 'goals': 0, 'assists': 7, 'points': 7, 'pims': 32, 'plus_minus': -8, 'gp': 35, 'age': 32, 'team_id': 3},
        {'first_name': 'Mike', 'last_name': 'Sullivan', 'position': 'C', 'number': 26, 'goals': 2, 'assists': 4, 'points': 6, 'pims': 24, 'plus_minus': -11, 'gp': 63, 'age': 30, 'team_id': 3},
        {'first_name': 'Trevor', 'last_name': 'Letowski', 'position': 'C', 'number': 50, 'goals': 2, 'assists': 2, 'points': 4, 'pims': 2, 'plus_minus': 1, 'gp': 14, 'age': 21, 'team_id': 3},
        {'first_name': 'Tavis', 'last_name': 'Hansen', 'position': 'R', 'number': 47, 'goals': 2, 'assists': 1, 'points': 3, 'pims': 12, 'plus_minus': -4, 'gp': 20, 'age': 23, 'team_id': 3},
        {'first_name': 'Rob', 'last_name': 'Murray', 'position': 'C', 'number': 12, 'goals': 1, 'assists': 2, 'points': 3, 'pims': 4, 'plus_minus': 2, 'gp': 13, 'age': 31, 'team_id': 3},
        {'first_name': 'Steve', 'last_name': 'Leach', 'position': 'R', 'number': 23, 'goals': 1, 'assists': 1, 'points': 2, 'pims': 37, 'plus_minus': -6, 'gp': 22, 'age': 32, 'team_id': 3},
        {'first_name': 'Nikolai', 'last_name': 'Khabibulin', 'position': 'G', 'number': 35, 'wins': 32, 'gaa': 2.13, 'svp': .923, 'gp': 63, 'age': 25, 'team_id': 3},
        {'first_name': 'Jimmy', 'last_name': 'Waite', 'position': 'G', 'number': 28, 'wins': 6, 'gaa': 2.74, 'svp': .895, 'gp': 16, 'age': 31, 'team_id': 3}
    ]
    team4 = [
        {'first_name': 'Jeremy', 'last_name': 'Roenick', 'position': 'C', 'number': 97, 'goals': 34, 'assists': 44, 'points': 78, 'pims': 102, 'plus_minus': 11, 'gp': 75, 'age': 29, 'team_id': 4},
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 26, 'assists': 25, 'points': 51, 'pims': 66, 'plus_minus': 6, 'gp': 81, 'age': 22, 'team_id': 4},
        {'first_name': 'Travis', 'last_name': 'Green', 'position': 'C', 'number': 39, 'goals': 25, 'assists': 21, 'points': 46, 'pims': 45, 'plus_minus': -4, 'gp': 78, 'age': 28, 'team_id': 4},
        {'first_name': 'Greg', 'last_name': 'Adams', 'position': 'L', 'number': 17, 'goals': 19, 'assists': 27, 'points': 46, 'pims': 14, 'plus_minus': -1, 'gp': 69, 'age': 36, 'team_id': 4},
        {'first_name': 'Dallas', 'last_name': 'Drake', 'position': 'R', 'number': 11, 'goals': 15, 'assists': 30, 'points': 45, 'pims': 62, 'plus_minus': 11, 'gp': 79, 'age': 30, 'team_id': 4},
        {'first_name': 'Keith', 'last_name': 'Tkachuk', 'position': 'C', 'number': 7, 'goals': 22, 'assists': 21, 'points': 43, 'pims': 82, 'plus_minus': 7, 'gp': 50, 'age': 27, 'team_id': 4},
        {'first_name': 'Teppo', 'last_name': 'Numminen', 'position': 'D', 'number': 27, 'goals': 8, 'assists': 34, 'points': 42, 'pims': 16, 'plus_minus': 21, 'gp': 79, 'age': 31, 'team_id': 4},
        {'first_name': 'Jyrki', 'last_name': 'Lumme', 'position': 'D', 'number': 21, 'goals': 8, 'assists': 32, 'points': 40, 'pims': 44, 'plus_minus': 9, 'gp': 74, 'age': 33, 'team_id': 4},
        {'first_name': 'Trevor', 'last_name': 'Letowski', 'position': 'C', 'number': 10, 'goals': 19, 'assists': 20, 'points': 39, 'pims': 20, 'plus_minus': 2, 'gp': 82, 'age': 22, 'team_id': 4},
        {'first_name': 'Rick', 'last_name': 'Tocchet', 'position': 'R', 'number': 22, 'goals': 12, 'assists': 17, 'points': 29, 'pims': 67, 'plus_minus': -5, 'gp': 64, 'age': 35, 'team_id': 4},
        {'first_name': 'Juha', 'last_name': 'Ylonen', 'position': 'C', 'number': 36, 'goals': 6, 'assists': 23, 'points': 29, 'pims': 12, 'plus_minus': -6, 'gp': 76, 'age': 27, 'team_id': 4},
        {'first_name': 'Mika', 'last_name': 'Alatalo', 'position': 'L', 'number': 18, 'goals': 10, 'assists': 17, 'points': 27, 'pims': 36, 'plus_minus': -3, 'gp': 82, 'age': 28, 'team_id': 4},
        {'first_name': 'Keith', 'last_name': 'Carney', 'position': 'D', 'number': 3, 'goals': 4, 'assists': 20, 'points': 24, 'pims': 87, 'plus_minus': 11, 'gp': 82, 'age': 29, 'team_id': 4},
        {'first_name': 'Mike', 'last_name': 'Sullivan', 'position': 'C', 'number': 26, 'goals': 5, 'assists': 10, 'points': 15, 'pims': 10, 'plus_minus': -4, 'gp': 79, 'age': 31, 'team_id': 4},
        {'first_name': 'Benoit', 'last_name': 'Hogue', 'position': 'L', 'number': 12, 'goals': 3, 'assists': 10, 'points': 13, 'pims': 10, 'plus_minus': -1, 'gp': 27, 'age': 32, 'team_id': 4},
        {'first_name': 'Deron', 'last_name': 'Quint', 'position': 'D', 'number': 5, 'goals': 3, 'assists': 7, 'points': 10, 'pims': 22, 'plus_minus': 0, 'gp': 50, 'age': 23, 'team_id': 4},
        {'first_name': 'Stanislav', 'last_name': 'Neckar', 'position': 'D', 'number': 24, 'goals': 2, 'assists': 8, 'points': 10, 'pims': 36, 'plus_minus': 1, 'gp': 66, 'age': 23, 'team_id': 4},
        {'first_name': 'Lyle', 'last_name': 'Odelein', 'position': 'D', 'number': 4, 'goals': 1, 'assists': 7, 'points': 8, 'pims': 19, 'plus_minus': 1, 'gp': 16, 'age': 31, 'team_id': 4},
        {'first_name': 'Louie', 'last_name': 'DeBrusk', 'position': 'L', 'number': 29, 'goals': 4, 'assists': 3, 'points': 7, 'pims': 78, 'plus_minus': 1, 'gp': 61, 'age': 28, 'team_id': 4},
        {'first_name': 'Todd', 'last_name': 'Gill', 'position': 'D', 'number': 23, 'goals': 1, 'assists': 6, 'points': 7, 'pims': 30, 'plus_minus': -10, 'gp': 41, 'age': 33, 'team_id': 4},
        {'first_name': 'J.J.', 'last_name': 'Daigneault', 'position': 'D', 'number': 33, 'goals': 1, 'assists': 6, 'points': 7, 'pims': 22, 'plus_minus': -17, 'gp': 53, 'age': 33, 'team_id': 4},
        {'first_name': 'Mikael', 'last_name': 'Renberg', 'position': 'R', 'number': 20, 'goals': 2, 'assists': 4, 'points': 6, 'pims': 2, 'plus_minus': 0, 'gp': 10, 'age': 27, 'team_id': 4},
        {'first_name': 'Radoslav', 'last_name': 'Suchy', 'position': 'D', 'number': 15, 'goals': 0, 'assists': 6, 'points': 6, 'pims': 16, 'plus_minus': 2, 'gp': 60, 'age': 23, 'team_id': 4},
        {'first_name': 'Daniel', 'last_name': 'Briere', 'position': 'C', 'number': 8, 'goals': 1, 'assists': 1, 'points': 2, 'pims': 0, 'plus_minus': 0, 'gp': 13, 'age': 21, 'team_id': 4},
        {'first_name': 'Sean', 'last_name': 'Burke', 'position': 'G', 'number': 1, 'wins': 17, 'gaa': 2.55, 'svp': .914, 'gp': 35, 'age': 32, 'team_id': 4},
        {'first_name': 'Bob', 'last_name': 'Essensa', 'position': 'G', 'number': 31, 'wins': 13, 'gaa': 2.78, 'svp': .898, 'gp': 30, 'age': 34, 'team_id': 4},
        {'first_name': 'Mikhail', 'last_name': 'Shtalenkov', 'position': 'G', 'number': 30, 'wins': 7, 'gaa': 2.39, 'svp': .903, 'gp': 15, 'age': 33, 'team_id': 4},
    ]
    team5 = [
        {'first_name': 'Jeremy', 'last_name': 'Roenick', 'position': 'C', 'number': 97, 'goals': 30, 'assists': 46, 'points': 76, 'pims': 114, 'plus_minus': -1, 'gp': 80, 'age': 30, 'team_id': 5},
        {'first_name': 'Keith', 'last_name': 'Tkachuk', 'position': 'C', 'number': 15, 'goals': 29, 'assists': 42, 'points': 71, 'pims': 108, 'plus_minus': 6, 'gp': 64, 'age': 28, 'team_id': 5},
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 26, 'assists': 37, 'points': 63, 'pims': 89, 'plus_minus': 0, 'gp': 76, 'age': 23, 'team_id': 5},
        {'first_name': 'Joe', 'last_name': 'Juneau', 'position': 'C', 'number': 90, 'goals': 10, 'assists': 23, 'points': 33, 'pims': 28, 'plus_minus': -2, 'gp': 69, 'age': 32, 'team_id': 5},
        {'first_name': 'Landon', 'last_name': 'Wilson', 'position': 'R', 'number': 28, 'goals': 18, 'assists': 13, 'points': 31, 'pims': 92, 'plus_minus': 3, 'gp': 70, 'age': 25, 'team_id': 5},
        {'first_name': 'Teppo', 'last_name': 'Numminen', 'position': 'D', 'number': 27, 'goals': 5, 'assists': 26, 'points': 31, 'pims': 36, 'plus_minus': 9, 'gp': 72, 'age': 32, 'team_id': 5},
        {'first_name': 'Travis', 'last_name': 'Green', 'position': 'C', 'number': 39, 'goals': 13, 'assists': 15, 'points': 28, 'pims': 63, 'plus_minus': -11, 'gp': 69, 'age': 29, 'team_id': 5},
        {'first_name': 'Claude', 'last_name': 'Lemieux', 'position': 'R', 'number': 22, 'goals': 10, 'assists': 16, 'points': 26, 'pims': 58, 'plus_minus': 1, 'gp': 46, 'age': 35, 'team_id': 5},
        {'first_name': 'Brad', 'last_name': 'May', 'position': 'L', 'number': 32, 'goals': 11, 'assists': 14, 'points': 25, 'pims': 107, 'plus_minus': 10, 'gp': 62, 'age': 28, 'team_id': 5},
        {'first_name': 'Jyrki', 'last_name': 'Lumme', 'position': 'D', 'number': 21, 'goals': 4, 'assists': 21, 'points': 25, 'pims': 44, 'plus_minus': 3, 'gp': 58, 'age': 34, 'team_id': 5},
        {'first_name': 'Juha', 'last_name': 'Ylonen', 'position': 'C', 'number': 36, 'goals': 9, 'assists': 14, 'points': 23, 'pims': 38, 'plus_minus': 10, 'gp': 69, 'age': 28, 'team_id': 5},
        {'first_name': 'Trevor', 'last_name': 'Letowski', 'position': 'C', 'number': 10, 'goals': 7, 'assists': 15, 'points': 22, 'pims': 32, 'plus_minus': -2, 'gp': 77, 'age': 23, 'team_id': 5},
        {'first_name': 'Mika', 'last_name': 'Alatalo', 'position': 'L', 'number': 18, 'goals': 7, 'assists': 12, 'points': 19, 'pims': 22, 'plus_minus': 1, 'gp': 70, 'age': 29, 'team_id': 5},
        {'first_name': 'Ossi', 'last_name': 'Vaananen', 'position': 'D', 'number': 4, 'goals': 4, 'assists': 12, 'points': 16, 'pims': 90, 'plus_minus': 9, 'gp': 81, 'age': 20, 'team_id': 5},
        {'first_name': 'Keith', 'last_name': 'Carney', 'position': 'D', 'number': 3, 'goals': 2, 'assists': 14, 'points': 16, 'pims': 86, 'plus_minus': 15, 'gp': 82, 'age': 30, 'team_id': 5},
        {'first_name': 'Daniel', 'last_name': 'Briere', 'position': 'C', 'number': 8, 'goals': 11, 'assists': 4, 'points': 15, 'pims': 12, 'plus_minus': -2, 'gp': 30, 'age': 22, 'team_id': 5},
        {'first_name': 'Wyatt', 'last_name': 'Smith', 'position': 'C', 'number': 20, 'goals': 3, 'assists': 7, 'points': 10, 'pims': 13, 'plus_minus': 7, 'gp': 42, 'age': 23, 'team_id': 5},
        {'first_name': 'Radoslav', 'last_name': 'Suchy', 'position': 'D', 'number': 15, 'goals': 0, 'assists': 10, 'points': 10, 'pims': 22, 'plus_minus': 1, 'gp': 72, 'age': 24, 'team_id': 5},
        {'first_name': 'Mike', 'last_name': 'Sullivan', 'position': 'C', 'number': 26, 'goals': 5, 'assists': 4, 'points': 9, 'pims': 16, 'plus_minus': -6, 'gp': 72, 'age': 32, 'team_id': 5},
        {'first_name': 'Michal', 'last_name': 'Handzus', 'position': 'C', 'number': 16, 'goals': 4, 'assists': 4, 'points': 8, 'pims': 21, 'plus_minus': 5, 'gp': 10, 'age': 23, 'team_id': 5},
        {'first_name': 'Mike', 'last_name': 'Johnson', 'position': 'R', 'number': 12, 'goals': 2, 'assists': 3, 'points': 5, 'pims': 4, 'plus_minus': 0, 'gp': 12, 'age': 25, 'team_id': 5},
        {'first_name': 'Stanislav', 'last_name': 'Neckar', 'position': 'D', 'number': 35, 'goals': 2, 'assists': 2, 'points': 4, 'pims': 63, 'plus_minus': -2, 'gp': 53, 'age': 24, 'team_id': 5},
        {'first_name': 'Paul', 'last_name': 'Mara', 'position': 'D', 'number': 23, 'goals': 0, 'assists': 4, 'points': 4, 'pims': 14, 'plus_minus': 1, 'gp': 16, 'age': 20, 'team_id': 5},
        {'first_name': 'Joel', 'last_name': 'Bouchard', 'position': 'D', 'number': 6, 'goals': 1, 'assists': 2, 'points': 3, 'pims': 22, 'plus_minus': -8, 'gp': 32, 'age': 26, 'team_id': 5},
        {'first_name': 'Sean', 'last_name': 'Burke', 'position': 'G', 'number': 1, 'wins': 25, 'gaa': 2.27, 'svp': .922, 'gp': 62, 'age': 33, 'team_id': 5},
        {'first_name': 'Robert', 'last_name': 'Esche', 'position': 'G', 'number': 42, 'wins': 10, 'gaa': 3.02, 'svp': .896, 'gp': 25, 'age': 22, 'team_id': 5}
    ]
    team6 = [
        {'first_name': 'Daymond', 'last_name': 'Langkow', 'position': 'C', 'number': 11, 'goals': 27, 'assists': 35, 'points': 62, 'pims': 36, 'plus_minus': 18, 'gp': 80, 'age': 24, 'team_id': 6},
        {'first_name': 'Daniel', 'last_name': 'Briere', 'position': 'C', 'number': 8, 'goals': 32, 'assists': 28, 'points': 60, 'pims': 52, 'plus_minus': 6, 'gp': 78, 'age': 23, 'team_id': 6},
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 20, 'assists': 29, 'points': 49, 'pims': 61, 'plus_minus': 11, 'gp': 81, 'age': 24, 'team_id': 6},
        {'first_name': 'Teppo', 'last_name': 'Numminen', 'position': 'D', 'number': 27, 'goals': 13, 'assists': 35, 'points': 48, 'pims': 20, 'plus_minus': 13, 'gp': 76, 'age': 33, 'team_id': 6},
        {'first_name': 'Michal', 'last_name': 'Handzus', 'position': 'C', 'number': 16, 'goals': 14, 'assists': 30, 'points': 44, 'pims': 34, 'plus_minus': -8, 'gp': 79, 'age': 24, 'team_id': 6},
        {'first_name': 'Ladislav', 'last_name': 'Nagy', 'position': 'R', 'number': 17, 'goals': 23, 'assists': 19, 'points': 42, 'pims': 50, 'plus_minus': 6, 'gp': 74, 'age': 22, 'team_id': 6},
        {'first_name': 'Claude', 'last_name': 'Lemieux', 'position': 'R', 'number': 22, 'goals': 16, 'assists': 25, 'points': 41, 'pims': 70, 'plus_minus': -5, 'gp': 82, 'age': 36, 'team_id': 6},
        {'first_name': 'Danil', 'last_name': 'Markov', 'position': 'D', 'number': 55, 'goals': 6, 'assists': 30, 'points': 36, 'pims': 67, 'plus_minus': -7, 'gp': 72, 'age': 25, 'team_id': 6},
        {'first_name': 'Mike', 'last_name': 'Johnson', 'position': 'R', 'number': 12, 'goals': 5, 'assists': 22, 'points': 27, 'pims': 28, 'plus_minus': 14, 'gp': 57, 'age': 26, 'team_id': 6},
        {'first_name': 'Paul', 'last_name': 'Mara', 'position': 'D', 'number': 23, 'goals': 7, 'assists': 17, 'points': 24, 'pims': 58, 'plus_minus': -6, 'gp': 75, 'age': 21, 'team_id': 6},
        {'first_name': 'Krys', 'last_name': 'Kolanos', 'position': 'C', 'number': 36, 'goals': 11, 'assists': 11, 'points': 22, 'pims': 48, 'plus_minus': 6, 'gp': 57, 'age': 20, 'team_id': 6},
        {'first_name': 'Brad', 'last_name': 'May', 'position': 'L', 'number': 32, 'goals': 10, 'assists': 12, 'points': 22, 'pims': 95, 'plus_minus': 11, 'gp': 72, 'age': 29, 'team_id': 6},
        {'first_name': 'Landon', 'last_name': 'Wilson', 'position': 'R', 'number': 28, 'goals': 7, 'assists': 12, 'points': 19, 'pims': 46, 'plus_minus': 4, 'gp': 47, 'age': 26, 'team_id': 6},
        {'first_name': 'Radoslav', 'last_name': 'Suchy', 'position': 'D', 'number': 15, 'goals': 5, 'assists': 12, 'points': 17, 'pims': 10, 'plus_minus': 25, 'gp': 81, 'age': 25, 'team_id': 6},
        {'first_name': 'Sergei', 'last_name': 'Berezin', 'position': 'L', 'number': 94, 'goals': 7, 'assists': 9, 'points': 16, 'pims': 4, 'plus_minus': -1, 'gp': 41, 'age': 29, 'team_id': 6},
        {'first_name': 'Todd', 'last_name': 'Simpson', 'position': 'D', 'number': 2, 'goals': 2, 'assists': 13, 'points': 15, 'pims': 152, 'plus_minus': 20, 'gp': 67, 'age': 28, 'team_id': 6},
        {'first_name': 'Ossi', 'last_name': 'Vaananen', 'position': 'D', 'number': 4, 'goals': 2, 'assists': 12, 'points': 14, 'pims': 74, 'plus_minus': 6, 'gp': 76, 'age': 21, 'team_id': 6},
        {'first_name': 'Brian', 'last_name': 'Savage', 'position': 'L', 'number': 49, 'goals': 6, 'assists': 6, 'points': 12, 'pims': 8, 'plus_minus': 1, 'gp': 30, 'age': 30, 'team_id': 6},
        {'first_name': 'Andrei', 'last_name': 'Nazarov', 'position': 'L', 'number': 44, 'goals': 6, 'assists': 3, 'points': 9, 'pims': 51, 'plus_minus': 7, 'gp': 30, 'age': 27, 'team_id': 6},
        {'first_name': 'Trevor', 'last_name': 'Letowski', 'position': 'C', 'number': 10, 'goals': 2, 'assists': 6, 'points': 8, 'pims': 4, 'plus_minus': 2, 'gp': 33, 'age': 24, 'team_id': 6},
        {'first_name': 'Branko', 'last_name': 'Radivojevic', 'position': 'R', 'number': 29, 'goals': 4, 'assists': 2, 'points': 6, 'pims': 4, 'plus_minus': 1, 'gp': 18, 'age': 20, 'team_id': 6},
        {'first_name': 'Drake', 'last_name': 'Berehowsky', 'position': 'D', 'number': 5, 'goals': 1, 'assists': 4, 'points': 5, 'pims': 42, 'plus_minus': 5, 'gp': 32, 'age': 29, 'team_id': 6},
        {'first_name': 'Mike', 'last_name': 'Sullivan', 'position': 'C', 'number': 26, 'goals': 1, 'assists': 2, 'points': 3, 'pims': 16, 'plus_minus': -3, 'gp': 42, 'age': 33, 'team_id': 6},
        {'first_name': 'Todd', 'last_name': 'Warriner', 'position': 'L', 'number': 21, 'goals': 0, 'assists': 3, 'points': 3, 'pims': 8, 'plus_minus': -3, 'gp': 18, 'age': 27, 'team_id': 6},
        {'first_name': 'Sean', 'last_name': 'Burke', 'position': 'G', 'number': 1, 'wins': 33, 'gaa': 2.29, 'svp': .920, 'gp': 60, 'age': 34, 'team_id': 6},
        {'first_name': 'Robert', 'last_name': 'Esche', 'position': 'G', 'number': 42, 'wins': 6, 'gaa': 2.72, 'svp': .902, 'gp': 22, 'age': 23, 'team_id': 6}
    ]
    team7 = [
        {'first_name': 'Mike', 'last_name': 'Johnson', 'position': 'R', 'number': 12, 'goals': 23, 'assists': 40, 'points': 63, 'pims': 47, 'plus_minus': 9, 'gp': 82, 'age': 27, 'team_id': 7},
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 21, 'assists': 37, 'points': 58, 'pims': 86, 'plus_minus': 3, 'gp': 82, 'age': 25, 'team_id': 7},
        {'first_name': 'Ladislav', 'last_name': 'Nagy', 'position': 'R', 'number': 17, 'goals': 22, 'assists': 35, 'points': 57, 'pims': 92, 'plus_minus': 17, 'gp': 80, 'age': 23, 'team_id': 7},
        {'first_name': 'Daymond', 'last_name': 'Langkow', 'position': 'C', 'number': 11, 'goals': 20, 'assists': 32, 'points': 52, 'pims': 56, 'plus_minus': 20, 'gp': 82, 'age': 25, 'team_id': 7},
        {'first_name': 'Daniel', 'last_name': 'Briere', 'position': 'C', 'number': 8, 'goals': 17, 'assists': 29, 'points': 46, 'pims': 50, 'plus_minus': -21, 'gp': 68, 'age': 24, 'team_id': 7},
        {'first_name': 'Tony', 'last_name': 'Amonte', 'position': 'R', 'number': 10, 'goals': 13, 'assists': 23, 'points': 36, 'pims': 26, 'plus_minus': -12, 'gp': 59, 'age': 32, 'team_id': 7},
        {'first_name': 'Teppo', 'last_name': 'Numminen', 'position': 'D', 'number': 27, 'goals': 6, 'assists': 24, 'points': 30, 'pims': 30, 'plus_minus': 0, 'gp': 78, 'age': 34, 'team_id': 7},
        {'first_name': 'Branko', 'last_name': 'Radivojevic', 'position': 'R', 'number': 29, 'goals': 12, 'assists': 15, 'points': 27, 'pims': 63, 'plus_minus': -2, 'gp': 79, 'age': 21, 'team_id': 7},
        {'first_name': 'Paul', 'last_name': 'Mara', 'position': 'D', 'number': 23, 'goals': 10, 'assists': 15, 'points': 25, 'pims': 78, 'plus_minus': -7, 'gp': 73, 'age': 22, 'team_id': 7},
        {'first_name': 'Danil', 'last_name': 'Markov', 'position': 'D', 'number': 55, 'goals': 4, 'assists': 16, 'points': 20, 'pims': 36, 'plus_minus': 2, 'gp': 64, 'age': 26, 'team_id': 7},
        {'first_name': 'Ramzi', 'last_name': 'Abid', 'position': 'C', 'number': 34, 'goals': 10, 'assists': 8, 'points': 18, 'pims': 30, 'plus_minus': 1, 'gp': 30, 'age': 22, 'team_id': 7},
        {'first_name': 'Deron', 'last_name': 'Quint', 'position': 'D', 'number': 7, 'goals': 7, 'assists': 10, 'points': 17, 'pims': 20, 'plus_minus': -5, 'gp': 51, 'age': 26, 'team_id': 7},
        {'first_name': 'Brian', 'last_name': 'Savage', 'position': 'L', 'number': 49, 'goals': 6, 'assists': 10, 'points': 16, 'pims': 22, 'plus_minus': -4, 'gp': 43, 'age': 31, 'team_id': 7},
        {'first_name': 'Landon', 'last_name': 'Wilson', 'position': 'R', 'number': 28, 'goals': 6, 'assists': 8, 'points': 14, 'pims': 26, 'plus_minus': 1, 'gp': 31, 'age': 27, 'team_id': 7},
        {'first_name': 'Claude', 'last_name': 'Lemieux', 'position': 'R', 'number': 22, 'goals': 6, 'assists': 8, 'points': 14, 'pims': 30, 'plus_minus': -3, 'gp': 36, 'age': 37, 'team_id': 7},
        {'first_name': 'Kelly', 'last_name': 'Buchberger', 'position': 'R', 'number': 16, 'goals': 3, 'assists': 9, 'points': 12, 'pims': 109, 'plus_minus': 0, 'gp': 79, 'age': 35, 'team_id': 7},
        {'first_name': 'Todd', 'last_name': 'Simpson', 'position': 'D', 'number': 2, 'goals': 2, 'assists': 7, 'points': 9, 'pims': 135, 'plus_minus': 7, 'gp': 66, 'age': 29, 'team_id': 7},
        {'first_name': 'Ossi', 'last_name': 'Vaananen', 'position': 'D', 'number': 4, 'goals': 2, 'assists': 7, 'points': 9, 'pims': 82, 'plus_minus': 1, 'gp': 67, 'age': 22, 'team_id': 7},
        {'first_name': 'Radoslav', 'last_name': 'Suchy', 'position': 'D', 'number': 15, 'goals': 1, 'assists': 8, 'points': 9, 'pims': 18, 'plus_minus': 2, 'gp': 77, 'age': 26, 'team_id': 7},
        {'first_name': 'Brad', 'last_name': 'May', 'position': 'L', 'number': 32, 'goals': 3, 'assists': 4, 'points': 7, 'pims': 32, 'plus_minus': 3, 'gp': 20, 'age': 30, 'team_id': 7},
        {'first_name': 'Paul', 'last_name': 'Ranheim', 'position': 'L', 'number': 18, 'goals': 3, 'assists': 4, 'points': 7, 'pims': 10, 'plus_minus': -4, 'gp': 40, 'age': 36, 'team_id': 7},
        {'first_name': 'Jeff', 'last_name': 'Taffe', 'position': 'C', 'number': 14, 'goals': 3, 'assists': 1, 'points': 4, 'pims': 4, 'plus_minus': -4, 'gp': 20, 'age': 21, 'team_id': 7},
        {'first_name': 'Jan', 'last_name': 'Hrdina', 'position': 'C', 'number': 24, 'goals': 0, 'assists': 4, 'points': 4, 'pims': 8, 'plus_minus': 3, 'gp': 4, 'age': 26, 'team_id': 7},
        {'first_name': 'Andrei', 'last_name': 'Nazarov', 'position': 'L', 'number': 44, 'goals': 3, 'assists': 0, 'points': 3, 'pims': 135, 'plus_minus': -9, 'gp': 59, 'age': 28, 'team_id': 7},
        {'first_name': 'Sean', 'last_name': 'Burke', 'position': 'G', 'number': 1, 'wins': 12, 'gaa': 2.12, 'svp': .930, 'gp': 22, 'age': 35, 'team_id': 7},
        {'first_name': 'Brian', 'last_name': 'Boucher', 'position': 'G', 'number': 33, 'wins': 15, 'gaa': 3.02, 'svp': .894, 'gp': 45, 'age': 25, 'team_id': 7}
    ]
    team8 = [
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 27, 'assists': 41, 'points': 68, 'pims': 47, 'plus_minus': -11, 'gp': 79, 'age': 26, 'team_id': 8},
        {'first_name': 'Ladislav', 'last_name': 'Nagy', 'position': 'R', 'number': 17, 'goals': 24, 'assists': 28, 'points': 52, 'pims': 46, 'plus_minus': 11, 'gp': 55, 'age': 24, 'team_id': 8},
        {'first_name': 'Daymond', 'last_name': 'Langkow', 'position': 'C', 'number': 11, 'goals': 21, 'assists': 31, 'points': 52, 'pims': 40, 'plus_minus': 4, 'gp': 81, 'age': 26, 'team_id': 8},
        {'first_name': 'Paul', 'last_name': 'Mara', 'position': 'D', 'number': 23, 'goals': 6, 'assists': 36, 'points': 42, 'pims': 48, 'plus_minus': -11, 'gp': 81, 'age': 23, 'team_id': 8},
        {'first_name': 'Chris', 'last_name': 'Gratton', 'position': 'C', 'number': 77, 'goals': 11, 'assists': 18, 'points': 29, 'pims': 93, 'plus_minus': -19, 'gp': 68, 'age': 28, 'team_id': 8},
        {'first_name': 'Jan', 'last_name': 'Hrdina', 'position': 'C', 'number': 24, 'goals': 11, 'assists': 15, 'points': 26, 'pims': 30, 'plus_minus': -10, 'gp': 55, 'age': 27, 'team_id': 8},
        {'first_name': 'Brian', 'last_name': 'Savage', 'position': 'L', 'number': 49, 'goals': 12, 'assists': 13, 'points': 25, 'pims': 36, 'plus_minus': -5, 'gp': 61, 'age': 32, 'team_id': 8},
        {'first_name': 'Branko', 'last_name': 'Radivojevic', 'position': 'R', 'number': 29, 'goals': 9, 'assists': 14, 'points': 23, 'pims': 36, 'plus_minus': -5, 'gp': 53, 'age': 22, 'team_id': 8},
        {'first_name': 'Radoslav', 'last_name': 'Suchy', 'position': 'D', 'number': 15, 'goals': 7, 'assists': 14, 'points': 21, 'pims': 8, 'plus_minus': 1, 'gp': 82, 'age': 27, 'team_id': 8},
        {'first_name': 'Cale', 'last_name': 'Hulse', 'position': 'D', 'number': 32, 'goals': 3, 'assists': 17, 'points': 20, 'pims': 123, 'plus_minus': -4, 'gp': 82, 'age': 29, 'team_id': 8},
        {'first_name': 'Jeff', 'last_name': 'Taffe', 'position': 'C', 'number': 14, 'goals': 8, 'assists': 10, 'points': 18, 'pims': 20, 'plus_minus': -8, 'gp': 59, 'age': 22, 'team_id': 8},
        {'first_name': 'Daniel', 'last_name': 'Cleary', 'position': 'R', 'number': 8, 'goals': 6, 'assists': 11, 'points': 17, 'pims': 42, 'plus_minus': -8, 'gp': 68, 'age': 24, 'team_id': 8},
        {'first_name': 'Mike', 'last_name': 'Comrie', 'position': 'C', 'number': 89, 'goals': 8, 'assists': 7, 'points': 15, 'pims': 16, 'plus_minus': -8, 'gp': 28, 'age': 22, 'team_id': 8},
        {'first_name': 'Mike', 'last_name': 'Sillinger', 'position': 'C', 'number': 16, 'goals': 8, 'assists': 6, 'points': 14, 'pims': 54, 'plus_minus': -14, 'gp': 60, 'age': 32, 'team_id': 8},
        {'first_name': 'Fredrik', 'last_name': 'Sjostrom', 'position': 'R', 'number': 20, 'goals': 7, 'assists': 6, 'points': 13, 'pims': 22, 'plus_minus': -7, 'gp': 57, 'age': 20, 'team_id': 8},
        {'first_name': 'Dave', 'last_name': 'Tanabe', 'position': 'D', 'number': 5, 'goals': 5, 'assists': 7, 'points': 12, 'pims': 22, 'plus_minus': 4, 'gp': 45, 'age': 23, 'team_id': 8},
        {'first_name': 'Krys', 'last_name': 'Kolanos', 'position': 'C', 'number': 36, 'goals': 4, 'assists': 6, 'points': 10, 'pims': 24, 'plus_minus': -9, 'gp': 41, 'age': 22, 'team_id': 8},
        {'first_name': 'Mike', 'last_name': 'Johnson', 'position': 'R', 'number': 12, 'goals': 1, 'assists': 9, 'points': 10, 'pims': 10, 'plus_minus': -1, 'gp': 11, 'age': 28, 'team_id': 8},
        {'first_name': 'Tyson', 'last_name': 'Nash', 'position': 'L', 'number': 18, 'goals': 3, 'assists': 5, 'points': 8, 'pims': 110, 'plus_minus': -6, 'gp': 69, 'age': 28, 'team_id': 8},
        {'first_name': 'Ossi', 'last_name': 'Vaananen', 'position': 'D', 'number': 4, 'goals': 2, 'assists': 4, 'points': 6, 'pims': 87, 'plus_minus': -10, 'gp': 67, 'age': 23, 'team_id': 8},
        {'first_name': 'Brad', 'last_name': 'Ference', 'position': 'D', 'number': 45, 'goals': 0, 'assists': 5, 'points': 5, 'pims': 103, 'plus_minus': -19, 'gp': 63, 'age': 24, 'team_id': 8},
        {'first_name': 'Landon', 'last_name': 'Wilson', 'position': 'R', 'number': 28, 'goals': 1, 'assists': 3, 'points': 4, 'pims': 16, 'plus_minus': -3, 'gp': 35, 'age': 28, 'team_id': 8},
        {'first_name': 'Derek', 'last_name': 'Morris', 'position': 'D', 'number': 2, 'goals': 0, 'assists': 4, 'points': 4, 'pims': 2, 'plus_minus': -5, 'gp': 14, 'age': 25, 'team_id': 8},
        {'first_name': 'Andrei', 'last_name': 'Nazarov', 'position': 'L', 'number': 44, 'goals': 1, 'assists': 2, 'points': 3, 'pims': 125, 'plus_minus': -7, 'gp': 33, 'age': 29, 'team_id': 8},
        {'first_name': 'Sean', 'last_name': 'Burke', 'position': 'G', 'number': 1, 'wins': 10, 'gaa': 2.81, 'svp': .908, 'gp': 32, 'age': 36, 'team_id': 8},
        {'first_name': 'Brian', 'last_name': 'Boucher', 'position': 'G', 'number': 33, 'wins': 10, 'gaa': 2.74, 'svp': .906, 'gp': 40, 'age': 26, 'team_id': 8}
    ]
    team9 = [
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 30, 'assists': 36, 'points': 66, 'pims': 91, 'plus_minus': -5, 'gp': 81, 'age': 29, 'team_id': 9},
        {'first_name': 'Mike', 'last_name': 'Comrie', 'position': 'C', 'number': 89, 'goals': 30, 'assists': 30, 'points': 60, 'pims': 38, 'plus_minus': -8, 'gp': 80, 'age': 25, 'team_id': 9},
        {'first_name': 'Ladislav', 'last_name': 'Nagy', 'position': 'L', 'number': 17, 'goals': 15, 'assists': 41, 'points': 56, 'pims': 74, 'plus_minus': 8, 'gp': 51, 'age': 26, 'team_id': 9},
        {'first_name': 'Mike', 'last_name': 'Johnson', 'position': 'R', 'number': 12, 'goals': 16, 'assists': 38, 'points': 54, 'pims': 50, 'plus_minus': 7, 'gp': 80, 'age': 30, 'team_id': 9},
        {'first_name': 'Paul', 'last_name': 'Mara', 'position': 'D', 'number': 23, 'goals': 15, 'assists': 32, 'points': 47, 'pims': 70, 'plus_minus': -12, 'gp': 78, 'age': 25, 'team_id': 9},
        {'first_name': 'Geoff', 'last_name': 'Sanderson', 'position': 'L', 'number': 8, 'goals': 25, 'assists': 21, 'points': 46, 'pims': 58, 'plus_minus': -14, 'gp': 75, 'age': 33, 'team_id': 9},
        {'first_name': 'Keith', 'last_name': 'Ballard', 'position': 'D', 'number': 2, 'goals': 8, 'assists': 31, 'points': 39, 'pims': 99, 'plus_minus': -18, 'gp': 82, 'age': 22, 'team_id': 9},
        {'first_name': 'Derek', 'last_name': 'Morris', 'position': 'D', 'number': 53, 'goals': 6, 'assists': 21, 'points': 27, 'pims': 54, 'plus_minus': -7, 'gp': 53, 'age': 27, 'team_id': 9},
        {'first_name': 'Oleg', 'last_name': 'Saprykin', 'position': 'L', 'number': 91, 'goals': 11, 'assists': 14, 'points': 25, 'pims': 50, 'plus_minus': -16, 'gp': 67, 'age': 24, 'team_id': 9},
        {'first_name': 'Zbynek', 'last_name': 'Michalek', 'position': 'D', 'number': 39, 'goals': 9, 'assists': 15, 'points': 24, 'pims': 62, 'plus_minus': 4, 'gp': 82, 'age': 22, 'team_id': 9},
        {'first_name': 'Steven', 'last_name': 'Reinprecht', 'position': 'C', 'number': 29, 'goals': 12, 'assists': 11, 'points': 23, 'pims': 8, 'plus_minus': 1, 'gp': 28, 'age': 29, 'team_id': 9},
        {'first_name': 'Dave', 'last_name': 'Scatchard', 'position': 'C', 'number': 38, 'goals': 11, 'assists': 12, 'points': 23, 'pims': 84, 'plus_minus': -11, 'gp': 47, 'age': 29, 'team_id': 9},
        {'first_name': 'Fredrik', 'last_name': 'Sjostrom', 'position': 'R', 'number': 20, 'goals': 6, 'assists': 17, 'points': 23, 'pims': 42, 'plus_minus': 1, 'gp': 75, 'age': 22, 'team_id': 9},
        {'first_name': 'Boyd', 'last_name': 'Devereaux', 'position': 'C', 'number': 15, 'goals': 8, 'assists': 14, 'points': 22, 'pims': 44, 'plus_minus': -13, 'gp': 78, 'age': 27, 'team_id': 9},
        {'first_name': 'Mike', 'last_name': 'Leclerc', 'position': 'L', 'number': 28, 'goals': 9, 'assists': 12, 'points': 21, 'pims': 29, 'plus_minus': 0, 'gp': 35, 'age': 28, 'team_id': 9},
        {'first_name': 'Jamie', 'last_name': 'Lundmark', 'position': 'C', 'number': 16, 'goals': 5, 'assists': 13, 'points': 18, 'pims': 36, 'plus_minus': -1, 'gp': 38, 'age': 24, 'team_id': 9},
        {'first_name': 'Mike', 'last_name': 'Ricci', 'position': 'C', 'number': 40, 'goals': 10, 'assists': 6, 'points': 16, 'pims': 69, 'plus_minus': -22, 'gp': 78, 'age': 33, 'team_id': 9},
        {'first_name': 'Oleg', 'last_name': 'Kvasha', 'position': 'L', 'number': 11, 'goals': 4, 'assists': 7, 'points': 11, 'pims': 6, 'plus_minus': 5, 'gp': 15, 'age': 27, 'team_id': 9},
        {'first_name': 'Petr', 'last_name': 'Nedved', 'position': 'L', 'number': 93, 'goals': 2, 'assists': 9, 'points': 11, 'pims': 34, 'plus_minus': -6, 'gp': 25, 'age': 33, 'team_id': 9},
        {'first_name': 'Denis', 'last_name': 'Gauthier', 'position': 'D', 'number': 3, 'goals': 2, 'assists': 9, 'points': 11, 'pims': 61, 'plus_minus': -4, 'gp': 45, 'age': 28, 'team_id': 9},
        {'first_name': 'Dennis', 'last_name': 'Seidenberg', 'position': 'D', 'number': 22, 'goals': 1, 'assists': 10, 'points': 11, 'pims': 14, 'plus_minus': -9, 'gp': 34, 'age': 24, 'team_id': 9},
        {'first_name': 'Sean', 'last_name': 'O\'Donnell', 'position': 'D', 'number': 21, 'goals': 1, 'assists': 7, 'points': 8, 'pims': 121, 'plus_minus': 3, 'gp': 57, 'age': 33, 'team_id': 9},
        {'first_name': 'Tyson', 'last_name': 'Nash', 'position': 'L', 'number': 18, 'goals': 0, 'assists': 6, 'points': 6, 'pims': 84, 'plus_minus': -7, 'gp': 50, 'age': 30, 'team_id': 9},
        {'first_name': 'Jamie', 'last_name': 'Rivers', 'position': 'D', 'number': 5, 'goals': 0, 'assists': 5, 'points': 5, 'pims': 26, 'plus_minus': 2, 'gp': 18, 'age': 30, 'team_id': 9},
        {'first_name': 'Curtis', 'last_name': 'Joseph', 'position': 'G', 'number': 31, 'wins': 32, 'gaa': 2.91, 'svp': .902, 'gp': 60, 'age': 38, 'team_id': 9},
        {'first_name': 'David', 'last_name': 'LeNeveu', 'position': 'G', 'number': 30, 'wins': 3, 'gaa': 3.24, 'svp': .886, 'gp': 15, 'age': 22, 'team_id': 9},
        {'first_name': 'Brian', 'last_name': 'Boucher', 'position': 'G', 'number': 33, 'wins': 3, 'gaa': 3.87, 'svp': .877, 'gp': 11, 'age': 28, 'team_id': 9}
    ]
    team10 = [
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 27, 'assists': 28, 'points': 55, 'pims': 73, 'plus_minus': -14, 'gp': 73, 'age': 29, 'team_id': 10},
        {'first_name': 'Ladislav', 'last_name': 'Nagy', 'position': 'R', 'number': 17, 'goals': 8, 'assists': 33, 'points': 41, 'pims': 48, 'plus_minus': -2, 'gp': 55, 'age': 27, 'team_id': 10},
        {'first_name': 'Owen', 'last_name': 'Nolan', 'position': 'R', 'number': 11, 'goals': 16, 'assists': 24, 'points': 40, 'pims': 56, 'plus_minus': -2, 'gp': 76, 'age': 34, 'team_id': 10},
        {'first_name': 'Oleg', 'last_name': 'Saprykin', 'position': 'L', 'number': 91, 'goals': 14, 'assists': 20, 'points': 34, 'pims': 54, 'plus_minus': 8, 'gp': 59, 'age': 25, 'team_id': 10},
        {'first_name': 'Yanic', 'last_name': 'Perreault', 'position': 'C', 'number': 94, 'goals': 19, 'assists': 14, 'points': 33, 'pims': 30, 'plus_minus': -2, 'gp': 49, 'age': 35, 'team_id': 10},
        {'first_name': 'Steven', 'last_name': 'Reinprecht', 'position': 'C', 'number': 28, 'goals': 9, 'assists': 24, 'points': 33, 'pims': 28, 'plus_minus': -3, 'gp': 49, 'age': 30, 'team_id': 10},
        {'first_name': 'Ed', 'last_name': 'Jovanovski', 'position': 'D', 'number': 55, 'goals': 11, 'assists': 18, 'points': 29, 'pims': 63, 'plus_minus': -6, 'gp': 54, 'age': 30, 'team_id': 10},
        {'first_name': 'Jeremy', 'last_name': 'Roenick', 'position': 'C', 'number': 97, 'goals': 11, 'assists': 17, 'points': 28, 'pims': 32, 'plus_minus': -18, 'gp': 70, 'age': 36, 'team_id': 10},
        {'first_name': 'Zbynek', 'last_name': 'Michalek', 'position': 'D', 'number': 4, 'goals': 4, 'assists': 24, 'points': 28, 'pims': 34, 'plus_minus': -20, 'gp': 82, 'age': 23, 'team_id': 10},
        {'first_name': 'Keith', 'last_name': 'Ballard', 'position': 'D', 'number': 2, 'goals': 5, 'assists': 22, 'points': 27, 'pims': 59, 'plus_minus': -7, 'gp': 69, 'age': 23, 'team_id': 10},
        {'first_name': 'Derek', 'last_name': 'Morris', 'position': 'D', 'number': 53, 'goals': 6, 'assists': 19, 'points': 25, 'pims': 115, 'plus_minus': -18, 'gp': 82, 'age': 28, 'team_id': 10},
        {'first_name': 'Mike', 'last_name': 'Zigomanis', 'position': 'C', 'number': 15, 'goals': 14, 'assists': 9, 'points': 23, 'pims': 46, 'plus_minus': -8, 'gp': 75, 'age': 25, 'team_id': 10},
        {'first_name': 'Georges', 'last_name': 'Laraque', 'position': 'L', 'number': 37, 'goals': 5, 'assists': 17, 'points': 22, 'pims': 52, 'plus_minus': 7, 'gp': 56, 'age': 29, 'team_id': 10},
        {'first_name': 'Mike', 'last_name': 'Comrie', 'position': 'C', 'number': 89, 'goals': 7, 'assists': 13, 'points': 20, 'pims': 20, 'plus_minus': 1, 'gp': 24, 'age': 25, 'team_id': 10},
        {'first_name': 'Travis', 'last_name': 'Roche', 'position': 'D', 'number': 29, 'goals': 6, 'assists': 13, 'points': 19, 'pims': 22, 'plus_minus': 2, 'gp': 50, 'age': 28, 'team_id': 10},
        {'first_name': 'Fredrik', 'last_name': 'Sjostrom', 'position': 'R', 'number': 20, 'goals': 9, 'assists': 9, 'points': 18, 'pims': 48, 'plus_minus': -11, 'gp': 78, 'age': 23, 'team_id': 10},
        {'first_name': 'Bill', 'last_name': 'Thomas', 'position': 'R', 'number': 21, 'goals': 8, 'assists': 6, 'points': 14, 'pims': 2, 'plus_minus': -6, 'gp': 24, 'age': 23, 'team_id': 10},
        {'first_name': 'Nick', 'last_name': 'Boynton', 'position': 'D', 'number': 44, 'goals': 2, 'assists': 9, 'points': 11, 'pims': 138, 'plus_minus': -13, 'gp': 59, 'age': 27, 'team_id': 10},
        {'first_name': 'Patrick', 'last_name': 'Fischer', 'position': 'C', 'number': 12, 'goals': 4, 'assists': 6, 'points': 10, 'pims': 24, 'plus_minus': 0, 'gp': 27, 'age': 30, 'team_id': 10},
        {'first_name': 'Mathias', 'last_name': 'Tjarnqvist', 'position': 'R', 'number': 22, 'goals': 5, 'assists': 4, 'points': 9, 'pims': 2, 'plus_minus': -2, 'gp': 26, 'age': 27, 'team_id': 10},
        {'first_name': 'Niko', 'last_name': 'Kapanen', 'position': 'C', 'number': 39, 'goals': 2, 'assists': 7, 'points': 9, 'pims': 8, 'plus_minus': -11, 'gp': 19, 'age': 28, 'team_id': 10},
        {'first_name': 'Dave', 'last_name': 'Scatchard', 'position': 'C', 'number': 38, 'goals': 3, 'assists': 5, 'points': 8, 'pims': 72, 'plus_minus': -18, 'gp': 46, 'age': 30, 'team_id': 10},
        {'first_name': 'Kevyn', 'last_name': 'Adams', 'position': 'C', 'number': 14, 'goals': 1, 'assists': 7, 'points': 8, 'pims': 8, 'plus_minus': -10, 'gp': 33, 'age': 31, 'team_id': 10},
        {'first_name': 'Daniel', 'last_name': 'Carcillo', 'position': 'L', 'number': 13, 'goals': 4, 'assists': 3, 'points': 7, 'pims': 74, 'plus_minus': -7, 'gp': 18, 'age': 21, 'team_id': 10},
        {'first_name': 'Curtis', 'last_name': 'Joseph', 'position': 'G', 'number': 31, 'wins': 31, 'gaa': 3.19, 'svp': .893, 'gp': 55, 'age': 39, 'team_id': 10},
        {'first_name': 'Mikael', 'last_name': 'Tellqvist', 'position': 'G', 'number': 32, 'wins': 11, 'gaa': 3.86, 'svp': .894, 'gp': 30, 'age': 26, 'team_id': 10}
    ]
    team11 = [
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 28, 'assists': 50, 'points': 78, 'pims': 59, 'plus_minus': 4, 'gp': 80, 'age': 30, 'team_id': 11},
        {'first_name': 'Radim', 'last_name': 'Vrbata', 'position': 'R', 'number': 17, 'goals': 27, 'assists': 29, 'points': 56, 'pims': 14, 'plus_minus': 6, 'gp': 76, 'age': 26, 'team_id': 11},
        {'first_name': 'Peter', 'last_name': 'Mueller', 'position': 'C', 'number': 88, 'goals': 22, 'assists': 32, 'points': 54, 'pims': 32, 'plus_minus': -13, 'gp': 81, 'age': 19, 'team_id': 11},
        {'first_name': 'Ed', 'last_name': 'Jovanovski', 'position': 'D', 'number': 55, 'goals': 12, 'assists': 39, 'points': 51, 'pims': 73, 'plus_minus': -13, 'gp': 80, 'age': 31, 'team_id': 11},
        {'first_name': 'Steven', 'last_name': 'Reinprecht', 'position': 'C', 'number': 28, 'goals': 16, 'assists': 30, 'points': 46, 'pims': 26, 'plus_minus': -3, 'gp': 81, 'age': 31, 'team_id': 11},
        {'first_name': 'Martin', 'last_name': 'Hanzal', 'position': 'C', 'number': 11, 'goals': 8, 'assists': 27, 'points': 35, 'pims': 28, 'plus_minus': -7, 'gp': 72, 'age': 20, 'team_id': 11},
        {'first_name': 'Niko', 'last_name': 'Kapanen', 'position': 'C', 'number': 39, 'goals': 10, 'assists': 18, 'points': 28, 'pims': 34, 'plus_minus': -1, 'gp': 79, 'age': 29, 'team_id': 11},
        {'first_name': 'Daniel', 'last_name': 'Winnik', 'position': 'L', 'number': 34, 'goals': 11, 'assists': 15, 'points': 26, 'pims': 25, 'plus_minus': -3, 'gp': 79, 'age': 22, 'team_id': 11},
        {'first_name': 'Derek', 'last_name': 'Morris', 'position': 'D', 'number': 53, 'goals': 8, 'assists': 17, 'points': 25, 'pims': 83, 'plus_minus': 8, 'gp': 82, 'age': 29, 'team_id': 11},
        {'first_name': 'Daniel', 'last_name': 'Carcillo', 'position': 'L', 'number': 13, 'goals': 13, 'assists': 11, 'points': 24, 'pims': 324, 'plus_minus': 1, 'gp': 57, 'age': 22, 'team_id': 11},
        {'first_name': 'Keith', 'last_name': 'Ballard', 'position': 'D', 'number': 2, 'goals': 6, 'assists': 15, 'points': 21, 'pims': 85, 'plus_minus': 7, 'gp': 82, 'age': 24, 'team_id': 11},
        {'first_name': 'Fredrik', 'last_name': 'Sjostrom', 'position': 'R', 'number': 20, 'goals': 10, 'assists': 9, 'points': 19, 'pims': 14, 'plus_minus': -2, 'gp': 51, 'age': 24, 'team_id': 11},
        {'first_name': 'Joel', 'last_name': 'Perrault', 'position': 'C', 'number': 26, 'goals': 7, 'assists': 10, 'points': 17, 'pims': 48, 'plus_minus': -11, 'gp': 49, 'age': 24, 'team_id': 11},
        {'first_name': 'Zbynek', 'last_name': 'Michalek', 'position': 'D', 'number': 4, 'goals': 4, 'assists': 13, 'points': 17, 'pims': 34, 'plus_minus': 9, 'gp': 75, 'age': 24, 'team_id': 11},
        {'first_name': 'Mike', 'last_name': 'York', 'position': 'C', 'number': 16, 'goals': 6, 'assists': 8, 'points': 14, 'pims': 4, 'plus_minus': -8, 'gp': 63, 'age': 29, 'team_id': 11},
        {'first_name': 'Keith', 'last_name': 'Yandle', 'position': 'D', 'number': 3, 'goals': 5, 'assists': 7, 'points': 12, 'pims': 14, 'plus_minus': -12, 'gp': 43, 'age': 20, 'team_id': 11},
        {'first_name': 'Nick', 'last_name': 'Boynton', 'position': 'D', 'number': 44, 'goals': 3, 'assists': 9, 'points': 12, 'pims': 125, 'plus_minus': -9, 'gp': 79, 'age': 28, 'team_id': 11},
        {'first_name': 'Mathias', 'last_name': 'Tjarnqvist', 'position': 'R', 'number': 22, 'goals': 4, 'assists': 7, 'points': 11, 'pims': 34, 'plus_minus': -1, 'gp': 78, 'age': 28, 'team_id': 11},
        {'first_name': 'Craig', 'last_name': 'Weller', 'position': 'R', 'number': 78, 'goals': 3, 'assists': 8, 'points': 11, 'pims': 80, 'plus_minus': -7, 'gp': 59, 'age': 26, 'team_id': 11},
        {'first_name': 'Enver', 'last_name': 'Lisin', 'position': 'R', 'number': 18, 'goals': 4, 'assists': 1, 'points': 5, 'pims': 6, 'plus_minus': -5, 'gp': 13, 'age': 21, 'team_id': 11},
        {'first_name': 'Mike', 'last_name': 'Zigomanis', 'position': 'C', 'number': 15, 'goals': 2, 'assists': 1, 'points': 3, 'pims': 6, 'plus_minus': -7, 'gp': 33, 'age': 26, 'team_id': 11},
        {'first_name': 'Matt', 'last_name': 'Jones', 'position': 'D', 'number': 5, 'goals': 0, 'assists': 2, 'points': 2, 'pims': 10, 'plus_minus': -13, 'gp': 45, 'age': 24, 'team_id': 11},
        {'first_name': 'Matt', 'last_name': 'Murley', 'position': 'L', 'number': 18, 'goals': 0, 'assists': 1, 'points': 1, 'pims': 0, 'plus_minus': 1, 'gp': 3, 'age': 27, 'team_id': 11},
        {'first_name': 'Kyle', 'last_name': 'Turris', 'position': 'C', 'number': 91, 'goals': 0, 'assists': 1, 'points': 1, 'pims': 2, 'plus_minus': -5, 'gp': 3, 'age': 18, 'team_id': 11},
        {'first_name': 'Ilya', 'last_name': 'Bryzgalov', 'position': 'G', 'number': 30, 'wins': 26, 'gaa': 2.42, 'svp': .921, 'gp': 55, 'age': 27, 'team_id': 11},
        {'first_name': 'Mikael', 'last_name': 'Tellqvist', 'position': 'G', 'number': 32, 'wins': 9, 'gaa': 3.86, 'svp': .894, 'gp': 22, 'age': 27, 'team_id': 11}
    ]
    team12 = [
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 31, 'assists': 42, 'points': 73, 'pims': 72, 'plus_minus': 5, 'gp': 82, 'age': 31, 'team_id': 12},
        {'first_name': 'Olli', 'last_name': 'Jokinen', 'position': 'C', 'number': 12, 'goals': 21, 'assists': 21, 'points': 42, 'pims': 49, 'plus_minus': -5, 'gp': 57, 'age': 29, 'team_id': 12},
        {'first_name': 'Steven', 'last_name': 'Reinprecht', 'position': 'C', 'number': 28, 'goals': 14, 'assists': 27, 'points': 41, 'pims': 20, 'plus_minus': 0, 'gp': 73, 'age': 32, 'team_id': 12},
        {'first_name': 'Peter', 'last_name': 'Mueller', 'position': 'C', 'number': 88, 'goals': 13, 'assists': 23, 'points': 36, 'pims': 24, 'plus_minus': -7, 'gp': 72, 'age': 20, 'team_id': 12},
        {'first_name': 'Ed', 'last_name': 'Jovanovski', 'position': 'D', 'number': 55, 'goals': 9, 'assists': 27, 'points': 36, 'pims': 106, 'plus_minus': -15, 'gp': 82, 'age': 32, 'team_id': 12},
        {'first_name': 'Martin', 'last_name': 'Hanzal', 'position': 'C', 'number': 11, 'goals': 11, 'assists': 20, 'points': 31, 'pims': 40, 'plus_minus': -4, 'gp': 74, 'age': 21, 'team_id': 12},
        {'first_name': 'Keith', 'last_name': 'Yandle', 'position': 'D', 'number': 3, 'goals': 4, 'assists': 26, 'points': 30, 'pims': 37, 'plus_minus': -4, 'gp': 69, 'age': 21, 'team_id': 12},
        {'first_name': 'Mikkel', 'last_name': 'Boedker', 'position': 'L', 'number': 89, 'goals': 11, 'assists': 17, 'points': 28, 'pims': 18, 'plus_minus': -6, 'gp': 78, 'age': 18, 'team_id': 12},
        {'first_name': 'Zbynek', 'last_name': 'Michalek', 'position': 'D', 'number': 4, 'goals': 6, 'assists': 21, 'points': 27, 'pims': 28, 'plus_minus': -13, 'gp': 82, 'age': 25, 'team_id': 12},
        {'first_name': 'Enver', 'last_name': 'Lisin', 'position': 'R', 'number': 18, 'goals': 13, 'assists': 8, 'points': 21, 'pims': 24, 'plus_minus': -13, 'gp': 48, 'age': 22, 'team_id': 12},
        {'first_name': 'Joakim', 'last_name': 'Lindstrom', 'position': 'L', 'number': 38, 'goals': 9, 'assists': 11, 'points': 20, 'pims': 28, 'plus_minus': -6, 'gp': 44, 'age': 24, 'team_id': 12},
        {'first_name': 'Kyle', 'last_name': 'Turris', 'position': 'C', 'number': 91, 'goals': 8, 'assists': 12, 'points': 20, 'pims': 21, 'plus_minus': -15, 'gp': 63, 'age': 19, 'team_id': 12},
        {'first_name': 'Viktor', 'last_name': 'Tikhonov', 'position': 'L', 'number': 41, 'goals': 8, 'assists': 8, 'points': 16, 'pims': 20, 'plus_minus': -3, 'gp': 61, 'age': 20, 'team_id': 12},
        {'first_name': 'Matthew', 'last_name': 'Lombardi', 'position': 'C', 'number': 15, 'goals': 5, 'assists': 11, 'points': 16, 'pims': 14, 'plus_minus': 2, 'gp': 19, 'age': 26, 'team_id': 12},
        {'first_name': 'Scottie', 'last_name': 'Upshall', 'position': 'R', 'number': 8, 'goals': 8, 'assists': 5, 'points': 13, 'pims': 26, 'plus_minus': 2, 'gp': 19, 'age': 24, 'team_id': 12},
        {'first_name': 'Todd', 'last_name': 'Fedoruk', 'position': 'L', 'number': 17, 'goals': 6, 'assists': 7, 'points': 13, 'pims': 72, 'plus_minus': -9, 'gp': 72, 'age': 29, 'team_id': 12},
        {'first_name': 'Derek', 'last_name': 'Morris', 'position': 'D', 'number': 53, 'goals': 5, 'assists': 7, 'points': 12, 'pims': 24, 'plus_minus': -13, 'gp': 57, 'age': 30, 'team_id': 12},
        {'first_name': 'Ken', 'last_name': 'Klee', 'position': 'D', 'number': 2, 'goals': 1, 'assists': 10, 'points': 11, 'pims': 24, 'plus_minus': 9, 'gp': 68, 'age': 37, 'team_id': 12},
        {'first_name': 'Kevin', 'last_name': 'Porter', 'position': 'C', 'number': 13, 'goals': 5, 'assists': 5, 'points': 10, 'pims': 4, 'plus_minus': -2, 'gp': 34, 'age': 22, 'team_id': 12},
        {'first_name': 'Daniel', 'last_name': 'Carcillo', 'position': 'L', 'number': 36, 'goals': 3, 'assists': 7, 'points': 10, 'pims': 174, 'plus_minus': -13, 'gp': 54, 'age': 23, 'team_id': 12},
        {'first_name': 'Petr', 'last_name': 'Prucha', 'position': 'L', 'number': 16, 'goals': 2, 'assists': 8, 'points': 10, 'pims': 6, 'plus_minus': 1, 'gp': 19, 'age': 25, 'team_id': 12},
        {'first_name': 'David', 'last_name': 'Hale', 'position': 'D', 'number': 21, 'goals': 3, 'assists': 6, 'points': 9, 'pims': 36, 'plus_minus': -11, 'gp': 48, 'age': 27, 'team_id': 12},
        {'first_name': 'Daniel', 'last_name': 'Winnik', 'position': 'L', 'number': 34, 'goals': 3, 'assists': 4, 'points': 7, 'pims': 63, 'plus_minus': 1, 'gp': 49, 'age': 23, 'team_id': 12},
        {'first_name': 'Kurt', 'last_name': 'Sauer', 'position': 'D', 'number': 44, 'goals': 1, 'assists': 6, 'points': 7, 'pims': 36, 'plus_minus': -1, 'gp': 68, 'age': 27, 'team_id': 12},
        {'first_name': 'Ilya', 'last_name': 'Bryzgalov', 'position': 'G', 'number': 30, 'wins': 26, 'gaa': 2.98, 'svp': .906, 'gp': 65, 'age': 28, 'team_id': 12},
        {'first_name': 'Mikael', 'last_name': 'Tellqvist', 'position': 'G', 'number': 32, 'wins': 7, 'gaa': 2.86, 'svp': .907, 'gp': 15, 'age': 28, 'team_id': 12}
    ]
    team13 = [
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 18, 'assists': 37, 'points': 55, 'pims': 41, 'plus_minus': 3, 'gp': 82, 'age': 32, 'team_id': 13},
        {'first_name': 'Matthew', 'last_name': 'Lombardi', 'position': 'C', 'number': 15, 'goals': 19, 'assists': 34, 'points': 53, 'pims': 36, 'plus_minus': 8, 'gp': 78, 'age': 27, 'team_id': 13},
        {'first_name': 'Radim', 'last_name': 'Vrbata', 'position': 'R', 'number': 17, 'goals': 24, 'assists': 19, 'points': 43, 'pims': 24, 'plus_minus': 6, 'gp': 82, 'age': 28, 'team_id': 13},
        {'first_name': 'Keith', 'last_name': 'Yandle', 'position': 'D', 'number': 3, 'goals': 12, 'assists': 29, 'points': 41, 'pims': 45, 'plus_minus': 16, 'gp': 82, 'age': 22, 'team_id': 13},
        {'first_name': 'Ed', 'last_name': 'Jovanovski', 'position': 'D', 'number': 55, 'goals': 10, 'assists': 24, 'points': 34, 'pims': 55, 'plus_minus': -12, 'gp': 66, 'age': 33, 'team_id': 13},
        {'first_name': 'Martin', 'last_name': 'Hanzal', 'position': 'C', 'number': 11, 'goals': 11, 'assists': 22, 'points': 33, 'pims': 104, 'plus_minus': 0, 'gp': 81, 'age': 22, 'team_id': 13},
        {'first_name': 'Scottie', 'last_name': 'Upshall', 'position': 'R', 'number': 8, 'goals': 18, 'assists': 14, 'points': 32, 'pims': 50, 'plus_minus': 5, 'gp': 49, 'age': 25, 'team_id': 13},
        {'first_name': 'Vern', 'last_name': 'Fiddler', 'position': 'C', 'number': 38, 'goals': 8, 'assists': 22, 'points': 30, 'pims': 46, 'plus_minus': 13, 'gp': 76, 'age': 29, 'team_id': 13},
        {'first_name': 'Robert', 'last_name': 'Lang', 'position': 'C', 'number': 20, 'goals': 9, 'assists': 20, 'points': 29, 'pims': 28, 'plus_minus': -4, 'gp': 64, 'age': 38, 'team_id': 13},
        {'first_name': 'Adrian', 'last_name': 'Aucoin', 'position': 'D', 'number': 33, 'goals': 8, 'assists': 20, 'points': 28, 'pims': 56, 'plus_minus': 2, 'gp': 82, 'age': 36, 'team_id': 13},
        {'first_name': 'Taylor', 'last_name': 'Pyatt', 'position': 'L', 'number': 14, 'goals': 12, 'assists': 11, 'points': 23, 'pims': 39, 'plus_minus': 13, 'gp': 74, 'age': 28, 'team_id': 13},
        {'first_name': 'Petr', 'last_name': 'Prucha', 'position': 'L', 'number': 16, 'goals': 13, 'assists': 9, 'points': 22, 'pims': 23, 'plus_minus': -2, 'gp': 79, 'age': 26, 'team_id': 13},
        {'first_name': 'Daniel', 'last_name': 'Winnik', 'position': 'L', 'number': 34, 'goals': 4, 'assists': 15, 'points': 19, 'pims': 12, 'plus_minus': 1, 'gp': 74, 'age': 24, 'team_id': 13},
        {'first_name': 'Lee', 'last_name': 'Stempniak', 'position': 'R', 'number': 22, 'goals': 14, 'assists': 4, 'points': 18, 'pims': 8, 'plus_minus': 10, 'gp': 18, 'age': 26, 'team_id': 13},
        {'first_name': 'Wojtek', 'last_name': 'Wolski', 'position': 'L', 'number': 86, 'goals': 6, 'assists': 12, 'points': 18, 'pims': 6, 'plus_minus': 6, 'gp': 18, 'age': 23, 'team_id': 13},
        {'first_name': 'Peter', 'last_name': 'Mueller', 'position': 'C', 'number': 32, 'goals': 4, 'assists': 13, 'points': 17, 'pims': 8, 'plus_minus': -5, 'gp': 54, 'age': 21, 'team_id': 13},
        {'first_name': 'Zbynek', 'last_name': 'Michalek', 'position': 'D', 'number': 4, 'goals': 3, 'assists': 14, 'points': 17, 'pims': 30, 'plus_minus': 5, 'gp': 72, 'age': 26, 'team_id': 13},
        {'first_name': 'Jim', 'last_name': 'Vandermeer', 'position': 'D', 'number': 2, 'goals': 4, 'assists': 8, 'points': 12, 'pims': 60, 'plus_minus': 3, 'gp': 62, 'age': 29, 'team_id': 13},
        {'first_name': 'Lauri', 'last_name': 'Korpikoski', 'position': 'L', 'number': 29, 'goals': 5, 'assists': 6, 'points': 11, 'pims': 16, 'plus_minus': -10, 'gp': 71, 'age': 23, 'team_id': 13},
        {'first_name': 'Sami', 'last_name': 'Lepisto', 'position': 'D', 'number': 18, 'goals': 1, 'assists': 10, 'points': 11, 'pims': 60, 'plus_minus': 14, 'gp': 66, 'age': 24, 'team_id': 13},
        {'first_name': 'Paul', 'last_name': 'Bissonnette', 'position': 'L', 'number': 12, 'goals': 3, 'assists': 2, 'points': 5, 'pims': 117, 'plus_minus': -2, 'gp': 41, 'age': 24, 'team_id': 13},
        {'first_name': 'David', 'last_name': 'Schlemko', 'position': 'D', 'number': 6, 'goals': 1, 'assists': 4, 'points': 5, 'pims': 8, 'plus_minus': 1, 'gp': 17, 'age': 22, 'team_id': 13},
        {'first_name': 'Derek', 'last_name': 'Morris', 'position': 'D', 'number': 53, 'goals': 1, 'assists': 3, 'points': 4, 'pims': 11, 'plus_minus': 4, 'gp': 18, 'age': 31, 'team_id': 13},
        {'first_name': 'Mathieu', 'last_name': 'Schneider', 'position': 'D', 'number': 23, 'goals': 0, 'assists': 4, 'points': 4, 'pims': 4, 'plus_minus': 5, 'gp': 8, 'age': 40, 'team_id': 13},
        {'first_name': 'Mikkel', 'last_name': 'Boedker', 'position': 'L', 'number': 89, 'goals': 1, 'assists': 2, 'points': 3, 'pims': 0, 'plus_minus': 2, 'gp': 14, 'age': 19, 'team_id': 13},
        {'first_name': 'Ilya', 'last_name': 'Bryzgalov', 'position': 'G', 'number': 30, 'wins': 42, 'gaa': 2.29, 'svp': .920, 'gp': 69, 'age': 29, 'team_id': 13},
        {'first_name': 'Jason', 'last_name': 'Labarbara', 'position': 'G', 'number': 1, 'wins': 8, 'gaa': 2.13, 'svp': .928, 'gp': 17, 'age': 29, 'team_id': 13}
    ]
    team14 = [
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 20, 'assists': 40, 'points': 60, 'pims': 67, 'plus_minus': 5, 'gp': 72, 'age': 33, 'team_id': 14},
        {'first_name': 'Keith', 'last_name': 'Yandle', 'position': 'D', 'number': 3, 'goals': 11, 'assists': 48, 'points': 59, 'pims': 68, 'plus_minus': 12, 'gp': 82, 'age': 23, 'team_id': 14},
        {'first_name': 'Ray', 'last_name': 'Whitney', 'position': 'L', 'number': 13, 'goals': 17, 'assists': 40, 'points': 57, 'pims': 24, 'plus_minus': 0, 'gp': 75, 'age': 38, 'team_id': 14},
        {'first_name': 'Radim', 'last_name': 'Vrbata', 'position': 'R', 'number': 17, 'goals': 19, 'assists': 29, 'points': 48, 'pims': 20, 'plus_minus': 5, 'gp': 79, 'age': 29, 'team_id': 14},
        {'first_name': 'Lauri', 'last_name': 'Korpikoski', 'position': 'L', 'number': 28, 'goals': 19, 'assists': 21, 'points': 40, 'pims': 20, 'plus_minus': 17, 'gp': 79, 'age': 24, 'team_id': 14},
        {'first_name': 'Eric', 'last_name': 'Belanger', 'position': 'C', 'number': 20, 'goals': 13, 'assists': 27, 'points': 40, 'pims': 36, 'plus_minus': 11, 'gp': 82, 'age': 32, 'team_id': 14},
        {'first_name': 'Lee', 'last_name': 'Stempniak', 'position': 'R', 'number': 22, 'goals': 19, 'assists': 19, 'points': 38, 'pims': 19, 'plus_minus': 4, 'gp': 82, 'age': 27, 'team_id': 14},
        {'first_name': 'Taylor', 'last_name': 'Pyatt', 'position': 'L', 'number': 14, 'goals': 18, 'assists': 13, 'points': 31, 'pims': 27, 'plus_minus': 11, 'gp': 76, 'age': 29, 'team_id': 14},
        {'first_name': 'Scottie', 'last_name': 'Upshall', 'position': 'R', 'number': 8, 'goals': 16, 'assists': 11, 'points': 27, 'pims': 42, 'plus_minus': 5, 'gp': 61, 'age': 26, 'team_id': 14},
        {'first_name': 'Martin', 'last_name': 'Hanzal', 'position': 'C', 'number': 11, 'goals': 16, 'assists': 10, 'points': 26, 'pims': 54, 'plus_minus': 4, 'gp': 61, 'age': 23, 'team_id': 14},
        {'first_name': 'Kyle', 'last_name': 'Turris', 'position': 'C', 'number': 91, 'goals': 11, 'assists': 14, 'points': 25, 'pims': 16, 'plus_minus': 0, 'gp': 65, 'age': 21, 'team_id': 14},
        {'first_name': 'Vern', 'last_name': 'Fiddler', 'position': 'C', 'number': 38, 'goals': 6, 'assists': 16, 'points': 22, 'pims': 46, 'plus_minus': 3, 'gp': 71, 'age': 30, 'team_id': 14},
        {'first_name': 'Adrian', 'last_name': 'Aucoin', 'position': 'D', 'number': 33, 'goals': 3, 'assists': 19, 'points': 22, 'pims': 52, 'plus_minus': 18, 'gp': 75, 'age': 37, 'team_id': 14},
        {'first_name': 'Wojtek', 'last_name': 'Wolski', 'position': 'L', 'number': 30, 'goals': 6, 'assists': 10, 'points': 16, 'pims': 10, 'plus_minus': -6, 'gp': 36, 'age': 24, 'team_id': 14},
        {'first_name': 'Derek', 'last_name': 'Morris', 'position': 'D', 'number': 53, 'goals': 5, 'assists': 11, 'points': 16, 'pims': 58, 'plus_minus': -2, 'gp': 77, 'age': 32, 'team_id': 14},
        {'first_name': 'Ed', 'last_name': 'Jovanovski', 'position': 'D', 'number': 55, 'goals': 5, 'assists': 9, 'points': 14, 'pims': 39, 'plus_minus': 4, 'gp': 50, 'age': 34, 'team_id': 14},
        {'first_name': 'Mikkel', 'last_name': 'Boedker', 'position': 'L', 'number': 89, 'goals': 4, 'assists': 10, 'points': 14, 'pims': 8, 'plus_minus': 11, 'gp': 34, 'age': 20, 'team_id': 14},
        {'first_name': 'David', 'last_name': 'Schlemko', 'position': 'D', 'number': 6, 'goals': 4, 'assists': 10, 'points': 14, 'pims': 24, 'plus_minus': 8, 'gp': 43, 'age': 23, 'team_id': 14},
        {'first_name': 'Sami', 'last_name': 'Lepisto', 'position': 'D', 'number': 35, 'goals': 4, 'assists': 7, 'points': 11, 'pims': 37, 'plus_minus': 7, 'gp': 51, 'age': 25, 'team_id': 14},
        {'first_name': 'Oliver', 'last_name': 'Ekman-Larsson', 'position': 'D', 'number': 23, 'goals': 1, 'assists': 10, 'points': 11, 'pims': 24, 'plus_minus': 3, 'gp': 48, 'age': 19, 'team_id': 14},
        {'first_name': 'Michal', 'last_name': 'Rozsival', 'position': 'D', 'number': 32, 'goals': 3, 'assists': 3, 'points': 6, 'pims': 20, 'plus_minus': 3, 'gp': 33, 'age': 31, 'team_id': 14},
        {'first_name': 'Andrew', 'last_name': 'Ebbett', 'position': 'C', 'number': 26, 'goals': 2, 'assists': 3, 'points': 5, 'pims': 4, 'plus_minus': -1, 'gp': 33, 'age': 27, 'team_id': 14},
        {'first_name': 'Brett', 'last_name': 'MacLean', 'position': 'L', 'number': 39, 'goals': 2, 'assists': 1, 'points': 3, 'pims': 2, 'plus_minus': 0, 'gp': 13, 'age': 21, 'team_id': 14},
        {'first_name': 'Rostislav', 'last_name': 'Klesla', 'position': 'D', 'number': 16, 'goals': 1, 'assists': 0, 'points': 1, 'pims': 12, 'plus_minus': -6, 'gp': 16, 'age': 28, 'team_id': 14},
        {'first_name': 'Paul', 'last_name': 'Bissonnette', 'position': 'L', 'number': 12, 'goals': 1, 'assists': 0, 'points': 1, 'pims': 71, 'plus_minus': 6, 'gp': 48, 'age': 25, 'team_id': 14},
        {'first_name': 'Ilya', 'last_name': 'Bryzgalov', 'position': 'G', 'number': 30, 'wins': 36, 'gaa': 2.48, 'svp': .921, 'gp': 68, 'age': 30, 'team_id': 14},
        {'first_name': 'Jason', 'last_name': 'Labarbara', 'position': 'G', 'number': 1, 'wins': 7, 'gaa': 3.26, 'svp': .909, 'gp': 17, 'age': 30, 'team_id': 14}
    ]
    team15 = [
        {'first_name': 'Ray', 'last_name': 'Whitney', 'position': 'L', 'number': 13, 'goals': 24, 'assists': 53, 'points': 77, 'pims': 28, 'plus_minus': 26, 'gp': 82, 'age': 39, 'team_id': 15},
        {'first_name': 'Radim', 'last_name': 'Vrbata', 'position': 'R', 'number': 17, 'goals': 35, 'assists': 27, 'points': 62, 'pims': 24, 'plus_minus': 24, 'gp': 77, 'age': 30, 'team_id': 15},
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 22, 'assists': 28, 'points': 50, 'pims': 48, 'plus_minus': -8, 'gp': 79, 'age': 34, 'team_id': 15},
        {'first_name': 'Keith', 'last_name': 'Yandle', 'position': 'D', 'number': 3, 'goals': 11, 'assists': 32, 'points': 43, 'pims': 51, 'plus_minus': 5, 'gp': 82, 'age': 24, 'team_id': 15},
        {'first_name': 'Lauri', 'last_name': 'Korpikoski', 'position': 'L', 'number': 28, 'goals': 17, 'assists': 20, 'points': 37, 'pims': 14, 'plus_minus': 3, 'gp': 82, 'age': 25, 'team_id': 15},
        {'first_name': 'Martin', 'last_name': 'Hanzal', 'position': 'C', 'number': 11, 'goals': 8, 'assists': 26, 'points': 34, 'pims': 63, 'plus_minus': 12, 'gp': 64, 'age': 24, 'team_id': 15},
        {'first_name': 'Oliver', 'last_name': 'Ekman-Larsson', 'position': 'D', 'number': 23, 'goals': 13, 'assists': 19, 'points': 32, 'pims': 32, 'plus_minus': 0, 'gp': 82, 'age': 20, 'team_id': 15},
        {'first_name': 'Daymond', 'last_name': 'Langkow', 'position': 'C', 'number': 22, 'goals': 11, 'assists': 19, 'points': 30, 'pims': 14, 'plus_minus': -4, 'gp': 73, 'age': 34, 'team_id': 15},
        {'first_name': 'Raffi', 'last_name': 'Torres', 'position': 'L', 'number': 37, 'goals': 15, 'assists': 11, 'points': 26, 'pims': 83, 'plus_minus': 2, 'gp': 79, 'age': 29, 'team_id': 15},
        {'first_name': 'Mikkel', 'last_name': 'Boedker', 'position': 'L', 'number': 89, 'goals': 11, 'assists': 13, 'points': 24, 'pims': 12, 'plus_minus': -2, 'gp': 82, 'age': 21, 'team_id': 15},
        {'first_name': 'Boyd', 'last_name': 'Gordon', 'position': 'C', 'number': 15, 'goals': 8, 'assists': 15, 'points': 23, 'pims': 10, 'plus_minus': 9, 'gp': 75, 'age': 27, 'team_id': 15},
        {'first_name': 'Taylor', 'last_name': 'Pyatt', 'position': 'L', 'number': 14, 'goals': 9, 'assists': 10, 'points': 19, 'pims': 23, 'plus_minus': -4, 'gp': 73, 'age': 30, 'team_id': 15},
        {'first_name': 'Kyle', 'last_name': 'Chipchura', 'position': 'C', 'number': 24, 'goals': 3, 'assists': 13, 'points': 16, 'pims': 42, 'plus_minus': 2, 'gp': 53, 'age': 25, 'team_id': 15},
        {'first_name': 'Gilbert', 'last_name': 'Brule', 'position': 'C', 'number': 8, 'goals': 5, 'assists': 9, 'points': 14, 'pims': 11, 'plus_minus': 7, 'gp': 33, 'age': 24, 'team_id': 15},
        {'first_name': 'Rostislav', 'last_name': 'Klesla', 'position': 'D', 'number': 16, 'goals': 3, 'assists': 10, 'points': 13, 'pims': 54, 'plus_minus': 13, 'gp': 65, 'age': 29, 'team_id': 15},
        {'first_name': 'Michal', 'last_name': 'Rozsival', 'position': 'D', 'number': 32, 'goals': 1, 'assists': 12, 'points': 13, 'pims': 34, 'plus_minus': 8, 'gp': 54, 'age': 32, 'team_id': 15},
        {'first_name': 'Derek', 'last_name': 'Morris', 'position': 'D', 'number': 53, 'goals': 2, 'assists': 9, 'points': 11, 'pims': 38, 'plus_minus': -12, 'gp': 59, 'age': 33, 'team_id': 15},
        {'first_name': 'David', 'last_name': 'Schlemko', 'position': 'D', 'number': 6, 'goals': 1, 'assists': 10, 'points': 11, 'pims': 10, 'plus_minus': 7, 'gp': 46, 'age': 24, 'team_id': 15},
        {'first_name': 'Antoine', 'last_name': 'Vermette', 'position': 'C', 'number': 50, 'goals': 3, 'assists': 7, 'points': 10, 'pims': 16, 'plus_minus': 4, 'gp': 22, 'age': 29, 'team_id': 15},
        {'first_name': 'Adrian', 'last_name': 'Aucoin', 'position': 'D', 'number': 33, 'goals': 2, 'assists': 7, 'points': 9, 'pims': 42, 'plus_minus': 14, 'gp': 64, 'age': 38, 'team_id': 15},
        {'first_name': 'Cal', 'last_name': 'O\'Reilly', 'position': 'C', 'number': 26, 'goals': 2, 'assists': 3, 'points': 5, 'pims': 2, 'plus_minus': -5, 'gp': 22, 'age': 24, 'team_id': 15},
        {'first_name': 'Patrick', 'last_name': 'O\'Sullivan', 'position': 'L', 'number': 18, 'goals': 2, 'assists': 2, 'points': 4, 'pims': 2, 'plus_minus': -4, 'gp': 23, 'age': 26, 'team_id': 15},
        {'first_name': 'Marc-Antoine', 'last_name': 'Pouliot', 'position': 'C', 'number': 43, 'goals': 0, 'assists': 4, 'points': 4, 'pims': 2, 'plus_minus': -2, 'gp': 13, 'age': 26, 'team_id': 15},
        {'first_name': 'Michael', 'last_name': 'Stone', 'position': 'D', 'number': 26, 'goals': 1, 'assists': 2, 'points': 3, 'pims': 2, 'plus_minus': 7, 'gp': 13, 'age': 21, 'team_id': 15},
        {'first_name': 'Mike', 'last_name': 'Smith', 'position': 'G', 'number': 41, 'wins': 38, 'gaa': 2.21, 'svp': .930, 'gp': 67, 'age': 29, 'team_id': 15},
        {'first_name': 'Jason', 'last_name': 'Labarbara', 'position': 'G', 'number': 1, 'wins': 3, 'gaa': 2.54, 'svp': .911, 'gp': 19, 'age': 31, 'team_id': 15}
    ]
    team16 = [
        {'first_name': 'Keith', 'last_name': 'Yandle', 'position': 'D', 'number': 3, 'goals': 10, 'assists': 20, 'points': 30, 'pims': 54, 'plus_minus': 4, 'gp': 48, 'age': 25, 'team_id': 16},
        {'first_name': 'Radim', 'last_name': 'Vrbata', 'position': 'R', 'number': 17, 'goals': 12, 'assists': 16, 'points': 28, 'pims': 14, 'plus_minus': 6, 'gp': 34, 'age': 31, 'team_id': 16},
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 13, 'assists': 14, 'points': 27, 'pims': 37, 'plus_minus': 6, 'gp': 48, 'age': 35, 'team_id': 16},
        {'first_name': 'Mikkel', 'last_name': 'Boedker', 'position': 'L', 'number': 89, 'goals': 7, 'assists': 19, 'points': 26, 'pims': 12, 'plus_minus': 0, 'gp': 48, 'age': 22, 'team_id': 16},
        {'first_name': 'Oliver', 'last_name': 'Ekman-Larsson', 'position': 'D', 'number': 23, 'goals': 3, 'assists': 21, 'points': 24, 'pims': 26, 'plus_minus': 5, 'gp': 48, 'age': 21, 'team_id': 16},
        {'first_name': 'Martin', 'last_name': 'Hanzal', 'position': 'C', 'number': 11, 'goals': 11, 'assists': 12, 'points': 23, 'pims': 24, 'plus_minus': 2, 'gp': 39, 'age': 25, 'team_id': 16},
        {'first_name': 'Antoine', 'last_name': 'Vermette', 'position': 'C', 'number': 50, 'goals': 13, 'assists': 8, 'points': 21, 'pims': 36, 'plus_minus': -3, 'gp': 48, 'age': 30, 'team_id': 16},
        {'first_name': 'David', 'last_name': 'Moss', 'position': 'R', 'number': 18, 'goals': 5, 'assists': 15, 'points': 20, 'pims': 21, 'plus_minus': 3, 'gp': 45, 'age': 30, 'team_id': 16},
        {'first_name': 'Kyle', 'last_name': 'Chipchura', 'position': 'C', 'number': 24, 'goals': 5, 'assists': 9, 'points': 14, 'pims': 50, 'plus_minus': 1, 'gp': 46, 'age': 26, 'team_id': 16},
        {'first_name': 'Boyd', 'last_name': 'Gordon', 'position': 'C', 'number': 15, 'goals': 4, 'assists': 10, 'points': 14, 'pims': 8, 'plus_minus': 0, 'gp': 48, 'age': 28, 'team_id': 16},
        {'first_name': 'Raffi', 'last_name': 'Torres', 'position': 'L', 'number': 37, 'goals': 5, 'assists': 7, 'points': 12, 'pims': 13, 'plus_minus': -1, 'gp': 28, 'age': 30, 'team_id': 16},
        {'first_name': 'Steve', 'last_name': 'Sullivan', 'position': 'C', 'number': 26, 'goals': 5, 'assists': 7, 'points': 12, 'pims': 20, 'plus_minus': -8, 'gp': 33, 'age': 38, 'team_id': 16},
        {'first_name': 'Lauri', 'last_name': 'Korpikoski', 'position': 'L', 'number': 28, 'goals': 6, 'assists': 5, 'points': 11, 'pims': 12, 'plus_minus': -3, 'gp': 36, 'age': 26, 'team_id': 16},
        {'first_name': 'Rob', 'last_name': 'Klinkhammer', 'position': 'L', 'number': 36, 'goals': 5, 'assists': 6, 'points': 11, 'pims': 10, 'plus_minus': 7, 'gp': 22, 'age': 26, 'team_id': 16},
        {'first_name': 'Derek', 'last_name': 'Morris', 'position': 'D', 'number': 53, 'goals': 0, 'assists': 11, 'points': 11, 'pims': 36, 'plus_minus': -6, 'gp': 39, 'age': 34, 'team_id': 16},
        {'first_name': 'Michael', 'last_name': 'Stone', 'position': 'D', 'number': 29, 'goals': 5, 'assists': 4, 'points': 9, 'pims': 16, 'plus_minus': 2, 'gp': 40, 'age': 22, 'team_id': 16},
        {'first_name': 'Matthew', 'last_name': 'Lombardi', 'position': 'C', 'number': 8, 'goals': 4, 'assists': 4, 'points': 8, 'pims': 4, 'plus_minus': 0, 'gp': 21, 'age': 30, 'team_id': 16},
        {'first_name': 'Rostislav', 'last_name': 'Klesla', 'position': 'D', 'number': 16, 'goals': 2, 'assists': 6, 'points': 8, 'pims': 22, 'plus_minus': 0, 'gp': 38, 'age': 30, 'team_id': 16},
        {'first_name': 'Nick', 'last_name': 'Johnson', 'position': 'R', 'number': 32, 'goals': 4, 'assists': 2, 'points': 6, 'pims': 0, 'plus_minus': 3, 'gp': 17, 'age': 26, 'team_id': 16},
        {'first_name': 'David', 'last_name': 'Schlemko', 'position': 'D', 'number': 6, 'goals': 1, 'assists': 5, 'points': 6, 'pims': 12, 'plus_minus': 8, 'gp': 30, 'age': 25, 'team_id': 16},
        {'first_name': 'Paul', 'last_name': 'Bissonnette', 'position': 'L', 'number': 12, 'goals': 0, 'assists': 6, 'points': 6, 'pims': 36, 'plus_minus': 2, 'gp': 28, 'age': 27, 'team_id': 16},
        {'first_name': 'Chris', 'last_name': 'Conner', 'position': 'R', 'number': 14, 'goals': 1, 'assists': 1, 'points': 2, 'pims': 2, 'plus_minus': 3, 'gp': 12, 'age': 28, 'team_id': 16},
        {'first_name': 'Zbynek', 'last_name': 'Michalek', 'position': 'D', 'number': 4, 'goals': 0, 'assists': 2, 'points': 2, 'pims': 14, 'plus_minus': 4, 'gp': 34, 'age': 29, 'team_id': 16},
        {'first_name': 'David', 'last_name': 'Rundblad', 'position': 'D', 'number': 2, 'goals': 0, 'assists': 1, 'points': 1, 'pims': 0, 'plus_minus': -5, 'gp': 8, 'age': 21, 'team_id': 16},
        {'first_name': 'Mike', 'last_name': 'Smith', 'position': 'G', 'number': 41, 'wins': 15, 'gaa': 2.58, 'svp': .910, 'gp': 34, 'age': 30, 'team_id': 16},
        {'first_name': 'Jason', 'last_name': 'Labarbara', 'position': 'G', 'number': 1, 'wins': 4, 'gaa': 2.64, 'svp': .923, 'gp': 15, 'age': 32, 'team_id': 16}
    ]
    team17 = [
        {'first_name': 'Keith', 'last_name': 'Yandle', 'position': 'D', 'number': 3, 'goals': 8, 'assists': 45, 'points': 53, 'pims': 63, 'plus_minus': -23, 'gp': 82, 'age': 26, 'team_id': 17},
        {'first_name': 'Radim', 'last_name': 'Vrbata', 'position': 'R', 'number': 17, 'goals': 20, 'assists': 31, 'points': 51, 'pims': 22, 'plus_minus': -6, 'gp': 80, 'age': 32, 'team_id': 17},
        {'first_name': 'Mikkel', 'last_name': 'Boedker', 'position': 'L', 'number': 89, 'goals': 19, 'assists': 32, 'points': 51, 'pims': 20, 'plus_minus': -9, 'gp': 82, 'age': 23, 'team_id': 17},
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 23, 'assists': 24, 'points': 47, 'pims': 34, 'plus_minus': -7, 'gp': 69, 'age': 36, 'team_id': 17},
        {'first_name': 'Mike', 'last_name': 'Ribeiro', 'position': 'C', 'number': 63, 'goals': 16, 'assists': 31, 'points': 47, 'pims': 52, 'plus_minus': -13, 'gp': 80, 'age': 33, 'team_id': 17},
        {'first_name': 'Antoine', 'last_name': 'Vermette', 'position': 'C', 'number': 50, 'goals': 24, 'assists': 21, 'points': 45, 'pims': 44, 'plus_minus': 0, 'gp': 82, 'age': 31, 'team_id': 17},
        {'first_name': 'Oliver', 'last_name': 'Ekman-Larsson', 'position': 'D', 'number': 23, 'goals': 15, 'assists': 29, 'points': 44, 'pims': 50, 'plus_minus': -4, 'gp': 80, 'age': 22, 'team_id': 17},
        {'first_name': 'Martin', 'last_name': 'Hanzal', 'position': 'C', 'number': 11, 'goals': 15, 'assists': 25, 'points': 40, 'pims': 73, 'plus_minus': -9, 'gp': 65, 'age': 26, 'team_id': 17},
        {'first_name': 'Lauri', 'last_name': 'Korpikoski', 'position': 'L', 'number': 28, 'goals': 9, 'assists': 16, 'points': 25, 'pims': 24, 'plus_minus': -7, 'gp': 64, 'age': 27, 'team_id': 17},
        {'first_name': 'David', 'last_name': 'Moss', 'position': 'R', 'number': 18, 'goals': 8, 'assists': 14, 'points': 22, 'pims': 18, 'plus_minus': -1, 'gp': 79, 'age': 31, 'team_id': 17},
        {'first_name': 'Michael', 'last_name': 'Stone', 'position': 'D', 'number': 26, 'goals': 8, 'assists': 13, 'points': 21, 'pims': 38, 'plus_minus': -10, 'gp': 70, 'age': 23, 'team_id': 17},
        {'first_name': 'Rob', 'last_name': 'Klinkhammer', 'position': 'L', 'number': 36, 'goals': 11, 'assists': 9, 'points': 20, 'pims': 19, 'plus_minus': 6, 'gp': 72, 'age': 27, 'team_id': 17},
        {'first_name': 'Kyle', 'last_name': 'Chipchura', 'position': 'C', 'number': 24, 'goals': 5, 'assists': 15, 'points': 20, 'pims': 45, 'plus_minus': 3, 'gp': 80, 'age': 27, 'team_id': 17},
        {'first_name': 'Derek', 'last_name': 'Morris', 'position': 'D', 'number': 53, 'goals': 5, 'assists': 12, 'points': 17, 'pims': 41, 'plus_minus': -2, 'gp': 63, 'age': 35, 'team_id': 17},
        {'first_name': 'Jeff', 'last_name': 'Halpern', 'position': 'C', 'number': 14, 'goals': 5, 'assists': 7, 'points': 12, 'pims': 24, 'plus_minus': -8, 'gp': 69, 'age': 37, 'team_id': 17},
        {'first_name': 'Zbynek', 'last_name': 'Michalek', 'position': 'D', 'number': 4, 'goals': 2, 'assists': 8, 'points': 10, 'pims': 24, 'plus_minus': 6, 'gp': 59, 'age': 30, 'team_id': 17},
        {'first_name': 'David', 'last_name': 'Schlemko', 'position': 'D', 'number': 6, 'goals': 1, 'assists': 8, 'points': 9, 'pims': 18, 'plus_minus': 2, 'gp': 48, 'age': 26, 'team_id': 17},
        {'first_name': 'Tim', 'last_name': 'Kennedy', 'position': 'L', 'number': 34, 'goals': 2, 'assists': 6, 'points': 8, 'pims': 4, 'plus_minus': 0, 'gp': 37, 'age': 27, 'team_id': 17},
        {'first_name': 'Paul', 'last_name': 'Bissonnette', 'position': 'L', 'number': 12, 'goals': 2, 'assists': 6, 'points': 8, 'pims': 53, 'plus_minus': 6, 'gp': 39, 'age': 28, 'team_id': 17},
        {'first_name': 'Connor', 'last_name': 'Murphy', 'position': 'D', 'number': 5, 'goals': 1, 'assists': 7, 'points': 8, 'pims': 10, 'plus_minus': 5, 'gp': 30, 'age': 20, 'team_id': 17},
        {'first_name': 'Brandon', 'last_name': 'McMillan', 'position': 'L', 'number': 38, 'goals': 2, 'assists': 4, 'points': 6, 'pims': 4, 'plus_minus': 0, 'gp': 22, 'age': 23, 'team_id': 17},
        {'first_name': 'Martin', 'last_name': 'Erat', 'position': 'R', 'number': 10, 'goals': 2, 'assists': 3, 'points': 5, 'pims': 6, 'plus_minus': 4, 'gp': 17, 'age': 32, 'team_id': 17},
        {'first_name': 'Rostislav', 'last_name': 'Klesla', 'position': 'D', 'number': 16, 'goals': 1, 'assists': 3, 'points': 4, 'pims': 24, 'plus_minus': -3, 'gp': 25, 'age': 31, 'team_id': 17},
        {'first_name': 'Jordan', 'last_name': 'Szwarz', 'position': 'C', 'number': 29, 'goals': 3, 'assists': 0, 'points': 3, 'pims': 19, 'plus_minus': -6, 'gp': 26, 'age': 22, 'team_id': 17},
        {'first_name': 'Mike', 'last_name': 'Smith', 'position': 'G', 'number': 41, 'wins': 27, 'gaa': 2.54, 'svp': .916, 'gp': 62, 'age': 31, 'team_id': 17},
        {'first_name': 'Thomas', 'last_name': 'Greiss', 'position': 'G', 'number': 1, 'wins': 10, 'gaa': 2.29, 'svp': .920, 'gp': 25, 'age': 27, 'team_id': 17}
    ]
    team18 = [
        {'first_name': 'Oliver', 'last_name': 'Ekman-Larsson', 'position': 'D', 'number': 23, 'goals': 23, 'assists': 20, 'points': 43, 'pims': 40, 'plus_minus': -18, 'gp': 82, 'age': 23, 'team_id': 18},
        {'first_name': 'Sam', 'last_name': 'Gagner', 'position': 'C', 'number': 9, 'goals': 15, 'assists': 26, 'points': 41, 'pims': 28, 'plus_minus': -28, 'gp': 81, 'age': 25, 'team_id': 18},
        {'first_name': 'Keith', 'last_name': 'Yandle', 'position': 'D', 'number': 3, 'goals': 4, 'assists': 37, 'points': 41, 'pims': 32, 'plus_minus': -32, 'gp': 63, 'age': 27, 'team_id': 18},
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 14, 'assists': 22, 'points': 36, 'pims': 65, 'plus_minus': -29, 'gp': 79, 'age': 37, 'team_id': 18},
        {'first_name': 'Antoine', 'last_name': 'Vermette', 'position': 'C', 'number': 50, 'goals': 13, 'assists': 22, 'points': 35, 'pims': 34, 'plus_minus': -23, 'gp': 63, 'age': 32, 'team_id': 18},
        {'first_name': 'Martin', 'last_name': 'Erat', 'position': 'R', 'number': 10, 'goals': 9, 'assists': 23, 'points': 32, 'pims': 48, 'plus_minus': -16, 'gp': 79, 'age': 33, 'team_id': 18},
        {'first_name': 'Mikkel', 'last_name': 'Boedker', 'position': 'L', 'number': 89, 'goals': 14, 'assists': 14, 'points': 28, 'pims': 6, 'plus_minus': -10, 'gp': 45, 'age': 24, 'team_id': 18},
        {'first_name': 'Martin', 'last_name': 'Hanzal', 'position': 'C', 'number': 11, 'goals': 8, 'assists': 16, 'points': 24, 'pims': 31, 'plus_minus': -1, 'gp': 37, 'age': 27, 'team_id': 18},
        {'first_name': 'Tobias', 'last_name': 'Rieder', 'position': 'C', 'number': 9, 'goals': 13, 'assists': 8, 'points': 21, 'pims': 14, 'plus_minus': -19, 'gp': 72, 'age': 21, 'team_id': 18},
        {'first_name': 'Lauri', 'last_name': 'Korpikoski', 'position': 'L', 'number': 28, 'goals': 6, 'assists': 15, 'points': 21, 'pims': 12, 'plus_minus': -27, 'gp': 69, 'age': 28, 'team_id': 18},
        {'first_name': 'Michael', 'last_name': 'Stone', 'position': 'D', 'number': 26, 'goals': 3, 'assists': 15, 'points': 18, 'pims': 60, 'plus_minus': -24, 'gp': 81, 'age': 24, 'team_id': 18},
        {'first_name': 'Mark', 'last_name': 'Arcobello', 'position': 'F', 'number': 36, 'goals': 9, 'assists': 7, 'points': 16, 'pims': 6, 'plus_minus': -4, 'gp': 27, 'age': 26, 'team_id': 18},
        {'first_name': 'Kyle', 'last_name': 'Chipchura', 'position': 'C', 'number': 24, 'goals': 4, 'assists': 10, 'points': 14, 'pims': 82, 'plus_minus': -23, 'gp': 70, 'age': 28, 'team_id': 18},
        {'first_name': 'David', 'last_name': 'Moss', 'position': 'R', 'number': 18, 'goals': 4, 'assists': 8, 'points': 12, 'pims': 24, 'plus_minus': -18, 'gp': 60, 'age': 32, 'team_id': 18},
        {'first_name': 'Joe', 'last_name': 'Vitale', 'position': 'C', 'number': 14, 'goals': 3, 'assists': 6, 'points': 9, 'pims': 36, 'plus_minus': -11, 'gp': 70, 'age': 29, 'team_id': 18},
        {'first_name': 'Zbynek', 'last_name': 'Michalek', 'position': 'D', 'number': 4, 'goals': 2, 'assists': 6, 'points': 8, 'pims': 12, 'plus_minus': -6, 'gp': 53, 'age': 31, 'team_id': 18},
        {'first_name': 'Connor', 'last_name': 'Murphy', 'position': 'D', 'number': 5, 'goals': 4, 'assists': 3, 'points': 7, 'pims': 42, 'plus_minus': -27, 'gp': 73, 'age': 21, 'team_id': 18},
        {'first_name': 'B.J.', 'last_name': 'Crombeen', 'position': 'R', 'number': 44, 'goals': 3, 'assists': 3, 'points': 6, 'pims': 79, 'plus_minus': -6, 'gp': 58, 'age': 29, 'team_id': 18},
        {'first_name': 'Lucas', 'last_name': 'Lessio', 'position': 'L', 'number': 38, 'goals': 2, 'assists': 3, 'points': 5, 'pims': 8, 'plus_minus': -10, 'gp': 26, 'age': 21, 'team_id': 18},
        {'first_name': 'John', 'last_name': 'Moore', 'position': 'D', 'number': 17, 'goals': 1, 'assists': 4, 'points': 5, 'pims': 11, 'plus_minus': -11, 'gp': 19, 'age': 23, 'team_id': 18},
        {'first_name': 'Brandon', 'last_name': 'Gormley', 'position': 'D', 'number': 33, 'goals': 2, 'assists': 2, 'points': 4, 'pims': 10, 'plus_minus': -7, 'gp': 27, 'age': 22, 'team_id': 18},
        {'first_name': 'Craig', 'last_name': 'Cunningham', 'position': 'R', 'number': 22, 'goals': 1, 'assists': 3, 'points': 4, 'pims': 2, 'plus_minus': -3, 'gp': 19, 'age': 23, 'team_id': 18},
        {'first_name': 'David', 'last_name': 'Schlemko', 'position': 'D', 'number': 6, 'goals': 1, 'assists': 3, 'points': 4, 'pims': 4, 'plus_minus': -5, 'gp': 20, 'age': 27, 'team_id': 18},
        {'first_name': 'Rob', 'last_name': 'Klinkhammer', 'position': 'L', 'number': 36, 'goals': 3, 'assists': 0, 'points': 3, 'pims': 4, 'plus_minus': 3, 'gp': 19, 'age': 28, 'team_id': 18},
        {'first_name': 'Brandon', 'last_name': 'McMillan', 'position': 'L', 'number': 22, 'goals': 1, 'assists': 2, 'points': 3, 'pims': 16, 'plus_minus': -18, 'gp': 50, 'age': 24, 'team_id': 18},
        {'first_name': 'Mike', 'last_name': 'Smith', 'position': 'G', 'number': 41, 'wins': 14, 'gaa': 3.16, 'svp': .904, 'gp': 62, 'age': 32, 'team_id': 18},
        {'first_name': 'Devan', 'last_name': 'Dubnyk', 'position': 'G', 'number': 40, 'wins': 9, 'gaa': 2.72, 'svp': .916, 'gp': 19, 'age': 28, 'team_id': 18},
        {'first_name': 'Louis', 'last_name': 'Domingue', 'position': 'G', 'number': 35, 'wins': 1, 'gaa': 2.73, 'svp': .911, 'gp': 7, 'age': 22, 'team_id': 18}
    ]
    team19 = [
        {'first_name': 'Oliver', 'last_name': 'Ekman-Larsson', 'position': 'D', 'number': 23, 'goals': 21, 'assists': 34, 'points': 55, 'pims': 96, 'plus_minus': -6, 'gp': 75, 'age': 24, 'team_id': 19},
        {'first_name': 'Max', 'last_name': 'Domi', 'position': 'C', 'number': 16, 'goals': 18, 'assists': 34, 'points': 52, 'pims': 72, 'plus_minus': 3, 'gp': 81, 'age': 20, 'team_id': 19},
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 28, 'assists': 19, 'points': 47, 'pims': 98, 'plus_minus': 4, 'gp': 72, 'age': 38, 'team_id': 19},
        {'first_name': 'Anthony', 'last_name': 'Duclair', 'position': 'L', 'number': 10, 'goals': 20, 'assists': 24, 'points': 44, 'pims': 49, 'plus_minus': 12, 'gp': 81, 'age': 20, 'team_id': 19},
        {'first_name': 'Martin', 'last_name': 'Hanzal', 'position': 'C', 'number': 11, 'goals': 13, 'assists': 28, 'points': 41, 'pims': 77, 'plus_minus': -5, 'gp': 64, 'age': 28, 'team_id': 19},
        {'first_name': 'Mikkel', 'last_name': 'Boedker', 'position': 'L', 'number': 89, 'goals': 13, 'assists': 26, 'points': 39, 'pims': 10, 'plus_minus': -28, 'gp': 62, 'age': 25, 'team_id': 19},
        {'first_name': 'Antoine', 'last_name': 'Vermette', 'position': 'C', 'number': 50, 'goals': 17, 'assists': 21, 'points': 38, 'pims': 93, 'plus_minus': -14, 'gp': 76, 'age': 33, 'team_id': 19},
        {'first_name': 'Tobias', 'last_name': 'Rieder', 'position': 'C', 'number': 8, 'goals': 14, 'assists': 23, 'points': 37, 'pims': 10, 'plus_minus': -21, 'gp': 82, 'age': 22, 'team_id': 19},
        {'first_name': 'Michael', 'last_name': 'Stone', 'position': 'D', 'number': 26, 'goals': 6, 'assists': 30, 'points': 36, 'pims': 62, 'plus_minus': -10, 'gp': 75, 'age': 25, 'team_id': 19},
        {'first_name': 'Brad', 'last_name': 'Richardson', 'position': 'R', 'number': 12, 'goals': 11, 'assists': 20, 'points': 31, 'pims': 46, 'plus_minus': 8, 'gp': 82, 'age': 30, 'team_id': 19},
        {'first_name': 'Jordan', 'last_name': 'Martinook', 'position': 'L', 'number': 48, 'goals': 9, 'assists': 15, 'points': 24, 'pims': 18, 'plus_minus': -9, 'gp': 81, 'age': 23, 'team_id': 19},
        {'first_name': 'Connor', 'last_name': 'Murphy', 'position': 'D', 'number': 5, 'goals': 6, 'assists': 11, 'points': 17, 'pims': 48, 'plus_minus': 5, 'gp': 78, 'age': 22, 'team_id': 19},
        {'first_name': 'Alex', 'last_name': 'Tanguay', 'position': 'L', 'number': 40, 'goals': 4, 'assists': 9, 'points': 13, 'pims': 8, 'plus_minus': 5, 'gp': 18, 'age': 35, 'team_id': 19},
        {'first_name': 'Kyle', 'last_name': 'Chipchura', 'position': 'C', 'number': 24, 'goals': 4, 'assists': 8, 'points': 12, 'pims': 38, 'plus_minus': -10, 'gp': 70, 'age': 29, 'team_id': 19},
        {'first_name': 'Kevin', 'last_name': 'Connauton', 'position': 'D', 'number': 44, 'goals': 4, 'assists': 5, 'points': 9, 'pims': 39, 'plus_minus': -3, 'gp': 38, 'age': 25, 'team_id': 19},
        {'first_name': 'Klas', 'last_name': 'Dahlbeck', 'position': 'D', 'number': 34, 'goals': 2, 'assists': 6, 'points': 8, 'pims': 28, 'plus_minus': -5, 'gp': 71, 'age': 24, 'team_id': 19},
        {'first_name': 'Nicklas', 'last_name': 'Grossmann', 'position': 'D', 'number': 2, 'goals': 3, 'assists': 4, 'points': 7, 'pims': 24, 'plus_minus': -3, 'gp': 58, 'age': 30, 'team_id': 19},
        {'first_name': 'Zbynek', 'last_name': 'Michalek', 'position': 'D', 'number': 4, 'goals': 2, 'assists': 5, 'points': 7, 'pims': 20, 'plus_minus': 3, 'gp': 70, 'age': 32, 'team_id': 19},
        {'first_name': 'Steve', 'last_name': 'Downie', 'position': 'R', 'number': 17, 'goals': 3, 'assists': 3, 'points': 6, 'pims': 53, 'plus_minus': 1, 'gp': 26, 'age': 28, 'team_id': 19},
        {'first_name': 'Viktor', 'last_name': 'Tikhonov', 'position': 'L', 'number': 9, 'goals': 3, 'assists': 3, 'points': 6, 'pims': 14, 'plus_minus': -6, 'gp': 39, 'age': 27, 'team_id': 19},
        {'first_name': 'Stefan', 'last_name': 'Elliott', 'position': 'D', 'number': 45, 'goals': 2, 'assists': 4, 'points': 6, 'pims': 4, 'plus_minus': -2, 'gp': 19, 'age': 24, 'team_id': 19},
        {'first_name': 'Boyd', 'last_name': 'Gordon', 'position': 'C', 'number': 15, 'goals': 2, 'assists': 2, 'points': 4, 'pims': 10, 'plus_minus': -7, 'gp': 65, 'age': 31, 'team_id': 19},
        {'first_name': 'Tyler', 'last_name': 'Gaudet', 'position': 'C', 'number': 32, 'goals': 1, 'assists': 2, 'points': 3, 'pims': 0, 'plus_minus': -2, 'gp': 14, 'age': 22, 'team_id': 19},
        {'first_name': 'Dustin', 'last_name': 'Jeffrey', 'position': 'C', 'number': 37, 'goals': 1, 'assists': 1, 'points': 2, 'pims': 2, 'plus_minus': 2, 'gp': 7, 'age': 27, 'team_id': 19},
        {'first_name': 'Mike', 'last_name': 'Smith', 'position': 'G', 'number': 41, 'wins': 15, 'gaa': 2.63, 'svp': .916, 'gp': 32, 'age': 33, 'team_id': 19},
        {'first_name': 'Anders', 'last_name': 'Lindback', 'position': 'G', 'number': 29, 'wins': 5, 'gaa': 3.11, 'svp': .894, 'gp': 19, 'age': 27, 'team_id': 19},
        {'first_name': 'Louis', 'last_name': 'Domingue', 'position': 'G', 'number': 35, 'wins': 15, 'gaa': 2.75, 'svp': .912, 'gp': 39, 'age': 23, 'team_id': 19}
    ]
    team20 = [
        {'first_name': 'Radim', 'last_name': 'Vrbata', 'position': 'R', 'number': 17, 'goals': 20, 'assists': 35, 'points': 55, 'pims': 16, 'plus_minus': -18, 'gp': 81, 'age': 35, 'team_id': 20},
        {'first_name': 'Oliver', 'last_name': 'Ekman-Larsson', 'position': 'D', 'number': 23, 'goals': 12, 'assists': 27, 'points': 39, 'pims': 48, 'plus_minus': -25, 'gp': 79, 'age': 25, 'team_id': 20},
        {'first_name': 'Max', 'last_name': 'Domi', 'position': 'C', 'number': 16, 'goals': 9, 'assists': 29, 'points': 38, 'pims': 40, 'plus_minus': -9, 'gp': 59, 'age': 21, 'team_id': 20},
        {'first_name': 'Alex', 'last_name': 'Goligoski', 'position': 'D', 'number': 33, 'goals': 6, 'assists': 30, 'points': 36, 'pims': 28, 'plus_minus': -9, 'gp': 82, 'age': 31, 'team_id': 20},
        {'first_name': 'Tobias', 'last_name': 'Rieder', 'position': 'C', 'number': 8, 'goals': 16, 'assists': 18, 'points': 34, 'pims': 6, 'plus_minus': -8, 'gp': 80, 'age': 23, 'team_id': 20},
        {'first_name': 'Christian', 'last_name': 'Dvorak', 'position': 'C', 'number': 18, 'goals': 15, 'assists': 18, 'points': 33, 'pims': 22, 'plus_minus': 7, 'gp': 78, 'age': 20, 'team_id': 20},
        {'first_name': 'Shane', 'last_name': 'Doan', 'position': 'R', 'number': 19, 'goals': 6, 'assists': 21, 'points': 27, 'pims': 48, 'plus_minus': -3, 'gp': 74, 'age': 39, 'team_id': 20},
        {'first_name': 'Martin', 'last_name': 'Hanzal', 'position': 'C', 'number': 11, 'goals': 16, 'assists': 10, 'points': 26, 'pims': 43, 'plus_minus': -15, 'gp': 51, 'age': 29, 'team_id': 20},
        {'first_name': 'Jordan', 'last_name': 'Martinook', 'position': 'L', 'number': 48, 'goals': 11, 'assists': 14, 'points': 25, 'pims': 40, 'plus_minus': -8, 'gp': 77, 'age': 24, 'team_id': 20},
        {'first_name': 'Brendan', 'last_name': 'Perlini', 'position': 'L', 'number': 29, 'goals': 14, 'assists': 7, 'points': 21, 'pims': 20, 'plus_minus': -4, 'gp': 57, 'age': 20, 'team_id': 20},
        {'first_name': 'Jakob', 'last_name': 'Chychrun', 'position': 'D', 'number': 6, 'goals': 7, 'assists': 13, 'points': 20, 'pims': 47, 'plus_minus': -14, 'gp': 68, 'age': 18, 'team_id': 20},
        {'first_name': 'Jamie', 'last_name': 'McGinn', 'position': 'L', 'number': 88, 'goals': 9, 'assists': 8, 'points': 17, 'pims': 23, 'plus_minus': -23, 'gp': 72, 'age': 28, 'team_id': 20},
        {'first_name': 'Connor', 'last_name': 'Murphy', 'position': 'D', 'number': 5, 'goals': 2, 'assists': 15, 'points': 17, 'pims': 45, 'plus_minus': -13, 'gp': 77, 'age': 23, 'team_id': 20},
        {'first_name': 'Anthony', 'last_name': 'Duclair', 'position': 'L', 'number': 10, 'goals': 5, 'assists': 10, 'points': 15, 'pims': 14, 'plus_minus': -7, 'gp': 58, 'age': 21, 'team_id': 20},
        {'first_name': 'Alexander', 'last_name': 'Burmistrov', 'position': 'C', 'number': 91, 'goals': 5, 'assists': 9, 'points': 14, 'pims': 6, 'plus_minus': -1, 'gp': 26, 'age': 24, 'team_id': 20},
        {'first_name': 'Tony', 'last_name': 'DeAngelo', 'position': 'D', 'number': 77, 'goals': 5, 'assists': 9, 'points': 14, 'pims': 37, 'plus_minus': -13, 'gp': 39, 'age': 20, 'team_id': 20},
        {'first_name': 'Ryan', 'last_name': 'White', 'position': 'C', 'number': 25, 'goals': 7, 'assists': 6, 'points': 13, 'pims': 70, 'plus_minus': -8, 'gp': 46, 'age': 28, 'team_id': 20},
        {'first_name': 'Lawson', 'last_name': 'Crouse', 'position': 'L', 'number': 67, 'goals': 5, 'assists': 7, 'points': 12, 'pims': 48, 'plus_minus': -20, 'gp': 72, 'age': 19, 'team_id': 20},
        {'first_name': 'Peter', 'last_name': 'Holland', 'position': 'C', 'number': 24, 'goals': 5, 'assists': 6, 'points': 11, 'pims': 18, 'plus_minus': -14, 'gp': 40, 'age': 26, 'team_id': 20},
        {'first_name': 'Josh', 'last_name': 'Jooris', 'position': 'R', 'number': 86, 'goals': 3, 'assists': 7, 'points': 10, 'pims': 10, 'plus_minus': -3, 'gp': 42, 'age': 26, 'team_id': 20},
        {'first_name': 'Brad', 'last_name': 'Richardson', 'position': 'R', 'number': 15, 'goals': 5, 'assists': 4, 'points': 9, 'pims': 15, 'plus_minus': -1, 'gp': 16, 'age': 31, 'team_id': 20},
        {'first_name': 'Michael', 'last_name': 'Stone', 'position': 'D', 'number': 26, 'goals': 1, 'assists': 8, 'points': 9, 'pims': 12, 'plus_minus': -5, 'gp': 45, 'age': 26, 'team_id': 20},
        {'first_name': 'Luke', 'last_name': 'Schenn', 'position': 'D', 'number': 2, 'goals': 1, 'assists': 7, 'points': 8, 'pims': 85, 'plus_minus': -9, 'gp': 78, 'age': 26, 'team_id': 20},
        {'first_name': 'Christian', 'last_name': 'Fischer', 'position': 'R', 'number': 36, 'goals': 3, 'assists': 0, 'points': 3, 'pims': 0, 'plus_minus': 0, 'gp': 7, 'age': 19, 'team_id': 20},
        {'first_name': 'Mike', 'last_name': 'Smith', 'position': 'G', 'number': 41, 'wins': 19, 'gaa': 2.92, 'svp': .914, 'gp': 55, 'age': 34, 'team_id': 20},
        {'first_name': 'Louis', 'last_name': 'Domingue', 'position': 'G', 'number': 35, 'wins': 11, 'gaa': 3.08, 'svp': .908, 'gp': 31, 'age': 24, 'team_id': 20}
    ]
    team21 = [
        {'first_name': 'Clayton', 'last_name': 'Keller', 'position': 'C', 'number': 9, 'goals': 23, 'assists': 42, 'points': 65, 'pims': 26, 'plus_minus': -7, 'gp': 82, 'age': 19, 'team_id': 21},
        {'first_name': 'Derek', 'last_name': 'Stepan', 'position': 'C', 'number': 21, 'goals': 14, 'assists': 42, 'points': 56, 'pims': 20, 'plus_minus': -13, 'gp': 82, 'age': 27, 'team_id': 21},
        {'first_name': 'Oliver', 'last_name': 'Ekman-Larsson', 'position': 'D', 'number': 23, 'goals': 14, 'assists': 28, 'points': 42, 'pims': 64, 'plus_minus': -28, 'gp': 82, 'age': 26, 'team_id': 21},
        {'first_name': 'Christian', 'last_name': 'Dvorak', 'position': 'C', 'number': 18, 'goals': 15, 'assists': 22, 'points': 37, 'pims': 22, 'plus_minus': -19, 'gp': 78, 'age': 21, 'team_id': 21},
        {'first_name': 'Alex', 'last_name': 'Goligoski', 'position': 'D', 'number': 33, 'goals': 12, 'assists': 23, 'points': 35, 'pims': 26, 'plus_minus': -31, 'gp': 78, 'age': 32, 'team_id': 21},
        {'first_name': 'Christian', 'last_name': 'Fischer', 'position': 'R', 'number': 36, 'goals': 15, 'assists': 18, 'points': 33, 'pims': 14, 'plus_minus': -17, 'gp': 79, 'age': 20, 'team_id': 21},
        {'first_name': 'Brendan', 'last_name': 'Perlini', 'position': 'L', 'number': 11, 'goals': 17, 'assists': 13, 'points': 30, 'pims': 28, 'plus_minus': -2, 'gp': 74, 'age': 21, 'team_id': 21},
        {'first_name': 'Kevin', 'last_name': 'Connauton', 'position': 'D', 'number': 44, 'goals': 11, 'assists': 10, 'points': 21, 'pims': 20, 'plus_minus': 3, 'gp': 73, 'age': 27, 'team_id': 21},
        {'first_name': 'Jason', 'last_name': 'Demers', 'position': 'D', 'number': 55, 'goals': 6, 'assists': 14, 'points': 20, 'pims': 37, 'plus_minus': -4, 'gp': 69, 'age': 29, 'team_id': 21},
        {'first_name': 'Nick', 'last_name': 'Cousins', 'position': 'C', 'number': 25, 'goals': 12, 'assists': 7, 'points': 19, 'pims': 31, 'plus_minus': -7, 'gp': 71, 'age': 24, 'team_id': 21},
        {'first_name': 'Richard', 'last_name': 'Panik', 'position': 'R', 'number': 14, 'goals': 8, 'assists': 11, 'points': 19, 'pims': 12, 'plus_minus': 4, 'gp': 35, 'age': 27, 'team_id': 21},
        {'first_name': 'Tobias', 'last_name': 'Rieder', 'position': 'C', 'number': 8, 'goals': 8, 'assists': 11, 'points': 19, 'pims': 6, 'plus_minus': -11, 'gp': 58, 'age': 24, 'team_id': 21},
        {'first_name': 'Anthony', 'last_name': 'Duclair', 'position': 'L', 'number': 10, 'goals': 9, 'assists': 6, 'points': 15, 'pims': 10, 'plus_minus': -5, 'gp': 33, 'age': 22, 'team_id': 21},
        {'first_name': 'Jordan', 'last_name': 'Martinook', 'position': 'L', 'number': 48, 'goals': 6, 'assists': 9, 'points': 15, 'pims': 45, 'plus_minus': -24, 'gp': 81, 'age': 25, 'team_id': 21},
        {'first_name': 'Brad', 'last_name': 'Richardson', 'position': 'R', 'number': 15, 'goals': 3, 'assists': 12, 'points': 15, 'pims': 45, 'plus_minus': -24, 'gp': 76, 'age': 32, 'team_id': 21},
        {'first_name': 'Jakob', 'last_name': 'Chychrun', 'position': 'D', 'number': 6, 'goals': 4, 'assists': 10, 'points': 14, 'pims': 16, 'plus_minus': 2, 'gp': 50, 'age': 19, 'team_id': 21},
        {'first_name': 'Josh', 'last_name': 'Archibald', 'position': 'R', 'number': 45, 'goals': 5, 'assists': 6, 'points': 11, 'pims': 25, 'plus_minus': -2, 'gp': 39, 'age': 24, 'team_id': 21},
        {'first_name': 'Dylan', 'last_name': 'Strome', 'position': 'C', 'number': 20, 'goals': 4, 'assists': 5, 'points': 9, 'pims': 8, 'plus_minus': 4, 'gp': 21, 'age': 20, 'team_id': 21},
        {'first_name': 'Niklas', 'last_name': 'Hjalmarsson', 'position': 'D', 'number': 4, 'goals': 1, 'assists': 8, 'points': 9, 'pims': 18, 'plus_minus': -3, 'gp': 48, 'age': 30, 'team_id': 21},
        {'first_name': 'Zac', 'last_name': 'Rinaldo', 'position': 'C', 'number': 14, 'goals': 5, 'assists': 2, 'points': 7, 'pims': 44, 'plus_minus': -7, 'gp': 53, 'age': 27, 'team_id': 21},
        {'first_name': 'Luke', 'last_name': 'Schenn', 'position': 'D', 'number': 2, 'goals': 1, 'assists': 6, 'points': 7, 'pims': 35, 'plus_minus': -12, 'gp': 64, 'age': 27, 'team_id': 21},
        {'first_name': 'Mario', 'last_name': 'Kempe', 'position': 'R', 'number': 18, 'goals': 2, 'assists': 2, 'points': 4, 'pims': 4, 'plus_minus': -1, 'gp': 18, 'age': 29, 'team_id': 21},
        {'first_name': 'Trevor', 'last_name': 'Murphy', 'position': 'D', 'number': 46, 'goals': 1, 'assists': 2, 'points': 3, 'pims': 0, 'plus_minus': 5, 'gp': 8, 'age': 23, 'team_id': 21},
        {'first_name': 'Adam', 'last_name': 'Clendening', 'position': 'D', 'number': 5, 'goals': 0, 'assists': 2, 'points': 2, 'pims': 2, 'plus_minus': -1, 'gp': 5, 'age': 25, 'team_id': 21},
        {'first_name': 'Antti', 'last_name': 'Raanta', 'position': 'G', 'number': 32, 'wins': 21, 'gaa': 2.24, 'svp': .930, 'gp': 47, 'age': 28, 'team_id': 21},
        {'first_name': 'Scott', 'last_name': 'Wedgewood', 'position': 'G', 'number': 31, 'wins': 5, 'gaa': 3.45, 'svp': .893, 'gp': 20, 'age': 25, 'team_id': 21},
        {'first_name': 'Darcy', 'last_name': 'Kuemper', 'position': 'G', 'number': 35, 'wins': 2, 'gaa': 3.22, 'svp': .899, 'gp': 10, 'age': 27, 'team_id': 21}
    ]
    team22 = [
        {'first_name': 'Clayton', 'last_name': 'Keller', 'position': 'C', 'number': 9, 'goals': 14, 'assists': 33, 'points': 47, 'pims': 14, 'plus_minus': -21, 'gp': 82, 'age': 20, 'team_id': 22},
        {'first_name': 'Oliver', 'last_name': 'Ekman-Larsson', 'position': 'D', 'number': 23, 'goals': 14, 'assists': 30, 'points': 44, 'pims': 52, 'plus_minus': -16, 'gp': 81, 'age': 27, 'team_id': 22},
        {'first_name': 'Alex', 'last_name': 'Galchenyuk', 'position': 'C', 'number': 17, 'goals': 19, 'assists': 22, 'points': 41, 'pims': 34, 'plus_minus': -19, 'gp': 72, 'age': 24, 'team_id': 22},
        {'first_name': 'Vinny', 'last_name': 'Hinostroza', 'position': 'C', 'number': 13, 'goals': 16, 'assists': 23, 'points': 39, 'pims': 14, 'plus_minus': -4, 'gp': 72, 'age': 24, 'team_id': 22},
        {'first_name': 'Derek', 'last_name': 'Stepan', 'position': 'C', 'number': 21, 'goals': 15, 'assists': 20, 'points': 35, 'pims': 14, 'plus_minus': -2, 'gp': 72, 'age': 28, 'team_id': 22},
        {'first_name': 'Richard', 'last_name': 'Panik', 'position': 'R', 'number': 14, 'goals': 14, 'assists': 19, 'points': 33, 'pims': 44, 'plus_minus': -3, 'gp': 75, 'age': 27, 'team_id': 22},
        {'first_name': 'Brad', 'last_name': 'Richardson', 'position': 'R', 'number': 15, 'goals': 19, 'assists': 8, 'points': 27, 'pims': 22, 'plus_minus': 6, 'gp': 66, 'age': 33, 'team_id': 22},
        {'first_name': 'Nick', 'last_name': 'Cousins', 'position': 'C', 'number': 25, 'goals': 7, 'assists': 20, 'points': 27, 'pims': 35, 'plus_minus': -8, 'gp': 81, 'age': 25, 'team_id': 22},
        {'first_name': 'Alex', 'last_name': 'Goligoski', 'position': 'D', 'number': 33, 'goals': 3, 'assists': 24, 'points': 27, 'pims': 16, 'plus_minus': -7, 'gp': 76, 'age': 33, 'team_id': 22},
        {'first_name': 'Lawson', 'last_name': 'Crouse', 'position': 'L', 'number': 67, 'goals': 11, 'assists': 14, 'points': 25, 'pims': 67, 'plus_minus': 5, 'gp': 81, 'age': 21, 'team_id': 22},
        {'first_name': 'Josh', 'last_name': 'Archibald', 'position': 'R', 'number': 45, 'goals': 12, 'assists': 10, 'points': 22, 'pims': 15, 'plus_minus': 1, 'gp': 68, 'age': 25, 'team_id': 22},
        {'first_name': 'Jordan', 'last_name': 'Oesterle', 'position': 'D', 'number': 82, 'goals': 6, 'assists': 14, 'points': 20, 'pims': 12, 'plus_minus': -3, 'gp': 71, 'age': 26, 'team_id': 22},
        {'first_name': 'Jakob', 'last_name': 'Chychrun', 'position': 'D', 'number': 6, 'goals': 5, 'assists': 15, 'points': 20, 'pims': 28, 'plus_minus': -12, 'gp': 53, 'age': 20, 'team_id': 22},
        {'first_name': 'Conor', 'last_name': 'Garland', 'position': 'R', 'number': 83, 'goals': 13, 'assists': 5, 'points': 18, 'pims': 12, 'plus_minus': 1, 'gp': 47, 'age': 22, 'team_id': 22},
        {'first_name': 'Christian', 'last_name': 'Fischer', 'position': 'R', 'number': 36, 'goals': 11, 'assists': 7, 'points': 18, 'pims': 27, 'plus_minus': -13, 'gp': 71, 'age': 21, 'team_id': 22},
        {'first_name': 'Michael', 'last_name': 'Grabner', 'position': 'R', 'number': 40, 'goals': 9, 'assists': 7, 'points': 16, 'pims': 8, 'plus_minus': -2, 'gp': 41, 'age': 30, 'team_id': 22},
        {'first_name': 'Nick', 'last_name': 'Schmaltz', 'position': 'C', 'number': 8, 'goals': 5, 'assists': 9, 'points': 14, 'pims': 2, 'plus_minus': -8, 'gp': 17, 'age': 22, 'team_id': 22},
        {'first_name': 'Niklas', 'last_name': 'Hjalmarsson', 'position': 'D', 'number': 4, 'goals': 0, 'assists': 10, 'points': 10, 'pims': 44, 'plus_minus': 8, 'gp': 82, 'age': 31, 'team_id': 22},
        {'first_name': 'Mario', 'last_name': 'Kempe', 'position': 'R', 'number': 29, 'goals': 4, 'assists': 5, 'points': 9, 'pims': 18, 'plus_minus': 5, 'gp': 52, 'age': 29, 'team_id': 22},
        {'first_name': 'Jason', 'last_name': 'Demers', 'position': 'D', 'number': 55, 'goals': 2, 'assists': 6, 'points': 8, 'pims': 12, 'plus_minus': 9, 'gp': 35, 'age': 30, 'team_id': 22},
        {'first_name': 'Kevin', 'last_name': 'Connauton', 'position': 'D', 'number': 44, 'goals': 1, 'assists': 7, 'points': 8, 'pims': 22, 'plus_minus': -2, 'gp': 50, 'age': 28, 'team_id': 22},
        {'first_name': 'Christian', 'last_name': 'Dvorak', 'position': 'C', 'number': 18, 'goals': 2, 'assists': 5, 'points': 7, 'pims': 2, 'plus_minus': -2, 'gp': 20, 'age': 22, 'team_id': 22},
        {'first_name': 'Dylan', 'last_name': 'Strome', 'position': 'C', 'number': 20, 'goals': 3, 'assists': 3, 'points': 6, 'pims': 6, 'plus_minus': -10, 'gp': 20, 'age': 21, 'team_id': 22},
        {'first_name': 'Brendan', 'last_name': 'Perlini', 'position': 'L', 'number': 11, 'goals': 2, 'assists': 4, 'points': 6, 'pims': 8, 'plus_minus': -5, 'gp': 22, 'age': 22, 'team_id': 22},
        {'first_name': 'Antti', 'last_name': 'Raanta', 'position': 'G', 'number': 32, 'wins': 5, 'gaa': 2.88, 'svp': .906, 'gp': 13, 'age': 29, 'team_id': 22},
        {'first_name': 'Adin', 'last_name': 'Hill', 'position': 'G', 'number': 31, 'wins': 7, 'gaa': 2.76, 'svp': .906, 'gp': 13, 'age': 22, 'team_id': 22},
        {'first_name': 'Darcy', 'last_name': 'Kuemper', 'position': 'G', 'number': 35, 'wins': 27, 'gaa': 2.88, 'svp': .906, 'gp': 55, 'age': 28, 'team_id': 22}
    ]
    team23 = [
        {'first_name': 'Nick', 'last_name': 'Schmaltz', 'position': 'C', 'number': 8, 'goals': 11, 'assists': 34, 'points': 45, 'pims': 20, 'plus_minus': 3, 'gp': 70, 'age': 23, 'team_id': 23},
        {'first_name': 'Clayton', 'last_name': 'Keller', 'position': 'R', 'number': 9, 'goals': 17, 'assists': 27, 'points': 44, 'pims': 28, 'plus_minus': -6, 'gp': 70, 'age': 21, 'team_id': 23},
        {'first_name': 'Conor', 'last_name': 'Garland', 'position': 'R', 'number': 83, 'goals': 22, 'assists': 17, 'points': 39, 'pims': 20, 'plus_minus': 1, 'gp': 68, 'age': 23, 'team_id': 23},
        {'first_name': 'Christian', 'last_name': 'Dvorak', 'position': 'C', 'number': 18, 'goals': 18, 'assists': 20, 'points': 38, 'pims': 12, 'plus_minus': 6, 'gp': 70, 'age': 23, 'team_id': 23},
        {'first_name': 'Phil', 'last_name': 'Kessel', 'position': 'R', 'number': 81, 'goals': 14, 'assists': 24, 'points': 38, 'pims': 22, 'plus_minus': -21, 'gp': 70, 'age': 31, 'team_id': 23},
        {'first_name': 'Carl', 'last_name': 'Soderberg', 'position': 'C', 'number': 34, 'goals': 17, 'assists': 18, 'points': 35, 'pims': 18, 'plus_minus': 6, 'gp': 70, 'age': 33, 'team_id': 23},
        {'first_name': 'Alex', 'last_name': 'Goligoski', 'position': 'D', 'number': 33, 'goals': 4, 'assists': 28, 'points': 32, 'pims': 24, 'plus_minus': 8, 'gp': 70, 'age': 34, 'team_id': 23},
        {'first_name': 'Oliver', 'last_name': 'Ekman-Larsson', 'position': 'D', 'number': 23, 'goals': 9, 'assists': 21, 'points': 30, 'pims': 38, 'plus_minus': -3, 'gp': 66, 'age': 28, 'team_id': 23},
        {'first_name': 'Derek', 'last_name': 'Stepan', 'position': 'C', 'number': 21, 'goals': 10, 'assists': 18, 'points': 28, 'pims': 16, 'plus_minus': -4, 'gp': 70, 'age': 29, 'team_id': 23},
        {'first_name': 'Taylor', 'last_name': 'Hall', 'position': 'L', 'number': 91, 'goals': 10, 'assists': 17, 'points': 27, 'pims': 14, 'plus_minus': -3, 'gp': 35, 'age': 27, 'team_id': 23},
        {'first_name': 'Jakob', 'last_name': 'Chychrun', 'position': 'D', 'number': 6, 'goals': 12, 'assists': 14, 'points': 26, 'pims': 38, 'plus_minus': 4, 'gp': 63, 'age': 21, 'team_id': 23},
        {'first_name': 'Lawson', 'last_name': 'Crouse', 'position': 'L', 'number': 67, 'goals': 15, 'assists': 10, 'points': 25, 'pims': 33, 'plus_minus': 0, 'gp': 66, 'age': 22, 'team_id': 23},
        {'first_name': 'Vinny', 'last_name': 'Hinostroza', 'position': 'C', 'number': 13, 'goals': 5, 'assists': 17, 'points': 22, 'pims': 14, 'plus_minus': 1, 'gp': 68, 'age': 25, 'team_id': 23},
        {'first_name': 'Jordan', 'last_name': 'Oesterle', 'position': 'D', 'number': 82, 'goals': 3, 'assists': 10, 'points': 13, 'pims': 14, 'plus_minus': -9, 'gp': 58, 'age': 27, 'team_id': 23},
        {'first_name': 'Michael', 'last_name': 'Grabner', 'position': 'R', 'number': 40, 'goals': 8, 'assists': 3, 'points': 11, 'pims': 6, 'plus_minus': -4, 'gp': 46, 'age': 31, 'team_id': 23},
        {'first_name': 'Brad', 'last_name': 'Richardson', 'position': 'R', 'number': 15, 'goals': 6, 'assists': 5, 'points': 11, 'pims': 20, 'plus_minus': 1, 'gp': 59, 'age': 34, 'team_id': 23},
        {'first_name': 'Jason', 'last_name': 'Demers', 'position': 'D', 'number': 55, 'goals': 0, 'assists': 11, 'points': 11, 'pims': 25, 'plus_minus': 5, 'gp': 50, 'age': 31, 'team_id': 23},
        {'first_name': 'Christian', 'last_name': 'Fischer', 'position': 'R', 'number': 36, 'goals': 6, 'assists': 3, 'points': 9, 'pims': 16, 'plus_minus': 2, 'gp': 56, 'age': 22, 'team_id': 23},
        {'first_name': 'Niklas', 'last_name': 'Hjalmarsson', 'position': 'D', 'number': 4, 'goals': 1, 'assists': 4, 'points': 5, 'pims': 14, 'plus_minus': -2, 'gp': 27, 'age': 32, 'team_id': 23},
        {'first_name': 'Barrett', 'last_name': 'Hayton', 'position': 'C', 'number': 29, 'goals': 1, 'assists': 3, 'points': 4, 'pims': 14, 'plus_minus': 2, 'gp': 20, 'age': 19, 'team_id': 23},
        {'first_name': 'Ilya', 'last_name': 'Lyubushkin', 'position': 'D', 'number': 46, 'goals': 0, 'assists': 4, 'points': 4, 'pims': 18, 'plus_minus': 4, 'gp': 51, 'age': 25, 'team_id': 23},
        {'first_name': 'Kyle', 'last_name': 'Capobianco', 'position': 'D', 'number': 75, 'goals': 1, 'assists': 0, 'points': 1, 'pims': 2, 'plus_minus': -1, 'gp': 9, 'age': 22, 'team_id': 23},
        {'first_name': 'Jordan', 'last_name': 'Gross', 'position': 'D', 'number': 79, 'goals': 0, 'assists': 1, 'points': 1, 'pims': 0, 'plus_minus': 2, 'gp': 2, 'age': 24, 'team_id': 23},
        {'first_name': 'Aaron', 'last_name': 'Ness', 'position': 'D', 'number': 42, 'goals': 0, 'assists': 1, 'points': 1, 'pims': 0, 'plus_minus': 1, 'gp': 24, 'age': 29, 'team_id': 23},
        {'first_name': 'Antti', 'last_name': 'Raanta', 'position': 'G', 'number': 32, 'wins': 15, 'gaa': 2.63, 'svp': .921, 'gp': 33, 'age': 30, 'team_id': 23},
        {'first_name': 'Adin', 'last_name': 'Hill', 'position': 'G', 'number': 31, 'wins': 2, 'gaa': 2.62, 'svp': .918, 'gp': 13, 'age': 23, 'team_id': 23},
        {'first_name': 'Darcy', 'last_name': 'Kuemper', 'position': 'G', 'number': 35, 'wins': 16, 'gaa': 2.22, 'svp': .928, 'gp': 29, 'age': 29, 'team_id': 23}
    ]
    team24 = [
        {'first_name': 'Phil', 'last_name': 'Kessel', 'position': 'R', 'number': 81, 'goals': 20, 'assists': 23, 'points': 43, 'pims': 12, 'plus_minus': -17, 'gp': 56, 'age': 32, 'team_id': 24},
        {'first_name': 'Jakob', 'last_name': 'Chychrun', 'position': 'D', 'number': 6, 'goals': 18, 'assists': 23, 'points': 41, 'pims': 42, 'plus_minus': -6, 'gp': 56, 'age': 22, 'team_id': 24},
        {'first_name': 'Conor', 'last_name': 'Garland', 'position': 'R', 'number': 83, 'goals': 12, 'assists': 27, 'points': 39, 'pims': 26, 'plus_minus': -3, 'gp': 49, 'age': 24, 'team_id': 24},
        {'first_name': 'Clayton', 'last_name': 'Keller', 'position': 'R', 'number': 9, 'goals': 14, 'assists': 21, 'points': 35, 'pims': 18, 'plus_minus': -5, 'gp': 56, 'age': 22, 'team_id': 24},
        {'first_name': 'Nick', 'last_name': 'Schmaltz', 'position': 'C', 'number': 8, 'goals': 10, 'assists': 22, 'points': 32, 'pims': 16, 'plus_minus': -1, 'gp': 52, 'age': 24, 'team_id': 24},
        {'first_name': 'Christian', 'last_name': 'Dvorak', 'position': 'C', 'number': 18, 'goals': 17, 'assists': 14, 'points': 31, 'pims': 12, 'plus_minus': -11, 'gp': 56, 'age': 24, 'team_id': 24},
        {'first_name': 'Oliver', 'last_name': 'Ekman-Larsson', 'position': 'D', 'number': 23, 'goals': 3, 'assists': 21, 'points': 24, 'pims': 32, 'plus_minus': -17, 'gp': 46, 'age': 29, 'team_id': 24},
        {'first_name': 'Alex', 'last_name': 'Goligoski', 'position': 'D', 'number': 33, 'goals': 3, 'assists': 19, 'points': 22, 'pims': 14, 'plus_minus': 2, 'gp': 56, 'age': 35, 'team_id': 24},
        {'first_name': 'Derick', 'last_name': 'Brassard', 'position': 'C', 'number': 16, 'goals': 8, 'assists': 12, 'points': 20, 'pims': 12, 'plus_minus': -10, 'gp': 53, 'age': 32, 'team_id': 24},
        {'first_name': 'Johan', 'last_name': 'Larsson', 'position': 'L', 'number': 22, 'goals': 8, 'assists': 6, 'points': 14, 'pims': 24, 'plus_minus': -13, 'gp': 52, 'age': 28, 'team_id': 24},
        {'first_name': 'Michael', 'last_name': 'Bunting', 'position': 'L', 'number': 58, 'goals': 10, 'assists': 3, 'points': 13, 'pims': 12, 'plus_minus': -1, 'gp': 21, 'age': 24, 'team_id': 24},
        {'first_name': 'Lawson', 'last_name': 'Crouse', 'position': 'L', 'number': 67, 'goals': 4, 'assists': 9, 'points': 13, 'pims': 46, 'plus_minus': -10, 'gp': 51, 'age': 23, 'team_id': 24},
        {'first_name': 'Tyler', 'last_name': 'Pitlick', 'position': 'C', 'number': 17, 'goals': 6, 'assists': 5, 'points': 11, 'pims': 16, 'plus_minus': -1, 'gp': 38, 'age': 28, 'team_id': 24},
        {'first_name': 'Christian', 'last_name': 'Fischer', 'position': 'R', 'number': 36, 'goals': 3, 'assists': 8, 'points': 11, 'pims': 6, 'plus_minus': -10, 'gp': 52, 'age': 23, 'team_id': 24},
        {'first_name': 'Jordan', 'last_name': 'Oesterle', 'position': 'D', 'number': 82, 'goals': 1, 'assists': 10, 'points': 11, 'pims': 10, 'plus_minus': -10, 'gp': 43, 'age': 28, 'team_id': 24},
        {'first_name': 'Dryden', 'last_name': 'Hunt', 'position': 'L', 'number': 28, 'goals': 3, 'assists': 5, 'points': 8, 'pims': 4, 'plus_minus': -6, 'gp': 26, 'age': 24, 'team_id': 24},
        {'first_name': 'Drake', 'last_name': 'Caggiula', 'position': 'C', 'number': 91, 'goals': 1, 'assists': 6, 'points': 7, 'pims': 15, 'plus_minus': -1, 'gp': 27, 'age': 26, 'team_id': 24},
        {'first_name': 'John', 'last_name': 'Hayden', 'position': 'C', 'number': 15, 'goals': 2, 'assists': 3, 'points': 5, 'pims': 37, 'plus_minus': -4, 'gp': 29, 'age': 25, 'team_id': 24},
        {'first_name': 'Niklas', 'last_name': 'Hjalmarsson', 'position': 'D', 'number': 4, 'goals': 0, 'assists': 5, 'points': 5, 'pims': 18, 'plus_minus': -6, 'gp': 41, 'age': 33, 'team_id': 24},
        {'first_name': 'Jason', 'last_name': 'Demers', 'position': 'D', 'number': 55, 'goals': 0, 'assists': 4, 'points': 4, 'pims': 26, 'plus_minus': -4, 'gp': 41, 'age': 32, 'team_id': 24},
        {'first_name': 'Barrett', 'last_name': 'Hayton', 'position': 'C', 'number': 29, 'goals': 2, 'assists': 1, 'points': 3, 'pims': 0, 'plus_minus': -1, 'gp': 14, 'age': 20, 'team_id': 24},
        {'first_name': 'Lane', 'last_name': 'Pederson', 'position': 'C', 'number': 93, 'goals': 1, 'assists': 2, 'points': 3, 'pims': 2, 'plus_minus': -2, 'gp': 15, 'age': 23, 'team_id': 24},
        {'first_name': 'Jordan', 'last_name': 'Gross', 'position': 'D', 'number': 79, 'goals': 0, 'assists': 3, 'points': 3, 'pims': 2, 'plus_minus': -3, 'gp': 7, 'age': 25, 'team_id': 24},
        {'first_name': 'Jan', 'last_name': 'Jenik', 'position': 'R', 'number': 73, 'goals': 2, 'assists': 0, 'points': 2, 'pims': 0, 'plus_minus': 3, 'gp': 2, 'age': 19, 'team_id': 24},
        {'first_name': 'Victor', 'last_name': 'Soderstrom', 'position': 'D', 'number': 77, 'goals': 1, 'assists': 1, 'points': 2, 'pims': 0, 'plus_minus': 4, 'gp': 4, 'age': 19, 'team_id': 24},
        {'first_name': 'Antti', 'last_name': 'Raanta', 'position': 'G', 'number': 32, 'wins': 5, 'gaa': 3.36, 'svp': .905, 'gp': 12, 'age': 31, 'team_id': 24},
        {'first_name': 'Adin', 'last_name': 'Hill', 'position': 'G', 'number': 31, 'wins': 9, 'gaa': 2.74, 'svp': .913, 'gp': 19, 'age': 24, 'team_id': 24},
        {'first_name': 'Darcy', 'last_name': 'Kuemper', 'position': 'G', 'number': 35, 'wins': 10, 'gaa': 2.56, 'svp': .907, 'gp': 27, 'age': 30, 'team_id': 24}
    ]
    team25 = [
        {'first_name': 'Clayton', 'last_name': 'Keller', 'position': 'R', 'number': 9, 'goals': 28, 'assists': 35, 'points': 63, 'pims': 14, 'plus_minus': 3, 'gp': 67, 'age': 23, 'team_id': 25},
        {'first_name': 'Nick', 'last_name': 'Schmaltz', 'position': 'C', 'number': 8, 'goals': 23, 'assists': 36, 'points': 59, 'pims': 22, 'plus_minus': -15, 'gp': 63, 'age': 25, 'team_id': 25},
        {'first_name': 'Phil', 'last_name': 'Kessel', 'position': 'R', 'number': 81, 'goals': 8, 'assists': 44, 'points': 52, 'pims': 28, 'plus_minus': -24, 'gp': 82, 'age': 34, 'team_id': 25},
        {'first_name': 'Shayne', 'last_name': 'Gostisbehere', 'position': 'D', 'number': 14, 'goals': 11, 'assists': 38, 'points': 49, 'pims': 50, 'plus_minus': -23, 'gp': 82, 'age': 28, 'team_id': 25},
        {'first_name': 'Lawson', 'last_name': 'Crouse', 'position': 'L', 'number': 67, 'goals': 20, 'assists': 14, 'points': 34, 'pims': 54, 'plus_minus': -10, 'gp': 65, 'age': 24, 'team_id': 25},
        {'first_name': 'Travis', 'last_name': 'Boyd', 'position': 'C', 'number': 72, 'goals': 17, 'assists': 18, 'points': 35, 'pims': 18, 'plus_minus': -8, 'gp': 74, 'age': 28, 'team_id': 25},
        {'first_name': 'Johan', 'last_name': 'Larsson', 'position': 'L', 'number': 22, 'goals': 6, 'assists': 9, 'points': 15, 'pims': 30, 'plus_minus': -3, 'gp': 29, 'age': 29, 'team_id': 25},
        {'first_name': 'Anton', 'last_name': 'Stralman', 'position': 'D', 'number': 86, 'goals': 8, 'assists': 15, 'points': 23, 'pims': 12, 'plus_minus': -16, 'gp': 74, 'age': 35, 'team_id': 25},
        {'first_name': 'Barrett', 'last_name': 'Hayton', 'position': 'C', 'number': 29, 'goals': 10, 'assists': 14, 'points': 24, 'pims': 20, 'plus_minus': -8, 'gp': 60, 'age': 21, 'team_id': 25},
        {'first_name': 'Andrew', 'last_name': 'Ladd', 'position': 'L', 'number': 16, 'goals': 7, 'assists': 5, 'points': 12, 'pims': 47, 'plus_minus': -20, 'gp': 51, 'age': 36, 'team_id': 25},
        {'first_name': 'Anton', 'last_name': 'Roussel', 'position': 'L', 'number': 26, 'goals': 4, 'assists': 4, 'points': 8, 'pims': 59, 'plus_minus': -16, 'gp': 53, 'age': 32, 'team_id': 25},
        {'first_name': 'Liam', 'last_name': 'O\'Brien', 'position': 'C', 'number': 38, 'goals': 1, 'assists': 3, 'points': 4, 'pims': 106, 'plus_minus': -8, 'gp': 39, 'age': 27, 'team_id': 25},
        {'first_name': 'Ilya', 'last_name': 'Lyubushkin', 'position': 'D', 'number': 46, 'goals': 0, 'assists': 9, 'points': 9, 'pims': 26, 'plus_minus': -6, 'gp': 46, 'age': 27, 'team_id': 25},
        {'first_name': 'Loui', 'last_name': 'Eriksson', 'position': 'R', 'number': 21, 'goals': 3, 'assists': 16, 'points': 19, 'pims': 6, 'plus_minus': -12, 'gp': 73, 'age': 36, 'team_id': 25},
        {'first_name': 'Kyle', 'last_name': 'Capobianco', 'position': 'D', 'number': 75, 'goals': 2, 'assists': 7, 'points': 9, 'pims': 38, 'plus_minus': -12, 'gp': 45, 'age': 24, 'team_id': 25},
        {'first_name': 'Christian', 'last_name': 'Fischer', 'position': 'R', 'number': 36, 'goals': 5, 'assists': 5, 'points': 10, 'pims': 14, 'plus_minus': -15, 'gp': 53, 'age': 24, 'team_id': 25},
        {'first_name': 'Dysin', 'last_name': 'Mayo', 'position': 'D', 'number': 61, 'goals': 4, 'assists': 8, 'points': 12, 'pims': 27, 'plus_minus': -22, 'gp': 67, 'age': 25, 'team_id': 25},
        {'first_name': 'Michael', 'last_name': 'Carcone', 'position': 'L', 'number': 53, 'goals': 4, 'assists': 2, 'points': 6, 'pims': 14, 'plus_minus': -8, 'gp': 21, 'age': 25, 'team_id': 25},
        {'first_name': 'Matias', 'last_name': 'Maccelli', 'position': 'L', 'number': 63, 'goals': 1, 'assists': 5, 'points': 6, 'pims': 4, 'plus_minus': -10, 'gp': 23, 'age': 20, 'team_id': 25},
        {'first_name': 'Nathan', 'last_name': 'Smith', 'position': 'C', 'number': 13, 'goals': 2, 'assists': 2, 'points': 4, 'pims': 2, 'plus_minus': -1, 'gp': 10, 'age': 22, 'team_id': 25},
        {'first_name': 'Riley', 'last_name': 'Nash', 'position': 'C', 'number': 20, 'goals': 1, 'assists': 3, 'points': 4, 'pims': 4, 'plus_minus': -3, 'gp': 24, 'age': 32, 'team_id': 25},
        {'first_name': 'Jack', 'last_name': 'McBain', 'position': 'C', 'number': 22, 'goals': 2, 'assists': 1, 'points': 3, 'pims': 6, 'plus_minus': -6, 'gp': 10, 'age': 21, 'team_id': 25},
        {'first_name': 'Jan', 'last_name': 'Jenik', 'position': 'R', 'number': 73, 'goals': 2, 'assists': 1, 'points': 3, 'pims': 11, 'plus_minus': -6, 'gp': 13, 'age': 21, 'team_id': 25},
        {'first_name': 'Vladislav', 'last_name': 'Kolyachonok', 'position': 'D', 'number': 92, 'goals': 1, 'assists': 2, 'points': 3, 'pims': 6, 'plus_minus': 0, 'gp': 32, 'age': 20, 'team_id': 25},
        {'first_name': 'Scott', 'last_name': 'Wedgewood', 'position': 'G', 'number': 31, 'wins': 10, 'gaa': 3.16, 'svp': .911, 'gp': 26, 'age': 29, 'team_id': 25},
        {'first_name': 'Karel', 'last_name': 'Vejmelka', 'position': 'G', 'number': 70, 'wins': 13, 'gaa': 3.68, 'svp': .898, 'gp': 52, 'age': 25, 'team_id': 25}
    ]
    team26 = [
        {'first_name': 'Clayton', 'last_name': 'Keller', 'position': 'R', 'number': 9, 'goals': 37, 'assists': 49, 'points': 86, 'pims': 49, 'plus_minus': -2, 'gp': 82, 'age': 24, 'team_id': 26},
        {'first_name': 'Nick', 'last_name': 'Schmaltz', 'position': 'C', 'number': 8, 'goals': 22, 'assists': 36, 'points': 58, 'pims': 20, 'plus_minus': 4, 'gp': 63, 'age': 26, 'team_id': 26},
        {'first_name': 'Matias', 'last_name': 'Maccelli', 'position': 'L', 'number': 63, 'goals': 11, 'assists': 38, 'points': 49, 'pims': 18, 'plus_minus': 0, 'gp': 64, 'age': 21, 'team_id': 26},
        {'first_name': 'Lawson', 'last_name': 'Crouse', 'position': 'L', 'number': 67, 'goals': 24, 'assists': 21, 'points': 45, 'pims': 35, 'plus_minus': -3, 'gp': 77, 'age': 25, 'team_id': 26},
        {'first_name': 'Barrett', 'last_name': 'Hayton', 'position': 'C', 'number': 29, 'goals': 19, 'assists': 24, 'points': 43, 'pims': 42, 'plus_minus': -5, 'gp': 82, 'age': 22, 'team_id': 26},
        {'first_name': 'Travis', 'last_name': 'Boyd', 'position': 'C', 'number': 72, 'goals': 15, 'assists': 19, 'points': 34, 'pims': 26, 'plus_minus': -32, 'gp': 82, 'age': 28, 'team_id': 26},
        {'first_name': 'Juuso', 'last_name': 'Valimaki', 'position': 'D', 'number': 4, 'goals': 4, 'assists': 30, 'points': 34, 'pims': 59, 'plus_minus': -10, 'gp': 78, 'age': 23, 'team_id': 26},
        {'first_name': 'Shayne', 'last_name': 'Gostisbehere', 'position': 'D', 'number': 14, 'goals': 10, 'assists': 21, 'points': 31, 'pims': 28, 'plus_minus': -6, 'gp': 52, 'age': 29, 'team_id': 26},
        {'first_name': 'J.J.', 'last_name': 'Moser', 'position': 'D', 'number': 90, 'goals': 7, 'assists': 24, 'points': 31, 'pims': 35, 'plus_minus': -12, 'gp': 82, 'age': 22, 'team_id': 26},
        {'first_name': 'Jakob', 'last_name': 'Chychrun', 'position': 'D', 'number': 6, 'goals': 7, 'assists': 21, 'points': 28, 'pims': 22, 'plus_minus': 8, 'gp': 36, 'age': 24, 'team_id': 26},
        {'first_name': 'Christian', 'last_name': 'Fischer', 'position': 'R', 'number': 36, 'goals': 13, 'assists': 14, 'points': 27, 'pims': 20, 'plus_minus': -7, 'gp': 80, 'age': 25, 'team_id': 26},
        {'first_name': 'Jack', 'last_name': 'McBain', 'position': 'C', 'number': 22, 'goals': 12, 'assists': 14, 'points': 26, 'pims': 64, 'plus_minus': -8, 'gp': 82, 'age': 22, 'team_id': 26},
        {'first_name': 'Nick', 'last_name': 'Bjugstad', 'position': 'C', 'number': 17, 'goals': 13, 'assists': 10, 'points': 23, 'pims': 26, 'plus_minus': 7, 'gp': 59, 'age': 30, 'team_id': 26},
        {'first_name': 'Nick', 'last_name': 'Ritchie', 'position': 'L', 'number': 12, 'goals': 9, 'assists': 12, 'points': 21, 'pims': 43, 'plus_minus': -15, 'gp': 58, 'age': 26, 'team_id': 26},
        {'first_name': 'Dylan', 'last_name': 'Guenther', 'position': 'R', 'number': 11, 'goals': 6, 'assists': 9, 'points': 15, 'pims': 10, 'plus_minus': -7, 'gp': 33, 'age': 19, 'team_id': 26},
        {'first_name': 'Liam', 'last_name': 'O\'Brien', 'position': 'C', 'number': 38, 'goals': 3, 'assists': 8, 'points': 11, 'pims': 114, 'plus_minus': -5, 'gp': 56, 'age': 28, 'team_id': 26},
        {'first_name': 'Victor', 'last_name': 'Soderstrom', 'position': 'D', 'number': 77, 'goals': 0, 'assists': 9, 'points': 9, 'pims': 24, 'plus_minus': -3, 'gp': 30, 'age': 21, 'team_id': 26},
        {'first_name': 'Josh', 'last_name': 'Brown', 'position': 'D', 'number': 3, 'goals': 4, 'assists': 3, 'points': 7, 'pims': 87, 'plus_minus': -18, 'gp': 68, 'age': 28, 'team_id': 26},
        {'first_name': 'Troy', 'last_name': 'Stecher', 'position': 'D', 'number': 51, 'goals': 0, 'assists': 7, 'points': 7, 'pims': 29, 'plus_minus': -3, 'gp': 61, 'age': 28, 'team_id': 26},
        {'first_name': 'Brett', 'last_name': 'Ritchie', 'position': 'R', 'number': 24, 'goals': 2, 'assists': 3, 'points': 5, 'pims': 2, 'plus_minus': -2, 'gp': 16, 'age': 29, 'team_id': 26},
        {'first_name': 'Patrik', 'last_name': 'Nemeth', 'position': 'D', 'number': 2, 'goals': 0, 'assists': 5, 'points': 5, 'pims': 30, 'plus_minus': -7, 'gp': 75, 'age': 30, 'team_id': 26},
        {'first_name': 'Connor', 'last_name': 'Mackey', 'position': 'D', 'number': 12, 'goals': 1, 'assists': 3, 'points': 4, 'pims': 39, 'plus_minus': 2, 'gp': 20, 'age': 25, 'team_id': 26},
        {'first_name': 'Michael', 'last_name': 'Carcone', 'position': 'L', 'number': 53, 'goals': 2, 'assists': 1, 'points': 3, 'pims': 2, 'plus_minus': 3, 'gp': 9, 'age': 26, 'team_id': 26},
        {'first_name': 'Michael', 'last_name': 'Kesselring', 'position': 'D', 'number': 5, 'goals': 0, 'assists': 3, 'points': 3, 'pims': 6, 'plus_minus': -1, 'gp': 9, 'age': 22, 'team_id': 26},
        {'first_name': 'Connor', 'last_name': 'Ingram', 'position': 'G', 'number': 39, 'wins': 6, 'gaa': 3.37, 'svp': .907, 'gp': 27, 'age': 25, 'team_id': 26},
        {'first_name': 'Karel', 'last_name': 'Vejmelka', 'position': 'G', 'number': 70, 'wins': 18, 'gaa': 3.41, 'svp': .900, 'gp': 50, 'age': 26, 'team_id': 26}
    ]
    team27 = [
        {'first_name': 'Clayton', 'last_name': 'Keller', 'position': 'R', 'number': 9, 'goals': 33, 'assists': 43, 'points': 76, 'pims': 32, 'plus_minus': -2, 'gp': 78, 'age': 25, 'team_id': 27},
        {'first_name': 'Nick', 'last_name': 'Schmaltz', 'position': 'C', 'number': 8, 'goals': 22, 'assists': 39, 'points': 61, 'pims': 10, 'plus_minus': 4, 'gp': 79, 'age': 27, 'team_id': 27},
        {'first_name': 'Matias', 'last_name': 'Maccelli', 'position': 'L', 'number': 63, 'goals': 17, 'assists': 40, 'points': 57, 'pims': 8, 'plus_minus': 0, 'gp': 82, 'age': 22, 'team_id': 27},
        {'first_name': 'Nick', 'last_name': 'Bjugstad', 'position': 'C', 'number': 17, 'goals': 22, 'assists': 23, 'points': 45, 'pims': 59, 'plus_minus': 7, 'gp': 76, 'age': 31, 'team_id': 27},
        {'first_name': 'Alex', 'last_name': 'Kerfoot', 'position': 'C', 'number': 15, 'goals': 13, 'assists': 32, 'points': 45, 'pims': 26, 'plus_minus': -3, 'gp': 82, 'age': 29, 'team_id': 27},
        {'first_name': 'Logan', 'last_name': 'Cooley', 'position': 'C', 'number': 92, 'goals': 20, 'assists': 24, 'points': 44, 'pims': 18, 'plus_minus': -3, 'gp': 82, 'age': 19, 'team_id': 27},
        {'first_name': 'Lawson', 'last_name': 'Crouse', 'position': 'L', 'number': 67, 'goals': 23, 'assists': 19, 'points': 42, 'pims': 36, 'plus_minus': -3, 'gp': 81, 'age': 26, 'team_id': 27},
        {'first_name': 'Sean', 'last_name': 'Durzi', 'position': 'D', 'number': 50, 'goals': 9, 'assists': 32, 'points': 41, 'pims': 63, 'plus_minus': -10, 'gp': 76, 'age': 24, 'team_id': 27},
        {'first_name': 'Dylan', 'last_name': 'Guenther', 'position': 'R', 'number': 11, 'goals': 18, 'assists': 17, 'points': 35, 'pims': 14, 'plus_minus': -7, 'gp': 45, 'age': 20, 'team_id': 27},
        {'first_name': 'Michael', 'last_name': 'Carcone', 'position': 'L', 'number': 53, 'goals': 21, 'assists': 8, 'points': 29, 'pims': 35, 'plus_minus': -3, 'gp': 74, 'age': 27, 'team_id': 27},
        {'first_name': 'Jack', 'last_name': 'McBain', 'position': 'C', 'number': 22, 'goals': 8, 'assists': 18, 'points': 26, 'pims': 50, 'plus_minus': -8, 'gp': 67, 'age': 23, 'team_id': 27},
        {'first_name': 'J.J.', 'last_name': 'Moser', 'position': 'D', 'number': 90, 'goals': 5, 'assists': 21, 'points': 26, 'pims': 35, 'plus_minus': -12, 'gp': 80, 'age': 23, 'team_id': 27},
        {'first_name': 'Jason', 'last_name': 'Zucker', 'position': 'L', 'number': 16, 'goals': 9, 'assists': 16, 'points': 25, 'pims': 58, 'plus_minus': -10, 'gp': 51, 'age': 31, 'team_id': 27},
        {'first_name': 'Michael', 'last_name': 'Kesselring', 'position': 'D', 'number': 5, 'goals': 5, 'assists': 16, 'points': 21, 'pims': 66, 'plus_minus': -1, 'gp': 65, 'age': 23, 'team_id': 27},
        {'first_name': 'Juuso', 'last_name': 'Valimaki', 'position': 'D', 'number': 4, 'goals': 2, 'assists': 15, 'points': 17, 'pims': 12, 'plus_minus': -10, 'gp': 68, 'age': 24, 'team_id': 27},
        {'first_name': 'Liam', 'last_name': 'O\'Brien', 'position': 'C', 'number': 38, 'goals': 5, 'assists': 9, 'points': 14, 'pims': 153, 'plus_minus': -5, 'gp': 75, 'age': 29, 'team_id': 27},
        {'first_name': 'Matt', 'last_name': 'Dumba', 'position': 'D', 'number': 24, 'goals': 4, 'assists': 6, 'points': 10, 'pims': 55, 'plus_minus': -7, 'gp': 58, 'age': 29, 'team_id': 27},
        {'first_name': 'Barrett', 'last_name': 'Hayton', 'position': 'C', 'number': 29, 'goals': 3, 'assists': 7, 'points': 10, 'pims': 26, 'plus_minus': -6, 'gp': 33, 'age': 23, 'team_id': 27},
        {'first_name': 'Josh', 'last_name': 'Brown', 'position': 'D', 'number': 3, 'goals': 3, 'assists': 7, 'points': 10, 'pims': 75, 'plus_minus': -8, 'gp': 51, 'age': 29, 'team_id': 27},
        {'first_name': 'Josh', 'last_name': 'Doan', 'position': 'R', 'number': 91, 'goals': 5, 'assists': 4, 'points': 9, 'pims': 0, 'plus_minus': 0, 'gp': 11, 'age': 21, 'team_id': 27},
        {'first_name': 'Travis', 'last_name': 'Boyd', 'position': 'C', 'number': 72, 'goals': 2, 'assists': 6, 'points': 8, 'pims': 2, 'plus_minus': -5, 'gp': 16, 'age': 29, 'team_id': 27},
        {'first_name': 'Travis', 'last_name': 'Dermott', 'position': 'D', 'number': 33, 'goals': 2, 'assists': 5, 'points': 7, 'pims': 26, 'plus_minus': -7, 'gp': 50, 'age': 26, 'team_id': 27},
        {'first_name': 'Troy', 'last_name': 'Stecher', 'position': 'D', 'number': 51, 'goals': 1, 'assists': 4, 'points': 5, 'pims': 24, 'plus_minus': -3, 'gp': 47, 'age': 29, 'team_id': 27},
        {'first_name': 'Vladislav', 'last_name': 'Kolyachonok', 'position': 'D', 'number': 52, 'goals': 1, 'assists': 3, 'points': 4, 'pims': 2, 'plus_minus': -3, 'gp': 5, 'age': 22, 'team_id': 27},
        {'first_name': 'Connor', 'last_name': 'Ingram', 'position': 'G', 'number': 39, 'wins': 23, 'gaa': 2.91, 'svp': .907, 'gp': 50, 'age': 26, 'team_id': 27},
        {'first_name': 'Karel', 'last_name': 'Vejmelka', 'position': 'G', 'number': 70, 'wins': 13, 'gaa': 3.29, 'svp': .897, 'gp': 38, 'age': 27, 'team_id': 27}
    ]
    for players in team1:
        player = Player(**players)
        db.session.add(player)
    for players in team2:
        player = Player(**players)
        db.session.add(player)
    for players in team3:
        player = Player(**players)
        db.session.add(player)
    for players in team4:
        player = Player(**players)
        db.session.add(player)
    for players in team5:
        player = Player(**players)
        db.session.add(player)
    for players in team6:
        player = Player(**players)
        db.session.add(player)
    for players in team7:
        player = Player(**players)
        db.session.add(player)
    for players in team8:
        player = Player(**players)
        db.session.add(player)
    for players in team9:
        player = Player(**players)
        db.session.add(player)
    for players in team10:
        player = Player(**players)
        db.session.add(player)
    for players in team11:
        player = Player(**players)
        db.session.add(player)
    for players in team12:
        player = Player(**players)
        db.session.add(player)
    for players in team13:
        player = Player(**players)
        db.session.add(player)
    for players in team14:
        player = Player(**players)
        db.session.add(player)
    for players in team15:
        player = Player(**players)
        db.session.add(player)
    for players in team16:
        player = Player(**players)
        db.session.add(player)
    for players in team17:
        player = Player(**players)
        db.session.add(player)
    for players in team18:
        player = Player(**players)
        db.session.add(player)
    for players in team19:
        player = Player(**players)
        db.session.add(player)
    for players in team20:
        player = Player(**players)
        db.session.add(player)
    for players in team21:
        player = Player(**players)
        db.session.add(player)
    for players in team22:
        player = Player(**players)
        db.session.add(player)
    for players in team23:
        player = Player(**players)
        db.session.add(player)
    for players in team24:
        player = Player(**players)
        db.session.add(player)
    for players in team25:
        player = Player(**players)
        db.session.add(player)
    for players in team26:
        player = Player(**players)
        db.session.add(player)
    for players in team27:
        player = Player(**players)
        db.session.add(player)

    db.session.commit()

def undo_players():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.players RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM players"))

    db.session.commit()
