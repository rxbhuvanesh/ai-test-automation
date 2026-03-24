import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.title("QA Automation Dashboard 🚀")

menu = st.sidebar.selectbox("Menu", [
    "Run Tests",
    "API Testing",
    "Test History"
])
if menu == "Run Tests":

    st.subheader("Run Automated Tests")

    if "results_data" not in st.session_state:
        st.session_state.results_data = []

    if "history" not in st.session_state:
        st.session_state.history = []

    if st.button("Run Tests"):

        # ✅ MOCK DATA (for Streamlit Cloud)
        data = {
            "results": [
                {"test": "Valid Login", "status": "Pass"},
                {"test": "Invalid Login", "status": "Fail"},
                {"test": "Empty Fields", "status": "Pass"}
            ]
        }

        st.session_state.results_data = []

        pass_count = 0
        fail_count = 0

        for result in data["results"]:
            st.write(f"Test: {result['test']}")

            st.session_state.results_data.append(result)

            if result["status"] == "Pass":
                st.success("Pass ✅")
                pass_count += 1
            else:
                st.error("Fail ❌")
                fail_count += 1

        # Save to history
        st.session_state.history.extend(st.session_state.results_data)

        # 📊 Dashboard
        st.subheader("Dashboard")
        st.write(f"✅ Passed: {pass_count}")
        st.write(f"❌ Failed: {fail_count}")

        fig, ax = plt.subplots()
        ax.pie([pass_count, fail_count], labels=["Pass", "Fail"], autopct='%1.1f%%')
        st.pyplot(fig)

    # 📥 Download Option (OUTSIDE BUTTON)
    if st.session_state.results_data:
        df = pd.DataFrame(st.session_state.results_data)

        st.download_button(
            label="Download Results",
            data=df.to_csv(index=False),
            file_name="test_results.csv",
            mime="text/csv"
        )
elif menu == "API Testing":
    st.subheader("API Testing")

    url = st.text_input("API URL", "https://jsonplaceholder.typicode.com/posts/1")
    method = st.selectbox("Method", ["GET", "POST"])

    if st.button("Test API"):
        try:
            if method == "GET":
                res = requests.get(url)
            else:
                res = requests.post(url)

            st.write(f"Status Code: {res.status_code}")
            st.json(res.json())

        except Exception as e:
            st.error(f"Error: {e}")
            
elif menu == "Test History":
    st.subheader("Test History")

    if st.session_state.history:
        df_history = pd.DataFrame(st.session_state.history)
        st.dataframe(df_history)
    else:
        st.info("No test history available.")