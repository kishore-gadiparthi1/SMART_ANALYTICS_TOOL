# Smart Analytics Tool: Dynamic CSV Data Explorer

## Project Overview
This repository contains a Smart Analytics Web Application built using Python and Streamlit. This utility serves as a code-free data analysis platform, allowing users to upload any standard CSV dataset to instantly generate automated data summaries, profile statistical structural attributes, and build customizable interactive data visualizations on the fly.

The application is fully dynamic and adapts its interface elements automatically based on the columns present in the uploaded file.

---

## Application Features & Minimum Requirements Met

* **Dynamic File Uploader:** Features a drag-and-drop file upload widget supporting any arbitrary tabular `.csv` data source.
* **Automated Data Profiling:** * Displays structural data shapes (total rows and columns).
  * Outlines structural metadata including detected data types and column listings.
  * Generates missing value summaries and automatic statistical descriptions (`df.describe()`).
* **Dynamic Visualizations:** Provides interactive data plotting panels using Plotly Express where users can select custom columns for axes:
  * **Bar Charts:** For categorical aggregations.
  * **Line Charts:** For temporal and sequential trend tracking.
  * **Scatter Plots:** For multi-variable correlation inspection.
* **Data Inspection:** Includes an interactive, searchable raw data preview table.

---

## Technologies Used
* Python
* Streamlit
* Pandas
* Plotly Express

---

## Setup and Installation Instructions

To run this application locally, ensure you have Python installed and follow these steps:

1. Clone this repository to your workstation:
   ```bash
   git clone [https://github.com/kishore-gadiparthi1/SMART_ANALYTICS_TOOL.git](https://github.com/kishore-gadiparthi1/SMART_ANALYTICS_TOOL.git)
