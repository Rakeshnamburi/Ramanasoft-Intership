log_data = [ 
("2023-10-26 10:00:00", "INFO", "User logged in"),  
("2023-10-26 10:01:00", "ERROR", "Database connection failed"),  
("2023-10-26 10:01:30", "INFO", "Data processed successfully"),  
("2023-10-26 10:02:00", "WARN", "Low disk space"),  
("2023-10-26 10:03:00", "ERROR", "Database connection failed"),  
("2023-10-26 10:04:00", "INFO", "User logged out"),  
("2023-10-26 10:05:00", "ERROR", "Null pointer exception"),  
("2023-10-26 10:05:30", "DEBUG", "Debugging user session"),  
]

# from collections import defaultdict



# def error_log_levels(log_data):
#     log_level_error = defaultdict(int)
#     for entry in log_data:
#         log_error = entry[1]
#         log_level_error[log_error] += 1
#     return log_level_error

# TASK-1  (QUESTION): Write a Python program to filter out all the log entries with the log level "ERROR" from the given log_data list. 
# The program should create a new list containing only the error logs and print them.

error_logs = [log for log in log_data if log[1] == "ERROR"]
print("Error Logs:")
for log in error_logs:
    print(log)

    # ekkada error_logs list comprehension lo log_data ni iterate chesi, prathi entry lo log level ni check chesthundi.

# ekkada count log_levels function lo log_data ni iterate chesi, prathi entry lo log level ni extract chesi, 
# dani count ni defaultdict lo increment chesthundi. Final ga, log_level_counts dictionary return chesthundi,
#     idi prathi log level ki count chupistundi.  







# task-1(2). Count Specific Errors: Count how many times the "Database connection failed" message 
# appears in the ERROR logs.

# import collections

# error_logs = [log for log in log_data if log[1] == "ERROR"]
# specific_error_count = collections.Counter(log[2] for log in error_logs)
# database_connection_failed_count = specific_error_count["Database connection failed"]



# specific error message only wanted like at above it shows how many messages 
# there are 2 "Database connection failed" errors.
# 2 logs are their so given the loop when it exceute it will redirect to 2









# Task 1(3). Find First Warning: Find the timestamp and message of the first "WARN" log. If no "WARN" 
# log exists, report that.

# import collections

# warn_logs = [log for log in log_data if log[1] == "WARN"]
# if warn_logs:
#     first_warn = warn_logs[0]
#     print(f"First WARN log: {first_warn[0]} - {first_warn[2]}")
# else:
#     print("No WARN logs found.")

# here we want to find the first warning log from the log_data list. 
# We filter the logs to get only those with the "WARN" level and check if any exist. 
# If they do, we print the timestamp and message of the first one; otherwise, we report that no WARN logs were found.







# Task-1(4)sort Logs by Timestamp: Create a new list of all log entries sorted by their timestamp 
# (ascending).

sorted_logs = sorted(log_data, key=lambda x: x[0])
print("\nSorted Logs:")
for log in sorted_logs:
    print(log)

    # e code ela use itundhi ante time stamp ni ascending order lo sort chesthundi.
    # ekkada lambda function use chesi prathi log entry lo timestamp ni key ga use chesi sort chesthundi. 
    # Final ga, sorted_logs list lo sorted log entries untayi, vatini print chesthundi.

    # asalike lambda endhuku use chesthundi ante, lambda function is a small anonymous function that can take any number of arguments but can only have one expression. In this case, it takes each log entry (which is a tuple) and returns the first element (the timestamp) to be used as the sorting key. 
    # This allows the `sorted()` function to sort the log entries based on their timestamps in ascending order.
    # \nsorted_logs list lo sorted log entries untayi, vatini print chesthundi.


# Task1-(5). Check for Critical Issues:  
# • Use all() to check if all log messages are shorter than 100 characters.  
# • Use any() to check if there is any log entry with the level "CRITICAL" (assume  
# "CRITICAL" is a possible level, though not in sample data).




all_short = all(len(message) < 100 for _, _, message in log_data)
any_critical = any(level == "CRITICAL" for _, level, _ in log_data)

print("\nAll messages <100 chars:", all_short)
print("Any CRITICAL log present:", any_critical)

# ekkada all() function use chesi prathi log message length ni check chesthundi, 100 characters kanna takkuva unte True return chesthundi.
# any() function use chesi prathi log level ni check chesthundi, "CRITICAL" level unte True return chesthundi. Final ga, results print chesthundi.
# log data endhuke use chesam ante, log data lo prathi log entry ni iterate chesi, message length and log level ni check cheyadaniki use chesam.





# Task1-(6). Append New Log: A new log entry has arrived: ("2023-10-26 10:06:00", "INFO", "System 
# check complete"). Append this to the original log_data list. 


log_data.append(("2023-10-26 10:06:00", "INFO", "System check complete"))
print("\nUpdated Log Data:")
for log in log_data:
    print(log)

    # e question ardham eenti ante, new log entry ni original log_data list ki append cheyali.
    # new log ne old log lo add cheyali anthe andhuke manam  \n update login chesam
    # for loop use chesi prathi log entry ni print chesthundi.
