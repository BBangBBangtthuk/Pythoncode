clear; clc; close all;

% 단일 CSV 파일 경로 설정
csvFilePath = 'C:\Users\chohs\BMS\아이오닉5\01241227999\012412279999\Save_file\trip_by_trip\01241227999-03-trip-4.csv';

% CSV 파일 읽기
dataTable = readtable(csvFilePath);

% 'Time'와 'batt_coolant_inlet_temp' 추출
time = datetime(dataTable.time, 'InputFormat', 'yyyy-MM-dd HH:mm:ss');
batt_coolant_inlet_temp = dataTable.batt_coolant_inlet_temp;

% 플로팅
figure;
plot(time, batt_coolant_inlet_temp);

% 축 레이블 및 그래프 제목 설정
xlabel('Time');
ylabel('Batt Coolant Inlet Temp');
title('trip 4');

% 그리드 표시
grid on;
