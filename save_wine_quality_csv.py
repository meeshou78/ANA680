# save_wine_quality_csv.py
import pandas as pd
from ucimlrepo import fetch_ucirepo

# Step 1: Fetch dataset
wine_quality = fetch_ucirepo(id=186)

# Step 2: Extract features and targets
X = wine_quality.data.features
y = wine_quality.data.targets

# Step 3: Combine features and targets
df = pd.concat([X, y], axis=1)

# Step 4: Save as CSV
df.to_csv("wine_quality_dataset.csv", index=False)
print("Saved as 'wine_quality_dataset.csv'")