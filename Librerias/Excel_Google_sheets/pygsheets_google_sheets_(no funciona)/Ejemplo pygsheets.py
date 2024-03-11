import pygsheets

client = pygsheets.authorize()

# Open the spreadsheet and the first sheet.
sh = client.open('Activos')
wks = sh.sheet1

# Update a single cell.
wks.update_value('A1', "Numbers on Stuff")

# Update the worksheet with the numpy array values. Beginning at cell 'A2'.
wks.update_values('A2', my_numpy_array.to_list())

# Share the sheet with your friend. (read access only)
sh.share('friend@gmail.com')
# sharing with write access
sh.share('friend@gmail.com', role='writer')