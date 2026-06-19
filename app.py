import streamlit as st #streamlite import 

 #--- Page congigration ----
st.set_page_config(
    page_title = "Data quality Copilot",
    page_icon = "🤖")
#--- Title ----
st.title("Data quality Copilot")
#---------User input text box and reutrn ----------
question = st.text_input("Ask your data quality question here:")

if question: 
    st.write(f"You asked: {question}")
#---------Read the report file and count the passed and failed rules ----
with open("reports/validation_report.txt", "r") as f:
    report_lines = f.readlines()

passed = 0
failed = 0
failed_rules = []
rule_dict ={}
with open("rules/dq_rules.txt") as f:  
    for line in f:
        if "-" in line: 
            rule_id, description = line.split("-", 1)
            rule_dict[rule_id.strip()] = description.strip()

for line in report_lines:
    if line.startswith("DQ"):
        if "PASSED" in line:
            passed += 1
    if "FAILED" in line:
        failed += 1
        failed_rules.append(line.split()[0])
#rule_dict["DQ001"]            
#--output ---
st.write(f"Passed Rules: {passed}")
st.write(f"Failed Rules: {failed}")
st.subheader("Failed Rule IDs")
for rule in failed_rules:
    st.write(f"{rule}-{rule_dict.get(rule,'Description not found')}")
