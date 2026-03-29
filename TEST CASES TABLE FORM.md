# Test Cases (Functional + Non-Functional)

**Version:** 1.0

------------------------------------------------------------------------

## All Requirements and Test Cases (Table Format)

  --------------------------------------------------------------------------------------------------
  Category         ID          Description     Steps          Expected Result  Actual     Status
                                                                               Result     
  ---------------- ----------- --------------- -------------- ---------------- ---------- ----------
  Functional       FR-001      System shall                                               
  Requirement                  display a live                                             
                               operational                                                
                               dashboard                                                  

  Functional       FR-002      System shall                                               
  Requirement                  generate                                                   
                               real-time                                                  
                               alerts from IoT                                            
                               telemetry                                                  

  Functional       FR-003      System shall                                               
  Requirement                  allow                                                      
                               authorized                                                 
                               users to                                                   
                               acknowledge and                                            
                               assign alerts                                              

  Functional       FR-004      System shall                                               
  Requirement                  allow users to                                             
                               create incident                                            
                               reports                                                    

  Functional       FR-005      System shall                                               
  Requirement                  allow                                                      
                               dispatching                                                
                               maintenance                                                
                               work orders                                                

  Functional       FR-006      System shall                                               
  Requirement                  allow                                                      
                               technicians to                                             
                               update work                                                
                               order status                                               

  Functional       FR-007      System shall                                               
  Requirement                  broadcast                                                  
                               passenger                                                  
                               notifications                                              
                               via selected                                               
                               channels                                                   

  Functional       FR-008      System shall                                               
  Requirement                  generate                                                   
                               operational KPI                                            
                               reports                                                    

  Non-Functional   NFR-001     Dashboard and                                              
  Requirement                  alert views                                                
                               shall respond                                              
                               within 2                                                   
                               seconds under                                              
                               expected load                                              

  Non-Functional   NFR-002     Only authorized                                            
  Requirement                  roles shall                                                
                               access CCTV and                                            
                               sensitive                                                  
                               security logs                                              

  Test Case        TC-001      View live       Login → Open   Dashboard loads             
                   (FR-001)    dashboard       Dashboard →    with correct                
                               successfully    Filter         metrics                     

  Test Case        TC-002      Generate alert  Simulate       Alert created               
                   (FR-002)    from abnormal   threshold      with correct                
                               sensor reading  breach → Open  details                     
                                               Alerts                                     

  Test Case        TC-003      Acknowledge and Open alert →   Status updated              
                   (FR-003)    assign alert    Acknowledge →  and assignment              
                                               Assign         visible                     

  Test Case        TC-004      Create incident Enter required Incident created            
                   (FR-004)    report          fields →       with ID and log             
                                               Submit                                     

  Test Case        TC-005      Dispatch        Open alert →   Work order                  
                   (FR-005)    maintenance     Dispatch →     created and                 
                               work order      Assign         assigned                    

  Test Case        TC-006      Update work     Open order →   Status updated              
                   (FR-006)    order to        Update status  and notification            
                               resolved                       sent                        

  Test Case        TC-007      Broadcast       Create message Notification                
                   (FR-007)    passenger       → Select       published and               
                               notification    channel        logged                      

  Test Case        TC-008      Generate KPI    Select report  Report available            
                   (FR-008)    report          → Generate     for export                  

  Test Case        TC-009      Duplicate alert Send repeated  Alerts grouped              
                   (FR-002)    grouping        alerts         correctly                   

  Test Case        TC-010      Work order      Set status to  Block recorded              
                   (FR-006)    blocked         blocked        and escalation              
                               scenario                       triggered                   

  Test Case        TC-NF-001   Performance     Simulate       Response ≤ 2                
                   (NFR-001)   under load      concurrent     seconds                     
                                               users                                      

  Test Case        TC-NF-002   Role-based      Attempt        Access                      
                   (NFR-002)   access control  unauthorized   denied/logged;              
                                               access         authorized                  
                                                              allowed                     
  --------------------------------------------------------------------------------------------------
