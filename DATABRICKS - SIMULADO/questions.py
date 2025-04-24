# perguntas.py

# Dicionário de perguntas e suas opções
questions = {
    "In a Databricks dashboard designed to track regional sales data, an analyst introduces a parameter that allows users to select a specific region from a dropdown list. Upon selection, the dashboard updates all visualizations, such as bar charts and line graphs, to reflect sales data exclusively for the chosen region. This change in data display triggered by the parameter selection is an example of which behavior in a Databricks dashboard?": [
        "The parameter behaves as a dynamic filter, altering the scope of the data presented based on user selection.",
        "The parameter solely adjusts the layout of the dashboard without changing the data displayed.",
        "The parameter serves as an input field for users to add new data into the dashboard for the selected region.",
        "The parameter automatically recalculates the entire dataset for the new region, affecting the data source.",
        "The parameter functions as a decorative element, enhancing the visual appeal but not the data content."
    ],
    "A data analyst is using Databricks SQL to visualize data showing the monthly sales trends across different regions. To effectively communicate the data, the analyst needs to choose an appropriate visualization type. Based on the data and the goal of showing trends over time, which visualization type should the analyst select in Databricks SQL?": [
        "Heatmap, for representing the intensity of sales in different regions.",
        "Line chart, as it effectively displays trends and changes over time.",
        "Scatter plot, to show the relationship between sales volume and time.",
        "Pie chart, to show the proportion of sales in each region compared to the whole.",
        "Bar chart, as it is best for comparing categories of data at a single point in time."
    ],
    "In Databricks, a data analyst is working on a dashboard composed of multiple visualizations and wants to ensure a consistent color scheme across all visualizations for better aesthetic coherence and readability. Which approach should the analyst take to change the colors of all the visualizations in the dashboard?": [
        "Implement a script in the dashboard code to automatically adjust the colors of all visualizations.",
        "Change the default color settings in the Databricks user preferences to automatically apply to all dashboards and visualizations.",
        "Export the dashboard data to a third-party tool for color scheme adjustments, then re-import it into Databricks.",
        "Manually adjust the color settings in each individual visualization to match the desired scheme.",
        "Use a dashboard-wide setting that allows the analyst to apply a uniform color scheme to all visualizations simultaneously."
    ],
    "In Azure Databricks, when using a table visualization type for SQL queries, which of the following statements accurately reflects its capabilities and limitations?":[
        "Table visualizations primarily function to display graphical representations like charts and graphs, rather than tabular data.",
        "Table visualizations in Databricks automatically aggregate data within the result set, providing a summary view.",
        "They allow for manual reordering, hiding, and formatting of data columns, but do not perform data aggregations within the result set.",
        "Table visualizations in Databricks are primarily used for external data export and are not suitable for in-dashboard data presentation.",
        "They are limited to displaying only numerical data and cannot handle textual or categorical data."
    ],
    "In Databricks, what is the impact on a dashboard if the configured refresh rate for the dashboard is set to be more frequent than the 'Auto Stop' setting of the SQL Warehouse?":[
        "The dashboard will continue to refresh at the set interval, the SQL Warehouse will continue running.",
        "The dashboard will stop refreshing once the warehouse enters 'Auto Stop' mode, potentially leading to outdated data being displayed.",
        "The warehouse's 'Auto Stop' setting is irrelevant, as the dashboard's refresh rate does not interact with warehouse settings.",
        "The dashboard will not be refreshed.",
        "The warehouse automatically adjusts its 'Auto Stop' setting to match the dashboard's refresh rate."
    ],
    "In Databricks, setting up a refresh schedule for dashboards is essential for ensuring that the displayed data is current. How does one configure a refresh schedule for a Databricks SQL dashboard?": [
        "Click Schedule at the upper-right of the dashboard. Then, click Add schedule.",
        "Utilizing an external tool to trigger refreshes in the Databricks dashboard.",
        "Writing a custom script in the dashboard's SQL queries to automate refreshes.",
        "Manually updating the dashboard at regular intervals without any automated scheduling.",
        "Sending periodic requests to the Databricks support team to refresh the dashboard."
    ],
    "In Databricks SQL, when creating a basic, schema-specific visualization, what is the first step you should take?": [
        "Select the visualization type from the visualization menu.",
        "Write a SQL query to retrieve data from the specific schema.",
        "Adjust the data refresh rate to ensure real-time visualization.",
        "Configure the dashboard settings to match the schema requirements.",
        "Import external visualization libraries for advanced charting."
    ],
    "A data analyst is creating a dashboard to present monthly sales data to company executives. The initial version of the dashboard contains accurate data but receives feedback that it is hard to interpret. The analyst then revises the dashboard by adjusting colors for better contrast, using consistent and clear fonts, and organizing charts logically. After these changes, the executives find the dashboard much more informative and easier to understand. This scenario illustrates which of the following points about visualization formatting?": [
        "Over-formatting can lead to data misinterpretation by introducing visual biases.",
        "Proper formatting can enhance readability and comprehension, leading to a more accurate interpretation of the data.",
        "Formatting changes the underlying data, thus altering the data's interpretation.",
        "Formatting is primarily used to reduce the size of the data set visually displayed.",
        "Formatting only affects the aesthetic aspect of the visualization and has no impact on its reception."
    ],
    "When sharing Databricks SQL dashboards, there are two primary settings: 'Run as viewer' and 'Run as owner'. What are the pros and cons of each setting in the context of sharing dashboards?": [
        "'Run as owner' offers greater customization of dashboard settings (pro), but requires viewers to have advanced knowledge of SQL (con). 'Run as viewer' simplifies the user experience (pro), but may lead to inconsistent data reporting (con).",
        "Both settings allow for easy sharing of dashboards (pro), but can lead to complexities in managing user permissions and data access (con).",
        "'Run as viewer' and 'Run as owner' both provide the same level of data visibility (pro), but may have limitations in customizing query execution (con).",
        "'Run as viewer' allows full customization of queries for each viewer (pro), but can be more resource-intensive (con). 'Run as owner' simplifies query management (pro), but doesn't account for individual user access levels (con).",
        "'Run as viewer' enhances data security by adhering to individual viewer's permissions (pro), but may limit data visibility (con). 'Run as owner' ensures consistent data visibility across users (pro), but might pose security risks if the owner has broader data access (con)."
    ]
    # Adicione mais perguntas aqui conforme necessário...
}

# Dicionário de respostas corretas
answers = {
    "In a Databricks dashboard designed to track regional sales data, an analyst introduces a parameter that allows users to select a specific region from a dropdown list. Upon selection, the dashboard updates all visualizations, such as bar charts and line graphs, to reflect sales data exclusively for the chosen region. This change in data display triggered by the parameter selection is an example of which behavior in a Databricks dashboard?": "The parameter behaves as a dynamic filter, altering the scope of the data presented based on user selection.",
    "A data analyst is using Databricks SQL to visualize data showing the monthly sales trends across different regions. To effectively communicate the data, the analyst needs to choose an appropriate visualization type. Based on the data and the goal of showing trends over time, which visualization type should the analyst select in Databricks SQL?": "Line chart, as it effectively displays trends and changes over time.",
    "In Databricks, a data analyst is working on a dashboard composed of multiple visualizations and wants to ensure a consistent color scheme across all visualizations for better aesthetic coherence and readability. Which approach should the analyst take to change the colors of all the visualizations in the dashboard?": "Use a dashboard-wide setting that allows the analyst to apply a uniform color scheme to all visualizations simultaneously.",
    "In Azure Databricks, when using a table visualization type for SQL queries, which of the following statements accurately reflects its capabilities and limitations?":"They allow for manual reordering, hiding, and formatting of data columns, but do not perform data aggregations within the result set.",
    "In Databricks, what is the impact on a dashboard if the configured refresh rate for the dashboard is set to be more frequent than the 'Auto Stop' setting of the SQL Warehouse?":"The dashboard will continue to refresh at the set interval, the SQL Warehouse will continue running.",
    "In Databricks, setting up a refresh schedule for dashboards is essential for ensuring that the displayed data is current. How does one configure a refresh schedule for a Databricks SQL dashboard?": "Click Schedule at the upper-right of the dashboard. Then, click Add schedule.",
    "In Databricks SQL, when creating a basic, schema-specific visualization, what is the first step you should take?": "Write a SQL query to retrieve data from the specific schema.",
    "A data analyst is creating a dashboard to present monthly sales data to company executives. The initial version of the dashboard contains accurate data but receives feedback that it is hard to interpret. The analyst then revises the dashboard by adjusting colors for better contrast, using consistent and clear fonts, and organizing charts logically. After these changes, the executives find the dashboard much more informative and easier to understand. This scenario illustrates which of the following points about visualization formatting?": "Proper formatting can enhance readability and comprehension, leading to a more accurate interpretation of the data.",
    "When sharing Databricks SQL dashboards, there are two primary settings: 'Run as viewer' and 'Run as owner'. What are the pros and cons of each setting in the context of sharing dashboards?": "'Run as viewer' enhances data security by adhering to individual viewer's permissions (pro), but may limit data visibility (con). 'Run as owner' ensures consistent data visibility across users (pro), but might pose security risks if the owner has broader data access (con)."

    # Adicione aqui as respostas corretas para as outras perguntas...
}
