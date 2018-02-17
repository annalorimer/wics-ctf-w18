In the following output from the traceroute command, how many hops did it take to get to mit.edu?

```
fhboxwal@mother-goose:~$ traceroute mit.edu
traceroute to mit.edu (184.86.32.128), 30 hops max, 60 byte packets
 1  mc-cs1-mathstudentorgsnet.uwaterloo.ca (129.97.134.1)  5.005 ms  4.982 ms  5.001 ms
 2  v483-mc-cs2.ns.uwaterloo.ca (172.19.1.29)  4.854 ms  4.860 ms  4.850 ms
 3  te2-7-dist-rt-mc-mc-cs2.ns.uwaterloo.ca (172.16.15.1)  0.515 ms  0.883 ms  0.899 ms
 4  xe1-0-0-u10-dist-sa-mc-trust.ns.uwaterloo.ca (172.31.0.145)  0.451 ms * *
 5  te2-12-dist-rt-mc-global.ns.uwaterloo.ca (172.31.0.161)  1.075 ms  1.160 ms  1.249 ms
 6  te2-16-cn-rt-mc.ns.uwaterloo.ca (172.16.31.117)  0.743 ms  0.800 ms  0.731 ms
 7  te0-0-2-0-ext-rt-mc.ns.uwaterloo.ca (172.16.32.149)  1.613 ms  1.423 ms  1.517 ms
 8  66.97.28.65 (66.97.28.65)  1.434 ms  1.378 ms  1.359 ms
 9  be119.p01-york.orion.on.ca (66.97.16.109)  4.885 ms  5.047 ms  4.554 ms
10  be202.gw01-toro.orion.on.ca (66.97.16.26)  4.903 ms  4.891 ms  4.891 ms
11  akamai.ip4.torontointernetxchange.net (206.108.34.24)  4.930 ms  4.944 ms  4.265 ms
12  a184-86-32-128.deploy.static.akamaitechnologies.com (184.86.32.128)  4.259 ms  4.229 ms  4.130 ms
```
