import datetime


class Log:
    database = ""
    database_host = ""
    time = ""
    timestamp = ""
    statement = ""
    query_time = 0
    lock_time = 0
    rows_sent = 0
    rows_examined = 0
    datetime_value = datetime.time(0,0)

    def __init__(self, datetime="", database_host="", time="", database="", timestamp="", statement="",
                 query_time=0, lock_time=0, rows_sent=0, rows_examined=0, datetime_value=datetime.time(0,0)):
        self.datetime = datetime
        self.database_host = database_host
        self.time = time
        self.database = database
        self.timestamp = timestamp
        self.statement = statement

        self.query_time = query_time
        self.lock_time = lock_time
        self.rows_sent = rows_sent
        self.rows_examined = rows_examined
        self.datetime_value = datetime_value
