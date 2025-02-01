import pandas as pd
import numpy as np
from src.metrics import calculate_AWT, calculate_kilometers_travelled, calculate_passenger_ridership
# load in data
joined_data = pd.read_csv('cache/joined_data.csv')


# Aggregate by day and short route name
days = set(joined_data['day'])
print(days)
data_aggregate = {day : {} for day in days}
x = 0

for day in days:
    day_data = joined_data[joined_data['day'] == day]
    route_names = set(day_data['route_short_name'])
    for route in route_names:
        grouped_by_route = day_data[day_data['route_short_name'] == route]
        dates = set(grouped_by_route['date'])
        if(route not in data_aggregate[day]):
            data_aggregate[day][route] = {"AWT" : [], "kilometers_travelled" : [], "passenger_ridership" : []}
        for date in dates:
            grouped_by_date_and_route = grouped_by_route[grouped_by_route['date'] == date]
            # if x < 5:
            #     grouped_by_date_and_route.to_csv(f'cache/{day}_{route}_{date}.csv')
            #     x += 1
            # Calculate metrics since they are on a per-day per-route basis
            data_aggregate[day][route]['AWT'].append(calculate_AWT(grouped_by_date_and_route, route, date, day))
            data_aggregate[day][route]['kilometers_travelled'].append(calculate_kilometers_travelled(grouped_by_date_and_route))
            data_aggregate[day][route]['passenger_ridership'].append(calculate_passenger_ridership(grouped_by_date_and_route))

# Test code to print metrics for monday on route 96 and E100
for day,route in zip(['Monday','Monday'],['96','E100']):
    AWT_all = data_aggregate[day][route]['AWT']
    AWT_avg = np.average([x for x in AWT_all if not np.isnan(x)])
    print(AWT_avg)
    data_aggregate[day][route]['kilometers_travelled']
    data_aggregate[day][route]['passenger_ridership']