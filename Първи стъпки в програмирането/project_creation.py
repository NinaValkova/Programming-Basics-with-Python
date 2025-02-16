"""
Write a program that calculates how many hours it will take
an architect to prepare the designs of several construction sites.
Preparing one design takes three hours.
"""

DURATION = 3

name = input()
project_count = int(input())
project_duration = project_count*DURATION

print(f"The architect {name} will need {project_duration} hours to complete {project_count} project/s.")