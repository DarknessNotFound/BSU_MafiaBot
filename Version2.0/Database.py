import sqlite3
DB = "/data/MafiaBot.db"

PLAYERS_T = "Players"
ROLES_T = "Roles"
PRELOAD_T = "Preloads"
GAME_T = "Games"
GAME_MODS_T = "GameMods"
GAME_PLAYERS_T = "GamePlayers"
ROUND_T = "Rounds"
ROUND_PLAYERS_T = "RoundsPlayers"
LEADERBOARD_T = "Leaderboard"

class ROLE_CATEGORIES(NamedTuple):
    KillingRole: int = 0
    NeutralEvil: int = 1
    Townie: int = 2
    DisabledTownie: int = 3

def InitializeDatabase() -> None:
    try:
        conn = sqlite3.connect(f'{DB}')
        cur = conn.cursor()
        cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {PLAYERS_T}(
                id INT PRIMARY KEY AUTOINCREMENT,
                isDeleted INT NOT NULL DEFAULT 0,
                DiscordId TEXT NULL,
                Name TEXT NULL,
                Permissions INTEGER NOT NULL DEFAULT 0);
            """)

        cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {ROLES_T}(
                id INT PRIMARY KEY,
                isDeleted INT NOT NULL DEFAULT 0,
                Name TEXT NULL,
                Description TEXT NULL,
                Category INT NOT NULL);
            """)

        
        conn.commit()
    except Exception as ex:
        print("Failed to initialize the database.")
    finally:
        conn.close()


if __name__ == "__main__":
    print("Database module for the program.")