import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.subheader("Run Automated Tests")

results_data = []

if "results_data" not in st.session_state:
    st.session_state.results_data = []

if st.button("Run Tests"):
    try:
        response = requests.get("http://localhost:8000/run-tests/")
        data = response.json()

        st.session_state.results_data = []

        pass_count = 0
        fail_count = 0

        for result in data["results"]:
            st.write(f"Test: {result['test']}")

            results_data.append({
                "Test Name": result["test"],
                "Status": result["status"]
            })

            if result["status"] == "Pass":
                st.success("Pass ✅")
                pass_count += 1
            else:
                st.error("Fail ❌")
                fail_count += 1

                if "screenshot" in result:
                    st.image(result["screenshot"], caption="Failure Screenshot")

        # 📊 Dashboard Section
        st.subheader("Test Report Dashboard")

        st.write(f"✅ Passed: {pass_count}")
        st.write(f"❌ Failed: {fail_count}")

        # Pie Chart
        labels = ['Pass', 'Fail']
        sizes = [pass_count, fail_count]

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax.set_title("Test Results Distribution")

        st.pyplot(fig)

        fig2, ax2 = plt.subplots()
        ax2.bar(labels, sizes)
        ax2.set_title("Pass vs Fail Count")
        st.pyplot(fig2)

    except Exception as e:
        st.error(f"Error: {e}")

if st.session_state.results_data:
    df = pd.DataFrame(st.session_state.results_data)

    st.download_button(
        label="Download Results",
        data=df.to_csv(index=False),
        file_name="test_results.csv",
        mime="text/csv"
    )
    
st.subheader("API Testing")

url = st.text_input("Enter API URL")
method = st.selectbox("Method", ["GET", "POST"])

if st.button("Test API"):
    response = requests.post(
        "http://localhost:8000/api-test/",
        json={"url": url, "method": method}
    )

    data = response.json()

    if "error" in data:
        st.error(data["error"])
    else:
        st.write("Status Code:", data["status_code"])
        st.text_area("Response", data["response"])

st.subheader("Test History")

if st.button("Load History"):
    import sqlite3
    conn = sqlite3.connect("test_history.db")
    df = pd.read_sql("SELECT * FROM results", conn)
    st.dataframe(df)