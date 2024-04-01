#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER maxSpan
#

def processLogs(logs, maxSpan):
    # Write your code here

    time_dict = {}
    
    for log in logs:
        user_id, timestamp, action = log.split()
        timestamp = int(timestamp)
        
        if user_id not in time_dict:
            time_dict[user_id] = {'sign-in': None, 'sign-out': None}
        time_dict[user_id][action] = timestamp
    
    filtered_users = [
        user_id for user_id, times in time_dict.items()
        if times['sign-out'] is not None and times['sign-in'] is not None and
           (times['sign-out'] - times['sign-in']) <= maxSpan
    ]

    return sorted(filtered_users, key=int)

    #
    # WARNING: Please do not use GitHub Copilot, ChatGPT, or other AI assistants
    #          when solving this problem!
    #
    # We use these tools in our coding too, but in our interviews, we also don't
    # allow using these, and want to see how we do without them.
    #

if __name__ == '__main__':
    fptr = sys.stdout

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    maxSpan = int(input().strip())

    result = processLogs(logs, maxSpan)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
