// ══════════════════════════════════════════════════════════
// BATO VISITOR LOGGER — Google Apps Script Web App
// ══════════════════════════════════════════════════════════
// 
// Deploy this as a Google Apps Script Web App:
//   1. Go to https://script.google.com
//   2. Create a new project, paste this code
//   3. Click Deploy > New Deployment > Type: Web App
//   4. Execute as: "Me", Who has access: "Anyone"
//   5. Copy the deployment URL — use it in index.html
//
// The script auto-creates a Google Sheet called "Bato Visitors"
// in your Google Drive with columns: Timestamp | Name | Company
// ══════════════════════════════════════════════════════════

function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const sheet = getOrCreateSheet('Bato Visitors');
    
    // Append row: timestamp, name, company
    sheet.appendRow([
      new Date().toISOString(),
      data.name,
      data.company
    ]);
    
    return ContentService
      .createTextOutput(JSON.stringify({ success: true }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({ success: false, error: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet() {
  return ContentService
    .createTextOutput(JSON.stringify({ status: 'Bato Visitor Logger is running' }))
    .setMimeType(ContentService.MimeType.JSON);
}

function getOrCreateSheet(name) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(name);
  if (!sheet) {
    sheet = ss.insertSheet(name);
    sheet.appendRow(['Timestamp', 'Name', 'Company']);
  }
  return sheet;
}
