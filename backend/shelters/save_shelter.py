from Database import Database
from shelters.get_shelters import get_shelters


def save_shelter(shelter):
    shelters = get_shelters()
    db = Database()
    for sh in shelters:
        if sh[1] == shelter["name"]:
            db.update_query(
                "UPDATE shelters SET description = '{}', latitude = '{}', longitude = '{}', link_to_donate = '{}' WHERE name = '{}'".format(
                    shelter["description"],
                    shelter["latitude"],
                    shelter["longitude"],
                    shelter["link_to_donate"],
                    shelter["name"],
                )
            )
            db.close()
            return {"status": "updated succesffully"}
    db.update_query(
        "INSERT INTO shelters (name, description, latitude, longitude, link_to_donate) VALUES ('{}', '{}', '{}', '{}', '{}')".format(
            shelter["name"],
            shelter["description"],
            shelter["latitude"],
            shelter["longitude"],
            shelter["link_to_donate"],
        )
    )
    db.close()
    return {"status": "created succesffully"}
