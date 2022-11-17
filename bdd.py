"""

Classe gérant les accès à la base de données et tout ce qu’elle contient.
Cette classe ne doit faire aucun affichage. Elle exécutera les
requêtes SQL et retournera le résultat sous forme de liste de tuples

"""

import os
import sqlite3


class DataBase:
    def __init__(self, file_name: str):
        """
        Initialize the class and open DB
        :param file_name: string
        """
        self.path = os.path.abspath(f"{file_name}.sqlite")

        self.database = sqlite3.connect(database=self.path)  # Open the database

        # Creating a dictionary which contains the sql requests
        self.sql_request_dictionary = {"1": """
        SELECT * 
        FROM Cinemas
                                        """,
                                        "2": """
        SELECT Projeter.idProjection, Projeter.idFilm, Films.titre, Projeter.date
        FROM Projeter
        INNER JOIN Films
        ON Projeter.idFilm = Films.idFilm
        WHERE idCinema = ?;
                                        """,
                                        "3": ["""
        SELECT Films.titre, Films.annee, Genres.nom, Personnes.nom, Personnes.prenom
        FROM Films
        INNER JOIN Genres, Personnes
        ON Films.idGenre = Genres.idGenre
        AND Films.idRealisateur = Personnes.idPersonne
        WHERE Films.idFilm = ?;
                                        ""","""
        SELECT Personnes.nom, Personnes.prenom
        FROM Personnes
        INNER JOIN Jouer
        ON Jouer.idActeur = Personnes.idPersonne
        WHERE Jouer.idFilm = ?;
                                        """],
                                        "4": """
        INSERT INTO Projeter (idFilm, idCinema, date)
        VALUES (?, ?, ?);
                                        """,
                                        "5": """
        UPDATE Projeter
        SET date = ?
        WHERE Projeter.idProjection = ?;
                                             """, "6": """
        DELETE FROM Projeter
        WHERE Projeter.idProjection = ?;
                                                        """}

    def execute(self, command, parameters):
        """
        Execute a sql request
        :param command: string
        :param parameters: Iterable
        :return: tuple
        """

        cursor = self.database.cursor()  # Placing cursor
        result_list = cursor.execute(command, parameters)  # Execute a sql request

        return result_list

    def create_command(self, id_choice: int, input1=None, input2=None, input3=None):
        """
        :param id_choice: integer
        :param input1: string
        :param input2: string
        :param input3: string
        :return: string
        """
        # Creating the parameters list
        inputs = [input1, input2, input3]

        parameters = []

        for input_ in inputs:
            if input_ is not None:
                parameters.append(input_)

        results = []

        try:
            command = self.sql_request_dictionary[str(id_choice)]
        except KeyError:
            return "Choice does not exist"

        if input1 is None:
            results += self.execute(command=command, parameters=parameters)
            return results

        if id_choice == 3:
            results += self.execute(command=command[0], parameters=parameters)
            results += self.execute(command=command[1], parameters=parameters)
            return results

        results += self.execute(command=command, parameters=parameters)
        return results


if __name__ == "__main__":
    data_base = DataBase(file_name="cinema_v2")
    result = data_base.create_command(id_choice=6, input1=1)
    for row in result:
        print(row)
