import os
import pandas as pd
import matplotlib.pyplot as plt

# Configuration
folder = 'C:\\Users\\chohs\\BMS\\아이오닉5\\01241227999\\012412279999\\Save_file\\trip_by_trip\\3월'
filelist = [file for file in os.listdir(folder) if file.endswith('.csv')]

# Sort files based on numbers in filenames
filelist.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

# Load and Plot Data
fig, axs = plt.subplots(3, 6, figsize=(18, 10))  # 3 rows, 6 columns for subplots
axs = axs.flatten()  # Flatten the 2D array of subplots to a 1D array

for i, filename in enumerate(filelist[3:4]):  # Adjust the range if needed
    data_now = pd.read_csv(os.path.join(folder, filename))

    # Check if 'time' column exists
    if 'time' not in data_now.columns:
        print(f"'time' column not found in file {filename}. Skipping.")
        continue

    # Convert 'time' to datetime
    data_now['time'] = pd.to_datetime(data_now['time'])
    t = data_now['time']

    for j in range(1, 19):  # Iterate over 'mod1' to 'mod18' columns
        mod_col_name = f'mod_temp_list{j}'

        # Check if 'mod_temp_list' column exists
        if mod_col_name not in data_now.columns:
            print(f"'{mod_col_name}' column not found in file {filename}. Skipping.")
            continue

        mod_data = data_now[mod_col_name]

        # Plot on individual subplot
        axs[j - 1].plot(t, mod_data)

        # Graph settings
        axs[j - 1].set_title(f'{mod_col_name}')
        axs[j - 1].set_xlabel('Time')
        axs[j - 1].set_ylabel('Mod_temp_list')
        axs[j - 1].xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M'))
plt.tight_layout()
date_str = pd.to_datetime(data_now['time'][0]).strftime('%Y-%m-%d')
plt.figtext(0.5, 1, f'Trip4', ha='center', va='top', fontsize=16)
plt.figtext(1, 0, date_str, ha='right', va='bottom')

plt.show()
