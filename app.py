import streamlit as st
import json
import datetime

st.set_page_config(layout="wide", page_title="HAR File Inspector")
st.title("HAR File Inspector")
st.subheader("A tool for backend developers to analyze HAR files")

uploaded_file = st.file_uploader("Upload a HAR file", type=["har"])

if uploaded_file is not None:
    har_data = json.load(uploaded_file)
    entries = har_data.get("log", {}).get("entries", [])

    st.write(f"Total requests found: {len(entries)}")

    # Filtering options
    col1, col2, col3 = st.columns(3)
    with col1:
        filter_method = st.multiselect(
            "Filter by HTTP Method",
            options=sorted(set(entry.get("request", {}).get("method", "") for entry in entries)),
            default=[]
        )
    with col2:
        filter_status = st.multiselect(
            "Filter by Status Code",
            options=sorted(set(str(entry.get("response", {}).get("status", "")) for entry in entries)),
            default=[]
        )
    with col3:
        search_url = st.text_input("Search in URL", "")

    # Apply filters
    filtered_entries = entries
    if filter_method:
        filtered_entries = [entry for entry in filtered_entries if entry.get("request", {}).get("method", "") in filter_method]
    if filter_status:
        filtered_entries = [entry for entry in filtered_entries if str(entry.get("response", {}).get("status", "")) in filter_status]
    if search_url:
        filtered_entries = [entry for entry in filtered_entries if search_url.lower() in entry.get("request", {}).get("url", "").lower()]

    st.write(f"Showing {len(filtered_entries)} of {len(entries)} requests")

    # Display entries
    for idx, entry in enumerate(filtered_entries):
        request = entry.get("request", {})
        response = entry.get("response", {})

        # Get timestamp and convert to readable format
        start_time = entry.get("startedDateTime", "")
        if start_time:
            try:
                # HAR timestamps are in ISO format
                timestamp = datetime.datetime.fromisoformat(start_time.replace('Z', '+00:00'))
                formatted_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            except:
                formatted_time = start_time
        else:
            formatted_time = "Unknown"

        # Get API endpoint from URL
        url = request.get("url", "")
        method = request.get("method", "")
        status = response.get("status", "")

        # Create an expander for each request
        with st.expander(f"{method} {url} - Status: {status} - Time: {formatted_time}"):
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### Request")
                st.markdown(f"**Method:** {method}")
                st.markdown(f"**URL:** {url}")

                # Request headers
                show_req_headers = st.checkbox("Show Headers", key=f"req_headers_{idx}_{method}_{url}")
                if show_req_headers:
                    headers = request.get("headers", [])
                    for header in headers:
                        st.markdown(f"**{header.get('name')}:** {header.get('value')}")

                # Request body
                post_data = request.get("postData", {}).get("text")
                if post_data:
                    show_req_body = st.checkbox("Show Request Body", key=f"req_body_{idx}_{method}_{url}")
                    if show_req_body:
                        try:
                            # Try to parse as JSON for better display
                            json_data = json.loads(post_data)
                            st.json(json_data)
                        except:
                            st.text(post_data)

            with col2:
                st.markdown("### Response")
                st.markdown(f"**Status:** {status} {response.get('statusText', '')}")

                # Response headers
                show_resp_headers = st.checkbox("Show Headers", key=f"resp_headers_{idx}_{method}_{url}")
                if show_resp_headers:
                    headers = response.get("headers", [])
                    for header in headers:
                        st.markdown(f"**{header.get('name')}:** {header.get('value')}")

                # Response body
                response_body = response.get("content", {}).get("text")
                if response_body:
                    show_resp_body = st.checkbox("Show Response Body", key=f"resp_body_{idx}_{method}_{url}")
                    if show_resp_body:
                        try:
                            # Try to parse as JSON for better display
                            json_data = json.loads(response_body)
                            st.json(json_data)
                        except:
                            st.text(response_body)

        st.markdown("---")
