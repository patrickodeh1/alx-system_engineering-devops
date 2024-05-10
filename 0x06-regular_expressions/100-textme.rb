#!/usr/bin/env ruby
# Define a method to parse each log entry
def parse_log_entry(log_entry)
    sender = log_entry.match(/\[from:(.*?)\]/)[1]
    receiver = log_entry.match(/\[to:(.*?)\]/)[1]
    flags = log_entry.match(/\[flags:(.*?)\]/)[1]
    "#{sender},#{receiver},#{flags}"
end

# Read the log file line by line
File.open('logfile.txt', 'r') do |file|
    file.each_line do |line|
        # Extract log entry timestamp and content
        timestamp, log_entry = line.match(/^\w{3} \d{1,2} \d{2}:\d{2}:\d{2} (.*?mdr: .*)$/)[1].split(' ', 2)
        # Check if it's an SMS transaction
        if log_entry.include?('Sent SMS') || log_entry.include?('Receive SMS')
            puts parse_log_entry(log_entry)
        end
    end
end
