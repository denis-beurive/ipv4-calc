
# calc.py

Test 1

    $ python calc.py 192.168.1.10/30
    ip=192.168.1.10 len=30
    
    network mask: 0xFFFFFFFC (11111111.11111111.11111111.11111100)
    host mask:    0x00000003 (00000000.00000000.00000000.00000011)
    network part: 0xC0A80108 (192.168.1.8)
    IP count:     4
    min IP:       192.168.1.8
    max IP:       192.168.1.11

Test 2

    $ python calc.py 192.168.1.3/17
    ip=192.168.1.3 len=17
    
    network mask: 0xFFFF8000 (11111111.11111111.10000000.00000000)
    host mask:    0x00007FFF (00000000.00000000.01111111.11111111)
    network part: 0xC0A80000 (192.168.0.0)
    IP count:     32768
    min IP:       192.168.0.0
    max IP:       192.168.127.255

