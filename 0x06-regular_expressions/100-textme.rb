#!/usr/bin/env ruby

def parse_log_entry(log_entry)
    sender = log_entry.match(/\[from:(.*?)\]/)[1]
    receiver = log_entry.match(/\[to:(.*?)\]/)[1]
    flags = log_entry.match(/\[flags:(.*?)\]/)[1]
    "#{sender},#{receiver},#{flags}"
end

# Extract the log entry from the command-line argument
log_entry = ARGV[0]

# Check if the log entry is not nil
if log_entry
    # Check if it's an SMS transaction
    if log_entry.include?('Sent SMS') || log_entry.include?('Receive SMS')
        puts parse_log_entry(log_entry)
    else
        puts "Not an SMS transaction."
    end
else
    puts "Usage: ./name 'log_entry'"
end
