import streamlit as st #streamlite import 

 #--- Page congigration ----
st.set_page_config(
    page_title = "Data quality Copilot",
    page_icon = "🤖")
#--- Title ----
st.title("Data quality Copilot")
#---------User input text box and reutrn ----------
#question = st.text_input("Ask your data quality question here:")
#if question: 
#  st.write(f"You asked: {question}")
#---File uploader----
st.subheader("Upload your file here")
uploaded_file = st.file_uploader("Upload your file here")


#---------Read the report file and count the passed and failed rules ----
if uploaded_file is not None:
    report_lines = uploaded_file.getvalue().decode("utf-8").splitlines()
else:
    with open("reports/validation_report.txt", "r") as f:
        report_lines = f.readlines()
passed = 0
failed = 0
failed_rules = []
rule_dict ={}
#--- Read DQ Rules ----
with open("rules/dq_rules.txt") as f:  
    for line in f:
        if "-" in line: 
            rule_id, description = line.split("-", 1)
            rule_dict[rule_id.strip()] = description.strip()

for line in report_lines:
    if line.startswith("DQ"):
        if "PASSED" in line:
            passed += 1
        elif "FAILED" in line:
            failed += 1
            failed_rules.append(line.split()[0])
#rule_dict["DQ001"]            
#--output ---
st.subheader("Data Quality Report Summary")
#--- Number of rules passed and failed with toal 
st.divider()
total_rules =  passed + failed 
total_rules =  passed + failed 
st.write(f"Total rules : {total_rules}")

if total_rules > 0:
    passed_rate  = (passed / total_rules)*100
    failed_rate = (failed / total_rules)*100
    st.success(f" Passed rules {passed} or {passed_rate:.2f}% of total rules")
    st.info (f" Failed Rules: {failed} or {failed_rate:.2f}% of total rules")
else:
    passed_rate = 0
    failed_rate = 0
    st.warning("Inadequate data available for analysis")


overall_data_quality_score = passed_rate
#st.write(f"Overall data quality scope: {100 - failed_rate:.2f}%")
if overall_data_quality_score < 80: 
    st.warning(f"Overall data quality score is {overall_data_quality_score:.2f}%"
               f"which is below the acceptable threshold of 80%. Please review the "
               f"failed rules and take necessary actions to improve data quality.")
elif overall_data_quality_score >= 80 and overall_data_quality_score < 90:
    st.info(f"Overall data quality score is {overall_data_quality_score:.2f}%,"
            f"which is in the acceptable range. However, there is room for improvement."
             f"Please review the failed rules and take necessary actions to further enhance data quality.")
else:
    st.success(f"Overall data quality score is {overalldataquality_score:.2f}%,"
               f"which is excellent! Keep up the good work in maintaining high data quality standards.")

#st.write(f"Failed Rules: {failed}")
st.subheader("Failed Rule IDs")
for rule in failed_rules:
    st.warning(f"{rule}-{rule_dict.get(rule,'Description not found')}")
