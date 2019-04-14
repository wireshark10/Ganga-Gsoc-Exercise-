filenames = ['/home/wireshark10/Desktop/subjobsstdoutfiles/stdout1.txt','/home/wireshark10/Desktop/subjobsstdoutfiles/stdout2.txt','/home/wireshark10/Desktop/subjobsstdoutfiles/stdout3.txt','/home/wireshark10/Desktop/subjobsstdoutfiles/stdout4.txt','/home/wireshark10/Desktop/subjobsstdoutfiles/stdout5.txt','/home/wireshark10/Desktop/subjobsstdoutfiles/stdout6.txt','/home/wireshark10/Desktop/subjobsstdoutfiles/stdout7.txt','/home/wireshark10/Desktop/subjobsstdoutfiles/stdout8.txt','/home/wireshark10/Desktop/subjobsstdoutfiles/stdout9.txt','/home/wireshark10/Desktop/subjobsstdoutfiles/stdout10.txt','/home/wireshark10/Desktop/subjobsstdoutfiles/stdout11.txt','/home/wireshark10/Desktop/subjobsstdoutfiles/stdout12.txt']
total = 0

with open('merger.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname, 'r') as infile:
            for line in infile:
            	total += int(line)

print total
