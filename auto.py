import os
import shutil
import schedule
import time
import datetime

 
source_dir = r"C:\Users\ROHIT\Documents"   # Folder to copy
destination_dir = r"C:\Users\ROHIT\Desktop"  # Where to save backups

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))  # Folder name with today's date
    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists: {dest_dir}")

# Schedule to run every day at 18:57
schedule.every().day.at("18:57").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

# Keep checking for schedule
while True:
    schedule.run_pending()
    time.sleep(60)
