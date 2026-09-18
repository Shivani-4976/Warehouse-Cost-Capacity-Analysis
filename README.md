<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00C6FF,50:0072FF,100:7F00FF&height=220&section=header&text=Warehouse%20Analytics&fontSize=45&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Cost%20%7C%20Capacity%20%7C%20Productivity%20%7C%20Commercial%20Insights&descAlignY=55&descSize=18"/>

# 📦 Warehouse Cost & Capacity Analysis by shivani raj

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&duration=2500&pause=800&color=00C6FF&center=true&vCenter=true&width=800&lines=Turning+Warehouse+Data+into+Business+Insights;Analyzing+Cost+%26+Capacity;Measuring+Labour+Productivity;Understanding+Revenue+%26+Contribution;Python+%7C+SQL+%7C+Excel+%7C+Power+BI" />

<br>

<img src="https://komarev.com/ghpvc/?username=YOUR_GITHUB_USERNAME&label=PROJECT%20VIEWS&color=0072FF&style=for-the-badge"/>

</div>

---

<div align="center">

## 🚀 PROJECT AT A GLANCE

<table>
<tr>
<td align="center">📦<br><b>Workload</b><br>Orders & Units</td>
<td align="center">💰<br><b>Cost</b><br>Operating Cost</td>
<td align="center">👷<br><b>Productivity</b><br>Labour Efficiency</td>
<td align="center">📈<br><b>Commercial</b><br>Revenue & Contribution</td>
</tr>
</table>

</div>

---

# 👩‍💻 Meet the Analyst

<img align="right" width="300" src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2x6aHk4dWR2eHk5eGx6N2d3cW5pZzN6b2F1cW9rY3h4bWZ4ZyZlcD0x/gHnBLfU2cD2qA/giphy.gif">

### Hi, I'm **Shivani Raj** 👋

I'm an aspiring **Data Analyst** interested in using data to solve real-world business problems.

My analytical toolkit includes:

🐍 Python
🗄️ SQL
📊 Excel
📈 Power BI
🤖 Machine Learning

I enjoy transforming:

**Raw Data → Analysis → KPIs → Insights → Business Decisions**

<br clear="right"/>

---

# 🎯 Business Objective

> **Convert warehouse operational data into actionable KPIs for capacity planning, cost analysis, productivity measurement and operational decision-making.**

This project uses **simulated warehouse order-level data** to analyze the relationship between:

```text
              📦 WORKLOAD
                  │
                  ▼
             👷 LABOUR
                  │
                  ▼
             ⏱️ TIME
                  │
                  ▼
             💰 COST
                  │
                  ▼
           📊 PRODUCTIVITY
                  │
                  ▼
          💵 COMMERCIAL VALUE
                  │
                  ▼
         🎯 BUSINESS DECISIONS
```

---

# 🔥 Key Questions

<div align="center">

|  📦 Operations |   💰 Cost   |  👷 Productivity | 💵 Commercial |
| :------------: | :---------: | :--------------: | :-----------: |
|  Total Orders? | Total Cost? |   Labour Hours?  |    Revenue?   |
|  Total Units?  | Cost/Order? |    Units/Hour?   | Contribution? |
| Zone Workload? |  Cost/Unit? | Zone Efficiency? |   Margin %?   |

</div>

---

# 📊 KPI ENGINE

### 💰 Cost per Order

```text
                 Total Operating Cost
Cost / Order = ───────────────────────
                    Total Orders
```

### 📦 Cost per Unit

```text
                 Total Operating Cost
Cost / Unit = ─────────────────────────
                    Total Units
```

### 💵 Contribution

```text
Contribution = Revenue − Operating Cost
```

### 📈 Contribution Margin

```text
                         Contribution
Contribution Margin = ──────────────── × 100
                           Revenue
```

### 👷 Labour Productivity

```text
                    Total Units
Units / Labour Hr = ─────────────
                    Labour Hours
```

---

# 🛠️ TECH STACK

<div align="center">

<img src="https://skillicons.dev/icons?i=python,postgresql,git,github,vscode" />

<br><br>

<img src="https://img.shields.io/badge/Excel-Data%20Modeling-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white"/>
<img src="https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black"/>
<img src="https://img.shields.io/badge/Pandas-EDA-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/NumPy-Analysis-013243?style=for-the-badge&logo=numpy&logoColor=white"/>

</div>

---

# 🔄 DATA ANALYTICS PIPELINE

```mermaid
flowchart LR

A["📦 Raw<br/>Warehouse Data"]
--> B["🧹 Data<br/>Cleaning"]

B --> C["🔍 Exploratory<br/>Analysis"]

C --> D["📊 KPI<br/>Engineering"]

D --> E["💰 Cost<br/>Analysis"]

D --> F["👷 Labour<br/>Productivity"]

D --> G["💵 Revenue &<br/>Contribution"]

E --> H["📈 Power BI<br/>Dashboard"]
F --> H
G --> H

H --> I["💡 Business<br/>Insights"]
```

---

# 🗂️ PROJECT ARCHITECTURE

```text
📦 Warehouse-Cost-Capacity-Analysis
│
├── 📁 data
│   └── 📄 warehouse_orders.csv
│
├── 📁 excel
│   └── 📊 cost_model.xlsx
│
├── 📁 python
│   └── 🐍 warehouse_analysis.py
│
├── 📁 sql
│   └── 🗄️ business_queries.sql
│
├── 📁 powerbi
│   └── 📈 dashboard_setup.md
│
├── 📁 screenshots
│   ├── 📊 workload.png
│   ├── 💰 cost_analysis.png
│   └── 📈 dashboard.png
│
└── 📄 README.md
```

---

# 🧹 STEP 01 — DATA PREPARATION

The simulated order-level dataset is prepared for analysis through:

```text
Raw Data
   ↓
Missing Value Check
   ↓
Duplicate Check
   ↓
Data Type Validation
   ↓
Outlier / Consistency Checks
   ↓
Feature Preparation
   ↓
Analysis Ready Dataset
```

---

# 🔍 STEP 02 — EXPLORATORY DATA ANALYSIS

Using **Python, Pandas, NumPy, Matplotlib and Seaborn**, the analysis explores:

📦 Order volume
📦 Unit volume
🏷️ Product categories
🏭 Warehouse zones
👷 Labour hours
💰 Operating cost
💵 Revenue
📈 Contribution

The objective is to identify patterns that can support operational and commercial analysis.

---

# 💰 STEP 03 — COST ANALYSIS

Warehouse operating costs are analyzed through two major categories:

### 🏢 Fixed / Allocated Costs

Costs that generally remain relatively stable within a relevant operating range.

Examples:

* Facility-related costs
* Allocated overhead
* Fixed operational expenses

### ⚙️ Variable Costs

Costs that change with operational activity.

Examples:

* Labour
* Handling
* Order-related operating costs

```text
FIXED COST
     +
VARIABLE COST
     ↓
OPERATING COST
     ↓
COST / ORDER
     ↓
COST / UNIT
```

---

# 👷 STEP 04 — PRODUCTIVITY ANALYSIS

Labour productivity is analyzed using:

### `Units per Labour Hour`

```text
              Units Processed
Productivity = ───────────────
               Labour Hours
```

The metric can be compared across warehouse zones to understand differences in workload handling and labour utilization.

---

# 📦 STEP 05 — CAPACITY ANALYSIS

Capacity analysis connects:

```text
Orders
  +
Units
  +
Labour Hours
  +
Handling Time
       ↓
Workload Requirement
       ↓
Capacity Planning
       ↓
Manpower Planning
```

This provides a framework for understanding how operational workload can translate into resource requirements.

---

# 💵 STEP 06 — COMMERCIAL ANALYSIS

Operational analysis is connected with commercial metrics:

```text
             REVENUE
                │
                ▼
        ┌───────────────┐
        │    OPERATING  │
        │      COST     │
        └───────┬───────┘
                │
                ▼
          CONTRIBUTION
                │
                ▼
       CONTRIBUTION MARGIN
```

This helps connect **warehouse operations with business performance**.

---

# 📊 POWER BI DASHBOARD

The dashboard is designed around four major analytical areas:

<div align="center">

### 📦 WORKLOAD

**Orders • Units • Zone Volume**

⬇️

### 💰 COST

**Operating Cost • Cost/Order • Cost/Unit**

⬇️

### 👷 PRODUCTIVITY

**Labour Hours • Units/Labour Hour**

⬇️

### 💵 COMMERCIAL

**Revenue • Contribution • Margin %**

</div>

---

# 🧠 BUSINESS INSIGHT FRAMEWORK

```text
                     DATA
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       WORKLOAD      COST     PRODUCTIVITY
          │           │           │
          └───────────┼───────────┘
                      ▼
                CAPACITY
                  PLANNING
                      │
                      ▼
              COMMERCIAL
               ANALYSIS
                      │
                      ▼
             BUSINESS INSIGHTS
```

---

# 🎤 INTERVIEW READY

### ❓ Why did you build this project?

> I wanted to create a practical analytics project where operational data could be connected to cost, productivity, capacity and commercial metrics. Instead of focusing only on visualization, I wanted to understand how warehouse KPIs can support operational decision-making.

### ❓ Why Cost per Order?

> Cost per order measures the average operating cost associated with processing an order. It provides a useful normalized view when comparing operational performance.

### ❓ Why Cost per Unit?

> Cost per unit normalizes operating cost against the number of units processed, which helps understand cost relative to physical workload.

### ❓ How did you measure productivity?

> I used Units per Labour Hour, calculated by dividing total processed units by total labour hours, and compared the metric across warehouse zones.

### ❓ How can this support manpower planning?

> Workload and labour-hour patterns can help estimate the labour requirement associated with different activity levels. In a real environment, historical productivity and handling-time data could be used to build more detailed workforce planning models.

### ❓ What are the limitations?

> The dataset is simulated and therefore the results should not be interpreted as actual warehouse performance. Cost allocations, labour assumptions and operational relationships are simplified for portfolio purposes.

---

# 🚀 FUTURE ENHANCEMENTS

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=2200&pause=700&color=7F00FF&center=true&vCenter=true&width=750&lines=Demand+Forecasting;Workforce+Planning;Capacity+Utilization;Scenario+Analysis;Machine+Learning;Automated+Power+BI+Refresh" />

Possible future extensions:

* 📅 Demand forecasting
* 👷 Workforce requirement prediction
* 📦 Capacity utilization modeling
* 💰 Scenario-based cost simulation
* 🤖 ML-based workload forecasting
* 🔔 Automated KPI alerts
* 📊 What-if analysis
* 🔄 Automated dashboard refresh

---

# ⚠️ DATA DISCLAIMER

> **All operational data used in this project is simulated for educational and portfolio purposes. It does not represent Edgistify or any real client's data.**

---

# 👩‍💻 SHIVANI RAJ

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=2500&pause=1000&color=00C6FF&center=true&vCenter=true&width=600&lines=Aspiring+Data+Analyst;Python+%7C+SQL+%7C+Excel+%7C+Power+BI;Turning+Data+into+Insights" />

<br><br>

<a href="mailto:shivaniraj4976@gmail.com">
<img src="https://img.shields.io/badge/Email-shivaniraj4976%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/>
</a>

<a href="YOUR_LINKEDIN_URL">
<img src="https://img.shields.io/badge/LinkedIn-Shivani%20Raj-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

<a href="YOUR_GITHUB_URL">
<img src="https://img.shields.io/badge/GitHub-Shivani%20Raj-181717?style=for-the-badge&logo=github&logoColor=white"/>
</a>

<br><br>

⭐ **Star this repository if you found it useful!**

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7F00FF,50:0072FF,100:00C6FF&height=160&section=footer&animation=fadeIn"/>

### 📊 DATA → INSIGHTS → DECISIONS

**Built with Python • SQL • Excel • Power BI**

</div>
