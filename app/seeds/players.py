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
    for players in team1:
        player = Player(**players)
        db.session.add(player)

    db.session.commit()

def undo_players():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.players RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM players"))

    db.session.commit()
