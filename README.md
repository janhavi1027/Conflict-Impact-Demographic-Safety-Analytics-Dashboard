# 📊 Conflict Impact & Demographic Safety Analytics Dashboard

An interactive decision-support system and analytical dashboard built to evaluate casualty trends, demographic vulnerabilities, hostility participation ratios, and high-risk regional hotspots in conflict zones.

🌐 **Live Interactive App:** [Conflict Analytics Dashboard](https://conflict-impact-demographic-safety-analytics-dashboard-jn2dakc.streamlit.app/)

---

## 📌 Executive Summary

Understanding casualty dynamics and demographic safety during geopolitical conflicts is critical for humanitarian organizations, policy researchers, and international relief teams. This project processes historical casualty data to extract actionable insights, measure civilian vulnerability metrics, and map spatial clustering of high-impact zones.

### Key Analytical Deliverables

- **Executive KPI Suite:** Real-time calculation of total fatalities, civilian safety ratio, average victim age, and primary impact districts.
- **Dynamic Filtering Engine:** Multi-variable filtering by year range, region, citizenship, and hostility participation status.
- **Demographic Vulnerability Profiling:** Age-group binning and gender breakdown to identify non-combatant impact.
- **Spatial Hotspot Analysis:** Identification of top high-risk districts for targeted relief allocation.

---

## 🛠️ Tech Stack & Architecture

| Domain | Tools & Technologies |
| :--- | :--- |
| **Frontend & App Framework** | Streamlit |
| **Data Manipulation & Pipeline** | Pandas, NumPy |
| **Interactive Visualizations** | Plotly Express |
| **Exploratory Analysis** | Jupyter Notebook |
| **Deployment & CI/CD** | Streamlit Cloud, GitHub |
| **Programming Language** | Python 3.10+ |

---

## 📈 Dashboard Features & Deep Dive

| Tab Feature | Analytical Focus | Business / Policy Value |
| :--- | :--- | :--- |
| **📈 Timeline Analysis** | Multi-year escalation curves and yearly fatality spikes | Enables humanitarian agencies to analyze surge periods and support resource planning. |
| **👥 Demographics** | Age-group distribution (Child, Minor, Adult, Senior) vs. Gender | Helps identify demographic groups experiencing higher levels of impact. |
| **📍 Regional Hotspots** | Horizontal bar profiling of top affected districts | Supports spatial prioritization of field teams and emergency resources. |
| **📄 Data Explorer** | Dynamic keyword search and filtered CSV dataset export | Provides research transparency and enables downstream analytical modeling. |

---

## 📊 Key Dashboard Insights

The dashboard provides interactive analysis across multiple dimensions:

### Casualty Trends

- Year-wise fatality trends
- Identification of periods with increased casualty counts
- Comparison of regional impact over time

### Demographic Analysis

- Age-group distribution
- Gender-wise casualty analysis
- Civilian and hostility participation breakdown
- Average victim age

### Regional Analysis

- Top affected districts
- Regional casualty concentration
- High-impact geographic hotspots

### Interactive Data Exploration

- Filter records by year
- Filter by region
- Filter by citizenship
- Filter by hostility participation
- Search and explore filtered records
- Export filtered data for further analysis

---

## 📂 Repository Structure

```text
Conflict-Impact-Demographic-Safety-Analytics-Dashboard/
│
├── Data/
│   └── Fatalities.csv
│
├── app.py
├── exploratory_analysis.ipynb
├── requirements.txt
└── README.md
```

### File Description

| File | Description |
| :--- | :--- |
| `Data/Fatalities.csv` | Raw casualty dataset |
| `app.py` | Main Streamlit application |
| `exploratory_analysis.ipynb` | Exploratory data analysis and data wrangling |
| `requirements.txt` | Python dependencies for deployment |
| `README.md` | Project documentation |

---

# 🚀 Local Installation & Execution Guide

Follow these steps to run the application locally.

## 1. Clone the Repository

```bash
git clone https://github.com/janhavi1027/Conflict-Impact-Demographic-Safety-Analytics-Dashboard.git
cd Conflict-Impact-Demographic-Safety-Analytics-Dashboard
```

## 2. Set Up Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the Streamlit Dashboard

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 🔄 Analytical Workflow

```text
Raw Casualty Dataset
        │
        ▼
Data Cleaning & Preprocessing
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Demographic Analysis
        │
        ├── Age Groups
        ├── Gender
        └── Hostility Participation
        │
        ▼
Regional & Temporal Analysis
        │
        ├── Year-wise Trends
        ├── Regional Distribution
        └── Hotspot Identification
        │
        ▼
Interactive Streamlit Dashboard
        │
        ├── KPI Cards
        ├── Interactive Filters
        ├── Charts
        └── Data Explorer
```

---

## 💡 Potential Applications

The dashboard can support analytical workflows such as:

- Monitoring historical casualty trends
- Identifying demographic vulnerability patterns
- Comparing regional impact
- Exploring high-impact districts
- Supporting humanitarian data analysis
- Providing an interactive interface for researchers
- Exporting filtered datasets for further analysis

---

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a new feature branch.
3. Make your changes.
4. Commit your changes.
5. Open a pull request.

You can also report bugs or request features through the repository's issue tracker.

---

## 📜 License

This project is open-source and available under the **MIT License**.

See the [`LICENSE`](LICENSE) file for details.

---

## 👤 Author

**Janhavi Sakore**

B.Tech — Artificial Intelligence & Machine Learning  
Madhav Institute of Technology and Science, Gwalior

---

⭐ If you found this project useful, consider giving the repository a star!
