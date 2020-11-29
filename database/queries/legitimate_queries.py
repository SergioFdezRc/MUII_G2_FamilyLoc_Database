DELETE_LEGITIMATE_PERSON = """
DELETE FROM legitimate 
WHERE %(person_mac)s = ANY(person_mac);
"""

GET_ALL_LEGITIMATE_PERSON_INFO = """
SELECT * FROM legitimate;
"""

GET_LEGITIMATE_PERSON_INFO = """
SELECT * 
FROM legitimate 
WHERE %(person_mac)s = ANY(person_mac);
"""

NEW_LEGITIMATE_PERSON = """
INSERT INTO legitimate (person_mac, person_name, person_phone_number, notification, dest_mac) 
VALUES (%(person_mac)s,%(person_name)s,%(person_phone_number)s,%(notification)s,%(dest_mac)s);
"""

UPDATE_LEGITIMATE_PERSON = """
UPDATE legitimate 
SET person_mac = %(new_person_mac)s 
WHERE %(person_mac)s = ANY(person_mac)
"""
