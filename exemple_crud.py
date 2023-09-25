from pymongo import MongoClient
import sys


MONGO_URI = "mongodb://root:example@localhost:27017/mongo_study?authSource=admin"

class MongoCrud:

    def __init__(self):
        try:
            client = MongoClient(MONGO_URI)
            self.database = client.get_database()
        except Exception as error:
            print(f"An Invalid URI host error was received {error}")
            sys.exit(1)

    def insert_new_games(self):
        if self.database:
            jogos_playstation = [
            {"nome": "The Last of Us Part II", "gênero": "Ação e Aventura", "classificação": "Mature"},
            {"nome": "God of War", "gênero": "Ação", "classificação": "Mature"},
            {"nome": "Spider-Man: Miles Morales", "gênero": "Ação e Aventura", "classificação": "Teen"},
            {"nome": "Demon's Souls", "gênero": "RPG de Ação", "classificação": "Mature"},
            {"nome": "Horizon Zero Dawn", "gênero": "Ação e Aventura", "classificação": "Teen"},
            {"nome": "Bloodborne", "gênero": "Ação e RPG", "classificação": "Mature"},
            {"nome": "Ghost of Tsushima", "gênero": "Ação e Aventura", "classificação": "Mature"},
            {"nome": "Uncharted 4: A Thief's End", "gênero": "Ação e Aventura", "classificação": "Teen"},
            {"nome": "Death Stranding", "gênero": "Ação e Aventura", "classificação": "Mature"},
            {"nome": "Ratchet & Clank: Rift Apart", "gênero": "Ação e Aventura", "classificação": "Everyone 10+"}
            ]
            self.database.games.insert_many(jogos_playstation)
            print("Lista de jogos inseridas com sucesso")
        else:
            print("Database nao encontrado")

    def get_one_game(self):
        game = self.database.games.find_one({}, {"nome": 1, "_id": 0})
        print(game)

    def update_name_game(self):
        self.database.games.update_one({"nome": "The Last of Us Part II"}, {"$set": {"GameOfTheYear": True}})

    def delete_game(self):
        self.database.games.delete_one({"nome": "Uncharted 4: A Thief's End"})
