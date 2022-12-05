"""https://adventofcode.com/2021/day/16
Crazy hex to binary conversion"""

import time

start = time.time()

loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day16.txt"
# d=[x for x in open(loc,"rt").read().strip().split(',')]
with open(loc) as fin:
    raw_data = fin.read().strip()

data = bin(int(raw_data, base=16))[2:]
data = data.zfill(-(-len(data)//4) * 4)

#print(len(d[0]))
conv_table = {
"0": "0000",
"1": "0001",
"2": "0010",
"3": "0011",
"4": "0100",
"5": "0101",
"6": "0110",
"7": "0111",
"8": "1000",
"9": "1001",
"A": "1010",
"B": "1011",
"C": "1100",
"D": "1101",
"E": "1110",
"F": "1111"
}

def convert_hex(s):
    """Converts input string from hex to bin"""
    teststr = ""
    for c in s:
        teststr += conv_table[c]
    return teststr

def format_bin(s):
    packet_value_str = ''
    version = s[:3] #packet version
    type_id = s[3:6] #packet type ID
    #print(type_id)
    if int("0b"+type_id,2) == 4: #literal value
        idx = 0
        next_five = s[6+5*idx:6+5*(idx+1)]
        while next_five[0] == '1':
            #print("next 5:",next_five)
            packet_value_str += next_five[1:5]
            idx += 1
            next_five = s[6 + 5 * idx:6 + 5 * (idx + 1)]
        packet_value_str += next_five[1:5]
    return int(packet_value_str,2)

def parse(packet, count=-1):
    """Parses a packet, or several concatenated together"""
    if packet == '' or int(packet) == 0:
        return 0
    if count == 0:
        return parse(packet,count = -1)
    ver = int(packet[:3],2)
    tid = int(packet[3:6],2)

    if tid == 4:
        i=6
        num_str = ''
        end = False
        while not end:
            if packet[i] == '0':
                #last packet
                end = True

            num_str += packet[i+1:i+5]
            i += 5
        val = int(num_str,2)
        return ver + parse(packet[i:],count-1)

    #otherwise it's an operator
    len_ID = packet[6]
    if len_ID == '0':
        #15 bits representing how many bits are inside
        num_bits = int(packet[7:22],2)
        return ver + parse(packet[22:22+num_bits],-1) + parse(packet[22+num_bits:],count-1)

    else:
        #11 bits representing how many packets are inside
        num_packs = int(packet[7:18],2)
        return ver + parse(packet[18:],num_packs)

ans = parse(data)
print(ans)

#print(format_bin(convert_hex("D2FE28")))
print("Time (sec):",round(time.time()-start,1))