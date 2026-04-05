# Assignment 6: Agile User Stories, Backlog, and Sprint Planning (PRASA System)

## 1. User Stories

  -------------------------------------------------------------------------
  Story ID      User Story       Acceptance Criteria          Priority
  ------------- ---------------- ---------------------------- -------------
  US-001        As a Control     Alerts displayed within 1--2 High
                Room Operator, I seconds                      
                want to view                                  
                real-time alerts                              
                so that I can                                 
                respond quickly                               
                to incidents                                  

  US-002        As a Control     Abnormal vibration triggers  High
                Room Operator, I alert                        
                want to monitor                               
                track vibrations                              
                so that I can                                 
                detect potential                              
                faults early                                  

  US-003        As a Security    Intrusion alerts generated   High
                Officer, I want  instantly                    
                to detect                                     
                intrusions so                                 
                that I can                                    
                secure railway                                
                infrastructure                                

  US-004        As a Maintenance Alerts triggered based on    High
                Technician, I    thresholds                   
                want to receive                               
                maintenance                                   
                alerts so that I                              
                can repair                                    
                faults before                                 
                failure                                       

  US-005        As a PRASA       Reports generated in ≤5      Medium
                Supervisor, I    seconds                      
                want to view                                  
                system reports                                
                so that I can                                 
                make operational                              
                decisions                                     

  US-006        As a System      Login authentication         High
                Administrator, I required                     
                want to manage                                
                users so that                                 
                only authorized                               
                personnel access                              
                the system                                    

  US-007        As a System, I   Data processed with minimal  High
                want to process  delay                        
                IoT sensor data                               
                in real-time so                               
                that monitoring                               
                is accurate                                   

  US-008        As a System      AES-256 encryption applied   High
                Administrator, I                              
                want data to be                               
                encrypted so                                  
                that sensitive                                
                railway data is                               
                protected                                     

  US-009        As a Control     Notifications sent instantly High
                Room Operator, I                              
                want to receive                               
                failure                                       
                notifications so                              
                that I can take                               
                immediate action                              

  US-010        As a Supervisor, Logs stored and accessible   Medium
                I want to track                               
                incident history                              
                so that I can                                 
                analyze system                                
                performance                                   

  US-011        As a Maintenance System predicts failures     Medium
                Technician, I    based on trends              
                want predictive                               
                maintenance                                   
                insights so that                              
                I can prevent                                 
                breakdowns                                    

  US-012        As a User, I     Response time \< 2 seconds   High
                want the system                               
                to be fast and                                
                responsive so                                 
                that I can work                               
                efficiently                                   
  -------------------------------------------------------------------------

------------------------------------------------------------------------

## 2. Product Backlog

  Story ID   User Story                 Priority (MoSCoW)   Effort   Dependencies
  ---------- -------------------------- ------------------- -------- ------------------
  US-001     View real-time alerts      Must-have           5        IoT sensors
  US-002     Monitor track vibrations   Must-have           4        Sensors
  US-003     Detect intrusions          Must-have           4        Security sensors
  US-004     Maintenance alerts         Must-have           3        US-002
  US-006     Manage users               Must-have           3        None
  US-007     Process IoT data           Must-have           5        Sensors
  US-008     Data encryption            Must-have           3        None
  US-009     Failure notifications      Must-have           3        US-001
  US-005     View reports               Should-have         3        US-001
  US-012     Fast system response       Should-have         3        Optimization
  US-010     Incident history           Could-have          2        Database
  US-011     Predictive maintenance     Could-have          5        AI + data

### Justification

Must-have stories are prioritized because they directly support railway
safety, real-time monitoring, and rapid incident response. Should-have
features improve usability, while could-have features enhance
intelligence.

------------------------------------------------------------------------

## 3. Sprint Planning

### Sprint Goal

Develop core PRASA monitoring system with real-time alerts, intrusion
detection, and user authentication.

### Selected User Stories

US-001, US-002, US-003, US-006, US-009

### Sprint Backlog

  --------------------------------------------------------------------------
  Task ID    Task Description   Assigned To    Estimated Hours     Status
  ---------- ------------------ -------------- ------------------- ---------
  T-001      Design real-time   Frontend Dev   6                   To Do
             dashboard UI                                          

  T-002      Develop backend    Backend Dev    10                  To Do
             for real-time                                         
             alerts                                                

  T-003      Integrate IoT      Backend Dev    10                  To Do
             sensor data                                           

  T-004      Implement          Backend Dev    8                   To Do
             intrusion                                             
             detection logic                                       

  T-005      Develop user       Backend Dev    6                   To Do
             authentication                                        
             system                                                

  T-006      Create             Backend Dev    6                   To Do
             notification                                          
             system                                                

  T-007      Connect frontend   Full Stack Dev 8                   To Do
             to backend APIs                                       

  T-008      Testing and        QA Tester      8                   To Do
             debugging                                             
  --------------------------------------------------------------------------

### Sprint Goal Explanation

This sprint delivers core monitoring features forming a functional MVP
for railway safety and operations.

------------------------------------------------------------------------

## 4. Traceability

  Requirement ID   Description                   User Story ID
  ---------------- ----------------------------- ----------------
  FR-001           Display real-time dashboard   US-001
  FR-002           Generate real-time alerts     US-001, US-009
  FR-003           Detect intrusions             US-003
  FR-004           Monitor track vibrations      US-002
  FR-005           Manage users                  US-006
  FR-006           Generate reports              US-005

------------------------------------------------------------------------

## 5. Reflection

The process of applying Agile methodology presented challenges in
prioritization and estimation. As the sole stakeholder, balancing system
needs required critical evaluation. Estimating story points was
difficult due to varying complexity. Breaking tasks into manageable
units required careful planning. GitHub tools improved organization and
traceability. Overall, the assignment enhanced understanding of Agile
principles and project structuring.
