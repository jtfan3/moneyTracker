import sqlite3

# Functions


def create():
    c.execute("""CREATE TABLE money (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                what text,
                amount decimal,
                add_date datetime DEFAULT CURRENT_TIMESTAMP
                )""")


def drop():
    c.execute("""DROP TABLE money""")


def add(wat, amnt):
    c.execute("INSERT INTO money (what, amount, add_date) VALUES (:what, :amnt, CURRENT_TIMESTAMP)",
              {'what': wat, 'amnt': amnt})


def deletefrom():
    c.execute("SELECT * FROM money ORDER BY id DESC")
    todel = c.fetchone()
    index = todel[0]
    c.execute("DELETE FROM money WHERE id={}".format(index))
    return todel


def lookup(x=0):
    c.execute("SELECT * FROM money ORDER BY id DESC")
    if x == 5:
        return c.fetchmany(x)
    else:
        return c.fetchall()


def printLu(lu):
    for i in lu:
        print('[{}] | {}: ${}\n'.format(i[3], i[1], i[2]))


# Start main body
# Open connection, setup cursor
conn = sqlite3.connect('money.db')
c = conn.cursor()

# logic loop
while(1):
    print('\nEnter command (h for help):')
    cmd = input('')
    print()
    if cmd == 'h':
        print('Help:\n'
              '(add) add new entry\n'
              '(bal) show balance'
              '(del) deletes the most recent entry\n'
              '(l5) returns 5 most recent entries\n'
              '(l) returns all previous entries\n'
              '(commit) saves and quits\n'
              '(quit) quit without saving\n')
    # Add a new entry
    elif cmd == 'add':
        print('Enter Description:')
        wat = input()
        print('Enter Amount:')
        try:
            amnt = float(input())
        except:
            print('Amount entered was not a number')
            continue
        add(wat, amnt)
    # Show balance
    elif cmd == 'bal':
        lu = lookup()
        sum = 0
        for i in lu:
            sum = sum + i[2]
        print('Balance is ${}'.format(sum))
    # Delete most recent entry
    elif cmd == 'del':
        try:
            deleted = deletefrom()
            print('Deleted entry is: {}'.format(deleted))
        except:
            print('Nothing to delete')
    # Look up 5 most recent
    elif cmd == 'l5':
        lu = lookup(5)
        print('Most Recent 5 Entries:')
        printLu(lu)
    # Lookup all
    elif cmd == 'l':
        lu = lookup()
        print('Entries')
        printLu(lu)
    # commit and leave
    elif cmd == 'commit':
        break
    # leave without saving
    elif cmd == 'quit':
        sys.exit()

# Run this to create or delete table.
# Create a table:
# create()
# Drop a table:
# drop()

# Done, commit and close connection
conn.commit()
conn.close()
