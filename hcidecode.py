import sys
print sys.argv[1:]

temp =  sys.argv[1]
ogf = int(temp.replace(",", ""), 0) >> 10
ocf = int(temp.replace(",", ""), 0) 
ocf = ocf & 0x3FF
temp_command = 'hcitool cmd ' + hex(ogf) + " " + hex(ocf) + " " + " ".join(sys.argv[2:])

hcicmd = temp_command.replace(",", "")

print(hcicmd)


