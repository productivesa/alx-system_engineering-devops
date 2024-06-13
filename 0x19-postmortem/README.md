0x19. Postmortem - Practice Exercise
On February 10th, 2023, from 9:30 PM to 4:45 AM (EAT),
our  web app experienced a complete outage.
The website became unresponsive, and users were unable to access the site during this time.
Impact:
The outage impacted all services provided by the website, including patient referral, Feedback functionality, and the report process. All users attempting to access the website were met with error messages or an unresponsive page. We estimate that approximately 100% of our users were affected by the outage.
Root Cause:
The root cause of the outage was a server failure in our virtual  web application server. The server crashes due to on and off electricity in the data center , resulting in the complete outage of the website.
Timeline:
- 9:30 PM — The issue was first detected by our liaison head, which sent out an alert to the head office team.
- 10:00 PM — The head office team attempted to check the issue
- 10:40 PM — The team began investigating the issue, assuming it was a problem with the server’s configuration.
- 11:00 PM — Further investigation revealed that the server’s crashs and the web server does not start.
- 12:00 AM — The team started recover the server to the working state
- 1:45 AM — The team identified the application crashes in the  began working on a fix.
- 2:30 AM — The team start to deployed the weapp to another virtual server the fix and restarted the web application server.
- 4:45 AM — The website was back online and fully operational.
Misleading Investigation/Debugging Paths:
The team initially assumed that the issue was related to the server’s configuration and spent valuable time investigating that angle. This delayed the identification of the actual root cause of the problem.
Incident Escalation:
The incident was initially handled by the development team, but they escalated it to the Devops team once they realized the issue was related to the server.
Resolution:
The crashed server was identified and fixed. The fix involved preparing other virtual server . The web application server was restarted after the fix was deployed, and the website was restored to full functionality.
Corrective and Preventative Measures:
To prevent similar issues in the future, we will implement the following corrective and preventative measures:
- Perform regular power checks and buys high capacity ups
- Implement more power monitoring tool
- Implement more robust monitoring of server performance and resource usage.
- Improve documentation and training for the devops team to better handle incidents like this in the future.
Specific tasks to address the issue include:
- Implement additional automated tests to server
-Monitor the system
- Provide additional training for devops team members on troubleshooting server crash issues.

