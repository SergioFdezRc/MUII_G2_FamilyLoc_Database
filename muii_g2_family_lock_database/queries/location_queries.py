GET_LOCATIONS = """
SELECT *
FROM locations;
"""

GET_LAST_LOCATION = """
SELECT * 
FROM locations
ORDER BY id DESC 
LIMIT 1;
"""

NEW_LOCATION = """
INSERT INTO locations (name) 
    VALUES (%(location)s);
"""
