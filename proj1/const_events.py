#!/usr/bin/env python

import subprocess
import os
in_rate = [30, 80, 120]
out_rate = [50, 100, 120]
buffer_size = [50, 100, 150]

total_result = open("./result/total.result","w")

head1 = "\\nextgroupplot[title=$\lambda$=%s, $\mu$=%s, $n$=%s]\n"
head2 = "\\addplot coordinates {\n"
tail = "};\n"

for i in in_rate:
    for j in out_rate:
        for k in buffer_size:
            retcode = subprocess.call(["./router", str(i), str(j), str(k)])
            file_in = open("./result/%s_%s_%s_in.result" % (str(i),str(j),str(k)))
            file_dropped = open("./result/%s_%s_%s_dropped.result" % (i,j,k))
            total_result.write(head1 % (str(i), str(j), str(k)))
            total_result.write(head2)
            for line in file_in:
                total_result.write(line)
            total_result.write(tail)
            total_result.write(head2)
            for line in file_dropped:
                total_result.write(line)
            total_result.write(tail)
            os.remove("./result/%s_%s_%s_in.result" % (str(i),str(j),str(k)))
            os.remove("./result/%s_%s_%s_dropped.result" % (i,j,k))
