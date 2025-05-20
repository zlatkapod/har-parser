import streamlit as st
import json

st.title("HAR File Inspector")

uploaded_file = st.file_uploader("Upload a HAR file", type=["har"])

if uploaded_file is not None:
    har_data = json.load(uploaded_file)
    entries = har_data.get("log", {}).get("entries", [])

    st.write(f"Total requests found: {len(entries)}")

    for entry in entries:
        request = entry.get("request", {})
        response = entry.get("response", {})

        st.markdown("### Request")
        st.json({
            "method": request.get("method"),
            "url": request.get("url"),
            "postData": request.get("postData", {}).get("text")
        })

        st.markdown("### Response")
        st.json({
            "status": response.get("status"),
            "statusText": response.get("statusText"),
            "body": response.get("content", {}).get("text")
        })

        st.markdown("---")