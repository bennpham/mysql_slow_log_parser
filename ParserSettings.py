class ParserSettings:
    def __init__(self):
        self.order = ''
        self.sort = ''
        self.default_log_folder = ''
        self.default_log_name = ''
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
        self.output_database_name = ''
        self.output_database_host = ''

    def read(self, file):
        settings = dict()

        with open(file, "r") as infile:
            for line in infile.readlines():
                parsed_line = line.strip('\n').split(":")
                if (len(parsed_line) == 2):
                    settings[parsed_line[0].strip()] = parsed_line[-1].strip()

        self.order = settings["order"]
        self.sort = settings["sort"]
        self.default_log_folder = settings["default_log_folder"]
        self.default_log_name = settings["default_log_name"]
        self.output_query_time_min = settings["output_query_time_min"]
        self.output_query_time_max = settings["output_query_time_max"]
        self.output_lock_time_min = settings["output_lock_time_min"]
        self.output_lock_time_max = settings["output_lock_time_max"]
        self.output_rows_sent_min = settings["output_rows_sent_min"]
        self.output_rows_sent_max = settings["output_rows_sent_max"]
        self.output_rows_examined_min = settings["output_rows_examined_min"]
        self.output_rows_examined_max = settings["output_rows_examined_max"]
        self.output_datetime_min = settings["output_datetime_min"]
        self.output_datetime_max = settings["output_datetime_max"]
        self.output_database_name = settings["output_database_name"]
        self.output_database_host = settings["output_database_host"]

    def write(self, file):
        with open(file, 'w') as outfile:
            outfile.write("order: " + self.order + "\n")
            outfile.write("sort: " + self.sort + "\n")
            outfile.write("default_log_folder: " + self.default_log_folder + "\n")
            outfile.write("default_log_name: " + self.default_log_name + "\n")
            outfile.write("output_query_time_min: " + self.output_query_time_min + "\n")
            outfile.write("output_query_time_max: " + self.output_query_time_max + "\n")
            outfile.write("output_lock_time_min: " + self.output_lock_time_min + "\n")
            outfile.write("output_lock_time_max: " + self.output_lock_time_max + "\n")
            outfile.write("output_rows_sent_min: " + self.output_rows_sent_min + "\n")
            outfile.write("output_rows_sent_max: " + self.output_rows_sent_max + "\n")
            outfile.write("output_rows_examined_min: " + self.output_rows_examined_min + "\n")
            outfile.write("output_rows_examined_max: " + self.output_rows_examined_max + "\n")
            outfile.write("output_datetime_min: " + self.output_datetime_min + "\n")
            outfile.write("output_datetime_max: " + self.output_datetime_max + "\n")
            outfile.write("output_database_name: " + self.output_database_name + "\n")
            outfile.write("output_database_host: " + self.output_database_host + "\n\n")
