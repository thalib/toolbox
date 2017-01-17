#!env3/bin/python
'''
	Usage example: ./hcidecode.py 0xFE10, 0x01, 120, 511, 0xFF
'''
import sys


temp =  sys.argv[1]
ogf = int(temp.replace(",", ""), 0) >> 10
ocf = int(temp.replace(",", ""), 0) 
ocf = ocf & 0x3FF
temp_command = 'hcitool cmd ' + hex(ogf) + " " + hex(ocf) + " " + " ".join(sys.argv[2:])

hcicmd = temp_command.replace(",", "")

print(hcicmd)


