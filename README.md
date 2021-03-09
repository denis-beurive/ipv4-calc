
# calc.py

Test 1

    $ python calc.py 192.168.1.10/30
    ip=192.168.1.10 len=30
    
    network mask: 0xFFFFFFFC (11111111.11111111.11111111.11111100) 255.255.255.252
    host mask:    0x00000003 (00000000.00000000.00000000.00000011)
    network part: 0xC0A80108 (192.168.1.8)
    IP count:     4
    min IP:       192.168.1.8
    max IP:       192.168.1.11

Test 2

    $ python calc.py 192.168.1.3/17
    ip=192.168.1.3 len=17
    
    network mask: 0xFFFF8000 (11111111.11111111.10000000.00000000) 255.255.128.0
    host mask:    0x00007FFF (00000000.00000000.01111111.11111111)
    network part: 0xC0A80000 (192.168.0.0)
    IP count:     32768
    min IP:       192.168.0.0
    max IP:       192.168.127.255

All privates:

    $ python calc.py
    ip=10.0.0.0 len=8
    
    network mask: 0xFF000000 (11111111.00000000.00000000.00000000) 255.0.0.0
    host mask:    0x00FFFFFF (00000000.11111111.11111111.11111111)
    network part: 0x0A000000 (10.0.0.0)
    IP count:     16777216
    min IP:       10.0.0.0
    max IP:       10.255.255.255
    
    ip=172.16.0.0 len=12
    
    network mask: 0xFFF00000 (11111111.11110000.00000000.00000000) 255.240.0.0
    host mask:    0x000FFFFF (00000000.00001111.11111111.11111111)
    network part: 0xAC100000 (172.16.0.0)
    IP count:     1048576
    min IP:       172.16.0.0
    max IP:       172.31.255.255
    
    ip=192.168.0.0 len=16
    
    network mask: 0xFFFF0000 (11111111.11111111.00000000.00000000) 255.255.0.0
    host mask:    0x0000FFFF (00000000.00000000.11111111.11111111)
    network part: 0xC0A80000 (192.168.0.0)
    IP count:     65536
    min IP:       192.168.0.0
    max IP:       192.168.255.255
