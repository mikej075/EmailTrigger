📧 Google Sheets Email Notification Script

📌 Overview
This Google Apps Script automates email notifications when:
A spreadsheet is edited ➡️ Sends an email detailing the changes.

🚀 Features
✅ Automatically detects spreadsheet edits and emails changes.
✅ Sends bulk emails from a list of recipients in the sheet.
✅ Includes a direct link to the Google Sheet in notification emails.
✅ Logs changes for easy tracking.

🛠️ Setup Instructions
Open your Google Sheet.
Click on Extensions ➡️ Apps Script.
Copy and paste the script into the Apps Script editor.
Save and deploy the project.
Ensure that your Google account has the necessary permissions to send emails via MailApp.sendEmail().

📜 Script Details
sendEmailWithSheetData() 📤
Retrieves data from the active sheet.
Iterates through rows and sends emails.
Ensures valid email format before sending.
emailChange(e) 🔄
Triggers when a cell is edited.
Extracts details like sheet name, cell location, old & new values.
Sends an email notification to the specified recipient.

onEdit(e) ✍️
Calls emailChange(e) whenever an edit occurs in the spreadsheet.

