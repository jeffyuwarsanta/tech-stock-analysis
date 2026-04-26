# Technology Stock Performance Explorer

## 1. Problem & User

This project is an interactive Python tool that helps beginner investors or finance students compare four major technology stocks: Apple, Microsoft, Nvidia, and Google.

The tool is designed for beginners who may not know how to compare stocks beyond looking at price movement.

## 2. Data

Source: WRDS CRSP monthly stock data 
Access date: 18 April 2026
The Streamlit app uses a cleaned CSV file exported from the WRDS-based notebook.

## 3. Stocks Compared

- AAPL: Apple
- MSFT: Microsoft
- NVDA: Nvidia
- GOOGL: Google 

# 4. methods

The project uses Python to:

- access WRDS data
- clean and prepare monthly stock data
- calculate growth over time
- calculate risk using volatility
- calculate consistency using positive monthly return rate
- calculate downside risk using drawdown
- visualise the results in Streamlit

## 5. Key Features

The app includes four beginner-friendly comparisons:
1. Growth over time
2. Risk vs return
3. Consistency
4. Downside risk

# 6. How to Run

Open the project folder and run:

```bash
python -m streamlit run app.py