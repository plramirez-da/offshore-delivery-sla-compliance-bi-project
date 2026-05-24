
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Setting a fixed seed
np.random.seed(42)
num_tickets = 4500
num_bugs = 500

# 1. FACT_TICKETS (4,500 rows)
# Define which software platforms are supported by each operational unit (Unit_ID)
ticket_platforms = {
    'U01': ['Salesforce Core'], 
    'U02': ['Salesforce Core', 'Non-Salesforce Native'],
    'U03': ['Non-Salesforce Native'], 
    'U04': ['Salesforce Flows'], 
    'U05': ['Salesforce Flows', 'Non-Salesforce Native']
}

# Dynamically distribute 50 agents across the 5 operational units using modular arithmetic
agent_units = {
    f'A{i:02d}': f'U{(i-1)%5+1:02d}' for i in range(1, 51)
}

# Standard ITIL priorities and their realistic operational probability distribution
priorities = ['Low', 'Medium', 'High', 'Critical']
prob_priorities = [0.4, 0.35, 0.2, 0.05]


# Define the fiscal period starting baseline
start_date = datetime(2026, 1, 1)
ticket_data = []

for i in range(1, num_tickets + 1):
    t_id = f"T{1000 + i}"

# Generate random timestamp distributions across a 120-day quarter during business hours    
    days_to_add = np.random.randint(0, 120)
    hours_to_add = np.random.randint(8, 18)
    mins_to_add = np.random.randint(0, 60)
    c_date = start_date + timedelta(days=days_to_add, hours=hours_to_add, minutes=mins_to_add)

# Randomly assign an active agent and fetch their corresponding unit mapping
    agent_id = f"A{np.random.randint(1, 51):02d}"
    unit_id = agent_units[agent_id]
    priority = np.random.choice(priorities, p=prob_priorities)
    platform = np.random.choice(ticket_platforms[unit_id])

    # Injecting operational anomaly: Tier 1 (U02) experiences resolution bottlenecks 
    # specifically during High and Critical priority spikes to simulate escalation friction.
    if unit_id == 'U02' and priority in ['High', 'Critical']:
        res_hours = round(np.random.exponential(scale=3.5), 2)  
    else:
        res_hours = round(np.random.exponential(scale=1.5), 2)

# Standardized contractual SLA thresholds per operational unit (SLA Goals)    
    goals = {'U01': 4.0, 'U02': 2.0, 'U03': 24.0, 'U04': 48.0, 'U05': 12.0}
    sla_status = "Within SLA" if res_hours <= goals[unit_id] else "Out of SLA"

# Calculate closure timestamp based on the generated resolution time
    cl_date = c_date + timedelta(hours=res_hours)

# Append structured record to the dataset array
    ticket_data.append([t_id, c_date.strftime('%Y-%m-%d %H:%M:%S'), cl_date.strftime('%Y-%m-%d %H:%M:%S'), agent_id, unit_id, priority, res_hours, sla_status, platform])

# Convert array to a Pandas DataFrame and export directly to a structured CSV
df_tickets = pd.DataFrame(ticket_data, columns=['Ticket_ID', 'Date_Created', 'Date_Closed', 'Agent_ID', 'Unit_ID', 'Priority', 'Resolution_Time_Hours', 'SLA_Status', 'Platform'])
df_tickets.to_csv('fact_tickets.csv', index=False)

#FACT_QA_BUGS (500 rows)
bug_data = []
for i in range(1, num_bugs + 1):
    b_id = f"B{2000 + i}"
    days_to_add = np.random.randint(0, 120)
    b_date = start_date + timedelta(days=days_to_add, hours=np.random.randint(9, 17))

    # INJECTING QA DEFECT LEAKAGE ANOMALY:
    # Non-Salesforce Native apps suffer from loose testing structures
    # Salesforce Flows benefit from secure sandboxes
    platform = np.random.choice(['Salesforce Flows', 'Non-Salesforce Native'], p=[0.4, 0.6])
    if platform == 'Non-Salesforce Native':
        env = np.random.choice(['UAT', 'Production'], p=[0.55, 0.45]) # leaking 45% of bugs to Production.
    else:
        env = np.random.choice(['UAT', 'Production'], p=[0.85, 0.15]) # leaking only 15% of bugs to Production.

# Determine defect logging source based on environmental mapping
    detected_by = 'QA Team' if env == 'UAT' else 'Client User'

    # Enforce relational integrity: Filter and isolate agents belonging strictly to the QA Unit (U05)
    qa_agents = [f'A{i:02d}' for i in range(1, 51) if agent_units[f'A{i:02d}'] == 'U05']
    agent_id = np.random.choice(qa_agents)
    severity = np.random.choice(['Minor', 'Major', 'Critical'], p=[0.5, 0.3, 0.2])

# Append structured record to the defect array
    bug_data.append([b_id, b_date.strftime('%Y-%m-%d %H:%M:%S'), env, detected_by, agent_id, severity, platform])

# Convert defect array to a Pandas DataFrame and export directly to a structured CSV
df_bugs = pd.DataFrame(bug_data, columns=['Bug_ID', 'Date_Detected', 'Environment', 'Detected_By', 'Agent_ID', 'Severity', 'Application_Platform'])
df_bugs.to_csv('fact_qa_bugs.csv', index=False)

print("Files 'fact_tickets.csv' & 'fact_qa_bugs.csv' successfully generated!")