NEW_DOOR = """
INSERT INTO door (name) VALUES (%(door_name)s);
"""

DELETE_DOOR = """
DELETE FROM door 
WHERE id = %(door_id)s;
"""

GET_ALL_DOORS_STATE = """
SELECT *
FROM door;
"""

GET_DOOR_STATE = """
SELECT * 
FROM door 
WHERE id = %(door_id)s;
"""

UPDATE_DOOR_STATE = """
UPDATE door SET state = %(door_state)s 
WHERE name = %(door_name)s;
"""
