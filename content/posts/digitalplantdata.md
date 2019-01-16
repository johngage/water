Title: Digital Plant Operational Data
Date: 2018-11-27
Category: Water

#### Notes on Rachel Slabaugh Nuclear Plant Digital Data and Machine Learning ####

*BIDS presentation Tuesday, 27 Nov 2018*

Nuclear plants are 3-5X more expensive to build and maintain than fossil fuel

Major operational and maintenance costs are personnel

Example of *Southern Nuclear*, one of US nuclear operators:
* 6 months of data is 1 Terabyte: reveals how little is monitored.
* No retention of older data
* Little analysis, not set up to allow machine learning

* Need physics-based models with machine learning parameter estimation

* Battery Fault Detection: capture beginning of temperature rise; do not wait until threshold temperature is reached, with damage already present. Use Kalman filter with Theta = 0.3 to catch beginning
