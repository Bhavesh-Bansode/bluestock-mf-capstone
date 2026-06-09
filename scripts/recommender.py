import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

performance = pd.read_csv("../data/processed/07_scheme_performance_clean.csv")

def recommend_funds(risk_level):
    df = performance[performance["risk_grade"]== risk_level]
    return (df.sort_values( "sharpe_ratio",ascending=False).head(3)[["scheme_name", "sharpe_ratio","risk_grade"]])

recommend_funds("High")