import pandas as pd
import gdown
import sys
import os

TS = 0
EMAIL = 1
RNAME = 2
LNAME = 3
FNAME = 4
UNITS = 5
MATERIAL = 6
COPIES = 7
FILE = 8
PNAME = 9
INFILL = 10

# This stuff is derived from responses spreadsheet link
# MAKE SURE THE SPREADSHEET IS SET SUCH THAT ANYONE CAN VIEW IT
SHEET_ID = "1aMOFh4E-XriIMeQIOr7SNVH_Zb_pv3WCJKdeB0NZh30"
SHEET_NAME = "1"

if __name__ == "__main__":
	if len(sys.argv) == 2:
		if sys.argv[1] == "download":
			gsheet_url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
			df = pd.read_csv(gsheet_url)
			#TODO CLEAN FOR INPUTS MORE

			# Desired format is <QUANTITY_NUMBER>x <EXPORT_UNITS> <MATERIAL> <INFILL>INFILL <PART NAME> - <LNAME>, <RNAME>.stl
			fail = []
			for order in df.values:
				try:
					url = "https://drive.google.com/uc?id=" + order[FILE].split('?id=')[1] # MAKE SURE TO SET FOLDER HOLDING THE FILES AS ANYONE CAN VIEW
					output = f'./{order[MATERIAL]}/{order[COPIES]}x_{order[UNITS]}_{order[MATERIAL]}_{order[INFILL]}FILL%_{order[PNAME]}_{order[LNAME]}{order[FNAME]}_{order[RNAME]}.stl'
					gdown.download(url, output, quiet=False)
				except:
					fail.append(order[TS])

			if fail:
				for f in fail:
					print(f + " failed.")
		elif sys.argv[1] == "clean":
			os.system("rm -r ONYX PLA TPU")
			os.system("mkdir ONYX PLA TPU")
		else:
			print("Invalid Command")
	else:
		print("Usage: python leathercut_prints.py <command>")
		print("Commands include:")
		print("download: rips all files and data from the responses sheet")
		print("clean: deletes contents of ONYX, PLA, TPU folders")