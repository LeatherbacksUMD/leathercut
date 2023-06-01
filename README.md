# Leathercut
Automation for SCR@M orders

## leathercut_prints
Google Form for parts submissions: 
https://docs.google.com/forms/d/1ubHqjs7VDlzSLh72HzKOEVBqqxskUAv7CbK58RnuQB8/edit?pli=1&pli=1

Spreadsheet of submitted parts (must remain publicly viewable): 
https://docs.google.com/spreadsheets/d/1aMOFh4E-XriIMeQIOr7SNVH_Zb_pv3WCJKdeB0NZh30/edit?resourcekey#gid=538601098

Drive folder of submitted parts (must remain publicly viewable):
https://drive.google.com/drive/u/1/folders/1q_PophYa31dDENcvi-fhw1dT0Mc5r4XSjkscxZEC5XKxl3oPBTdZLJLqIzSYmxIZoqxoQDet

To use download and name all prints submissions run the following
```
python leathercut_prints.py <command>
```
Commands include:
```
download: rips all files and data from the responses sheet
clean: DELETES contents of ONYX, PLA, TPU folders
```

leathercut_prints.py expects ONYX, PLA, TPU folders to be in the same directory. They will be populated with responses sheet data. Each folder should be submitted as a bulk order to papercut.

After you run leathercut_prints you should delete the contents of the spreadsheet so you don't download those prints again. Also clear out the folder holding the submitted parts semi frequently to avoid filling up the team account's storage. I (Eashan) wanted to do this automatically, but the only way seems to be with the Google Sheets API which costs money... I might look into it at a later date.

Files will be formatted as 
```
<QUANTITY_NUMBER>x <EXPORT_UNITS> <MATERIAL> <INFILL>INFILL <PART NAME> - <LNAME>, <RNAME>.stl
```

## leathercut_cuts
TBD (basically leathercut_prints but for waterjet parts)

## leathercut_parts
TBD (basically leathercut_prints but for parts requests; will generate orders sheet for treasurer to look over)