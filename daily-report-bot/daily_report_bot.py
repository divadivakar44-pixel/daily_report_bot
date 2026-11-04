
import pyautogui
import pyperclip
import subprocess
import time
import os
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

# =====================================
# 1. CONFIGURATION
# =====================================

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

project_folder = r"C:\Users\vdiwaka\Downloads\Gen AI program\daily-report-bot"

os.makedirs(project_folder, exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now()

excel_file = os.path.join(
    project_folder,
    f"daily_report_{today}.xlsx"
)

screenshot_file = os.path.join(
    project_folder,
    f"daily_report_{today}.png"
)

print("================================")
print("DAILY REPORT BOT STARTED")
print("================================")

# =====================================
# 2. OPEN CHROME
# =====================================

print("Opening Chrome...")

pyautogui.hotkey("win", "r")
time.sleep(2)

pyautogui.write(
    "https://wttr.in/Chennai?format=3",
    interval=0.04
)

pyautogui.press("enter")

# Wait for weather website
time.sleep(15)

# =====================================
# 3. COPY WEBSITE INFORMATION
# =====================================

# Copy weather information from the webpage
pyautogui.click(700, 400)  # Click inside the webpage
time.sleep(2)

pyautogui.hotkey("ctrl", "a")  # Select webpage content
time.sleep(1)

pyautogui.hotkey("ctrl", "c")  # Copy selected content
time.sleep(2)

weather_data = pyperclip.paste()

print("Weather information copied:")
print(weather_data)

# =====================================
# 4. PREPARE REPORT
# =====================================

comment = (
    "Check weather conditions before "
    "planning outdoor activities."
)

# =====================================
# 5. CREATE EXCEL WORKBOOK
# =====================================

print("Creating Excel report...")

wb = Workbook()
ws = wb.active

ws.title = "Daily Report"

# Add headings
headers = [
    "Date & Time",
    "Fetched Information",
    "Comment"
]

ws.append(headers)

# Add report data
ws.append([
    current_time,
    weather_data,
    comment
])

# =====================================
# 6. FORMAT EXCEL SHEET
# =====================================

for cell in ws[1]:
    cell.font = Font(
        bold=True,
        color="FFFFFF",
        size=12
    )

    cell.fill = PatternFill(
        "solid",
        fgColor="1F4E78"
    )

    cell.alignment = Alignment(
        horizontal="center",
        vertical="center"
    )

ws.column_dimensions["A"].width = 23
ws.column_dimensions["B"].width = 65
ws.column_dimensions["C"].width = 65

ws["A2"].number_format = "yyyy-mm-dd hh:mm:ss"

for cell in ws[2]:
    cell.alignment = Alignment(
        vertical="center",
        wrap_text=True
    )

ws.row_dimensions[1].height = 25
ws.row_dimensions[2].height = 40

ws.freeze_panes = "A2"

# =====================================
# 7. SAVE EXCEL FILE
# =====================================

print("Saving Excel file...")

try:
    wb.save(excel_file)

    if os.path.exists(excel_file):
        print("SUCCESS: Excel file saved!")
        print(excel_file)
    else:
        raise Exception("Excel file was not created.")

except Exception as error:
    print("Excel saving error:", error)
    raise

# =====================================
# 8. OPEN EXCEL FILE
# =====================================

print("Opening final Excel report...")

os.startfile(excel_file)

# Wait for Excel to open
time.sleep(12)

# Maximize Excel
pyautogui.hotkey("win", "up")
time.sleep(3)

# =====================================
# 9. TAKE SCREENSHOT
# =====================================

print("Capturing final Excel screenshot...")

pyautogui.screenshot().save(screenshot_file)

print("Screenshot saved:", screenshot_file)

# =====================================
# 10. FINAL STATUS
# =====================================

print("================================")
print("DAILY REPORT COMPLETED")
print("================================")

print("Excel File:", excel_file)
print("Screenshot:", screenshot_file)

print("SUCCESS: All operations completed!")
