
''' This module provides a reusable byline for the 'stellar_analytics_utils.py' module. '''

import math
import statistics

# Define Variables of Different Types
company_name: str = "Stellar Analytics Inc."
count_active_projects: int = 10
has_international_presence: bool = False
average_client_satisfaction: float = 4.7
services_offered: list = ["Data Analysis", "Machine Learning Consulting", "Business Intelligence Solutions"]
satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

# Define Formatted Strings
active_projects_string: str = f"Active Projects: {count_active_projects}"
international_presence_string: str = f"International Presence: {has_international_presence}"
client_satisfaction_string: str = f"Average Client Satisfaction: {average_client_satisfaction}"

# Calculate Descriptive Statistics
import statistics

smallest = min(satisfaction_scores)
largest = max(satisfaction_scores)
total = sum(satisfaction_scores)
count = len(satisfaction_scores)
mean = statistics.mean(satisfaction_scores)
mode = statistics.mode(satisfaction_scores)
median = statistics.median(satisfaction_scores)
standard_deviation = statistics.stdev(satisfaction_scores)

stats_string: str = f"""
Descriptive Statistics for Our Satisfaction Scores:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""

# Convert the list of services_offered to a formatted string
services_offered_string = "Services Offered: " + ", ".join(services_offered)

# Define Byline String
byline: str = f"""
{company_name}
{active_projects_string}
{international_presence_string}
{client_satisfaction_string}
{services_offered_string}
{stats_string}
"""

# Define Main Function
def main():
    ''' Display all output'''
    print(company_name)
    print(active_projects_string)
    print(international_presence_string)
    print(client_satisfaction_string)
    print(services_offered_string)
    print(stats_string)

# Call the main function
main()

# Conditional Script Execution
if __name__ == '__main__':
    # If all of the above works, then the byline should work too:
    print(byline)



# Standard library imports
import csv
import pathlib 

# External library imports (requires virtual environment)
import requests  

import stellar_analytics_utils