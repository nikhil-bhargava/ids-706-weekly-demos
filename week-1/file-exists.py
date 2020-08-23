from pathlib import Path
import os
start_path = Path(os.getcwd())
csv_path = start_path /'../../egrid2016.csv'
print(csv_path)
if csv_path.exists():
	print("the file exists!")
else:
	print("the file doesn't exist :(")
