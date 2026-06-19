#print("REPORT_READER LOADED")

def read_report(uploaded_file):

    if uploaded_file is None:
        return None

    return uploaded_file.getvalue().decode("utf-8").splitlines()