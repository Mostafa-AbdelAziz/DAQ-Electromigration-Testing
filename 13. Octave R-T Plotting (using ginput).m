% example evaluation file _ R Vs. T

clear all; close all; warning off

 

cd 'C:\Users\m8abdela\Desktop\Sample 11 - Jan 13, 2021\R-T'

load 'TCR_210113110242Resistance Measurements of SAC305 flip chip_cancinotech.mat'

T = Tread1
R = -1*V1*10 

m_s=[];d_s=[];

for k=1:length(R(:,1)); % looping over all R signals/channels/specimens

 

r=R(k,:);

Tm=[];Rm=[];ave_ind=[];

figure(1);

subplot(2,1,2);plot(r);xlabel('Index');ylabel('Resistance, Ohm');hold on

subplot(2,1,1);plot(T);xlabel('Index');ylabel('Temperature, C');hold on;

if k==1;inds=[];

  for j=1:3;title(['Enter range ' num2str(j)])

    [X,Y]=ginput(2);inds=[inds X];

  end

end

for j=1:3; X=inds(:,j); ave_ind=[ave_ind mean(X)];

  %subplot(2,1,1);plot([X(1):X(2)],T(X(1):X(2)),'r')

  %subplot(2,1,2);plot([X(1):X(2)],r(X(1):X(2)),'r')

  Tm=[Tm mean(T(X(1):X(2)))];Rm=[Rm mean(r(X(1):X(2)))]; 

end

subplot(2,1,1);hold on;plot([1:length(T)],T,ave_ind,Tm,'o')

subplot(2,1,2);hold on;plot([1:length(r)],r,ave_ind,Rm,'o')

 

figure(2)

[p,S]=polyfit(Tm,Rm,1);

m_s=[m_s p(1)];d_s=[d_s p(2)];

 

plot(Tm,Rm, Tm, Rm, 'o')

ylabel('Resistance, Ohm');xlabel('Temperature, degC')

title(['Channel: ' num2str(k) ', m: ' num2str(p(1)) ' Ohm/C, d: ' num2str(p(2)) ' Ohm, m/d: ' num2str(p(1)/p(2)) ' 1/K']);

disp(['Channel: ' num2str(k) ', m: ' num2str(p(1)) ' Ohm/C, d: ' num2str(p(2)) ' Ohm, m/d: ' num2str(p(1)/p(2)) ' 1/K']);

print(['graph_channel_' num2str(k) '.jpg'],'-djpg')

end

 

disp(['Solder only: average m/d = ' num2str(mean(m_s(1:2:end)./d_s(1:2:end))) ' 1/K']);

 

figure(3);

bar(m_s(1:2:end)./d_s(1:2:end))

title(['Solder specimens, ave.: ' num2str(mean(m_s(1:2:end)./d_s(1:2:end))) ' 1/K']);

ylabel(['TCR at 0C, 1/K'])

 

figure(4);

bar(m_s(2:2:end)./d_s(2:2:end))

title(['Solder-Line specimens, ave.: ' num2str(mean(m_s(2:2:end)./d_s(2:2:end))) ' 1/K']);

ylabel(['TCR at 0C, 1/K'])