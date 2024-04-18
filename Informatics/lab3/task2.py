from dict2xml import dict2xml 
from yaml import safe_load 
 
def convert_file(input_file_name, output_file_name, show = False): 
    dict = {} 
    with open(f"{input_file_name}.yml","r",encoding='utf-8') as file: 
        dict = safe_load(file) 
    with open(f"{output_file_name}.xml","w",encoding='utf-8') as file: 
        file.write(dict2xml(dict))
        
if __name__ == "__main__": 
    import time 
    start_time = time.perf_counter() 
    for n in range(10): 
        convert_file("timetable","timetable") 
    print("time: ",time.perf_counter() - start_time)
