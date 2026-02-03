{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d0ebd7d2-eadb-472c-ad42-f64e00a50860",
   "metadata": {},
   "source": [
    "# 📊 City Revenue Budget Analysis\n",
    "\n",
    "## Objective\n",
    "This project analyzes city-level revenue data by comparing **Budget vs Actual revenue**, evaluating **budget utilization efficiency**, and identifying patterns across cities and revenue types.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "730890b5-4491-494a-81c8-9dfc19df2937",
   "metadata": {},
   "source": [
    "## 1. Data Loading and Overview\n",
    "\n",
    "### Loading Objectives\n",
    "We will load the dataset and perform initial inspection to understand:\n",
    "\n",
    "- Number of records (rows)\n",
    "- Number of features (columns)\n",
    "- Column names and data types\n",
    "- Overall structure of the dataset\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1c70496b-8437-4cdc-9ede-db6f5a138b71",
   "metadata": {},
   "source": [
    "\n",
    "##Data Loading and Initial Overview"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e9e0871-ba7b-4a61-832d-771b0d288dbd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Load dataset\n",
    "df = pd.read_csv('City_Revenue.csv')\n",
    "\n",
    "print(\"Dataset loaded successfully!\")\n",
    "print(\"=\"*60)\n",
    "print(f\"Dataset Shape: {df.shape[0]} rows × {df.shape[1]} columns\")\n",
    "df.head()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bcc5dbd1-95ca-4a16-8668-4ce8eae3cd1e",
   "metadata": {},
   "source": [
    "###\n",
    "\n",
    "The city administration prepares an annual **revenue budget** for different sources such as taxes, fees, and service charges. At the end of the financial period, the **actual revenue collected** is recorded.\n",
    "\n",
    "However, decision-makers currently do not have a clear, data-driven view of:\n",
    "\n",
    "- Which cities are meeting their revenue targets\n",
    "- Which revenue sources are underperforming\n",
    "- Where budget allocation may be unrealistic or inefficient\n",
    "- How actual collections compare with planned budgets across cities\n",
    "\n",
    "To address this, we begin by loading the dataset and performing an initial inspection. This helps us understand the structure of the data and confirms that it contains the necessary information—such as city names, revenue types, budgeted amounts, and actual collections—required for meaningful analysis.\n",
    "\n",
    "This initial step lays the foundation for the entire project. By verifying the dataset’s size, structure, and sample records, we ensure that the data is suitable for further cleaning, transformation, and analytical exploration aimed at improving revenue planning and budget utilization across cities.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1d9135e4-87ab-444e-93ca-acb9cb4e0526",
   "metadata": {},
   "source": [
    "### Observation\n",
    "The dataset contains city-level revenue data including budgeted and actual values across multiple revenue sources.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "369fb11a-c752-4cf9-974f-8ddb96194e59",
   "metadata": {},
   "source": [
    "## 2. Understanding the Data Structure\n",
    "We inspect column names, data types, and missing values.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "10748c83-c9ac-47df-8c63-6c4184372882",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.info()\n",
    "df.isnull().sum()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0de6da9f-97d9-400e-a6df-957343424794",
   "metadata": {},
   "source": [
    "### Understanding Data Structure and Data Quality\n",
    "\n",
    "Before performing any analysis, it is essential to understand the **structure** and **quality** of the dataset.\n",
    "\n",
    "At this stage, we examine:\n",
    "\n",
    "- The data types of each column (numeric, text, etc.)\n",
    "- Whether the dataset contains any missing or incomplete values\n",
    "- The overall reliability of the data for analysis\n",
    "\n",
    "This step is crucial because revenue analysis depends heavily on accurate numerical values for **Budget** and **Actual collections**, along with correct identification of **City** and **Revenue Type**.\n",
    "\n",
    "By checking the structure and missing values, we ensure:\n",
    "\n",
    "- All required columns are present and correctly formatted\n",
    "- There are no gaps in critical fields that could distort analysis\n",
    "- The dataset is trustworthy for further cleaning, transformation, and visualization\n",
    "\n",
    "This validation step helps prevent incorrect insights that may arise due to hidden data quality issues.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e407e21f-8583-459e-a2ca-78d48806d0bf",
   "metadata": {},
   "source": [
    "## 3. Data Cleaning\n",
    "\n",
    "In this step, we handle:\n",
    "- Missing values\n",
    "- Incorrect data types\n",
    "- Formatting issues\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e66404e1-3094-4f87-b532-3753554b8c00",
   "metadata": {},
   "outputs": [],
   "source": [
    "# cleaning\n",
    "df.columns = df.columns.str.strip()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "175b4603-a64d-430c-9133-7babf7f22d91",
   "metadata": {},
   "source": [
    "###  Standardizing Column Names for Reliable Analysis\n",
    "\n",
    "In real-world datasets, column names often contain unwanted spaces or inconsistent formatting. These small issues can lead to errors while selecting columns, grouping data, or performing calculations.\n",
    "\n",
    "To avoid such proble\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "44b1850c-8f2b-469a-8d36-c4b78d70aee8",
   "metadata": {},
   "source": [
    "## 4. Budget vs Actual Revenue Analysis\n",
    "We compare budgeted revenue with actual revenue for each city.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2917fc28-7fba-4c7a-b44c-2988ce86f9f2",
   "metadata": {},
   "outputs": [],
   "source": [
    "city_summary = df.groupby('City_Name')[['Budget', 'Actual']].sum().reset_index()\n",
    "city_summary.head()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e3aa7098-e562-42be-b175-fdd56ce15fd0",
   "metadata": {},
   "source": [
    "### : Summarizing Revenue Performance by City\n",
    "\n",
    "To evaluate how each city is performing financially, we aggregate the data at the city level by summing the total **Budgeted revenue** and the total **Actual revenue collected**.\n",
    "\n",
    "This step helps transform detailed transaction-level data into a clear city-level summary that allows us to:\n",
    "\n",
    "- Compare planned revenue vs collected revenue for each city\n",
    "- Identify cities that are meeting or missing their revenue targets\n",
    "- Understand overall financial performance at the city level\n",
    "- Prepare the data for further visual analysis and comparisons\n",
    "\n",
    "By creating this city-wise summary, we move from raw data to meaningful information that directly supports decision-making and performance evaluation.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e8c547b4-b766-4076-8bd5-e3a436d8da58",
   "metadata": {},
   "source": [
    "## 5. Visualization: Budget vs Actual\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c015af0-0d0d-490b-bb18-906676f1f6a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "plt.figure(figsize=(8,6))\n",
    "sns.scatterplot(data=city_summary, x='Budget', y='Actual', s=100)\n",
    "plt.title('Budget vs Actual Revenue by City')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "89fb84a3-830b-44f5-94bb-502563b0daaa",
   "metadata": {},
   "source": [
    "### Scenario: Visual Comparison of Budgeted vs Actual Revenue\n",
    "\n",
    "After summarizing the revenue data at the city level, we use a scatter plot to visually compare the **Budgeted revenue** with the **Actual revenue collected** for each city.\n",
    "\n",
    "This visualization helps decision-makers quickly understand:\n",
    "\n",
    "- Which cities are performing close to their budget targets\n",
    "- Which cities are exceeding expectations\n",
    "- Which cities are significantly underperforming\n",
    "- The overall relationship between planned budgets and a\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b7224b79-11d4-43fe-9ddd-6232e5fa7d86",
   "metadata": {},
   "source": [
    "## 6. Revenue Type vs City Heatmap\n",
    "This heatmap shows how different revenue types perform across cities.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b3d1cdc-3683-4ba8-b48f-b961b92da0b7",
   "metadata": {},
   "outputs": [],
   "source": [
    "pivot2 = pd.pivot_table(\n",
    "    df,\n",
    "    values='Actual',\n",
    "    index='City_Name',\n",
    "    columns='Revenue_Type',\n",
    "    aggfunc='sum'\n",
    ")\n",
    "\n",
    "plt.figure(figsize=(12,8))\n",
    "sns.heatmap(pivot2, cmap='viridis')\n",
    "plt.title('City vs Revenue Type Revenue Heatmap')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "90c392eb-6972-4f63-8836-e536949d8f09",
   "metadata": {},
   "source": [
    "### : Analyzing Revenue Performance Across Cities and Revenue Types\n",
    "\n",
    "While the previous analysis focused on overall city performance, it is also important to understand **which specific revenue sources** contribute to that performance.\n",
    "\n",
    "In this step, we reorganize the data into a matrix where:\n",
    "\n",
    "- Rows represent different cities\n",
    "- Columns represent different revenue types\n",
    "- Values represent the total actual revenue collected\n",
    "\n",
    "This structure allows us to visually analyze how each revenue source performs across cities using a heatmap.\n",
    "\n",
    "The heatmap helps to:\n",
    "\n",
    "- Identify which revenue types generate the highest\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a6fcb931-9a14-4ad5-8d75-ed10d58d18dc",
   "metadata": {},
   "source": [
    "## 7. Key Insights\n",
    "\n",
    "- Some cities consistently exceed budget targets.\n",
    "- Certain revenue types underperform across all cities.\n",
    "- Budget allocation inefficiencies are visible.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8a219019-2f57-4029-9083-3162dc3c083b",
   "metadata": {},
   "source": [
    "## Conclusion\n",
    "\n",
    "This project analyzed city-level revenue data by comparing **Budgeted revenue** with **Actual revenue collections** across multiple cities and revenue sources.\n",
    "\n",
    "Through data inspection, cleaning, aggregation, and visualization, we derived meaningful insights into how effectively cities are achieving their financial targets.\n",
    "\n",
    "Key takeaways from the analysis:\n",
    "\n",
    "- Several cities show a strong alignment between budgeted and actual revenue, indicating effective planning and execution.\n",
    "- Some cities consistently underperform against their budgets, suggesting unrealistic targets or inefficiencies in revenue collection.\n",
    "- Certain revenue types contribute significantly to overall collections, while others remain weak across most cities.\n",
    "- Revenue performance is not uniform; it varies based on both city and revenue source.\n",
    "\n",
    "These findings highlight the importance of **data-driven budget planning** and continuous monitoring of revenue performance.\n",
    "\n",
    "By identifying underperforming areas and strong revenue streams, city administrators can:\n",
    "- Reallocate budgets more effectively\n",
    "- Set more realistic revenue targets\n",
    "- Improve collection strategies for weaker revenue sources\n",
    "- Make informed financial decisions for future planning\n",
    "\n",
    "Overall, this analysis demonstrates how structured data analysis and visualization can transform raw financial data into actionable insights for better governance and financial management.\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
