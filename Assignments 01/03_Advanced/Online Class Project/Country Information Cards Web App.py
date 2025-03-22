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
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(country["flags"]["png"], use_column_width=True)
    with col2:
        st.subheader(country["name"]["common"])
        st.text(f"Capital: {country.get('capital', ['N/A'])[0]}")
        st.text(f"Region: {country['region']}")
        st.text(f"Population: {country['population']:,}")
        st.text(f"Area: {country['area']:,} km²")

# Main Streamlit app
def main():
    st.title("Country Information Cards 🌍")
    st.markdown("Explore information about different countries.")

    # Fetch data
    country_data = fetch_country_data()

    if country_data:
        # Search filter
        search = st.text_input("Search for a country:")
        filtered_data = [
            country for country in country_data if search.lower() in country["name"]["common"].lower()
        ]

        # Display country cards
        if filtered_data:
            for country in filtered_data:
                display_country_card(country)
                st.markdown("---")
        else:
            st.warning("No countries match your search.")

if __name__ == "__main__":
    main()
