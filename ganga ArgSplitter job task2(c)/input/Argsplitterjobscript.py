j=Job()
j.name="Argsplitter Job"
j.application.exe=File('/home/wireshark10/Desktop/newtask'   )
j.splitter=ArgSplitter(args=[ ['/home/wireshark10/Desktop/text/Cerntext1.txt'             ],[  ' /home/wireshark10/Desktop/text/Cerntext2.txt'              ],[  '/home/wireshark10/Desktop/text/Cerntext3.txt'             ],[      '/home/wireshark10/Desktop/text/Cerntext4.txt'    ],[   '/home/wireshark10/Desktop/text/Cerntext5.txt'        ],[ '/home/wireshark10/Desktop/text/Cerntext6.txt'                 ],[      '/home/wireshark10/Desktop/text/Cerntext7.txt'          ],[        '/home/wireshark10/Desktop/text/Cerntext8.txt'       ],[  '/home/wireshark10/Desktop/text/Cerntext9.txt'        ],[   '/home/wireshark10/Desktop/text/Cerntext10.txt'          ],[      '/home/wireshark10/Desktop/text/Cerntext11.txt'       ],[     '/home/wireshark10/Desktop/text/Cerntext12.txt'          ]                ]    )
j.backend=Local()
j.submit()
