Change default_setting.cfg to change the ordering of how the parser will parse the data,
output the parsed data, read the data, etc.

order
    * Keyword parser will sort results by
    - query_time
    - lock_time
    - rows_sent
    - rows_examined
    - datetime

sort
    * ascending or descending order for sorting
    - asc
    - desc

default_log_folder
    * Default folder to find where all the log files to read are stored
    * Make sure there aren't any other files EXCEPT mysql-slow-logs
    - <ANY FOLDER NAME>

default_log_name
    * Default name to name the parsed log
    - <ANY FILENAME>

output_query_time_min
    * Minimum query time to output in the log
    * Default -1 (don't check)
    - <ANY NUMBER>

output_query_time_max
    * Maximum query time to output in the log
    * Default -1 (don't check)
    - <ANY NUMBER>

output_lock_time_min
    * Minimum lock time to output in the log
    * Default -1 (don't check)
    - <ANY NUMBER>

output_lock_time_max
    * Maximum lock time to output in the log
    * Default -1 (don't check)
    - <ANY NUMBER>

output_rows_sent_min
    * Minimum rows sent to output in the log
    * Default -1 (don't check)
    - <ANY NUMBER>

output_rows_sent_max
    * Maximum rows sent to output in the log
    * Default -1 (don't check)
    - <ANY NUMBER>

output_rows_examined_min
    * Minimum rows examined to output in the log
    * Default -1 (don't check)
    - <ANY NUMBER>

output_rows_examined_max
    * Maximum rows examined to output in the log
    * Default -1 (don't check)
    - <ANY NUMBER>

output_datetime_min
    * Minimum datetime to output in the log
    * Default 0000-00-00 (don't check)
    - Any date format in the form of YYYY-MM-DD

output_datetime_max
    * Maximum datetime to output in the log
    * Default 0000-00-00 (don't check)
    - Any date format in the form of YYYY-MM-DD

output_database_user
    * Database user to filter only
    * Default is empty
    - Any IP address or localhost

output_database_host
    * Database host to filter only (such as localhost or some IP address)
    * Default is empty
    - Any IP address or localhost

output_database_name
    * Database name to filter only
    * Default is empty
    - Any name

display_datetime:
    * Display time that slow query log occurs
    - 0 or 1

display_database_host:
    * Display name of database host and user
    - 0 or 1

display_time
    * Display query_time, lock_time, rows_sent, rows_examined
    - 0 or 1

display_database:
    * Display name of database
    - 0 or 1

display_timestamp:
    * Display numeric SET timestamp
    - 0 or 1

display_statement:
    * Display SQL statement that caused the slow query
    - 0 or 1
