import streamlit as st
import requests

# Fetch country data from API
def fetch_country_data():
    api_url = "https://restcountries.com/v3.1/all"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching country data: {e}")
        return []

# Display country card
def display_country_card(country):
    try:
        col1, col2 = st.columns([1, 2])
        with col1:
            flag_url = country.get("flags", {}).get("png", "")
            if flag_url:
                st.image(flag_url, use_column_width=True)
            else:
                st.warning("No flag available.")
        with col2:
            st.subheader(country.get("name", {}).get("common", "N/A"))
            st.text(f"Capital: {', '.join(country.get('capital', ['N/A']))}")
            st.text(f"Region: {country.get('region', 'N/A')}")
            st.text(f"Population: {country.get('population', 0):,}")
            st.text(f"Area: {country.get('area', 0):,} km²")
    except Exception as e:
        st.error(f"Error displaying country card: {e}")

# Main Streamlit app
def main():
    st.title("Country Information Cards 🌍")
    st.markdown("Explore information about different countries.")
    
    # Fetch data
    country_data = fetch_country_data()

    if country_data:
        # Search filter
        search = st.text_input("Search for a country:", "").strip()
        filtered_data = [
            country for country in country_data 
            if search.lower() in country.get("name", {}).get("common", "").lower()
        ]

        # Display country cards
        if filtered_data:
            for country in filtered_data:
                display_country_card(country)
                st.markdown("---")
        else:
            st.warning("No countries match your search.")
    else:
        st.error("No country data available. Please try again later.")

if __name__ == "__main__":
    main()
