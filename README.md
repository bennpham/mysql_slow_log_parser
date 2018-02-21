# MySQL Slow Log Parser
Python script used for parsing MySQL slow logs.

## How to Use
```bash
git clone https://github.com/bennpham/mysql_slow_log_parser.git
cd mysql_slow_log_parser
python run_parser.py
```

Run run_parser.py to execute the program.<br/>
If you want to parse multiple mysql-slow logs at a time, dump them in the logs folder. <br/>
The parsed logs should appear in your outputs folder.<br/>
Cfg folder is configuration files for how you want to parse your logs. You can also edit them in the program.<br/>
