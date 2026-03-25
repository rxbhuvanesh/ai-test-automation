import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.title("QA Automation 🚀")

menu = st.sidebar.selectbox("Menu", [
    "Run Tests",
    "API Testing",
    "Test History"
])

# Initialize session
if "results_data" not in st.session_state:
    st.session_state.results_data = []

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- RUN TESTS ----------------
if menu == "Run Tests":

    st.subheader("Run Automated Tests")

    if st.button("Run Tests"):

        response = requests.get("http://54.210.81.25:8000/run-tests")

        if response.status_code == 200:
            data = response.json()
        else:
            st.error(f"Backend Error: {response.text}")
            st.stop()
        
        st.write("Raw Response:", response.text)

        st.session_state.results_data = []

        pass_count = 0
        fail_count = 0

        # ✅ Safe handling
        if "results" in data:
            for result in data["results"]:
                st.write(f"Test: {result['test']}")

                st.session_state.results_data.append(result)

                if result["status"] == "Pass":
                    st.success("Pass ✅")
                    pass_count += 1
                else:
                    st.error("Fail ❌")
                    fail_count += 1
        else:
            st.error(f"Backend Error: {data}")
            st.stop()

        # Save history
        st.session_state.history.extend(st.session_state.results_data)

        # Dashboard
        st.subheader("Dashboard")
        st.write(f"✅ Passed: {pass_count}")
        st.write(f"❌ Failed: {fail_count}")

        fig, ax = plt.subplots()
        ax.pie([pass_count, fail_count], labels=["Pass", "Fail"], autopct='%1.1f%%')
        st.pyplot(fig)

    # Download option
    if st.session_state.results_data:
        df = pd.DataFrame(st.session_state.results_data)

        st.download_button(
            label="Download Results",
            data=df.to_csv(index=False),
            file_name="test_results.csv",
            mime="text/csv"
        )

# ---------------- API TESTING ----------------
elif menu == "API Testing":

    st.subheader("API Testing")

    url = st.text_input("Enter API URL")
    method = st.selectbox("Method", ["GET", "POST"])

    if st.button("Test API"):

        response = requests.post(
            "http://localhost:8000/api-test",
            json={"url": url, "method": method}
        )

        data = response.json()

        st.write("Status Code:", data["status_code"])
        st.text_area("Response", data["response"])

# ---------------- HISTORY ----------------
elif menu == "Test History":

    st.subheader("Test History")

    response = requests.get("http://localhost:8000/history")
    data = response.json()

    df = pd.DataFrame(data["history"])
    st.dataframe(df)

# Footer
st.markdown("---")
st.markdown("Built by Bhuvaneshwaran 🚀")