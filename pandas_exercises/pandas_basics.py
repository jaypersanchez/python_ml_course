## Beginner Creating and View Data
import pandas as pd

print(f'Panda version {pd.__version__}')

df = pd.read_csv('./data/sol_exchange_data_yearly.csv')
print(df)

# Locate Row
print(df.loc[[1]])

myvar = pd.Series(df['open_price'].values[4], index=["w","x", "y", "z"])
print(myvar)

# Count NaN values before dropping to verify
def countNanValueCells(df):
    # Assuming 'df' is your DataFrame
    
    # Count NaN values after dropping to verify
    nan_count_after = df.isna().sum().sum()

    # Calculate the number of dropped NaN values
    nan_dropped = nan_count_before - nan_count_after

    print(f"Number of NaN values before dropping: {nan_count_before}")
    print(f"Number of NaN values after dropping: {nan_count_after}")
    print(f"Number of NaN values dropped: {nan_dropped}")
    
# remove rows empty cells
nan_count_before = df.isna().sum().sum() # Count NaN values before dropping
df = df.dropna() # then remove cell
countNanValueCells(df)





