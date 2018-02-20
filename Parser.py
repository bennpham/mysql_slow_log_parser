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
        key = Log.Log.query_time
        reverse = True

        if order == "query_time":
            key = Log.Log.query_time
        elif order == "lock_time":
            key = Log.Log.lock_time
        elif order == "rows_sent":
            key = Log.Log.rows_sent
        elif order == "rows_examined":
            key = Log.Log.rows_examined
        elif order == "datetime":
            key = Log.Log.datetime_value

        if sort == 'asc':
            reverse = False
        elif sort == 'desc':
            reverse = True

        self.list.sort(key=key, reverse=reverse)

    def parse(self, file):
        with open(file, "r") as infile:
            lines = infile.readlines()[3:]
            num_of_entries = len(lines) // 6
            # Fails if remainder in divide by 6 and first line doesn't start with # Time
            if len(lines) % 6 != 0:
                return False
            if len(lines) > 0:
                if lines[0][0:7] != "# Time:":
                    return False
            for i in range(num_of_entries):
                log = Log.Log()
                log.datetime = lines[i*6]
                log.database_host = lines[i*6 + 1]
                log.time = lines[i*6 + 2]
                log.database = lines[i*6 + 3]
                log.timestamp = lines[i*6 + 4]
                log.statement = lines[i*6 + 5]
                # Get number values for query_time, lock_time, rows_sent, rows_examined
                time = lines[i*6 + 2].split()
                log.query_time = float(time[2])
                log.lock_time = float(time[4])
                log.rows_sent = float(time[6])
                log.rows_examined = float(time[8])
                log.datetime_value = datetime.datetime(int(log.datetime[8:12]), int(log.datetime[13:15]), int(log.datetime[16:18]),
                                                       int(log.datetime[19:21]), int(log.datetime[22:24]), int(log.datetime[25:27]))
                self.add(log)

    def write(self, file, parser_settings):
        with open(file, "w") as outfile:
            for log in self.list:
                if parser_settings.display_datetime == 1:
                    outfile.write(log.datetime + "\n")
                if parser_settings.display_database_host == 1:
                    outfile.write(log.database_host + "\n")
                if parser_settings.display_time == 1:
                    outfile.write(log.time + "\n")
                if parser_settings.display_database == 1:
                    outfile.write(log.database + "\n")
                if parser_settings.display_timestamp == 1:
                    outfile.write(log.timestamp + "\n")
                if parser_settings.display_statement == 1:
                    outfile.write(log.statement + "\n")
                outfile.write("\n")
