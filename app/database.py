import sqlite3

def connexion():
    return sqlite3.connect("BDD.db")

def creation_table_test():
    try:
        with connexion() as conn:
            cursor = conn.cursor()
            sql = "CREATE TABLE IF NOT EXISTS test (" \
            "id INTEGER PRIMARY KEY AUTOINCREMENT, " \
            "name TEXT NOT NULL)"
            cursor.execute(sql)
            conn.commit()
            print("Table créée avec succès !")
    except sqlite3.Error as e:
        print(f"An error occured while creating the table: {e}")

def inserer_valeurs_test(nom):
    try:
        with connexion() as conn:
            cursor = conn.cursor()
            sql = "INSERT INTO test (name) VALUES (?)"
            cursor.execute(sql, (nom,))
            conn.commit()
            print("Valeurs insérées avec succès !")
    except sqlite3.Error as e:
        print(f"An error occurred while inserting values: {e}")

def afficher_valeurs_table():
    try:
        with connexion() as conn:
            cursor = conn.cursor()
            sql = "SELECT * FROM test"
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(f"An error occurred while fetching values: {e}")

def supprimer_valeur_table_test(nom):
    try:
        with connexion() as conn:
            cursor = conn.cursor()
            sql = "DELETE FROM test WHERE name = ?"
            cursor.execute(sql, (nom,))
            conn.commit()
            print("Valeurs supprimées avec succès !")
    except sqlite3.Error as e:
        print(f"An error occurred while deleting values: {e}")

if (__name__ == "__main__"):
    nom = "test value"
    creation_table_test()
    inserer_valeurs_test(nom)
    afficher_valeurs_table()
    supprimer_valeur_table_test(nom)
    afficher_valeurs_table()