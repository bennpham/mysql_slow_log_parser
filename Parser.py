import Log
import datetime


class Parser:

    def __init__(self):
        self.list = []

    def add(self, log):
        self.list.append(log)

    def clear(self):
        self.list = []

    def reorder(self, order, sort):
        # Define default key
        key = lambda log: log.query_time
        reverse = True

        if order == "query_time":
            key = lambda log: log.query_time
        elif order == "lock_time":
            key = lambda log: log.lock_time
        elif order == "rows_sent":
            key = lambda log: log.rows_sent
        elif order == "rows_examined":
            key = lambda log: log.rows_examined
        elif order == "datetime":
            key = lambda log: log.datetime_value

        if sort == 'asc':
            reverse = False
        elif sort == 'desc':
            reverse = True

        self.list.sort(key=key, reverse=reverse)

    def parse(self, file):
        with open(file, "r") as infile:
            lines = infile.readlines()[3:]

            log = Log.Log()
            first_log = True
            for line in lines:
                if line[0:7] == "# Time:":
                    if first_log:
                        first_log = False
                    else:
                        self.add(log)
                        log = Log.Log()
                    log.datetime = line
                    log.datetime_value = datetime.datetime(int(line[8:12]), int(line[13:15]),
                                                           int(line[16:18]),
                                                           int(line[19:21]), int(line[22:24]),
                                                           int(line[25:27]))
                elif line[0:12] == "# User@Host:":
                    log.database_host = line
                elif line[0:13] == "# Query_time:":
                    log.time = line
                    # Get number values for query_time, lock_time, rows_sent, rows_examined
                    time = line.split()
                    log.query_time = float(time[2])
                    log.lock_time = float(time[4])
                    log.rows_sent = float(time[6])
                    log.rows_examined = float(time[8])
                elif line[0:3] == "use":
                    log.database = line
                elif line[0:14] == "SET timestamp=":
                    log.timestamp = line
                else:
                    log.statement = line

    def write(self, file, parser_settings):
        with open(file, "w") as outfile:
            for log in self.list:
                if parser_settings.display_datetime == 1:
                    outfile.write(log.datetime)
                if parser_settings.display_database_host == 1:
                    outfile.write(log.database_host)
                if parser_settings.display_time == 1:
                    outfile.write(log.time)
                if parser_settings.display_database == 1:
                    outfile.write(log.database)
                if parser_settings.display_timestamp == 1:
                    outfile.write(log.timestamp)
                if parser_settings.display_statement == 1:
                    outfile.write(log.statement)
                outfile.write("\n")
