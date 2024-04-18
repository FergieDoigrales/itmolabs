from subprocess import Popen, PIPE

prg_path = "./main"

inp = ["dopsa", "komsa", "ppaodin", "pusto", "maria" * 256, "kolobaka" * 260]
outp = ["DopSessia", "Komissia", "Promezhutochnaya Attestacia odin", "", "", ""]
errs = ["", "", "", "not found key", "too long key", "too long key"]

sum = 0

print(f"script: {prg_path} ")
for i in range(len(inp)):
    process = Popen(
        [prg_path], 
        stdin=PIPE, 
        stdout=PIPE, 
        stderr=PIPE)
    data = process.communicate(inp[i].encode())
    if data[0].decode().strip() == outp[i] and data[1].decode().strip() == errs[i]:
        print(f"TEST {i+1} IS PASSED\n")
        sum += 1
    else:
        print(f"TEST {i+1} IS FAILED : \n" + data[1].decode().strip())
print(f"total: {sum} passed out of 6")
