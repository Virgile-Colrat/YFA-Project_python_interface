Link communication protocol OMEGAETTE:https://www.mathworks.com/matlabcentral/answers/345402-communicating-with-omega-hh314a-humidity-sensor-in-matlab-solved

>>s = serial('COM3','BaudRate',9600);
>>fopen(s);
>>fwrite(s,'A'); %prompts device to send data
>>pause(1);
>>fwrite(s,'c'); %prompts device to stop sending data
>>humidity = ((arr(4,1)*255)+ arr(5,1))/10; %convert values
>>temp = ((arr(6,1)*255)+ arr(7,1))/10; %convert values
>>s=serial('com1');
>>set(s,'BaudRate',9600,'DataBits', 8, 'Parity', 'none','StopBits', 1, 'FlowControl', 'none','Terminator','CR','Timeout',10);
>>fopen(s);
>>fwrite(s, 'E'); % this starts recording data into the device
>>fscanf(s);
>>fwrite(s, 'P'); % this returns recorded data
