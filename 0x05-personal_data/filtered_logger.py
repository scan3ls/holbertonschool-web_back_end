#!/usr/bin/env python3
""" Pesonal Data Regex-ing"""
import logging
from typing import List
import re
import mysql.connector
from os import getenv

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ Use regex to replace occurrences of certain field values """
    for field in fields:
        message = re.sub(f"{field}=(.+?){separator}",
                         f"{field}={redaction}{separator}", message)
    return message


def get_logger() -> logging.Logger:
    """ returns a logger object """
    user_data = logging.getLogger('user_data')
    user_data.setLevel(logging.INFO)
    user_data.propogate = False

    streamHandler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    streamHandler.setFormatter(formatter)

    user_data.addHandler(streamHandler)

    return user_data


def main():
    """ """

    user_data = get_logger()
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = cursor.column_names
    for row in cursor:
        msg = "; ".join(
            [f"{fields[i]}={str(col)}" for i, col in enumerate(row)]
        )
        record = logging.LogRecord(
            user_data.name,
            logging.INFO,
            None, None,
            msg,
            None, None
        )
        print(user_data.handle(record))

    cursor.close()
    db.close()


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Return a connection to a MySQL server """
    mysql_login = {
        'user': getenv('PERSONAL_DATA_DB_USERNAME'),
        'password': getenv('PERSONAL_DATA_DB_PASSWORD'),
        'host': getenv('PERSONAL_DATA_DB_HOST'),
        'database': getenv('PERSONAL_DATA_DB_NAME')
    }
    cnx = mysql.connector.connect(**mysql_login)

    return cnx


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ constructor for Redacting Formatter """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.__fields = [i for i in fields]

    def format(self, record: logging.LogRecord) -> str:
        """ does some formatty stuff """
        return filter_datum(
            self.__fields,
            self.REDACTION,
            super().format(record),
            self.SEPARATOR
        )


if __name__ == "__main__":
    main()
