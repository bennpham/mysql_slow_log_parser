import datetime


class ParserSettings:
    def __init__(self):
        self.order = 'query_time'
        self.sort = 'desc'
        self.default_log_name = 'mysql_slow_log.txt'
        self.output_query_time_min = -1
        self.output_query_time_max = -1
        self.output_lock_time_min = -1
        self.output_lock_time_max = -1
        self.output_rows_sent_min = -1
        self.output_rows_sent_max = -1
        self.output_rows_examined_min = -1
        self.output_rows_examined_max = -1
        self.output_datetime_min = '0000-00-00'
        self.output_datetime_max = '0000-00-00'
        self.output_database_user = ''
        self.output_database_host = ''
        self.output_database_name = ''
        self.display_datetime = 1
        self.display_database_host = 0
        self.display_time = 1
        self.display_database = 1
        self.display_timestamp = 0
        self.display_statement = 1

    def read(self, file):
        settings = dict()

        with open(file, "r") as infile:
            for line in infile.readlines():
                parsed_line = line.strip('\n').split(":")
                if len(parsed_line) == 2:
                    settings[parsed_line[0].strip()] = parsed_line[1].strip().strip('"')

        self.order = sanitize_order(settings["order"])
        self.sort = sanitize_sort(settings["sort"])
        self.default_log_name = sanitize_filename(settings["default_log_name"])
        self.output_query_time_min = sanitize_number(settings["output_query_time_min"])
        self.output_query_time_max = sanitize_number(settings["output_query_time_max"])
        self.output_lock_time_min = sanitize_number(settings["output_lock_time_min"])
        self.output_lock_time_max = sanitize_number(settings["output_lock_time_max"])
        self.output_rows_sent_min = sanitize_number(settings["output_rows_sent_min"])
        self.output_rows_sent_max = sanitize_number(settings["output_rows_sent_max"])
        self.output_rows_examined_min = sanitize_number(settings["output_rows_examined_min"])
        self.output_rows_examined_max = sanitize_number(settings["output_rows_examined_max"])
        self.output_datetime_min = sanitize_datetime(settings["output_datetime_min"])
        self.output_datetime_max = sanitize_datetime(settings["output_datetime_max"])
        self.output_database_user = settings["output_database_user"]
        self.output_database_host = settings["output_database_host"]
        self.output_database_name = settings["output_database_name"]
        self.display_datetime = sanitize_binary_number(settings["display_datetime"])
        self.display_database_host = sanitize_binary_number(settings["display_database_host"])
        self.display_time = sanitize_binary_number(settings["display_time"])
        self.display_database = sanitize_binary_number(settings["display_database"])
        self.display_timestamp = sanitize_binary_number(settings["display_timestamp"])
        self.display_statement = sanitize_binary_number(settings["display_statement"])

    def write(self, file):
        with open(file, 'w') as outfile:
            outfile.write('order: "' + str(self.order) + '"\n')
            outfile.write('sort: "' + str(self.sort) + '"\n')
            outfile.write('default_log_name: "' + str(self.default_log_name) + '"\n')
            outfile.write('output_query_time_min: ' + str(self.output_query_time_min) + '\n')
            outfile.write('output_query_time_max: ' + str(self.output_query_time_max) + '\n')
            outfile.write('output_lock_time_min: ' + str(self.output_lock_time_min) + '\n')
            outfile.write('output_lock_time_max: ' + str(self.output_lock_time_max) + '\n')
            outfile.write('output_rows_sent_min: ' + str(self.output_rows_sent_min) + '\n')
            outfile.write('output_rows_sent_max: ' + str(self.output_rows_sent_max) + '\n')
            outfile.write('output_rows_examined_min: ' + str(self.output_rows_examined_min) + '\n')
            outfile.write('output_rows_examined_max: ' + str(self.output_rows_examined_max) + '\n')
            outfile.write('output_datetime_min: "' + str(self.output_datetime_min) + '"\n')
            outfile.write('output_datetime_max: "' + str(self.output_datetime_max) + '"\n')
            outfile.write('output_database_user: "' + str(self.output_database_user) + '"\n')
            outfile.write('output_database_host: "' + str(self.output_database_host) + '"\n')
            outfile.write('output_database_name: "' + str(self.output_database_name) + '"\n')
            outfile.write('display_datetime: ' + str(self.display_datetime) + '\n')
            outfile.write('display_database_host: ' + str(self.display_database_host) + '\n')
            outfile.write('display_time: ' + str(self.display_time) + '\n')
            outfile.write('display_database: ' + str(self.display_database) + '\n')
            outfile.write('display_timestamp: ' + str(self.display_timestamp) + '\n')
            outfile.write('display_statement: ' + str(self.display_statement) + '\n')


def sanitize_order(setting):
    default = "query_time"
    order_set = {"query_time", "lock_time", "rows_sent", "rows_examined", "datetime"}
    if setting.lower() in order_set:
        return setting.lower()
    else:
        print("Incorrect order parameters. Setting default to " + default + ".")
        return default


def sanitize_sort(setting):
    default = "desc"
    sort_set = {'asc', 'desc'}
    if setting.lower() in sort_set:
        return setting.lower()
    else:
        print("Incorrect sort parameters. Setting default to " + default + ".")
        return default


def sanitize_number(setting):
    default = -1
    try:
        converted_setting = float(setting)
        if converted_setting > 0 or converted_setting == -1:
            return converted_setting
    except ValueError:
        pass
    print("Incorrect number parameters. Setting default to " + str(default) + ".")
    return default


def sanitize_binary_number(setting):
    default = 0
    if (str(setting)).isdigit():
        if int(setting) == 1 or int(setting) == 0:
            return int(setting)
    print("Incorrect binary number parameters. Setting default to " + str(default) + ".")
    return default


def sanitize_datetime(setting):
    default = '0000-00-00'
    try:
        datetime.datetime.strptime(setting, '%Y-%m-%d');
        return setting
    except ValueError:
        print("Incorrect datetime parameters. Setting default to " + default + ".")
        return default


def sanitize_filename(setting):
    default = "mysql_slow_log.txt"
    invalid_chars = set('\/:*?"<>|')
    if any((c in invalid_chars) for c in setting):
        return default
    print("Incorrect filename parameters. Setting default to " + default + ".")
    return setting
