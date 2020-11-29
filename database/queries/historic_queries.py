GET_ALL_HISTORIC = """
SELECT * FROM historic;
"""

NEW_VISIT = """
INSERT INTO historic (person_mac, date, time) VALUES (%(person_mac)s,%(date)s,%(time)s);
"""

GET_VISIT = """
SELECT * 
FROM historic 
WHERE id = %(visit_id)s;
"""
