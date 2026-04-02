# Importing the Master BOM from Google Sheets

## Source Spreadsheet
- **URL**: https://docs.google.com/spreadsheets/d/1JEHx_08Zi1kPXPQiNM-eau-H2xfTsLFBgkRzyfTPdEI/edit?gid=1386834576#gid=1386834576
- **Access**: Requires Google account authentication (not publicly shared)

## Steps to Access the Spreadsheet

### 1. Request or Confirm Access
- Open the URL above in a browser while signed into the Google account that owns or has access to the sheet
- If you see "You need access", click "Request access" or ask the sheet owner to share it with your Google account
- The sheet owner can share via: **Share** button → enter your email → set permission to "Viewer" or "Editor"

### 2. Export as CSV or XLSX
Once you have access:
1. Open the spreadsheet in Google Sheets
2. Go to **File → Download**
3. Choose one of:
   - **Comma Separated Values (.csv)** — for the current active sheet/tab only
   - **Microsoft Excel (.xlsx)** — for all tabs
4. Save the downloaded file to this directory:
   ```
   ~/repos/pinball-soup/bill-of-materials/
   ```

### 3. Export Specific Tabs
The spreadsheet may have multiple tabs (e.g. per-machine BOMs, pricing, vendor info). To export a specific tab:
1. Click the tab you want at the bottom of the sheet
2. **File → Download → Comma Separated Values (.csv)** — this exports only the active tab
3. Name the file descriptively, e.g.:
   - `google-sheets-ozzfest-raw.csv`
   - `google-sheets-common-parts-raw.csv`

### 4. Alternative: Use Google Sheets API (Programmatic Access)
If you want to automate pulling data from the sheet:

```bash
# Install gspread (Python Google Sheets library)
pip install gspread oauth2client

# You will need a Google Cloud service account:
# 1. Go to https://console.cloud.google.com/
# 2. Create a project (or use existing)
# 3. Enable the Google Sheets API
# 4. Create a Service Account under IAM & Admin → Service Accounts
# 5. Download the JSON key file
# 6. Share the spreadsheet with the service account email address
```

Example Python script to pull sheet data:
```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]
creds = ServiceAccountCredentials.from_json_keyfile_name("service-account-key.json", scope)
client = gspread.authorize(creds)

# Open by URL
sheet = client.open_by_url(
    "https://docs.google.com/spreadsheets/d/1JEHx_08Zi1kPXPQiNM-eau-H2xfTsLFBgkRzyfTPdEI"
)

# Get specific worksheet by GID or name
worksheet = sheet.get_worksheet(0)  # first tab
records = worksheet.get_all_records()

# Write to local CSV
with open("google-sheets-export.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)
```

### 5. Merge into Local BOM Files
After exporting, manually review and merge relevant data into the machine-specific BOM markdown files in this directory. The markdown BOM files are the source of truth — the Google Sheet is a supplementary reference for initial part identification and pricing.

## Notes
- The Google Sheet may contain pricing that becomes outdated — always verify prices at vendor sites before purchasing
- Part numbers and availability change — cross-reference with FAST Pinball shop (https://shop.fastpinball.com/) and other vendors
- Keep the exported CSV/XLSX files in `.gitignore` if they contain sensitive or frequently-changing data
