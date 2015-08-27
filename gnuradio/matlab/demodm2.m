% function to demodulate M2 encoded data
% data: is the received signal data
% Ts: is the symbol duration (needs to be at least 4 to function)
% threshold: is the value used to decide between 1 and 0, this needs to be
% half the difference in voltage between the peak to peak voltage of the
% signal
function [output] = demodm2(data, Ts, threshold)
output = [];
for k=1:Ts:length(data)
   
    % integrate each half bit
    sum1 = 0;
    for (m=1:Ts/4)
        sum1 = sum1 + data(k+m - 1);
    end
    
    sum2 = 0;
    for (m=Ts/4+1:Ts/2)
        sum2 = sum2 + data(k+m - 1);
    end
    
    sum3 = 0;
    for (m=Ts/2+1:3*Ts/4)
        sum3 = sum3 + data(k+m - 1);
    end
    
    sum4 = 0;
    for (m=3*Ts/4+1:Ts)
        sum4 = sum4 + data(k+m - 1);
    end
    
    if (abs(sum1+sum3 - sum2-sum4) < threshold)
        output = [output 1];
    else
        output = [output 0];
    end
    
    %display(sprintf('diff=%f', abs(sum1+sum3 - sum2-sum4)));
end

