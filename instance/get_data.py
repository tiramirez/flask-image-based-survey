import sqlite3

conn = sqlite3.connect('survey.sqlite')
cur = conn.cursor()

# selection = cur.execute("SELECT * FROM user").fetchall()
selection = cur.execute("SELECT * FROM ans").fetchall()

for i in selection:
    print(i)

# (65, 1, '2018-10-30 23:06:17', 'Rojo', '26073614', '44646271', '1')
# (66, 1, '2018-10-30 23:06:29', 'Rojo', '77394988', '57946467', '2')
# (67, 1, '2018-10-30 23:06:40', 'Rojo', '85626345', '85626345', '3')
# (68, 1, '2018-10-30 23:07:01', 'Rojo', '57946467', '57946467', '2')
# (69, 1, '2018-10-30 23:07:12', 'Rojo', '44646271', '91171557', '1')

# 4433	9117	1
# 2607	8562	1