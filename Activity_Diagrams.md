# Activity Diagrams

## View Real-Time Alerts

``` mermaid
flowchart TD
    A[Start] --> B[Receive Sensor Data]
    B --> C[Generate Alert]
    C --> D[Display Dashboard]
    D --> E[Operator Reviews]
    E --> F[End]
```

**Explanation:** US-001: Operator views alerts and FR5: Generate alerts.

## Monitor Train Movement

``` mermaid
flowchart TD
    A[Start] --> B[Collect GPS Data]
    B --> C[Update System]
    C --> D[Display Dashboard]
    D --> E[End]
```

**Explanation:** Supports FR1: Track train locations.

## Detect Intrusion

``` mermaid
flowchart TD
    A[Start] --> B[Sensor Detects Movement]
    B --> C{Intrusion?}
    C -- Yes --> D[Trigger Alert]
    C -- No --> E[Ignore]
    D --> F[Notify Security]
    F --> G[End]
```

**Explanation:** Supports US-003: Security notified.

## Maintenance Workflow

``` mermaid
flowchart TD
    A[Start] --> B[Detect Fault]
    B --> C[Create Request]
    C --> D[Assign Technician]
    D --> E[Repair]
    E --> F[Update Status]
    F --> G[End]
```

**Explanation:** Supports FR8: Manage maintenance and US-004: Technician updates tasks.

## User Login

``` mermaid
flowchart TD
    A[Start] --> B[Enter Credentials]
    B --> C{Valid?}
    C -- Yes --> D[Access Granted]
    C -- No --> E[Access Denied]
    D --> F[End]
    E --> F
```

**Explanation:** Supports FR9: Authenticate users and US-006: Secure login.

## Generate Reports

``` mermaid
flowchart TD
    A[Start] --> B[Collect Data]
    B --> C[Process Data]
    C --> D[Generate Report]
    D --> E[Display Report]
    E --> F[End]
```

**Explanation:** Supports FR7: Generate reports and US-005: Manager uses reports.

## Send Notification

``` mermaid
flowchart TD
    A[Start] --> B[Trigger Event]
    B --> C[Create Notification]
    C --> D[Send to User]
    D --> E[Delivered]
    E --> F[End]
```

**Explanation:** Supports FR3: Send notifications and US-009: Receive notifications.

## Incident Reporting

``` mermaid
flowchart TD
    A[Start] --> B[Create Incident]
    B --> C[Review Incident]
    C --> D{Valid?}
    D -- Yes --> E[Approve]
    D -- No --> F[Reject]
    E --> G[Close]
    F --> G
```

**Explanation:** Supports FR6: Manage incidents.
