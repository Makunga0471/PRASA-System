# State Transition Diagrams

## Train

``` mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> InService : Start Trip
    InService --> Delayed : Fault Detected
    Delayed --> Maintenance : Assign Technician
    Maintenance --> InService : Repair Complete
    InService --> Completed : Trip Ends
```

**Explanation:** Supports FR1: Track train movement status and FR5: Generate alerts on faults.

## Alert

``` mermaid
stateDiagram-v2
    [*] --> Generated
    Generated --> Displayed
    Displayed --> Acknowledged
    Acknowledged --> Resolved
```

**Explanation:** Supports FR5: Manage alerts lifecycle, US-001: Operator views alerts, 
US-009: User receives notifications

## Maintenance Request

``` mermaid
stateDiagram-v2
    [*] --> Created
    Created --> Assigned
    Assigned --> InProgress
    InProgress --> Completed
    Completed --> Closed
```

**Explanation:** Supports FR8: Manage maintenance lifecycle and US-004: Technician updates tasks.

## User Account

``` mermaid
stateDiagram-v2
    [*] --> Registered
    Registered --> Active
    Active --> Suspended
    Suspended --> Active
```

**Explanation:** Supports FR9: Authenticate users and US-006: Secure login.

## Incident Report

``` mermaid
stateDiagram-v2
    [*] --> Created
    Created --> Reviewed
    Reviewed --> Approved
    Approved --> Closed
```

**Explanation:** Supports FR6: Manage incidents.

## Notification

``` mermaid
stateDiagram-v2
    [*] --> Created
    Created --> Sent
    Sent --> Delivered
    Delivered --> Read
```

**Explanation:** Supports FR3: Send notifications and US-009: Receive notifications.

## Sensor Data

``` mermaid
stateDiagram-v2
    [*] --> Collected
    Collected --> Processed
    Processed --> Stored
    Stored --> Analyzed
```

**Explanation:** Supports FR1: Process sensor data and FR6: Analyze for incidents.

## System Log

``` mermaid
stateDiagram-v2
    [*] --> Recorded
    Recorded --> Stored
    Stored --> Accessed
    Accessed --> Archived
```

**Explanation:** Supports FR10: Manage logs.
