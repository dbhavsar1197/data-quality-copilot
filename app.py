import streamlit as st
from utils.report_reader import read_report
from utils.rule_loader import load_rules

#-------------
# Load Rules 
#-------------
rule_dict = load_rules()


# ----------------------------------
# Page Configuration
# ----------------------------------
st.set_page_config(
    page_title="Data Quality Copilot",
    page_icon="🤖"
    )
st.title("Data Quality Copilot")
# ----------------------------------
# File Upload
# ----------------------------------
st.subheader("Upload Validation Report")
uploaded_file = st.file_uploader(
    "Upload report file",
    type=["txt"]
    )

# ----------------------------------
# Read Validation Report
# ----------------------------------
report_lines = read_report(uploaded_file)
if report_lines is None:
    st.info("Please upload a validation report to continue.")
    st.stop()
#st.write(type(uploaded_file))
# ----------------------------------
# Read DQ Rules
# ----------------------------------

#rule_dict = {}

#with open("rules/dq_rules.txt", "r") as f:
 #   for line in f:
  #      if "-" in line:
   #         rule_id, description = line.split("-", 1)
    #        rule_dict[rule_id.strip()] = description.strip()
# ----------------------------------

# Parse Validation Report

# ----------------------------------
passed = 0
failed = 0

failed_rules = []
failed_rule_details = {}

current_rule = None

for line in report_lines:

    line = line.strip()

    if line.startswith("DQ"):

        current_rule = line.split()[0]

        if "PASSED" in line:
            passed += 1

        elif "FAILED" in line:
            failed += 1
            failed_rules.append(current_rule)

    elif current_rule and line:

        if current_rule in failed_rules:
            failed_rule_details[current_rule] = line
# ----------------------------------

# Metrics

# ----------------------------------

total_rules = passed + failed

if total_rules > 0:
    passed_rate = (passed / total_rules) * 100
    failed_rate = (failed / total_rules) * 100
else:

    passed_rate = 0
    failed_rate = 0

overall_data_quality_score = passed_rate

# ----------------------------------

# Summary Section

# ----------------------------------

st.subheader("Data Quality Report Summary")

st.divider()

if total_rules == 0:
    st.warning("No valid rules found in report.")
else:
    if overall_data_quality_score < 80:
        st.warning(
            f"Overall Data Quality Score: "
            f"{overall_data_quality_score:.2f}%"
        )
    elif overall_data_quality_score < 90:
        st.info(
        f"Overall Data Quality Score: "
        f"{overall_data_quality_score:.2f}%")
    else:
        st.success(
        f"Overall Data Quality Score: "
        f"{overall_data_quality_score:.2f}%")
#st.write(uploaded_file)        

# ----------------------------------

# Tabs

# ----------------------------------

tab1, tab2, tab3, tab4 = st.tabs(
[
"📊 Summary",
"✅ Passed Rules",
"❌ Failed Rules",
"📋 DQ Rules"
]
)

# ----------------------------------

# Tab 1 - Summary

# ----------------------------------

with tab1:
    st.subheader("Summary")

    st.write(f"Total Rules: {total_rules}")
    st.write(f"Passed Rules: {passed}")
    st.write(f"Failed Rules: {failed}")
    st.write(f"Pass Rate: {passed_rate:.2f}%")
    st.write(f"Fail Rate: {failed_rate:.2f}%")

# ----------------------------------

# Tab 2 - Passed Rules

# ----------------------------------

with tab2:
    st.subheader("Passed Rules")
    for line in report_lines:
        if line.startswith("DQ") and "PASSED" in line:
            st.success(line)
# ----------------------------------
# Tab 3 - Failed Rules
# ----------------------------------
with tab3:
    st.subheader("Failed Rules")
    for rule in failed_rules:
        st.warning(
           f"{rule} - "
            f"{rule_dict.get(rule, 'Description not found')}")
        if rule in failed_rule_details:
            st.write(
            f"Details: "
            f"{failed_rule_details[rule]}")
# ----------------------------------

# Tab 4 - DQ Rules

# ----------------------------------

with tab4:
    st.subheader("Available DQ Rules")
    for rule_id, description in rule_dict.items():
        st.write(
        f"{rule_id} - {description}")