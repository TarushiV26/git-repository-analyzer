# Bug Investigation: Contributor Date Formatting Error

**Project:** Git Repository Analyzer  
**Course:** Open Source Technologies — CA-3  
**Component:** Contributor Statistics  
**Affected file:** `src/contributors.py`  
**Issue type:** Runtime error during dashboard analysis  
**Status:** Fix implemented; final verification in progress

---

## 1. Bug Summary

During practical testing of the Git Repository Analyzer, an `AttributeError` occurred when the application attempted to display contributor statistics.

The error was associated with Pandas date formatting. The application attempted to use the `.dt` accessor on a value that was not recognized as datetime-like.

**Observed error message:**

`AttributeError: Can only use .dt accessor with datetimelike values`

The traceback identified the contributor statistics function in `src/contributors.py` as the affected component.

## 2. Environment

- Operating system: Windows
- Python version: 3.14.5
- Application framework: Streamlit
- Data processing library: Pandas
- Repository: `TarushiV26/git-repository-analyzer`
- Development environment: Visual Studio Code and PowerShell
- Local Git branch during development: `feature/csv-export`

## 3. Steps to Reproduce

1. Open the project directory in Visual Studio Code.
2. Activate or use the project's Python virtual environment.
3. Start the application with:

   `python -m streamlit run app.py`

4. Enter the local repository path in the dashboard sidebar.
5. Select **Analyze repository**.
6. Open the **Contributors** tab.
7. Observe the runtime error related to date formatting.

## 4. Expected Result

The Contributors tab should display the contributor name, number of commits, and latest commit date without raising an exception.

The contributor statistics should also remain available for CSV export.

## 5. Actual Result

The application displayed an error instead of rendering the contributor statistics table.

The traceback indicated that the date-formatting operation failed because the value being processed was not recognized as datetime-like.

The initial error was captured in a screenshot before the correction.

<img width="2556" height="1512" alt="bug_ss" src="https://github.com/user-attachments/assets/8bd5b672-60be-44e6-9f8c-55a77b64f974" />


## 6. Root Cause Investigation

The failure occurred during the formatting of the latest commit date in `src/contributors.py`.

The original implementation used Pandas' `.dt.strftime()` accessor without explicitly ensuring that the source date column had a consistent datetime dtype.

This made the formatting operation vulnerable to date values that Pandas did not recognize as datetime-like.

## 7. Corrective Action

The contributor statistics function was updated to convert the source date column explicitly using:

`pd.to_datetime(df["date"], errors="coerce", utc=True)`

The updated implementation then formats valid dates and handles missing or invalid dates by displaying `N/A`.

This makes the date processing more robust and avoids applying `.dt` to a non-datetime series.

<img width="1144" height="992" alt="image" src="https://github.com/user-attachments/assets/bf2f3028-3ebe-4efb-97d4-c4f13efc76d2" />

## 8. Verification and Test Results

### Direct function test

The contributor statistics function was tested with a sample commit containing a valid Python datetime value.

**Observed result:** The function returned a contributor table containing the contributor name, commit count, and formatted latest commit date.

### Automated tests

Command:

`python -m pytest -q`

**Result:** Four tests passed before the latest date-formatting correction. The full suite must be rerun after the correction, and its final output should be recorded here.

### Dashboard verification

After restarting the Streamlit application, the Contributors tab displayed the contributor table and CSV download button without the previously observed error.

The Activity and File analysis CSV downloads still need to be verified before the final report is submitted.

<img width="2526" height="1342" alt="image" src="https://github.com/user-attachments/assets/c5413135-1985-4f40-9a98-17f0745565ef" />


<img width="2522" height="1322" alt="image" src="https://github.com/user-attachments/assets/7b070853-b6c0-4967-a9eb-cf6ab87456bc" />


<img width="2544" height="1344" alt="image" src="https://github.com/user-attachments/assets/5948db82-541f-4465-848b-53100fbe62e2" />


## 10. Conclusion

The practical investigation identified a date-formatting failure in the contributor statistics component.

The implementation was updated to normalize commit dates before formatting them. A direct function test confirmed that a valid datetime input produced the expected contributor table, and the restarted dashboard subsequently displayed the Contributors tab correctly.

The final automated test results and remaining CSV download checks must be confirmed before marking the bug investigation fully verified.
