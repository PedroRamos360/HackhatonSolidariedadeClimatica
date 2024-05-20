from Database import Database


def save_shelter(shelter):
    print(shelter)
    db = Database()
    db.execute_query(
        "INSERT INTO shelters (name, description, latitude, longitude, link_to_donate) VALUES ('{}', '{}', '{}', '{}', '{}')".format(
            shelter["name"],
            shelter["description"],
            shelter["latitude"],
            shelter["longitude"],
            shelter["link_to_donate"],
        )
    )
    db.close()
    return {"status": "success"}
