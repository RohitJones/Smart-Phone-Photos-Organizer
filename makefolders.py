import os
import shutil
Months = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

Working_Dir = "D:\\Mummy Phone Backup\\Camera\\New folder\\"

Days = {}
for each in os.listdir(Working_Dir):
    Date = each[2:10]

    if Date not in Days:
        Days[Date] = True
        Actual_Folder = Date[:4] + " (" + Date[4:6] + ") " + Months[Date[4:6]] + " " + Date[6:]
        os.mkdir(Working_Dir+Actual_Folder)

    shutil.move(Working_Dir+each, Working_Dir+Actual_Folder+"\\"+each)
