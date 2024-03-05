clc;clear;close all

path_folder = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\MATLAB R2023b\Matlab data';
filename = 'HNE_FCC_01_OCV_022.txt';

data_now = readtable([path_folder filesep filename], 'FileType', 'text', 'NumHeaderLines', 14,...  % load the data
           'readVariableNames',0);


    data1.I = data_now.Var7;
    data1.V = data_now.Var8;
    data1.t2 = data_now.Var2; 
    data1.t1 = data_now.Var4; % step time, format in duration
    data1.cycle = data_now.Var3;
    data1.step = data_now.Var5;
    data1.T = data_now.Var13;

figure(1)
yyaxis left
plot(data1.t2,data1.V); hold on
yyaxis right
plot(data1.t2, data1.step)

figure(2)
plot(data1.t2,data1.I)

% TAKE OCV STEP
% ////////////////////////////////////////////////////////////////////////////////////////
ocv_chg_data(:,1) = seconds(data1.t2(data1.I>0));
ocv_chg_data(:,2) = data1.I(data1.I>0);
ocv_chg_data(:,3) = data1.V(data1.I>0);

ocv_dch_data(:,1) = seconds(data1.t2(data1.step ==6));
ocv_dch_data(:,2) = data1.I(data1. step ==6);
ocv_dch_data(:,3) = data1.V(data1. step ==6);

figure(2)
plot(ocv_chg_data(:,1),ocv_chg_data(:,3)); hold on
plot(ocv_dch_data(:,1),ocv_dch_data(:,3))



%SOC Calculation
ocv_chg_data(:,4) = cumtrapz(ocv_chg_data(:,1),ocv_chg_data(:,2));
ocv_chg_data(:,5) = ocv_chg_data(:,4)/(ocv_chg_data(end,4));

ocv_dch_data(:,4) = cumtrapz(ocv_dch_data(:,1),ocv_dch_data(:,2));
ocv_dch_data(:,5) = 1-ocv_dch_data(:,4)/(ocv_dch_data(end,4));


figure(3)
plot(ocv_chg_data(:,5),ocv_chg_data(:,3))
hold on
plot(ocv_dch_data(:,5),ocv_dch_data(:,3))
legend('chg','dch')

return


% Save PCV
OCV = [ocv_chg_data(:,5), ocv_chg_data(:,3)];
save OCV_inclass.mat OCV



