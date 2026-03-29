Use Case Specifications (8)

Version: 1.0
System: PRASA Smart Digital Monitoring System for Operational Efficiency

---

### UC-01: View Live Dashboard
- **Primary Actor:** Operations Controller
- **Secondary Actors:** Station Manager, Passenger Info Officer
- **Description (Purpose/Scope):**
  Provide a real-time view of train operations, station status, and critical assets (signals, power, access points) through a single dashboard.
- **Preconditions:**
  1. Actor is authenticated.
  2. Actor has permission to view operational dashboards.
  3. System has telemetry available (real-time or last-known).
- **Postconditions:**
  1. Dashboard is displayed with latest available values.
  2. Access event is logged for auditing.
- **Basic Flow (Main Success Scenario):**
  1. Actor logs in.
  2. Actor navigates to **Dashboard**.
  3. System loads operational widgets (delays, faults, uptime, occupancy where applicable).
  4. Actor applies filters (line, station, time window).
  5. System refreshes and displays filtered results.
- **Alternative Flows / Exceptions:**
  - **A1: Telemetry delayed/unavailable**
    1. System displays a “Data delayed” notice with last update timestamp.
    2. System shows cached/last-known readings.
  - **A2: Unauthorized access**
    1. System denies access and shows an authorization error.

---

### UC-02: Receive Real-time Alerts
- **Primary Actor:** Operations Controller
- **Secondary Actors:** Maintenance Technician, Security Officer
- **Supporting Actor:** IoT Sensors (Train/Track/Station)
- **Description:**
  Detect anomalies from telemetry or events (faults, security breaches, service delays above threshold) and create alerts for action.
- **Preconditions:**
  1. Devices/sensors are registered and active.
  2. Alert rules and thresholds are configured.
- **Postconditions:**
  1. Alert is created with severity, category, timestamp, and location.
  2. Alert appears in the alert queue/dashboard.
  3. Notification is delivered to relevant roles (in-app).
- **Basic Flow:**
  1. IoT Sensors send telemetry/event data to the system.
  2. System validates and normalizes the data.
  3. System evaluates alert rules and thresholds.
  4. System creates an alert when a rule triggers.
  5. System displays the alert in the queue and notifies relevant users.
- **Alternative Flows / Exceptions:**
  - **A1: Duplicate/repeated events**
    - System groups duplicate alerts into a single alert thread and increments occurrence count.
  - **A2: Invalid payload**
    - System rejects the event, logs error details, and flags device health status.

---

### UC-03: Acknowledge/Assign Alert
- **Primary Actor:** Operations Controller
- **Description:**
  Confirm an alert is being handled and assign ownership to a team/role to ensure accountability and traceability.
- **Preconditions:**
  1. Alert exists in “New” state.
  2. Actor is authenticated and authorized to manage alerts.
- **Postconditions:**
  1. Alert status changes to “Acknowledged” (and optionally “Assigned”).
  2. Assignment, timestamps, and actor details are recorded.
- **Basic Flow:**
  1. Actor opens the alert queue.
  2. Actor selects an alert.
  3. System displays alert details (category, severity, location, history).
  4. Actor clicks **Acknowledge**.
  5. Actor selects an assignee group (Maintenance, Security, Station Ops) and submits.
  6. System updates alert status and records the assignment.
- **Alternative Flows / Exceptions:**
  - **A1: Alert already acknowledged**
    - System shows current owner; actor may reassign with a reason (if permitted).
  - **A2: No assignee available**
    - System allows acknowledgement without assignment and marks as “Needs assignment”.

---

### UC-04: Create Incident Report
- **Primary Actor:** Operations Controller
- **Secondary Actors:** Station Manager, Security Officer
- **Description:**
  Create a formal record of an operational/security/safety incident for auditing, investigation, and compliance.
- **Preconditions:**
  1. Actor is authenticated and authorized to create incidents.
  2. Incident categories/templates exist (optional).
- **Postconditions:**
  1. Incident report is stored with a unique incident ID.
  2. Incident is marked “Open” and can be tracked.
- **Basic Flow:**
  1. Actor selects **Create Incident**.
  2. System prompts for incident type, location, time, and description.
  3. Actor enters incident details and attaches references/evidence (alert reference, notes).
  4. Actor submits the incident report.
  5. System saves the incident and confirms the incident ID.
- **Alternative Flows / Exceptions:**
  - **A1: Missing mandatory fields**
    - System highlights missing fields and prevents submission.
  - **A2: Incident created from an alert**
    - System pre-fills fields from alert data and allows edits before saving.

---

### UC-05: Dispatch Maintenance
- **Primary Actor:** Operations Controller
- **Secondary Actor:** Maintenance Technician
- **Description:**
  Create and dispatch a work order to a maintenance team/technician to resolve a fault, including priority and SLA.
- **Preconditions:**
  1. Fault exists (from an alert or manually identified).
  2. Actor is authorized to dispatch work orders.
  3. Maintenance team roster is available.
- **Postconditions:**
  1. Work order is created and assigned.
  2. Work order status becomes “Dispatched”.
  3. Assigned technician/team is notified (in-app).
- **Basic Flow:**
  1. Actor opens a fault alert or fault record.
  2. Actor clicks **Dispatch Maintenance**.
  3. System prompts for priority, SLA/due time, required skills, and notes.
  4. Actor selects technician/team and submits.
  5. System creates the work order and assigns it.
- **Alternative Flows / Exceptions:**
  - **A1: No technician available**
    - System suggests next available team or schedules dispatch; status becomes “Pending dispatch”.
  - **A2: Incorrect alert category**
    - System warns if dispatch is attempted for a non-maintenance alert type.

---

### UC-06: Update Work Order Status
- **Primary Actor:** Maintenance Technician
- **Description:**
  Update the work order lifecycle (En Route, In Progress, Blocked, Resolved) and record actions and parts used.
- **Preconditions:**
  1. Technician is authenticated.
  2. Technician is assigned to the work order.
- **Postconditions:**
  1. Work order status and timestamps are updated.
  2. Resolution notes/actions are stored.
  3. Relevant stakeholders are notified (e.g., Operations Controller).
- **Basic Flow:**
  1. Technician opens assigned work order.
  2. Technician sets status to **En Route** or **In Progress**.
  3. Technician logs diagnostics/actions and parts used.
  4. Technician sets status to **Resolved** and submits resolution notes.
  5. System updates status, timestamps, and notifies Operations.
- **Alternative Flows / Exceptions:**
  - **A1: Work blocked**
    1. Technician sets status to **Blocked**.
    2. Technician selects a blocker reason (parts unavailable, access denied, safety risk).
    3. System notifies Operations for escalation.
  - **A2: Offline updates**
    - System stores updates locally and syncs once connectivity is restored.

---

### UC-07: Broadcast Passenger Notification
- **Primary Actor:** Passenger Info Officer
- **Secondary Actors:** Operations Controller, Station Manager
- **Description:**
  Publish passenger-facing updates (delays, platform changes, safety notices) via configured channels.
- **Preconditions:**
  1. Actor is authenticated and authorized to broadcast.
  2. Broadcast channels and templates exist (optional).
- **Postconditions:**
  1. Notification is published to selected channels.
  2. Broadcast is logged with author/time and scope (line/station).
- **Basic Flow:**
  1. Actor selects **Broadcast Notification**.
  2. System prompts for message type, affected line/station, and channels.
  3. Actor writes a message or selects a template.
  4. Actor previews and submits.
  5. System publishes and stores broadcast log entry.
- **Alternative Flows / Exceptions:**
  - **A1: Approval required**
    - System routes message for approval before publishing.
  - **A2: Channel failure**
    - System retries; if failure persists, system marks channel as failed and publishes to remaining channels.

---

### UC-08: Generate Operational Reports
- **Primary Actor:** Executive/Management
- **Secondary Actors:** Station Manager, Operations Controller
- **Description:**
  Generate KPI and operational reports (on-time performance, downtime, incident volume, MTTR, security events) for a chosen period and scope.
- **Preconditions:**
  1. Actor is authenticated and authorized to view reports.
  2. System has data available for selected time period.
- **Postconditions:**
  1. Report is generated and viewable/exportable (e.g., PDF/CSV).
  2. Report generation is logged.
- **Basic Flow:**
  1. Actor opens **Reports**.
  2. Actor selects report type and time period.
  3. Actor selects scope (line/station/region).
  4. System aggregates data and generates report.
  5. Actor views and exports the report.
- **Alternative Flows / Exceptions:**
  - **A1: Large dataset**
    - System generates a summarized report first and supports drill-down.
  - **A2: No data in period**
    - System displays “No data available for selected period” and suggests a valid range.


