import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# set matplotlib to use 'Agg' backend for environments without display (like servers)
matplotlib.use("tkagg")


df = pd.read_excel("./Specialty.xlsx")

df.columns = df.columns.str.lower().str.replace(" ", "_").str.replace(",", "_")

print(df.head())


cols = [
    "no_clear_specialty",
    "deciding_between_fam_med_and_other",
    "deciding_between_surgical_and_other",
    "primary_care",
    "non_primary_care",
    "surgical",
    "non_surgical",
]

summary_cols = [
    "no_clear_specialty",
    "deciding_between_fam_med_and_other",
    "deciding_between_surgical_and_other",
    "primary_care",
    "non_primary_care",
    "surgical",
    "non_surgical",
]

# Frequency of each specialization overall
specialty_counts = (
    df.drop(columns=["timepoint", "ppos", "ppos_s", "ppos_c"]) == 1
).sum()

# By timepoint
specialty_counts_by_tp = df.groupby("timepoint").apply(
    lambda g: (g.drop(columns=["timepoint", "ppos", "ppos_s", "ppos_c"]) == 1).sum()
)


# Overall
summary_counts = (df[summary_cols] == 1).sum()

# By timepoint
summary_counts_by_tp = df.groupby("timepoint").apply(
    lambda g: (g[summary_cols] == 1).sum()
)


# Count 1's in those columns
counts = (df[cols] == 1).sum()

# Plot
plt.figure(figsize=(10, 6))
counts.plot(kind="bar")
plt.title("Frequency of 1's in Specialty Columns")
plt.ylabel("Count of 1's")
plt.xlabel("Specialty Category")
plt.xticks(rotation=45, ha="right")
plt.show()

timepoint_counts = df.groupby("timepoint")[cols].apply(lambda g: (g == 1).sum())

print("\nPer timepoint counts:")
print(timepoint_counts)

# Plot each timepoint separately
for tp in ["M1", "M2", "M3", "M4"]:
    if tp in timepoint_counts.index:  # ensure the timepoint exists
        plt.figure(figsize=(10, 6))
        timepoint_counts.loc[tp].sort_values(ascending=False).plot(kind="bar")
        plt.title(f"Frequency of 1's in Specialty Columns — {tp}")
        plt.ylabel("Count")
        plt.xticks(rotation=45, ha="right")
        plt.show()
