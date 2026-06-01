import sqlite3
import os
p = os.path.join(os.path.dirname(__file__), '..', 'db.sqlite3')
p = os.path.normpath(p)
print('DB path:', p)
if not os.path.exists(p):
    print('No db.sqlite3 found')
else:
    conn = sqlite3.connect(p)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in cur.fetchall()]
    print('Tables:', tables)
    if 'django_migrations' in tables:
        cur.execute("SELECT app, name FROM django_migrations ORDER BY id")
        rows = cur.fetchall()
        print('\nApplied migrations (first 50):')
        for app, name in rows[:50]:
            print(app, name)
    conn.close()
