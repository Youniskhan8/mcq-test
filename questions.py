questions = [
    {
  "id": 1,
  "question": "What data types of Flow Designer variables are supported to store record data and complex data?",
  "type": "multiple",
  "options": [
    "Label data type",
    "Integer",
    "Array.Reference",
    "Choice",
    "String"
  ],
  "answer": [
    "Integer",
    "Choice",
    "String"
  ]
}
,
   {
  "id": 2,
  "question": "What are the features of Flow Designer? (Choose three.)",
  "type": "multiple",
  "options": [
    "Add stages to a flow",
    "Call a flow from another flow or subflow",
    "Test a flow using the \"Run as\" feature",
    "Support Java Scripting code to test conditions that trigger the flow",
    "Run a flow from a Catalog item",
    "Perform form field data validation at client side"
  ],
  "answer": [
    "Add stages to a flow",
    "Test a flow using the \"Run as\" feature",
    "Run a flow from a Catalog item"
  ]
}
,
{
  "id": 3,
  "question": "How is access to Application Menus and Modules controlled?",
  "type": "single",
  "options": [
    "Access Control",
    "Client Scripts",
    "Roles",
    "Application Rules"
  ],
  "answer": [
    "Roles"
  ]
}
,
{
  "id": 4,
  "question": "What is the ServiceNow App Repository?",
  "type": "single",
  "options": [
    "A Request table",
    "A database containing ServiceNow apps",
    "A collection of files in a Git database",
    "Another name for update sets"
  ],
  "answer": [
    "A database containing ServiceNow apps"
  ]
}
,
{
  "id": 5,
  "question": "What happens to the List view when a new field is added to an existing table?",
  "type": "single",
  "options": [
    "The new field is added at the start of the List",
    "The new field is added at the end of the List",
    "The new field is not added to the List view",
    "A List View is created with the new Field"
  ],
  "answer": [
    "The new field is not added to the List view"
  ]
},
{
  "id": 6,
  "question": "Exportitem table is extended from Item Table with the additional column of ItemCountry added. The Item table contains the columns ItemName and ItemQty. Which fields are available in the ExportItem Table?",
  "type": "single",
  "options": [
    "Only ItemCountry",
    "ItemName, ItemQty, and ItemCountry",
    "ItemCountry, Number",
    "Only ItemName, ItemQty"
  ],
  "answer": [
    "ItemName, ItemQty, and ItemCountry"
  ]
}
,
{
  "id": 7,
  "question": "What data types of Flow Variables are supported to store record data?(choose three)",
  "type": "multiple",
  "options": [
    "Choice",
    "Date",
    "Array",
    "Integer",
    "String"
  ],
  "answer": [
    "Date",
    "Integer",
    "String"
  ]
}
,{
  "id": 8,
  "question": "Which of the following objects does a Before Business Rule have access to in a script?",
  "type": "single",
  "options": [
    "current",
    "previous",
    "GlideRecord",
    "All of the above"
  ],
  "answer": [
    "All of the above"
  ]
}
,
{
  "id": 9,
  "question": "Which options are strategies for debugging client-side scripts? (Choose two.) ",
  "type": "multiple",
  "options": [
    "g_form.addInfoMessage()",
    "gs.addErrorMessage()",
    "gs.log()",
    "jslog()"
  ],
  "answer": [
    "g_form.addInfoMessage()",
    "jslog()"
  ]
}
,
{
  "id": 10,
  "question": "In a privately-scoped application, which methods are used for logging messages in server-side scripts? (Choose two.) ",
  "type": "multiple",
  "options": [
    "gs.logError()",
    "gs.log()",
    "gs.debug()",
    "gs.info()",
    "gs.error()"
  ],
  "answer": [
    "gs.debug()",
    "gs.info()"
  ]
}
,
{
  "id": 11,
  "question": "When creating an application through the Guided Application Creator, what are the options for creating a table? (Choose three.) ",
  "type": "multiple",
  "options": [
    "Run import jobs",
    "Use API calls",
    "Create a table from a template",
    "Create a table from scratch",
    "Link to external tables",
    "Extend a table",
    "Upload a spreadsheet"
  ],
  "answer": [
    "Create a table from scratch",
    "Extend a table",
    "Upload a spreadsheet"
  ]
}
,
{
  "id": 12,
  "question": "Which database operations can be controlled with Application Access? (Choose two.)",
  "type": "multiple",
  "options": [
    "Query",
    "Update",
    "Create",
    "Delete"
  ],
  "answer": [
    "Update",
    "Create"
  ]
}
,
{
  "id": 13,
  "question": "Which is an example of when an application might use a Scheduled Script Execution (Scheduled Job)?",
  "type": "single",
  "options": [
    "The application needs to run a client-side script at the same time every day.",
    " The application needs to query the database every day to look for unassigned records",
    "Display a custom welcome message when a user logs in",
    "Validate form input fields before record submission"
  ],
  "answer": [
    " The application needs to query the database every day to look for unassigned records"
  ]
}
,
{
  "id": 14,
  "question": "What field type would you select if you want to query records from another table on a form?",
  "type": "single",
  "options": [
    "Use the Date field type",
    "Use the Phone Number field type. ",
    "Use the String field type",
    "Use the Reference field type"
  ],
  "answer": [
    "Use the Reference field type"
  ]
}
,
{
  "id": 15,
  "question": "What functionality is supported by Flow Designer?",
  "type": "single",
  "options": [
    "The role flow_operator can create and edit flows",
    "Flows can be run as security admin",
    "Call a subflow from a flow",
    "Flows can trigger off record deletion"
  ],
  "answer": [
    "Call a subflow from a flow"
  ]
}
,
{
  "id": 16,
  "question": "What is a characteristic of Modules?",
  "type": "single",
  "options": [
    "Every Module must be associated with a table",
    "Access to Modules is not controlled with roles",
    "Every Module must be part of an Application Menu",
    "Modules cannot open forms or lists"
  ],
  "answer": [
    "Every Module must be part of an Application Menu"
  ]
}
,
{
  "id": 17,
  "question": "Which methods can be used to install an application on a ServiceNow instance?(Choose three.)",
  "type": "multiple",
  "options": [
    "Install from the Google Play Store",
    "Download from Stack Overflow",
    "Download and install a third-party application from the ServiceNow Store",
    "Use the Install button on the application record",
    "Install from the Application Repository",
    "Import an application from an XML file"
  ],
  "answer": [
    "Download and install a third-party application from the ServiceNow Store",
    "Install from the Application Repository",
    "Import an application from an XML file"
  ]
}
,
{
  "id": 18,
  "question": "Which one of the following is the correct Link Type to select when creating a module which opens the Record Producer UI for a user rather than the ServiceNow form UI?",
  "type": "single",
  "options": [
    "URL (from Arguments:)",
    "Content Page",
    "Script (from Arguments:)",
    "HTML (from Arguments:)"
  ],
  "answer": [
    "URL (from Arguments:)"
  ]
},
{
  "id": 19,
  "question": "What is the most common role that has access to almost all platform features, functions, and data?",
  "type": "single",
  "options": [
    "Security Admin [security_admin]",
    "Sys Admin [sys_admin]",
    "Admin [sn_admin]",
    "System Administrator [admin]",
    "Base Admin [base_admin]"
  ],
  "answer": [
    "System Administrator [admin]"
  ]
},
{
  "id": 20,
  "question": "Which items are valid UI Action types in ServiceNow?(Choose three.)",
  "type": "multiple",
  "options": [
    "List banner button",
    "Form button",
    "Record navigation button",
    "List choice",
    "Form choice",
    "Workflow action"
  ],
  "answer": [
    "List banner button",
    "Form button",
    "List choice"
  ]
}
,
{
  "id": 21,
  "question": "What occurs when an existing table is extended in ServiceNow?",
  "type": "single",
  "options": [
    "The parent table's Access Controls are ignored when determining access to the new table's records and field",
    "The new table does not inherit any of the fields from the parent table",
    "You must script and configure all required behaviors",
    "The new table inherits the functionality built into the parent table"
  ],
  "answer": [
    "The new table inherits the functionality built into the parent table"
  ]
}
,
{
  "id": 22,
  "question": "An application called My App has a table, MyAppTable, with this Application Access configuration: Accessible from: All application scopes Can read: Selected - Can delete: Not selected - Allow configuration: Selected - Which of the following is true based on this configuration",
  "type": "single",
  "options": [
    " An application developer working in another privately scoped application can write a Business Rule for the MyAppTable table which successfully deletes all records from the MyAppTable table ",
    "An application developer working in the My App scope can write a Business Rule for the MyAppTable table which successfully deletes all records from the MyAppTable table ",
    "Any Application developer can write a Business Rule which successfully deletes all records from the MyAppTable",
    "No Business Rule can delete records"
  ],
  "answer": [
    "An application developer working in the My App scope can write a Business Rule for the MyAppTable table which successfully deletes all records from the MyAppTable table "
  ]
}
,
{
  "id": 23,
  "question": "User records are stored in which table?",
  "type": "single",
  "options": [
    "User [sys_user]",
    "User [sn_user]",
    "User [u_sys_user]",
    "User [s_user]"
  ],
  "answer": [
    "User [sys_user]"
  ]
}
,
{
  "id": 24,
  "question": "How can Administrators expand the list of supported file types for code search in ServiceNow Studio?",
  "type": "single",
  "options": [
    "By Modify the default code search table",
    "By Configure metadata synchronization",
    "By Create a new code search group",
    "By Add new file types to a custom search group"
  ],
  "answer": [
    "By Add new file types to a custom search group"
  ]
}
,
{
  "id": 25,
  "question": "What happens if a record producer script aborts the record generation process in ServiceNow?",
  "type": "single",
  "options": [
    "Record creation displays an error message to the user",
    "Record is not generated in the Item Produced Record table",
    "Record creation is redirected to a confirmation page",
    "Record creation terminates without notifying the user"
  ],
  "answer": [
    "Record creation displays an error message to the user"
  ]
}

,
{
  "id": 26,
  "question": "What is a function of an update set in ServiceNow Studio?",
  "type": "single",
  "options": [
    "To track and monitor system performance metrics",
    "To create new custom applications",
    "To manage configurations directly in a production environment",
    "To group configuration changes for transfer between instances"
  ],
  "answer": [
    "To group configuration changes for transfer between instances"
  ]
}

,{
  "id": 27,
  "question": "How can an application respond to an Event triggered by the gs.eventQueue() method?(choose two)",
  "type": "multiple",
  "options": [
    "Client Script",
    "UI Policy",
    "Script Action",
    "Scheduled Script Execution",
    "Email Notification"
  ],
  "answer": [
    "Script Action",
    "Email Notification"
  ]
}
,
{
  "id": 28,
  "question": "What is a scoped application that contains Flow Designer actions tailored for a specific application or record type?",
  "type": "single",
  "options": [
    "Bundle",
    "Flow",
    "Spoke",
    "Action"
  ],
  "answer": [
    "Spoke"
  ]
}
,
{
  "id": 29,
  "question": "What is a reason for building a custom application?(choose two)",
  "type": "multiple",
  "options": [
    "Avoid using application repository",
    "Replace ServiceNow base tables",
    "Create a custom integration for a third-party system",
    "Fulfill a specific internal use case"
  ],
  "answer": [
    "Create a custom integration for a third-party system",
    "Fulfill a specific internal use case"
  ]
}
,
{
  "id": 30,
  "question": "What can a developer do with REST API Explorer?(choose two)",
  "type": "multiple",
  "options": [
    "Practice using REST to interact with public data providers",
    "Convert REST Message functions to REST methods",
    "Find resources on the web for learning about REST",
    "Create sample code for sending REST requests to ServiceNow",
    "Test API endpoints on ServiceNow"
  ],
  "answer": [
    "Create sample code for sending REST requests to ServiceNow",
    "Test API endpoints on ServiceNow"
  ]
}

,
{
  "id": 31,
  "question": "Which table stores the details of customizations included in an update set?",
  "type": "single",
  "options": [
    "Customer Update [sys_update_xml]",
    "System Properties [sys_properties]",
    "Application Registry [sys_app]",
    "Update Set [sys_update_set]"
  ],
  "answer": [
    "Customer Update [sys_update_xml]"
  ]
}
,
{
  "id": 32,
  "question": "What is the default module name when a new application table is created?",
  "type": "single",
  "options": [
    "X_ prefixed to the application name",
    "Plural form of the application name",
    "Same as application name",
    "U_ prefixed to the application name"
  ],
  "answer": [
    "Plural form of the application name"
  ]
},
{
  "id": 33,
  "question": "Which feature can be used to add instructions to a form?",
  "type": "single",
  "options": [
    "Context Menu UI Action",
    "Annotations",
    "Related links",
    "Read-only information field"
  ],
  "answer": [
    "Annotations"
  ]
},{
  "id": 34,
  "question": "What is displayed to delegated developers to package changes for deployment in ServiceNow Studio?",
  "type": "single",
  "options": [
    "Tools tab",
    "Export to XML",
    "Publish Button",
    "Update Set Picker"
  ],
  "answer": [
    "Update Set Picker"
  ]
}
,{
  "id": 36,
  "question": "Why are application files important?(choose two)",
  "type": "multiple",
  "options": [
    "They store user credentials for the application",
    "They define the app logic and behavior",
    "They restrict access to the application",
    "They monitor app performance metrics"
  ],
  "answer": [
    "They define the app logic and behavior",
    "They restrict access to the application"
  ]
}
,{
  "id": 37,
  "question": "What happens when an existing table is extended?(choose two)",
  "type": "multiple",
  "options": [
    "All required behavior must be newly scripted and configured from the new table",
    "Specific fields from the parent table can be selected to be inherited",
    "Parent table Access Controls are also evaluated while determining access for the new table",
    "The new table inherits the functionality built into the parent table",
    "The new table inherits all the fields from the parent table",
    "Dictionary entries for the new table also include records for fields from the parent table"
  ],
  "answer": [
    "Parent table Access Controls are also evaluated while determining access for the new table",
    "The new table inherits all the fields from the parent table"
  ]
}

,{
  "id": 38,
  "question": "When can the value \"Protected\" be leveraged in a Protected Policy for a Script Include?",
  "type": "single",
  "options": [
    "A user with the admin role enables the Policy option",
    "The glide.app.apply_protection system property is set to \"True\"",
    "The application is downloaded from the ServiceNow App Store",
    "A user with the protected_edit role edits the Script Include"
  ],
  "answer": [
    "The application is downloaded from the ServiceNow App Store"
  ]
}
,{
  "id": 39,
  "question": "When configuring a REST Message, what syntax indicates passing a variable during a function call?",
  "type": "single",
  "options": [
    "${variable_name}",
    "< variable_name >",
    "current.variable_name",
    "< variable_name >.do?WSDL"
  ],
  "answer": [
    "${variable_name}"
  ]
}

,{
  "id": 40,
  "question": "What does the \"Read-only\" protection policy for Script Includes allow in a custom application?",
  "type": "single",
  "options": [
    "Application developers can customize the Script Include",
    "Only administrators can delete the Script Include",
    "Application developers can view the script logic but not change it",
    "Only administrators can edit the Script Include"
  ],
  "answer": [
    "Application developers can view the script logic but not change it"
  ]
}

,{
  "id": 41,
  "question": "Which client-side scoped API class can be used as a replacement for GlideRecord?",
  "type": "single",
  "options": [
    "GlideElement",
    "GlideDialogWindow",
    "GlideAjax",
    "GlideForm"
  ],
  "answer": [
    "GlideAjax"
  ]
}
,{
  "id": 42,
  "question": "What Link type creates a module that opens a Record Producer UI instead of a Form UI?",
  "type": "single",
  "options": [
    "URL (from Arguments:)",
    "Content Page",
    "Script (from Arguments:)",
    "HTML (from Arguments:)"
  ],
  "answer": [
    "URL (from Arguments:)"
  ]
}
,{
  "id": 43,
  "question": "An app developer wants to review the scripts, reports, and other application artifacts included in a published app. What steps are taken to review those items?",
  "type": "single",
  "options": [
    "Enter the name of the Application in the Global search field",
    "Open the list of Update Sets for the instance",
    "Examine the Application Files Related List in the application to be published",
    "Open the artifact records individually to verify the value in the Application field"
  ],
  "answer": [
    "Examine the Application Files Related List in the application to be published"
  ]
}

,
{
  "id": 44,
  "question": "Which one of the following is true?",
  "type": "single",
  "options": [
    "A UI Policy's Actions execute before the UI Policy's Scripts",
    "The execution order for a UI Policy's Scripts and Actions is determined at runtime",
    "A UI Policy's Scripts execute before the UI Policy's Actions",
    "A UI Policy's Actions and Scripts execute at the same time"
  ],
  "answer": [
    "A UI Policy's Actions execute before the UI Policy's Scripts"
  ]
}

,

{
  "id": 45,
  "question": "It is best practice to define the business requirements and the process(es) an application will manage as part of the application development plan. What are some of the considerations to document as part of the business process?",
  "type": "single",
  "options": [
    "Business problem, data input/output, users/stakeholders, and process steps",
    "Business problem, data input/output, project schedule, and process steps",
    "Business problem, data input/output, users/stakeholders, and database capacity",
    "Business problem, users/stakeholders, available licenses, and database capacity"
  ],
  "answer": [
    "Business problem, data input/output, users/stakeholders, and process steps"
  ]
}

,
{
  "id": 46,
  "question": "When configuring an Access Control with no condition or script, which statement is NOT true?",
  "type": "single",
  "options": [
    "table.* grants access to every field in a record",
    "table.None grants access to every record on the table",
    "table.field grants access to a specific field in a record",
    "table.id grants access to a specific record on the table"
  ],
  "answer": [
    "table.id grants access to a specific record on the table"
  ]
}
,
{
  "id": 47,
  "question": "Which one of the following client-side scripts apply to Record Producers?",
  "type": "single",
  "options": [
    "Catalog Client Scripts and Catalog UI Policies",
    "UI Scripts and UI Actions",
    "UI Scripts and Record Producer Scripts",
    "Client Scripts and UI Policies"
  ],
  "answer": [
    "Catalog Client Scripts and Catalog UI Policies"
  ]
}

,
{
  "id": 48,
  "question": "Which script types execute on the server? (Choose three.)",
  "type": "multiple",
  "options": [
    "Business Rule",
    "Client Scripts",
    "UI Policies",
    "Script Actions",
    "Scheduled Jobs"
  ],
  "answer": [
    "Business Rule",
    "Script Actions",
    "Scheduled Jobs"
  ]
}
,{
  "id": 49,
  "question": "Which database operation cannot be controlled with Application Access?",
  "type": "single",
  "options": [
    "Query",
    "Update",
    "Create",
    "Delete"
  ],
  "answer": [
    "Query"
  ]
}
,{
  "id": 50,
  "question": "When the option 'Allow access to this table via web services' is selected, which statement is true?",
  "type": "single",
  "options": [
    "Delete is restricted but read is always allowed",
    "Users can access records even without permissions",
    "Only SOAP services are affected",
    "The user must have correct permissions to access records"
  ],
  "answer": [
    "The user must have correct permissions to access records"
  ]
}
,{
  "id": 51,
  "question": "Which of the following methods is NOT part of the ServiceNow REST API?",
  "type": "single",
  "options": [
    "COPY",
    "GET",
    "DELETE",
    "POST"
  ],
  "answer": [
    "COPY"
  ]
}
,{
  "id": 52,
  "question": "Which of the following statements is NOT true for the Form Designer?",
  "type": "single",
  "options": [
    "To add a section to the form layout, drag it from the Field Types tab to the desired destination on the form",
    "To add a field to the form layout, drag the field from the Fields tab to the desired destination on the form",
    "To remove a field from the form layout, hover over the field to enable the Action buttons, and select the Delete (X) button",
    "To create a new field on a form’s table, drag the appropriate data type from the Field Types tab to the form and then configure the new field"
  ],
  "answer": [
    "To add a section to the form layout, drag it from the Field Types tab to the desired destination on the form"
  ]
}

,{
  "id": 53,
  "question": "What records are used to track cross-scope applications or scripts that request access to an application, application resource, or event? ",
  "type": "single",
  "options": [
    "Restricted caller access records",
    "Caller tracking records",
    "Access control level records",
    "Cross-scope access records"
  ],
  "answer": [
    "Restricted caller access records"
  ]
},{
  "id": 54,
  "question": "Which ATF Test step allows you to create a user with specified roles and groups?",
  "type": "single",
  "options": [
    "Create a group",
    "Impersonation",
    "Create a user",
    "Create a role"
  ],
  "answer": [
    "Create a user"
  ]
},
{
  "id": 55,
  "question": "Why create Applications in ServiceNow? a) To replace outdated, inadequate, custom business applications and processes b) To extend service delivery and management to all enterprise departments c) To allow users full access to all ServiceNow tables, records, and fields d) To extend the value of ServiceNow  ",
  "type": "single",
  "options": [
    "a, b, and d",
    "a, b, c, and d",
    "a, b, and c",
    "b, c, and d"
  ],
  "answer": [
    "a, b, and d"
  ]
}


,{
  "id": 56,
  "question": "Client-side scripts manage what?",
  "type": "single",
  "options": [
    "User access",
    "Database and backend",
    "Playbook access",
    "Forms and Form Fields"
  ],
  "answer": [
    "Forms and Form Fields"
  ]
}
,{
  "id": 57,
  "question": "nce an application is ready to share, which of the following methods of publishing are supported by ServiceNow? (Choose three.)",
  "type": "multiple",
  "options": [
    "Publish to an application repository",
    "Publish to a local drive",
    "Publish to the ServiceNow Store",
    "Publish to an Update Set",
    "Publish to a spreadsheet",
    "Publish to a USB device"
  ],
  "answer": [
    "Publish to an application repository",
    "Publish to the ServiceNow Store",
    "Publish to an Update Set"
  ]
}
,{
  "id": 58,
  "question": "What is the Endpoint when configuring a REST Message?",
  "type": "single",
  "options": [
    "The URI of the web server",
    "A command to stop execution",
    "The URI of the data to be accessed or modified",
    "A provider response message"
  ],
  "answer": [
    "The URI of the data to be accessed or modified"
  ]
},{
  "id": 59,
  "question": "Which client-side scripts apply to Record Producers?",
  "type": "multiple",
  "options": [
    "Fix Scripts",
    "Catalog Client Scripts",
    "UI Scripts",
    "Catalog UI Policies",
    "Record Producer Policies"
  ],
  "answer": [
    "Catalog Client Scripts",
    "Catalog UI Policies"
  ]
}
,{
  "id": 60,
  "question": "Which business requirements and process(es) should be documented as part of the application development plan? (Choose four.) ",
  "type": "multiple",
  "options": [
    "Available licenses",
    "Business problem",
    "Process steps",
    "Users/stakeholders",
    "Database capacity",
    "Project schedule",
    "Data input/output"
  ],
  "answer": [
    "Business problem",
    "Process steps",
    "Users/stakeholders",
    "Data input/output"
  ]
} 





]
