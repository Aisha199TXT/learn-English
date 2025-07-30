import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv("progress.csv", parse_dates=["date"])

plt.figure(figsize=(8, 4))
plt.plot(df["date"], df["new_words"], marker="o", label="New Words Learned")
plt.plot(df["date"], df["mastered_words"], marker="o", label="Mastered Words (Cumulative)")
plt.xticks(rotation=45)
plt.ylabel("Word Count")
plt.title("Daily Vocabulary Study Progress")
plt.legend()
plt.tight_layout()

today = datetime.now().strftime("%Y-%m-%d")
plt.savefig(f"charts/progress_{today}.png")
plt.savefig("charts/progress_latest.png")
