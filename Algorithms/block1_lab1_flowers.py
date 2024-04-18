n = int(input())
flwr_type = list(map(int, input().split(' ')))

dublicate_cnt = 0
current_longest_segment = 1
longest_segment = 1
current_start_content = 0 
start_content = 0
i = 1

# for i in range(1, n):
while i < n:
    if current_longest_segment > longest_segment:
            longest_segment = current_longest_segment
            start_content = current_start_content
    if i + 1 <= n:
        if flwr_type[i-1] == flwr_type[i]:
                dublicate_cnt += 1
        else:
             dublicate_cnt = 0
                    
    if dublicate_cnt == 2:
        current_longest_segment = 1
        current_start_content = i - 1
        dublicate_cnt = 0
        i -= 1
    else: 
        current_longest_segment += 1
    i += 1
if current_longest_segment > longest_segment:
    start_content = current_start_content
    longest_segment = current_longest_segment


print(start_content + 1, start_content + longest_segment)
