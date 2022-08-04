import numpy as np
import pandas as pd


def create_date_array(start_date, count):
    base = np.datetime64(start_date)
    date_array = np.array([base + np.timedelta64(x, "D") for x in range(0, count)])
    date_array = np.datetime_as_string(date_array, unit="D")
    return date_array


def create_sine_array(size):
    x = np.arange(0, size)
    y = np.sin((x / 365 / np.pi / 32) * np.sin(x / (365 / np.pi / 32))) + 1
    return y


def create_training_sine_wave(start_date, end_date):
    start = np.datetime64(start_date)
    end = np.datetime64(end_date)
    number_of_days = (end - start).astype('int')

    date_array = create_date_array(start_date, number_of_days)
    sine_array = create_sine_array(number_of_days)
    return np.core.records.fromarrays([date_array, sine_array], names='date,value')


def blank_last_values(array, number_of_predictions):
    arr = np.copy(array)
    for (i, value) in enumerate(array):
        if (i > arr.size - number_of_predictions):
            arr[i] = None
    return arr


def create_prediction_sine_wave(start_date, end_date, number_of_predictions, begin_date):
    start = np.datetime64(start_date)
    end = np.datetime64(end_date)
    number_of_days = (end - start).astype('int')

    date_array = create_date_array(start_date, number_of_days)
    sine_array = create_sine_array(number_of_days)
    trimmed_array = blank_last_values(sine_array, number_of_predictions)
    combined_array = np.core.records.fromarrays([date_array, trimmed_array], names='date,value')
    combined_array = combined_array[combined_array['date'] >= begin_date]
    return combined_array


def save_array_to_csv(array, filename):
    df = pd.DataFrame(array)
    df = df.fillna('')
    df.to_csv(filename, index=False)
    return


def create():
    print('Creating freq_mod_training.csv')
    save_array_to_csv(create_training_sine_wave("2015-01-01", "2021-05-31"), "csv/freq_mod_training.csv")

    print('Creating freq_mod_prediction.csv')
    save_array_to_csv(create_prediction_sine_wave("2015-01-01", "2021-12-31", 30, "2021-06-01"),
                      "csv/freq_mod_prediction.csv")
