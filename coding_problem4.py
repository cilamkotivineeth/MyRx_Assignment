def findPlatforms(arrivals, departures):
    # Sort the arrival and departure times
    arrivals.sort()
    departures.sort()

    n = len(arrivals)
    platforms_needed = 1  # At least one platform is always needed
    result = 1  # Track the maximum platforms needed at any time

    i = 1  # Pointer for arrivals
    j = 0  # Pointer for departures

    while i < n and j < n:
        # If the next arrival is before the next departure, we need a platform
        if arrivals[i] <= departures[j]:
            platforms_needed += 1
            i += 1
        # If the next departure is before the next arrival, one platform can be freed
        elif arrivals[i] > departures[j]:
            platforms_needed -= 1
            j += 1

        # Update the result with the maximum platforms needed at any time
        result = max(result, platforms_needed)

    return result

# Example 1
arrivals1 = ['9:00', '9:40', '9:50', '11:00', '15:00', '18:00']
departures1 = ['9:10', '12:00', '11:20', '11:30', '19:00', '20:00']

# Converting the times from string to 24-hour format for easy comparison
from datetime import datetime

def time_to_minutes(time_str):
    return datetime.strptime(time_str, '%H:%M').hour * 60 + datetime.strptime(time_str, '%H:%M').minute

arrivals1 = [time_to_minutes(time) for time in arrivals1]
departures1 = [time_to_minutes(time) for time in departures1]

print(findPlatforms(arrivals1, departures1))  # Output: 3

# Example 2
arrivals2 = ['9:00', '9:40']
departures2 = ['9:10', '12:00']

arrivals2 = [time_to_minutes(time) for time in arrivals2]
departures2 = [time_to_minutes(time) for time in departures2]

print(findPlatforms(arrivals2, departures2))  # Output: 1
