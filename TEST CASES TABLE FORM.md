# Test Cases (Functional + Non-Functional)

**Version:** 1.0

------------------------------------------------------------------------

## Requirement IDs

### Functional Requirements (FR)

  -----------------------------------------------------------------------
  ID                                  Description
  ----------------------------------- -----------------------------------
  FR-001                              System shall display a live
                                      operational dashboard.

  FR-002                              System shall generate real-time
                                      alerts from IoT telemetry.

  FR-003                              System shall allow authorized users
                                      to acknowledge and assign alerts.

  FR-004                              System shall allow users to create
                                      incident reports.

  FR-005                              System shall allow dispatching
                                      maintenance work orders.

  FR-006                              System shall allow technicians to
                                      update work order status.

  FR-007                              System shall broadcast passenger
                                      notifications via selected
                                      channels.

  FR-008                              System shall generate operational
                                      KPI reports.
  -----------------------------------------------------------------------

### Non-Functional Requirements (NFR)

  -----------------------------------------------------------------------
  ID                                  Description
  ----------------------------------- -----------------------------------
  NFR-001                             Dashboard and alert views shall
                                      respond within 2 seconds under
                                      expected load.

  NFR-002                             Only authorized roles shall access
                                      CCTV and sensitive security logs.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Test Case Table

  ----------------------------------------------------------------------------------------------
  Test Case   Requirement   Description    Steps          Expected Result  Actual     Status
  ID          ID                                                           Result     
  ----------- ------------- -------------- -------------- ---------------- ---------- ----------
  TC-001      FR-001        View live      Login → Open   Dashboard loads             
                            dashboard      Dashboard →    with correct                
                            successfully   Filter         metrics                     

  TC-002      FR-002        Generate alert Simulate       Alert created               
                            from abnormal  threshold      with correct                
                            sensor reading breach → Open  details                     
                                           Alerts                                     

  TC-003      FR-003        Acknowledge    Open alert →   Status updated              
                            and assign     Acknowledge →  and assignment              
                            alert          Assign         visible                     

  TC-004      FR-004        Create         Enter required Incident created            
                            incident       fields →       with ID and log             
                            report         Submit                                     

  TC-005      FR-005        Dispatch       Open alert →   Work order                  
                            maintenance    Dispatch →     created and                 
                            work order     Assign         assigned                    

  TC-006      FR-006        Update work    Open order →   Status updated              
                            order to       Update status  and notification            
                            resolved                      sent                        

  TC-007      FR-007        Broadcast      Create message Notification                
                            passenger      → Select       published and               
                            notification   channel        logged                      

  TC-008      FR-008        Generate KPI   Select report  Report available            
                            report         → Generate     for export                  

  TC-009      FR-002        Duplicate      Send repeated  Alerts grouped              
                            alert grouping alerts         correctly                   

  TC-010      FR-006        Work order     Set status to  Block recorded              
                            blocked        blocked        and escalation              
                            scenario                      triggered                   

  TC-NF-001   NFR-001       Performance    Simulate       Response ≤ 2                
                            under load     concurrent     seconds                     
                                           users                                      

  TC-NF-002   NFR-002       Role-based     Attempt        Access                      
                            access control unauthorized   denied/logged;              
                                           access         authorized                  
                                                          allowed                     
  ----------------------------------------------------------------------------------------------
