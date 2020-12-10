import psycopg2

from muii_g2_family_lock_database.constants.db_conf import *
from muii_g2_family_lock_database.constants.literals import *
from muii_g2_family_lock_database.queries.account_queries import *
from muii_g2_family_lock_database.queries.door_queries import *
from muii_g2_family_lock_database.queries.historic_queries import *
from muii_g2_family_lock_database.queries.legitimate_queries import *
from muii_g2_family_lock_database.queries.location_queries import *


class PostgresDB:

    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(host=DATABASE_HOST, dbname=DATABASE_DB, user=DATABASE_USER,
                                         password=DATABASE_PWD,
                                         port=DATABASE_PORT)
        except ConnectionError as err:
            print("Error al conectar con la base de datos. Detalles: %s" % err)

    def __execute(self, query, args=None):
        __cursor = self.conn.cursor()
        __cursor.execute(query, args)
        __output = []

        if __cursor.description is not None:
            for item in __cursor:
                __output.append(item)
        __cursor.close()
        return __output

    def close(self):
        self.conn.commit()
        self.conn.close()

    def get_account_by_id(self, account_id: int):
        self.connect()
        try:
            locations = self.__execute(GET_ACCOUNT_BY_ID, {ACCOUNT_ID: account_id})
            self.close()
            return locations
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to get an account information by id. Error =>  {}".format(error)

    def delete_account(self, account_id: int):
        self.connect()
        try:
            last_location = self.__execute(DELETE_ACCOUNT, {ACCOUNT_ID: account_id})
            self.close()
            return last_location

        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to delete account. Error =>  {}".format(error)

    def add_new_account(self, username: str, password: str, birthdate: str, age: int):
        self.connect()
        try:
            self.__execute(NEW_ACCOUNT,
                           {USERNAME: username, PASSWORD: password, BIRTHDATE: birthdate, AGE: age})
            self.close()
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to add a new account. Error =>  {}".format(error)

    def update_account(self, account_id: int, password: str = ''):
        self.connect()
        try:
            self.__execute(UPDATE_ACCOUNT, {ACCOUNT_ID: account_id, PASSWORD: password})
            self.close()
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to update account. Error =>  {}".format(error)

    def get_account_id_by_username(self, username: str):
        self.connect()
        try:
            account_id = self.__execute(GET_ACCOUNT_ID_BY_USERNAME, {USERNAME: username})
            self.close()
            return account_id
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to get an account id by username. Error =>  {}".format(error)

    def get_account_id_by_username_and_password(self, username: str, password: str):
        self.connect()
        try:
            account_id = self.__execute(
                GET_ACCOUNT_ID_BY_USERNAME_AND_PASSWORD, {USERNAME: username,
                                                          PASSWORD: password})
            self.close()
            return account_id
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to get an account id by username and password. Error =>  {}".format(error)

    # LOCATION modules
    def get_locations(self):
        self.connect()
        try:
            locations = self.__execute(GET_LOCATIONS)
            self.close()
            return locations
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to get all locations. Error =>  {}".format(error)

    def insert_new_location(self, _location: str):
        self.connect()
        try:
            self.__execute(NEW_LOCATION, {LOCATION: _location})
            self.close()
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to add new location. Error =>  {}".format(error)

    def get_last_location(self):
        self.connect()
        try:
            last_location = self.__execute(GET_LAST_LOCATION)
            self.close()
            return last_location
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to get last location. Error =>  {}".format(error)

    # DOOR modules
    def add_new_door(self, door_name: str):
        self.connect()
        try:
            self.__execute(NEW_DOOR, {DOOR_NAME: door_name})
            self.close()
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to add a new door. Error =>  {}".format(error)

    def delete_door(self, door_id: int):
        self.connect()
        try:
            self.__execute(DELETE_DOOR, {DOOR_ID: door_id})
            self.close()
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to delete a door. Error =>  {}".format(error)

    def get_all_doors_state(self):
        self.connect()
        try:
            doors = self.__execute(GET_ALL_DOORS_STATE)
            self.close()
            return doors
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to get all doors state. Error =>  {}".format(error)

    def get_door_state(self, door_id: int):
        self.connect()
        try:
            door = self.__execute(GET_DOOR_STATE, {DOOR_ID: door_id})
            self.close()
            return door
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to get the door state. Error =>  {}".format(error)

    def update_door_state(self, door_state: str, door_name: str):
        self.connect()
        try:
            self.__execute(UPDATE_DOOR_STATE, {DOOR_STATE: door_state, DOOR_NAME: door_name})
            self.close()
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to update the door state. Error =>  {}".format(error)

    # HISTORIC
    def add_visit(self, person_mac, date, time):
        self.connect()
        try:
            self.__execute(NEW_VISIT, {PERSON_MAC: person_mac,
                                       DATE: date,
                                       TIME: time})
            self.close()
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to add a new visit. Error =>  {}".format(error)

    def get_all_historic(self):
        self.connect()
        try:
            historic = self.__execute(GET_ALL_HISTORIC)
            self.close()
            return historic
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to get all visits history. Error =>  {}".format(error)

    def get_visit(self, visit_id: int):
        self.connect()
        try:
            visit = self.__execute(GET_VISIT, {VISIT_ID: visit_id})
            self.close()
            return visit
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to get a visit. Error =>  {}".format(error)

    # LEGITIMATE OPERATIONS
    def delete_legitimate_person(self, person_mac: str):
        self.connect()
        try:
            self.__execute(DELETE_LEGITIMATE_PERSON, {PERSON_MAC: person_mac})
            self.close()
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to delete a legitimate person. Error =>  {}".format(error)

    def get_all_legitimate_person_info(self):
        self.connect()
        try:
            person_info_list = self.__execute(GET_ALL_LEGITIMATE_PERSON_INFO)
            self.close()
            return person_info_list
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to get all legitimate person info. Error =>  {}".format(error)

    def get_legitimate_person_info(self, person_mac: str):
        self.connect()
        try:
            person_info = self.__execute(GET_LEGITIMATE_PERSON_INFO, {PERSON_MAC: person_mac})
            self.close()
            return person_info
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to get a legitimate person. Error =>  {}".format(error)

    def add_legitimate_person(self, person_mac, person_name, person_phone_number, notification, relation):
        self.connect()
        try:
            self.__execute(NEW_LEGITIMATE_PERSON, {PERSON_MAC: person_mac,
                                                   PERSON_NAME: person_name,
                                                   PERSON_PHONE_NUMBER: person_phone_number,
                                                   NOTIFICATION: notification,
                                                   RELATION: relation})
            self.close()
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to add a new legitimate person. Error =>  {}".format(error)

    def update_legitimate_person(self, new_person_mac, person_mac):
        self.connect()
        try:
            self.__execute(UPDATE_LEGITIMATE_PERSON, {NEW_PERSON_MAC: new_person_mac,
                                                      PERSON_MAC: person_mac})
            self.close()
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                self.close()
                return "Failed when trying to update a legitimate person. Error =>  {}".format(error)
