#!/usr/bin/env python

# [Usage]
#   ./mpstat2csv.py <mpstat_log>
#     or
#   python mpstat2csv.py <mpstat_log>
#
# [mpstat_log]
#   The assumed mpstat log is as follows.
#   
#     Linux 3.10.0-327.el7.x86_64 (pydev01)   01/03/17  _x86_64_  (2 CPU)
#     
#     13:04:10     CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
#     13:04:15     all    0.00    0.00    0.10    0.00    0.00    0.10    0.00    0.00    0.00   99.80
#     13:04:15       0    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00  100.00
#     13:04:15       1    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00  100.00
#     
#     13:04:15     CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
#     13:04:20     all    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00  100.00
#     13:04:20       0    0.00    0.00    0.20    0.00    0.00    0.00    0.00    0.00    0.00   99.80
#      ...
#     
#     Average:        CPU     %usr    %nice   %sys    %iowait %irq    %soft   %steal  %guest  %gnice  %idle
#     Average:        all     0.01    0.00    0.05    0.02    0.00    0.04    0.00    0.00    0.00    99.88
#     Average:        0       0.00    0.00    0.02    0.00    0.00    0.02    0.00    0.00    0.00    99.96
#     Average:        1       0.02    0.00    0.06    0.04    0.00    0.06    0.00    0.00    0.00    99.82
# 
#   The execution result is as follows.
#   
#     hh:mm:ss,CPU,%usr,%nice,%sys,%iowait,%irq,%soft,%steal,%guest,%gnice,%idle,
#     13:04:15,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,100.00,
#     13:04:15,1,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,100.00,
#     13:04:20,0,0.00,0.00,0.20,0.00,0.00,0.00,0.00,0.00,0.00,99.80,
#     13:04:20,1,0.00,0.00,0.00,0.20,0.00,0.00,0.00,0.00,0.00,99.80,
#      ...
#

import re   # 正規表現モジュール
import sys  # 引数を受け取るため

mpstat_log = sys.argv[1]

with open(mpstat_log) as f:

  flag = 0

  for line in f:
    if flag == 0:
      if re.search(r"usr", line):
        line = re.sub(r"\s+", ",", line)                            # 空白をタブに変換
        line = re.sub(r"[0-9]+\:[0-9]+\:[0-9]+", "hh:mm:ss", line)  # 先頭の時刻表記をhh:mm:ssに変換
        print(line.strip())                                         # strip()で空白行を削除
        flag = 1
    else:
      if re.search(r"CPU|all|Average|^\n", line) is None:           # re.searchはmatchしないときにNoneを返す
        line = re.sub(r"\s+", ",", line)                            # 空白をタブに変換
        print(line.strip())                                         # strip()で空白行を削除

