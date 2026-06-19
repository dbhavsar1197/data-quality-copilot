# Data Quality Copilot

A small Streamlit app that summarizes a data quality validation report and displays failing data quality rule IDs with their descriptions.

## Project structure

- `app.py` - Streamlit application that reads a validation report and rule definitions, then displays a summary.
- `reports/validation_report.txt` - Data quality report file parsed by the app.
- `rules/dq_rules.txt` - Data quality rule definitions in the format `DQ001 - Rule description`.
- `data/` - Placeholder directory for input datasets or supporting data.
- `inputs/` - Alternate input directory; may be used for custom data inputs.
- `logs/` - Logging directory.
- `README.md` - Existing repository README.
- `read.md` - This file.

## How it works

`app.py` reads the report in `reports/validation_report.txt`, counts passed and failed rules, and then looks up failed rule descriptions from `rules/dq_rules.txt`.

The app expects rules to be declared as one per line with a hyphen separator, for example:

```
DQ001 - Column `id` has duplicate values
DQ002 - Required field `name` contains null values
```

The report parser looks for lines beginning with `DQ` and counts `PASSED` and `FAILED` lines.

## Requirements

- Python 3.9+ (recommended)
- `streamlit`

The repository currently includes a `requirement.txt` file, but it is empty. Install Streamlit directly with:

```bash
pip install streamlit
```

## Run locally

From the project root:

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

## Notes

- If `reports/validation_report.txt` or `rules/dq_rules.txt` do not exist, the app will fail when starting.
- The app currently reads only one report file.
- This repo is intended as a simple prototype for data quality report visualization and should be extended with real report generation and rule management.
