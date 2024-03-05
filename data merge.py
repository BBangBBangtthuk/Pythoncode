import os
import pandas as pd

# 디렉토리 경로 설정
directory = r'C:\Users\chohs\BMS\아이오닉5\01241227999\01241227999\2023-03'

# 모든 파일을 담을 빈 리스트 생성
all_files = []

# 디렉토리 내 파일들을 모두 순회하며 리스트에 추가
for filename in os.listdir(directory):
    if filename.endswith(".csv"):  # CSV 파일만 선택
        filepath = os.path.join(directory, filename)
        # CSV 파일을 DataFrame으로 읽어서 리스트에 추가
        df = pd.read_csv(filepath)
        all_files.append(df)

# 모든 DataFrame을 병합
combined_df = pd.concat(all_files, ignore_index=True)

# 시간값 = 오름차순
combined_df['시간'] = pd.to_datetime(combined_df['time'])
combined_df = combined_df.sort_values(by='time', ascending=True)

# csv file 저장 경로
save_directory = r'C:\Users\chohs\BMS\아이오닉5\01241227999\01241227999\Save_file'
save_path = os.path.join(save_directory, 'bms_01241227999_2023_03.csv')

# csv file 저장
combined_df.to_csv(save_path, index=False)
