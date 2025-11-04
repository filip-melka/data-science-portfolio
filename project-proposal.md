# Project Proposals

## 🏃‍♂️ Project 1: How Weather Affects Marathon Pace

### Overview

This project looks at how **temperature impacts marathon running pace** using **linear regression**. The idea is simple: **hotter weather makes runners slower**. I’ll combine marathon race results with weather data from the same days to see how much temperature affects performance.

### Why This Project

Recent research (BBC Sport, 2025) shows that climate change is already making it harder to break marathon records. As global temperatures rise, fewer races take place in ideal running conditions — around 4°C for men and 10°C for women.

### Approach

1. **Collect data** on marathon finish times from public sources (Boston, London, Berlin, etc.).
2. **Scrape weather info** — temperature, humidity, and wind speed — using APIs like Open-Meteo or NOAA.
3. **Combine both datasets** based on race date and location.
4. **Run a linear regression** to see how pace changes with temperature.
5. **Visualize** the relationship with scatter plots and trend lines.

### What I Expect

I expect to see a clear trend: as temperatures go up, runners’ paces get slower.

### Tools

- Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)
- Jupyter Notebook
- Weather APIs (Open-Meteo, NOAA, Meteostat)

---

## 💹 Project 2: Predicting Stock Movements with Random Forest

### Overview

This project predicts whether a stock’s price will **go up or down** the next day using a **Random Forest Classifier**.

### Idea

Use daily stock data from the **Alpaca API** to train a model that predicts the next day’s direction — up or down — based on recent price trends.

### Steps

1. **Collect stock data** (Open, High, Low, Close, Volume) for companies like AAPL, MSFT, or TSLA.
2. **Create features** such as:

   - Daily returns
   - Short-term moving averages (3, 7, 14 days)
   - Volume changes

3. **Label** each day as “Up” (if tomorrow’s price is higher) or “Down.”
4. **Train and test** a Random Forest model.
5. **Check accuracy** and see which features are most important.
6. **Visualize** predictions vs. real outcomes.

### Expected Outcome

- A model that predicts daily stock direction (Up/Down).
- Charts showing how well the model performs.
- Insights into which metrics matter most (returns, moving averages, etc.).

### Tools

- Python
- scikit-learn (Random Forest)
- pandas / NumPy (data manipulation)
- matplotlib / seaborn (visualization)
- Alpaca API (data source)

### Deliverables

- Jupyter Notebook with code, results, and charts
- Short summary explaining findings and model performance
