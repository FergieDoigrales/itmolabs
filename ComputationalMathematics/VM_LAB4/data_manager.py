# #с приложения передается от 8 до 12 строк
# def get_pairs(pairs_list):
#     valid_pairs = []
#     for pair_str in pairs_list:
#         pair = pair_str.split(' ')
#         if len(pair) == 2:
#             try:
#                 valid_pairs.append([float(pair[0]), float(pair[1])])
#             except ValueError:
#                 continue
#     if len(valid_pairs) >= 8:
#         return valid_pairs
#     else: 
#         return "There are less than 8 valid pairs, cannot solve approximation"
def get_pairs(pairs_list):
    valid_pairs = []
    for pair_str in pairs_list:
        pair = pair_str.replace(',','.').split(' ')
        if len(pair) == 2:
            try:
                valid_pairs.append([float(pair[0]), float(pair[1])])
            except ValueError:
                continue
    if len(valid_pairs) >= 8:
        return valid_pairs
    else: 
        return "There are less than 8 valid pairs, cannot solve approximation"
