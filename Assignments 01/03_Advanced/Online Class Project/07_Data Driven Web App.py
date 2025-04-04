import streamlit as st
import pandas as pd
import plotly.express as px

# App Title
st.title("Data-Driven Python Web App 📊")
st.markdown("Upload your CSV file to explore and visualize the data.")

# File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        # Read the uploaded file
        df = pd.read_csv(uploaded_file)
        
        # Display data preview
        st.subheader("Data Preview")
        st.dataframe(df.head())

        # Show basic information
        st.subheader("Basic Information")
        st.write(f"**Number of Rows:** {df.shape[0]}")
        st.write(f"**Number of Columns:** {df.shape[1]}")
        st.write("**Column Names:**")
        st.write(list(df.columns))

        # Check if the DataFrame is empty
        if df.empty:
            st.warning("The uploaded CSV file is empty. Please upload a valid CSV file.")
        else:
            # Column Selection for Visualization
            st.subheader("Visualize Data")
            columns = df.columns.tolist()

            # Dropdown to select column for X-axis
            x_col = st.selectbox("Select X-axis column", options=columns)

            # Dropdown to select column for Y-axis
            y_col = st.selectbox("Select Y-axis column", options=columns)

            # Visualization
            if x_col and y_col:
                try:
                    fig = px.scatter(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col}", size_max=60)
                    st.plotly_chart(fig)
                except Exception as e:
                    st.error(f"Error in creating visualization: {e}")

            # Filter Options
            st.subheader("Filter Data")
            filter_col = st.selectbox("Select column to filter data", options=columns)

            if filter_col:
                unique_values = df[filter_col].dropna().unique()
                filter_val = st.selectbox(f"Select a value from {filter_col}", options=unique_values)

                if filter_val:
                    filtered_data = df[df[filter_col] == filter_val]

                    st.write(f"Filtered Data (Where {filter_col} = {filter_val}):")
                    st.dataframe(filtered_data)
    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
else:
    st.info("Please upload a CSV file to proceed.")
