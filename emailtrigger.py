// Function that gets triggered when there's an edit in the spreadsheet
function emailChange(e) {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = e.range.getSheet();  // Get the sheet where the edit occurred
  var sheetName = sheet.getName(); // Get the sheet name
  var cellAddress = e.range.getA1Notation(); // Get the cell location (e.g., "B3")
  
  var newValue = e.value;
  var oldValue = e.oldValue ? e.oldValue : "No previous value"; // Handle cases where there's no old value
  var user = e.user ? e.user : "Unknown User"; // Handle cases where user info isn't available

  // Log the change action
  Logger.log('Change detected at ' + cellAddress + ' on sheet ' + sheetName);

  // Send an email notification with the updated details
  MailApp.sendEmail({
    to: "mikej09@gmail.com",
    subject: spreadsheet.getName() + " - Google Sheet Changes",
    htmlBody: 
   "<table border='1' style='border-collapse: collapse; width: 100%;'>"
    + "<tr><td colspan='2'><Center><strong>New Courses 2025-2026 Spreadsheet Changes</Center></strong></td></tr>"
    + "<tr><td><strong><center>Sheetname:</center></strong></td><td><strong><center>" + spreadsheet.getName() + "</strong></center></td></tr>"
    + "<tr><td><center><strong>Cell:</center></strong></td><td><center><strong>" + cellAddress + "</strong></center></td></tr>"
    + "<tr><td><center><strong>Previous Value:</center></td><td><strong><center>" + oldValue + "</center></strong></td></tr>"
    + "<tr><td><center><strong>New Value:<center></strong></td><td><strong><center>" + newValue + "</strong></center></td></tr>"
    + "<tr><td><center><strong>Edited By:</center></strong></td><td><strong><center><font color='green'>" + user + "</strong></center></font></td></tr>"
    + "<tr><td colspan='2'>Open sheet to view the changes: <a href='" + SpreadsheetApp.getActiveSpreadsheet() + "' target='_blank'>View Spreadsheet</a></td></tr>"
    + "</table>"

  });
}

// onEdit function triggers the emailChange function when an edit occurs
function onEdit(e) {
  emailChange(e);
}