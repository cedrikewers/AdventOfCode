import sqlite3

# Create File if it does not exist
with open("day1.db", "wb"): pass

db = sqlite3.connect("./day1.db")

with open('../input.txt') as f:
    lines = [[int(i) for i in line.strip().split('   ')] for line in f.readlines()]

c = db.cursor()
c.execute('DROP TABLE IF EXISTS input')
c.execute('CREATE TABLE input (left_value INTEGER, right_value INTEGER)')
c.executemany('INSERT INTO input (left_value, right_value) VALUES (?, ?)', lines)  
db.commit()

# Read scripts
with open("day1Part1.sql", "r") as f:
    part1_script = f.read()
with open("day1Part2.sql", "r") as f:
    part2_script = f.read()

# Execute Part 1
res = db.execute(part1_script)
print("Part 1:", res.fetchone()[0])

# Execute Part 2
res = db.execute(part2_script)
print("Part 2:", res.fetchone()[0])
