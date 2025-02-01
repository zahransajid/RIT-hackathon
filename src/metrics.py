import pandas as pd
import numpy as np


# TODO: Add implementations for the following functions
def calculate_AWT(df: pd.DataFrame, route: str, date: str, day: str) -> float:
    # group by stop and then direction = 0
    # calculate the average wait time for each stop
    stops = set(df['stop_code'])
    stop_WT_direction_0 = []
    stop_WT_direction_1 = []

    for stop in stops:
        stop_data = df[df['stop_code'] == stop]
        
        # Direction 0
        direction_0 = stop_data[stop_data['direction_id'] == 0].sort_values(by=['act_dep_time_x'])
        if len(direction_0) > 1:
            WT = direction_0['act_dep_time_x'].diff().dropna().tolist()
            if(len(WT) == 0):
                continue
            stop_WT_direction_0.append(sum(WT) / len(WT))

        # Direction 1
        direction_1 = stop_data[stop_data['direction_id'] == 1].sort_values(by=['act_dep_time_x'])
        if len(direction_1) > 1:
            WT = direction_1['act_dep_time_x'].diff().dropna().tolist()
            if(len(WT) == 0):
                continue
            stop_WT_direction_1.append(sum(WT) / len(WT))

    total_stops = len(stop_WT_direction_0) + len(stop_WT_direction_1)
    if total_stops == 0:
        return 0  # Avoid division by zero

    average_WT = (sum(stop_WT_direction_0) + sum(stop_WT_direction_1)) / total_stops
    return average_WT


def calculate_kilometers_travelled(df: pd.DataFrame) -> float:
    # takes in a dataframe and returns the kilometers travelled
    # assume that the df passed is for a specific route on a specific date
    return 0


def calculate_passenger_ridership(df: pd.DataFrame) -> float:
    # takes in a dataframe and returns passenger ridership
    # assume that the df passed is for a specific route on a specific date
    return 0
