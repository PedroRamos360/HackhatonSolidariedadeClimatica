from Database import Database


def get_shelters():
    db = Database()
    shelters = db.get_query("SELECT * FROM shelters")
    db.close()
    return shelters
