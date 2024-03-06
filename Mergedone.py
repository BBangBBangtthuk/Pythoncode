import os
import pandas as pd
from tqdm import tqdm
import chardet

start_path = "C:/Users/chohs/BMS/아이오닉5/01241227999/01241227999/2023-03"  # 시작 디렉토리

def extract_info_from_filename(file_name):
    """파일명에서 단말기 번호와 연월 추출"""
    try:
        parts = file_name.split('_')
        device_no = parts[1]  # 단말기 번호
        date_parts = parts[2].split('-')
        year_month = '-'.join(date_parts[:3])  # 연월 (YYYY-MM 형식)
        return device_no, year_month
    except IndexError:
        return None, None

def read_file_with_detected_encoding(file_path):
    try:
        # 파일의 인코딩을 감지하여 데이터를 읽음
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read(100000))  # 첫 100,000 바이트를 사용하여 인코딩 감지
        encoding = result['encoding']
        return pd.read_csv(file_path, encoding=encoding, header=0)
    except (pd.errors.ParserError, UnicodeDecodeError) as e:
        # 인코딩 오류 포함, 파싱 오류가 발생한 경우 처리
        print(f"오류가 발생한 파일: {file_path}, 오류: {e}")
        return None  # 오류가 발생한 경우 None 반환

dfs = []

total_files = sum([file.endswith('.csv') for file in os.listdir(start_path)])

with tqdm(total=total_files, desc="진행 상황", unit="file") as pbar:
    for file in os.listdir(start_path):
        file_path = os.path.join(start_path, file)
        if os.path.isfile(file_path) and file.endswith('.csv'):
            df = read_file_with_detected_encoding(file_path)

            if df is not None:  # df가 None이 아닐 때만 처리
                # 'Unnamed'가 포함되어 있는지 확인
                if 'Unnamed' in df.columns[0]:
                    # 'Unnamed'를 포함하는 첫 번째 열 제거
                    df = df.drop(df.columns[0], axis=1)
                else:
                    # 'Unnamed'가 포함되지 않은 경우, 에러 메시지 출력하고 다음 파일로 넘어감
                    print(f"'Unnamed'가 포함되지 않은 파일: {file_path}. 이 파일은 건너뜁니다.")
                    pbar.update(1)
                    continue  # 다음 파일로 넘어가기

                # 첫 행을 제외하고 역순으로 정렬
                df = df.iloc[1:][::-1]

                # 파일명에서 단말기 번호와 연월 추출
                device_no, year_month = extract_info_from_filename(file)

                if device_no is not None and year_month is not None:
                    # 전처리된 데이터를 리스트에 추가
                    dfs.append(df)
                else:
                    print(f"파일명에서 단말기 번호와 연월을 추출할 수 없습니다: {file_path}")
            else:
                print(f"파일을 읽는 도중 오류가 발생했습니다: {file_path}")

            pbar.update(1)

# 모든 DataFrame을 병합
combined_df = pd.concat(dfs, ignore_index=True)

# 병합된 DataFrame을 CSV 파일로 저장
output_file_name = 'combined_data.csv'
output_file_path = os.path.join(start_path, output_file_name)
combined_df.to_csv(output_file_path, index=False)

print("모든 파일의 처리가 완료되었습니다.")
print(f"병합된 데이터가 저장된 경로: {output_file_path}")
