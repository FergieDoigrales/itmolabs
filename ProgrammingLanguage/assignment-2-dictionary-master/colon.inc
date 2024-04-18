%define top 0
%macro colon 2
    %2: dq top
        db %1, 0
    %define top %2
%endmacro 
