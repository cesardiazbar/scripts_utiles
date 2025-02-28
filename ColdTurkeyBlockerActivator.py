import json
import sqlite3
import os
import subprocess

DB_PATH = "C:/ProgramData/Cold Turkey/data-app.db"

def close_cold_turkey():
    try:
        subprocess.run(["taskkill", "/f", "/im", "ColdTurkey.exe"], check=True)
        subprocess.run(["taskkill", "/f", "/im", "ColdTurkeyTray.exe"], check=True)
        print("Cold Turkey Blocker and tray icon closed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to close Cold Turkey Blocker. It might not be running.")

def activate():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        s = c.execute("SELECT value FROM settings WHERE key = 'settings'").fetchone()[0]
        dat = json.loads(s)

        if dat["additional"]["proStatus"] != "pro":
            print("Your version of Cold Turkey Blocker is not activated.")
            dat["additional"]["proStatus"] = "pro"
            print("But now it is activated.\nPlease close Cold Turkey Blocker and run it again.")
            c.execute("""UPDATE settings SET value = ? WHERE "key" = 'settings'""", (json.dumps(dat),))
            conn.commit()
        else:
            print("Looks like your copy of Cold Turkey Blocker is already activated.")
            print("Deactivating it now.")
            dat["additional"]["proStatus"] = "free"
            c.execute("""UPDATE settings set value = ? WHERE "key" = 'settings'""", (json.dumps(dat),))
            conn.commit()

    except sqlite3.Error as e:
        print("Failed to activate", e)
    finally:
        if conn:
            conn.close()

def main():
    if os.path.exists(DB_PATH):
        print("Data file found.\nLet's activate your copy of Cold Turkey Blocker.")
        close_cold_turkey()  # Cierra la aplicación antes de proceder
        activate()
    else:
        print("Looks like Cold Turkey Blocker is not installed.\nIf it is installed then run it at least once.")

if __name__ == '__main__':
    main()