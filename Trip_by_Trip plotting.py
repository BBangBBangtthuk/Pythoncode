import os
import pandas as pd
import matplotlib.pyplot as plt

# Configuration
folder = 'C:\\Users\\chohs\\BMS\\아이오닉5\\01241227999\\012412279999\\Save_file\\trip_by_trip\\3월' # 파일 경로 수정은 이부분이다.
filelist = [file for file in os.listdir(folder) if file.endswith('.csv')] # csv로 저장되어 있는 파일을 불러들인다.

# Sort files based on numbers in filenames
filelist.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

# Load and Plot Data
fig, ax = plt.subplots()

for filename in filelist[1:2]: # 이부분을 수정해주면 된다. 파일을 고를때
    data_now = pd.read_csv(os.path.join(folder, filename))

    t = pd.to_datetime(data_now['time'])  # Convert 'time' to datetime
    pack_volt = data_now['pack_volt']

    # Graph plotting
    ax.plot(t, pack_volt)

# Graph settings
ax.set_title('Trip4')
ax.set_xlabel('Time')
ax.set_ylabel('Pack_V')


# Set x-axis to show only time
ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M:%S'))

# Automatically extract and display the date on the bottom right outside the plot
date_str = pd.to_datetime(data_now['time'][0]).strftime('%Y-%m-%d')
plt.figtext(1, 0, date_str, ha='right', va='bottom')

plt.show()
