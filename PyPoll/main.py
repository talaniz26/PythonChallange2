import os
import csv

# Ensure the directory is the current directory of the Python script
os.chdir(os.path.dirname(__file__))

# Collect the data from the path of the Resources folder
election_data_csv = os.path.join("Resources", "election_data.csv")

# Initialize lists to store data
record_counts = []
total_votes = 0

# Open the CSV file
with open(election_data_csv, newline="") as csvfile:
    # Reading the data with the csv.reader module
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)  # Skip the header row

    # Iterate through each row in the CSV file
    for row in csv_reader:
        total_votes += 1
        value_to_count = row[2]

        # Check if the value is already in record_counts
        found = False
        for record in record_counts:
            if record[0] == value_to_count:
                record[1] += 1
                found = True
                break

        # If not found, add it to record_counts
        if not found:
            record_counts.append([value_to_count, 1])

# Output Structure
output_lines = []

output_lines.append("Election Results")
output_lines.append("----------------------------")

# Print the total votes
output_lines.append(f"Total Votes: {total_votes}")
output_lines.append("----------------------------")

# Print the counts and percentages for each unique record
for index, (record, count) in enumerate(record_counts, start=1):
    percentage = (count / total_votes) * 100
    percentage = round(percentage, 3)
    output_lines.append(f"{record}: {percentage}% ({count})")

# Find the winner, using the max function with a custom lambda function as the key parameter
winner_count = max(record_counts, key=lambda x: x[1])[1]
winners = [record[0] for record in record_counts if record[1] == winner_count]

# Print the winner(s)
output_lines.append("----------------------------")
for winner in winners:
    output_lines.append(f"Winner: {winner}")
    output_lines.append("----------------------------")

# Write to the output.txt file
output_file_path = os.path.join("Output", "Election_output.txt")
with open(output_file_path, 'w') as output_file: 
    for line in output_lines:
        print(line)
        output_file.write(line + '\n')

print("Results have been written to output.txt.")