# Simple Time Series Data Generator

Python utility tool to generate deterministic time series data. These can be used to play with time series prediction algorithms. You can generate complex signals that are entirely deterministic ... any time series algorithm worth its salt should be able to make 100% accurate predictions.

## Requirements

* Python 3.6+

## Usage

    $ python -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python main.py

## Result

Training and prediction files in the ```csv/``` directory.

* Sine wave (with harmonics - change the code as required)
* Amplitude modulation
* Frequency modulation (needs work)