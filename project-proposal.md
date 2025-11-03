# Project Proposals

## The Effect of Weather Temperature on Marathon Pace

### 1. Project Overview

This project aims to analyze the relationship between **weather temperature** and **marathon running performance** using **linear regression**. The core hypothesis is that **warmer temperatures lead to slower average marathon paces**. By combining race result data with corresponding weather information, this project will quantify how environmental conditions affect endurance performance.

### 2. Background and Motivation

Recent studies suggest that climate change is already influencing the outcomes of endurance events. According to a BBC Sport article (“_Climate change impacting marathon records_,” 28 Oct 2025), research by Climate Central found that rising global temperatures are making it increasingly difficult for runners to achieve record-breaking performances. The study predicts that by **2045**, nearly **86% of marathons worldwide** will no longer experience optimal running conditions — approximately **4°C for men** and **10°C for women**.

### 3. Research Question and Hypothesis

**Research Question:**
How does ambient temperature on race day affect marathon finish pace?

**Hypothesis:**
As temperature increases, average marathon pace becomes slower.

### 4. Methodology

1. **Data Collection**

   - Use publicly available datasets of marathon finish times (e.g., from major marathons such as Boston, London, Berlin).
   - Scrape or obtain corresponding **weather data** (temperature, humidity, wind speed) for each event date and location using APIs like _Open-Meteo_ or _NOAA_ archives.
   - Merge datasets based on date and race location.

2. **Data Processing**

   - Convert finish times into pace (minutes per kilometer).
   - Clean and standardize weather measurements.
   - Remove outliers (e.g., incomplete races, extreme conditions).

3. **Analysis**

   - Apply **simple linear regression** (pace vs. temperature).
   - Optionally extend to **multiple regression** to control for other variables (e.g., humidity, elevation, gender, year).
   - Visualize the relationship using scatter plots with regression lines.

4. **Evaluation**

   - Assess the model fit.

### 5. Expected Results

It is expected that the regression will show a **positive correlation** between temperature and marathon pace — meaning higher temperatures lead to slower running speeds.

### 6. Tools and Technologies

- **Python** (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)
- **Jupyter Notebook**
- **Data Sources:**

  - Public marathon results databases
  - Weather data APIs (Open-Meteo, NOAA, Meteostat)

### 7. Significance

This study combines **sports science** and **data analytics** to explore a real-world impact of **climate change on athletic performance**. By identifying how temperature affects race outcomes, the findings could inform race scheduling, athlete preparation, and environmental adaptation strategies for endurance events.
