# Tracker

Tracker is a data request tool for submitting and viewing the status of cancer studies to include in cBioPortal for CBTTC https://github.research.chop.edu/CBTTC/cBioPortal.

## Version 1.01

### Added 2016 March 09
Tracker for each dataset has an additional progress step added: 

0 - Request received
1 - Data downloaded
2 - Data staged (tranformed into cBioPortal format)
3 - Uploaded to S3 Bucket
4 - Available in cBioPortal
5 - Available in Cavatica

The following fields were added to the Tracker model
'dataset_name'
'study_link'
'cbio_link'
's3_link'
'L1'
'confirmation'
'subscription'
'summary'

The field previously called 'sample_type' has been depreciated to 'specimen_type' which refers to tissue or blood. Sample type now refers to patient, xenograft, cell line, or germline.

Tracker page has a new style the color codes which datasets contain L1 data
Light green indicates L3 data
Darker green indicates L1 data
Blue indicates that the data is available in Cavatica

Tables are updated with small glyphicons that link to published studies and the data set in cBioPortal if it is available

Email subscriptions are available in requests. Each requester can choose to receive a confirmation email containing details of their dataset request. Subscriptions are also available for the requester to choose to receive emails once the dataset becomes available in cBioPortal and/or Cavatica, or receive emails at every step along the progress.

A User management system has been created so that requesters may register, login, and control dataset management panels for group access management, view their own requests in a private panel. Sharing private datasets may be enabled in future versions.

Automation backends have been added to automatically trigger files from download to staging to checkpoints and loading into cBioPortal. Automation progression to upload to AWS S3 and reflect changes in Tracker are in progress and will be made in the next version.

### Added 2015 December 31

Version 1.00

First release includes three views:
Tracker interface with four progress indicators for each study
Table of study requests with filtering and sorting
Summary statistics of tissue types, adult or pediatric, open or restricted access, and study detail types
