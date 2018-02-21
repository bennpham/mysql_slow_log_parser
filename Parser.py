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
                if _check_parser_settings_to_log_values(parser_settings, log):
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

def _check_parser_settings_to_log_values(parser_settings, log):
    # Query Time Min
    if log.query_time <= parser_settings.output_query_time_min:
        return False
    # Query Time Max
    if log.query_time >= parser_settings.output_query_time_max and parser_settings.output_query_time_max != -1:
        return False
    # Lock Time Min
    if log.lock_time <= parser_settings.output_lock_time_min:
        return False
    # Lock Time Max
    if log.lock_time >= parser_settings.output_lock_time_max and parser_settings.output_lock_time_max != -1:
        return False
    # Rows Sent Min
    if log.rows_sent <= parser_settings.output_rows_sent_min:
        return False
    # Rows Sent Max
    if log.rows_sent >= parser_settings.output_rows_sent_max and parser_settings.output_rows_sent_max != -1:
        return False
    # Rows Examined Min
    if log.rows_examined <= parser_settings.output_rows_examined_min:
        return False
    # Rows Examined Max
    if log.rows_examined >= parser_settings.output_rows_examined_max and parser_settings.output_rows_examined_max != -1:
        return False
    # Datetime Min
    if parser_settings.output_datetime_min != '0000-00-00':
        try:
            if log.datetime_value >= datetime.datetime.strptime(parser_settings.output_datetime_min, '%Y-%m-%d'):
                return False
        except:
            pass
    # Datetime Max
    if parser_settings.output_datetime_max != '0000-00-00':
        try:
            if log.datetime_value <= datetime.datetime.strptime(parser_settings.output_datetime_max, '%Y-%m-%d'):
                return False
        except:
            pass
    # Output database_user
    if parser_settings.output_database_user != "" and parser_settings.output_database_user != log.database_host.split()[2]:
        return False
    # Output database_host
    if parser_settings.output_database_host != "" and parser_settings.output_database_host != log.database_host.split()[4]:
        return False
    # Output database_name
    if parser_settings.output_database_name != "" and parser_settings.output_database_name != log.database[4:-2]:
        return False
    return True
