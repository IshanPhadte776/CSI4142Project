Printing 'drillDown' query results:
    numofbedrooms  multipurposeroom  childrenplayarea  numofentries
0               5              True              True             2
1               4             False             False             1
2               4             False              True            34
3               4              True              True            47
4               3             False             False            29
5               3             False              True           284
6               3              True             False            14
7               3              True              True           394
8               2             False             False            79
9               2             False              True           259
10              2              True             False            27
11              2              True              True           360
12              1             False             False             6
13              1             False              True            31
14              1              True              True            27
Printing 'rollUp' query results:
   indoor_room  numofentries
0            1            64
1            1            37
2            1            27
3            2           725
4            2           338
5            2           387
6            3           313
7            3           721
8            3           408
9            4            82
10           4            47
11           4            35
12           5             2
13           5             2
14        None          1594
Printing 'slice' query results:
      refrigerator
0            False
1            False
2            False
3            False
4            False
...            ...
1589         False
1590         False
1591         False
1592         False
1593         False

[1594 rows x 1 columns]
Printing 'dice1' query results:
     shoppingmall  sportsfacility  school  hospital  communityid
0            True           False    True      True           13
1            True            True    True      True           94
2            True            True    True      True           95
3            True            True    True      True           96
4            True            True    True      True           97
..            ...             ...     ...       ...          ...
103          True           False    True      True         1450
104          True            True    True      True         1495
105          True            True    True      True         1507
106          True            True    True      True         1508
107          True            True    True      True         1509

[108 rows x 5 columns]
Printing 'dice2' query results:
     washingmachine    ac  ...  refrigerator  householdapplianceid
0              True  True  ...          True                    43
1              True  True  ...          True                    64
2              True  True  ...          True                   587
3              True  True  ...          True                   588
4              True  True  ...          True                   589
..              ...   ...  ...           ...                   ...
230            True  True  ...          True                  1566
231            True  True  ...          True                  1567
232            True  True  ...          True                  1568
233            True  True  ...          True                  1569
234            True  True  ...          True                  1570

[235 rows x 7 columns]
Printing 'combined1' query results:
         price
0     30000000
1      7888000
2      4866000
3      6845000
4      6797000
...        ...
1350   8306999
1351   4883000
1352  11500000
1353   8378000
1354   5951000

[1355 rows x 1 columns]
Printing 'combined2' query results:
         price
0     30000000
1      7888000
2      4866000
3      6845000
4      6797000
...        ...
1130   8306999
1131   4883000
1132  11500000
1133   8378000
1134   5951000

[1135 rows x 1 columns]
Printing 'combined3' query results:
        price
0     5600000
1    10500000
2    16900000
3    14900000
4    14100000
..        ...
230   6400000
231   9200000
232   7000000
233   8200000
234   6300000

[235 rows x 1 columns]
Printing 'combined4' query results:
        price
0     5600000
1    10500000
2    16900000
3    14900000
4    14100000
..        ...
230   6400000
231   9200000
232   7000000
233   8200000
234   6300000

[235 rows x 1 columns]
Printing 'iceBerg' query results:
        location  area  ...  communityid  indoorroomid
0         Hebbal  4600  ...          710           710
1         Hebbal  4400  ...          715           715
2         Hebbal  4200  ...          716           716
3  Richmond Town  2772  ...          790           790
4          Begur  1438  ...         1051          1051
5    Rajajinagar  4053  ...         1469          1469

[6 rows x 8 columns]
Printing 'window' query results:
    location     price  position
0   Horamavu   4100000         1
1   Horamavu   4371000         2
2   Horamavu   4371000         3
3   Horamavu   4545000         4
4   Horamavu   4582000         5
5   Horamavu   4619000         6
6   Horamavu   4700000         7
7   Horamavu   4737000         8
8   Horamavu   4785000         9
9   Horamavu   4815000        10
10  Horamavu   4831000        11
11  Horamavu   4845000        12
12  Horamavu   4854000        13
13  Horamavu   4855000        14
14  Horamavu   4880000        15
15  Horamavu   4888000        16
16  Horamavu   4972000        17
17  Horamavu   5050000        18
18  Horamavu   5100000        19
19  Horamavu   5200000        20
20  Horamavu   6581000        21
21  Horamavu   6631000        22
22  Horamavu   6664000        23
23  Horamavu   6797000        24
24  Horamavu   6892000        25
25  Horamavu   8529000        26
26  Horamavu   8763000        27
27  Horamavu   8957000        28
28  Horamavu   9319000        29
29  Horamavu   9640000        30
30  Horamavu   9879000        31
31  Horamavu  10000000        32
32   Kengeri   3990000         1
33   Kengeri   4021000         2
34   Kengeri   4088000         3
35   Kengeri   4582000         4
36   Kengeri   4586000         5
37   Kengeri   4722000         6
38   Kengeri   6787000         7
39   Kengeri   6845000         8
Printing 'windowing' query results:
           location  area  ...  avg_price_per_sqm  price_per_sqm_rank
0             Begur  1438  ...         5742.79862                   1
1     Richmond Town  2772  ...         5742.79862                   2
2            Domlur  1078  ...         5742.79862                   3
3            Domlur  1998  ...         5742.79862                   4
4            Domlur  1498  ...         5742.79862                   5
...             ...   ...  ...                ...                 ...
1589       Attibele  1639  ...         5742.79862                1586
1590       Attibele   995  ...         5742.79862                1586
1591       Attibele  1529  ...         5742.79862                1586
1592       Attibele  1365  ...         5742.79862                1586
1593       Attibele  1573  ...         5742.79862                1586

[1594 rows x 10 columns]