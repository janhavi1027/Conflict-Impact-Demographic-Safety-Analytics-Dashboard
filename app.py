import pandas as pd
import plotly.express as px
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Conflict Impact Analytics Dashboard",
    page_icon="📊",
    layout="wide",
)

# Title Header
st.title("📊 Conflict Impact & Demographic Safety Analytics Dashboard")
st.markdown(
    "An interactive decision-support system analyzing casualty trends, demographic vulnerability, and regional high-risk zones."
)
st.markdown("---")


# Data Loading Pipeline (Folder path updated to 'Data/Fatalities.csv')
@st.cache_data
def load_and_clean_data():
    df = pd.read_csv("Data/Fatalities.csv")

    # Datetime Parsing
    df["date_of_event"] = pd.to_datetime(df["date_of_event"], errors="coerce")
    df["date_of_death"] = pd.to_datetime(df["date_of_death"], errors="coerce")
    df["year"] = df["date_of_event"].dt.year
    df["month"] = df["date_of_event"].dt.strftime("%B")

    # String cleaning & fillna
    df["took_part_in_the_hostilities"] = (
        df["took_part_in_the_hostilities"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
    )
    df["event_location_region"] = (
        df["event_location_region"].fillna("Unknown").astype(str).str.strip()
    )
    df["event_location_district"] = (
        df["event_location_district"].fillna("Unknown").astype(str).str.strip()
    )
    df["citizenship"] = (
        df["citizenship"].fillna("Unknown").astype(str).str.strip()
    )

    # Age Group Binning
    bins = [-1, 12, 17, 35, 60, 120]
    labels = [
        "Child (0-12)",
        "Minor (13-17)",
        "Young Adult (18-35)",
        "Adult (36-60)",
        "Senior (60+)",
    ]
    df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels)

    return df


df = load_and_clean_data()

# ----------------- SIDEBAR FILTERS -----------------
st.sidebar.header("🔍 Analytical Filters")

# Year Range Slider
valid_years = df["year"].dropna()
min_year = int(valid_years.min()) if not valid_years.empty else 2000
max_year = int(valid_years.max()) if not valid_years.empty else 2023
selected_years = st.sidebar.slider(
    "Select Year Range", min_year, max_year, (min_year, max_year)
)

# Region Multiselect
available_regions = sorted(
    [r for r in df["event_location_region"].unique() if r != "Unknown"]
)
selected_regions = st.sidebar.multiselect(
    "Select Region", options=available_regions, default=available_regions
)

# Citizenship Multiselect
available_citizenships = sorted(
    [c for c in df["citizenship"].unique() if c != "Unknown"]
)
selected_citizenship = st.sidebar.multiselect(
    "Select Citizenship",
    options=available_citizenships,
    default=available_citizenships,
)

# Hostility Status Multiselect
hostility_options = df["took_part_in_the_hostilities"].unique().tolist()
selected_hostility = st.sidebar.multiselect(
    "Hostility Participation Status",
    options=hostility_options,
    default=hostility_options,
)

st.sidebar.caption(
    "💡 *Tip: Keep 'No' selected in Hostility Status to calculate Civilian metrics accurately.*"
)

# Filter Dataset
filtered_df = df[
    (df["year"] >= selected_years[0])
    & (df["year"] <= selected_years[1])
    & (df["took_part_in_the_hostilities"].isin(selected_hostility))
]

if selected_regions:
    filtered_df = filtered_df[
        filtered_df["event_location_region"].isin(selected_regions)
    ]
if selected_citizenship:
    filtered_df = filtered_df[
        filtered_df["citizenship"].isin(selected_citizenship)
    ]

# ----------------- EXECUTIVE KPI CARDS -----------------
st.subheader("📌 Key Performance Indicators (Executive Summary)")
col1, col2, col3, col4 = st.columns(4)

total_fatalities = len(filtered_df)

# Robust Civilian Calculation
civilians = len(
    filtered_df[
        filtered_df["took_part_in_the_hostilities"].str.lower() == "no"
    ]
)
civilian_pct = (
    (civilians / total_fatalities * 100) if total_fatalities > 0 else 0.0
)

avg_age = filtered_df["age"].mean() if not filtered_df.empty else 0.0

top_district = (
    filtered_df["event_location_district"].mode()[0]
    if not filtered_df.empty
    and len(filtered_df["event_location_district"].mode()) > 0
    else "N/A"
)

col1.metric("Total Fatalities", f"{total_fatalities:,}")
col2.metric("Civilian Ratio", f"{civilian_pct:.1f}%")
col3.metric(
    "Average Victim Age", f"{avg_age:.1f} Yrs" if avg_age > 0 else "N/A"
)
col4.metric("Highest Impact District", top_district)

st.markdown("---")

# ----------------- TABS & VISUALIZATIONS -----------------
tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📈 Timeline Analysis",
        "👥 Demographics & Vulnerability",
        "📍 Regional Hotspots",
        "📄 Data Explorer & Export",
    ]
)

# Tab 1: Timeline
with tab1:
    st.subheader("Fatalities Trend Over Time")
    if not filtered_df.empty:
        yearly_df = filtered_df.groupby("year").size().reset_index(name="Count")
        fig_line = px.line(
            yearly_df,
            x="year",
            y="Count",
            markers=True,
            title="Annual Casualty Escalation Curve",
            labels={"year": "Year", "Count": "Number of Fatalities"},
        )
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.warning("No data available for the selected filters.")

    st.info(
        "💡 **Business/Policy Insight:** Historical spikes highlight peak conflict periods. Humanitarian organizations can use these trends to allocate medical resources during high-risk cycles."
    )

# Tab 2: Demographics
with tab2:
    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("Age Group & Gender Breakdown")
        if not filtered_df.empty:
            fig_age = px.histogram(
                filtered_df,
                x="age_group",
                color="gender",
                barmode="group",
                title="Victims Distribution by Age Group and Gender",
            )
            st.plotly_chart(fig_age, use_container_width=True)

    with col_b:
        st.subheader("Hostility Participation Ratio")
        if not filtered_df.empty:
            fig_pie = px.pie(
                filtered_df,
                names="took_part_in_the_hostilities",
                title="Participation Status Breakdown",
                hole=0.4,
            )
            st.plotly_chart(fig_pie, use_container_width=True)

    st.info(
        "💡 **Business/Policy Insight:** High non-combatant civilian percentage indicates severe social impact and highlights policy needs for civilian safety infrastructure."
    )

# Tab 3: Regional Hotspots
with tab3:
    st.subheader("Top High-Risk Districts")
    if not filtered_df.empty:
        district_df = (
            filtered_df["event_location_district"]
            .value_counts()
            .head(10)
            .reset_index()
        )
        district_df.columns = ["District", "Fatalities"]

        fig_bar = px.bar(
            district_df,
            x="Fatalities",
            y="District",
            orientation="h",
            color="Fatalities",
            color_continuous_scale="Reds",
            title="Top 10 Most Affected Districts",
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    st.info(
        "💡 **Business/Policy Insight:** Spatial clustering helps pinpoint high-risk regions for deployment of relief teams and field operations."
    )

# Tab 4: Raw Data & Search
with tab4:
    st.subheader("Interactive Data Explorer")
    search_query = st.text_input("🔍 Search records by keyword (Name or Notes):")

    display_df = filtered_df
    if search_query:
        display_df = filtered_df[
            filtered_df["name"].str.contains(
                search_query, case=False, na=False
            )
            | filtered_df["notes"].str.contains(
                search_query, case=False, na=False
            )
        ]

    st.dataframe(
        display_df[
            [
                "name",
                "date_of_event",
                "age",
                "gender",
                "citizenship",
                "event_location_district",
                "took_part_in_the_hostilities",
            ]
        ],
        use_container_width=True,
    )

    # Export Button
    csv_data = display_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Filtered Dataset as CSV",
        data=csv_data,
        file_name="filtered_conflict_fatalities.csv",
        mime="text/csv",
    )