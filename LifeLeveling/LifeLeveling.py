# main vid https://www.youtube.com/watch?v=6CPjRJYtOBE
import gspread
import datetime
import json
from oauth2client.service_account import ServiceAccountCredentials


# Embed JSON file contents as a string
json_str = '''
{
  "type": "service_account",
  "project_id": "lifeleveling-381609",
  "private_key_id": "2595122b624a4d71e9db3b9bb0716605b1913c2b",
  "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDmeicobEIGkYet\\n1bdgENzZ9s/xvLbUYD77QeEhVFOZaMoI2KxfbtNuF40YmxHj+W+3nlL82RU4E15G\\nB8E/7ubvHzAGqb2giGXg7bDthpKILkb0Luo8ssEwAr4DYSkX1mVXaPHeZP+OcE2K\\nsg2wfj+xJl7IRdKMguBF00WFZpgwp7rg+DCjb5M8hMYOx/Do4hupzBOFrO6Ntpdc\\nCQ+3bOdc5680sY6fC3fltWYZRReXVF3/eFfQvAlD76GilNmu6paO/7bCUsQGnm42\\ntw4DfdL5dN/exILbrRMGwHL65R2yJFdv9xE8Z8E1HLMerIaB3HbrZjzC1QzRCHLb\\nefP8MeXnAgMBAAECggEAEF7WzzE5U1wc5gULHGC2Pykfxgzgc59OeexJAGQL+BaQ\\nWyaAv9qQW/6CQCArmiTKgaFWRa1pq2z8wj6kxFTExHFTqPV/iZqGmf5oFcb8O34F\\n/iwi6SLNRAq90mGhWJca5aWHoINN/6EMcPCKtmGRRpTyIImNFfvp0CvcgUgzQSlW\\nQzSawCeh51Nvsg+fR89sXYVug6+N1gql6Y1SYR8cxi4b7hdxcmt0GaKRu05BOXIp\\n2c01e/5cL95KzuQAJc4yiN6sgF5T9xdOBQfmUmIczdZrja6z1cynhLaJz7eugs4y\\nDyIpGOLoUIpCNVqv3F+eO5ZvMz1kaW1h/k+TUsWioQKBgQD2U7rHb9vQ2S0SWxLI\\nDXEroZsSQ/nMAWSh9peT2ndXoyoUY/AgGNpl2+lk0LWqmVUPxvj0isSKCIMHxnAJ\\nGXPUlLX4KK3FlGReqvabt+mN5qgMGIz23T849S7ZkoZpTKd1B8Tue0bCblYXOG85\\nkHgOQQvxhSMwc60egfnqjYEEEQKBgQDvhxZ6Jy6tDWwakdBAz6I0Aic2woxj2VdL\\nq/0QYRWS9ELn2hWLPSoOu9UrQE/So4KBpID3hxbHbXFnQTwFOXBcEaY5nu7xf9nC\\nUKMPWCYpB2dlSNCtrY9hjiDi6+PViApknb+fz0MixflwFwaDmrHAwWnsjuOmbMQ8\\ncZyLT4LidwKBgBOy5Hf4iRKtm34hTGI1OPytQtJ2Hy7iWaLeLocDbJHUmZPh3h0i\\n/6wvpv2J9006T+QgHF6qDkefoKLpiqIfp/SzI85BqovnbxNnBquzTHktnfjBqdxA\\nG0M50FJT9m3LVIT2ZxhPQXxhCH944uQumntBVmwtIoBIb+rFqC/KuyuRAoGACK4l\\nk2GuIFlXLJNSL7cWkrntP9/HBKtQrY5bCmfqRzwQ3KQbmcMqrgQCkqGvAtwoE5ip\\nj87WdX2y2WIU0b+mIcAF/RqUYC4Y7yDK9/hi0aPSDGqaHWEnzApBiNexlwBqGAFb\\ne2ggb7cq9fPvqX9Gp8yakRcQiuxwJByd5rKH9LsCgYAzXxLFkOuruUqPdMn0HrvR\\nDe2/xWziI8sJtrrut2HfLa5gdKIq/x2lgv1OWhgrk8ExYMet8XawZVPkAemAbC+r\\nLNmmpAXLpO30MGYb+NwLmpPKsaedwbVAyvoRG4oHeeT4XPBKpx5YFwwhEvC59EEz\\n8/RVAmT+nZBO3RwlgrDMvA==\\n-----END PRIVATE KEY-----\\n",
  "client_email": "admin01@lifeleveling-381609.iam.gserviceaccount.com",
  "client_id": "117135673057922690132",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/admin01%40lifeleveling-381609.iam.gserviceaccount.com"
}
'''
# appartently, you need to repalce all the \n with \\n because there seems to be a error when running the creds_dict = json.loads(json_str)
# Replacing
#json_str_replace = json_str.replace("\n", "\\n") --> using this doesnt work for some reason, ONLY REPLACE THE \N TO \\N IN THE "private key" part of the json


# Load JSON string into a dictionary
creds_dict = json.loads(json_str)



scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

#Date and Time
current_date = datetime.datetime.now()
date = current_date.strftime("%d/%m/%Y")
current_time = datetime.datetime.now()
time = current_time.strftime("%I:%M:%S %p")

spreadsheet = client.open("Python_System_Intergration_01")

stats_win = spreadsheet.worksheet("Stats_Window")

# to Read Cell Value
#print(stats_win.cell(2,3).value)

# to read Entire Row
#print(stats_win.row_values(25))

#to read Entire Column Value
#print(stats_win.col_values(4))

# to Write Cell Value
#stats_win.update_cell(12,9, "super read")
#print("Run Success")

# Printing the name of each worksheet in the spreadsheet
#for sheet_tags in spreadsheet.worksheets():
#    sheet_names = sheet_tags.title
#    print(sheet_names)

#printing a range of values
#print(stats_win.range("A1:D8"))

# Writing Data For a Row (should not overwrite the entire row, just append the cells specified)

def insert_log():
    row_num = stats_win.cell(9,10).value
    duration = 142
    type = "Piano"
    intensity = "Pretty Intense"
    row_data = [date,time,duration, type, intensity,]
    stats_win.append_row(row_data, table_range="A"+row_num+":"+"E"+row_num)

insert_log()