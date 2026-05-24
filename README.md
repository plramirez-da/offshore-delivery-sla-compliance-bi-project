# Offshore Delivery & Operational SLA Compliance Intelligence Dashboard

## 📌 Executive Summary
This project delivers a comprehensive, 3-page enterprise business intelligence solution designed to audit operational efficiency, contractual SLA health, and QA software release quality for high-volume U.S. telecom accounts. By engineering a relational star-schema model representing 4,500 service desk tickets and 500 QA defects, the dashboard uncovers that our **global SLA Compliance Rate sits at 91.71%**, structurally capped below the 92.00% target due to an operational bottleneck where Omnichannel Support (Tier 1) resolution times spike to **3.6 hours on Critical incidents**. Additionally, a severe **37.20% global defect leakage rate** was isolated, heavily driven by custom Non-Salesforce Native Applications. Immediate next steps involve implementing an automated "Fast-Track" escalation trigger for critical tickets and enforcing a automated CI/CD testing gate for native applications, successfully protecting the account from contractual penalties and securing long-term service stability without expanding employee headcount.

## 🛠️ Skills & Tech Stack Demonstrated
* **Data Engineering & Automation:** Python (Pandas, NumPy) for programmatic data generation and simulation of realistic operational anomalies.
* **Data Modeling:** Star Schema Architecture, 1:Many directional filtering, active/inactive relationship management.
* **Advanced BI Analytics:** Time-Series Performance Trends, Multi-Category Cost & Volume Analysis, Statistical Performance Quadrants, Conditional Formatting.
* **UI/UX & Governance:** Reference Labels for dynamic KPI tracking, executive minimalist grids, and high-contrast color signaling.

## 📐 Methodology & Project Architecture
To extract actionable business intelligence, the project followed a robust technical pipeline:
1. **Data Engineering Phase:** A custom Python script was developed to generate 5,000 rows of relational operational data, purposefully injecting behavioral anomalies (such as resolution delays during peak priority spikes) to test the dashboard's diagnostic strength.
2. **Data Modeling Phase:** Built a high-performance Star Schema in Power BI Desktop, connecting fact tables to independent dimensions to optimize calculation paths and slicer performance.
3. **Analytical Design Phase:** Constructed an executive-level 3-page interactive report tracking three critical management perspectives: Contractual Health, Resource Productivity, and Software Quality.

---

## 💼 Business Problem
The offshore delivery organization lacks centralized, data-driven visibility into its technical support and quality assurance operations. Management is currently unable to systematically verify if the team of 50 distributed agents is meeting contractual Service Level Agreements (SLAs), how workload capacity is balanced across resources, or where software bugs are bypassing testing filters before hitting live production environments. 

Establishing this data infrastructure is critical to isolate localized workflow friction, prevent resource burnout, and identify specific software infrastructure risks. Delivering these insights allows the organization to protect enterprise client relationships, prevent costly financial SLA breach penalties, and optimize team performance without incurring unnecessary hiring costs.

---

## 🗂️ Data Dictionary & Relationship Structure

### 1. FACT_TICKETS (Service Desk Operations)
| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| **Ticket_ID** | String (PK) | Unique identifier for each service desk ticket. |
| **Date_Created** | DateTime | Timestamp when the ticket was logged by the system. |
| **Date_Closed** | DateTime | Timestamp when the ticket was marked as resolved. |
| **Agent_ID** | String (FK) | Unique identifier mapping to the resolving professional. |
| **Unit_ID** | String (FK) | Unique identifier mapping to the operational unit. |
| **Priority** | String | Severity level of the incident: *Low, Medium, High, Critical*. |
| **Resolution_Time_Hours** | Decimal | Total active hours spent to resolve the incident. |
| **SLA_Status** | String | Categorization of contractual compliance: *Within SLA* or *Out of SLA*. |
| **Platform** | String | Digital environment context: *Salesforce Core, Salesforce Flows, Non-Salesforce Native*. |

### 2. FACT_QA_BUGS (Software Quality Engineering)
| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| **Bug_ID** | String (PK) | Unique identifier for each logged defect. |
| **Date_Detected** | DateTime | Timestamp when the software bug was discovered. |
| **Environment** | String | Software environment deployment context: *UAT* or *Production*. |
| **Detected_By** | String | Testing logging source: *QA Team* (Internal) or *Client User* (External Leakage). |
| **Agent_ID** | String (FK) | Unique identifier of the QA professional managing the bug. |
| **Severity** | String | Business impact level of the defect: *Minor, Major, Critical*. |
| **Application_Platform** | String | Core architecture codebase: *Salesforce Flows* or *Non-Salesforce Native*. |

### 🔗 Model Relationship Map
The analytical model utilizes a optimized **Star Schema Diagram** where both core fact tables (`fact_tickets` and `fact_qa_bugs`) are linked to centralized dimensional tables (`dim_agents` and `dim_units`) via active **1:Many (*)** directional cross-filtering on `Agent_ID` and `Unit_ID`, ensuring extreme query performance and seamless cross-filtering across report pages.

<img width="728" height="709" alt="offshore-delivery-model-view" src="https://github.com/user-attachments/assets/104614ac-d0c7-496e-a615-a11a2395a630" />

---

## 🔍 Insights & Business Questions

<img width="1268" height="716" alt="sla-contract-compliance-dashboard" src="https://github.com/user-attachments/assets/3ed66763-d290-4a35-be7a-f0c4fe83fa7f" />

### 📊 Page 1: Contractual Health & Service Desk Efficiency
* **BQ1:** What is our global SLA Compliance Rate, and how has it trended month-over-month throughout the fiscal year?
* **BQ2:** Which specific operational units exhibit the highest volume of SLA breaches, dragging down overall contractual performance?
* **BQ3:** How does ticket priority (Low, Medium, High, Critical) impact the average resolution time across different operational units?

* **Consolidated Insight:** The operation displays an exceptionally stable month-over-month global SLA baseline, tightly fluctuating between **91.23% (February)** and **92.37% (March)**, proving robust resilience against workload volatility. However, the system is chronically capped below the **92.00% target** due to severe workflow friction localized within **Omnichannel Support (Tier 1)**, which drives the vast majority of contract breaches. Granular priority analysis reveals a critical operational inversion: while Tier 1 manages routine tickets efficiently, its Average Time to Resolve (ATTR) drastically spikes to **3.6 hours exclusively on Critical incidents**, completely breaking the contractual turnaround agreement for emergency outages.

<img width="1267" height="712" alt="resource-productivity-capacity-planning-dashboard" src="https://github.com/user-attachments/assets/d326086e-13eb-4cbb-952f-a3465409ad63" />

### 👥 Page 2: Resource Productivity & Capacity Planning
* **BQ4:** Is the ticket workload equitably distributed across the 50 agents, or are certain team members over-utilized while others remain idle?
* **BQ5:** When cross-referencing total tickets closed against Average Time to Resolve (ATTR), who are our high-velocity outliers and who requires targeted training?

* **Consolidated Insight:** The individual workload allocation framework is highly balanced and secure, with most resources clustering tightly around the corporate benchmark of **90 tickets closed per quarter**, effectively mitigating extreme burnout risks. When cross-referencing output volume against velocity on the performance quadrant chart, a distinct behavioral divide emerges: *Salesforce Flow Developers* and *QA Testing teams* occupy the high-efficiency quadrants (Low ATTR / High Volume), cementing themselves as operational anchors. Conversely, specific underperforming resources within the Omnichannel Support (Tier 1) unit drift deep into the lower-right quadrant (High ATTR / Low Volume), identifying localized training deficiencies or poorly documented legacy ticket assignments.

<img width="1272" height="706" alt="sw-realese-quality-defect-leakage-dashboard" src="https://github.com/user-attachments/assets/fa447c2b-f926-4173-87ec-4d7611a4ea60" />

### 🛡️ Page 3: Software Release Quality & Defect Leakage
* **BQ6:** What is our global Defect Leakage Rate, and what portion of software bugs are escaping UAT filters to impact production?
* **BQ7:** How does defect leakage vary across different technical application infrastructures, and what is the severity breakdown of live bugs?

* **Consolidated Insight:** The software deployment pipeline possesses a high global Defect Leakage Rate of **37.20%**, allowing **186 bugs to bypass UAT filters** and hit live production environments, significantly breaching the quality threshold of **<= 15.00%**. This technical vulnerability is heavily asymmetrical, highly concentrated within **Non-Salesforce Native Applications** which suffer from an alarming **50% individual leakage rate**, while *Salesforce Flows* remain exceptionally secure. Crucially, the diagnostic breakdown indicates that while leakage volume is high, the quality gates successfully capture the worst system-blocking failures, as the live production bugs are overwhelmingly dominated by *Minor* severity levels.

---

## 🚀 Results & Data-Driven Recommendations

1. **SLA Rescue Framework (Page 1 Fix):** Establish an automated "Fast-Track" escalation trigger between Tier 1 and Tier 2 for all *Critical* enterprise incidents. If a front-line Omnichannel agent cannot resolve a *Critical* ticket within a strict 30-minute window, the system must bypass manual triage and auto-route the case directly to *Enterprise App Support (Tier 2)*, successfully pulling the global contract back over the green 92.00% line.
2. **Resource Optimization & Mentoring (Page 2 Fix):** Instead of opening costly new requisitions, initiate a structured peer-mentoring framework. Pair the slow-velocity outliers identified in the Tier 1 quadrant with the high-velocity "Rockstars" from the QA and Flow development teams to cross-pollinate troubleshooting best practices and standardize documentation procedures.
3. **QA Guardrails & Deployment Gates (Page 3 Fix):** Immediately transition the *Non-Salesforce Native Application* pipeline from manual testing to a mandatory automated regression testing gate. Reallocate 20% of engineering capacity from the highly stable *Salesforce Flow* track to reinforce native code reviews during the UAT phase, successfully squeezing the leakage rate back toward the 15.00% safety threshold.
