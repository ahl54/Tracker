TrackerID
===========

TrackerID is a field property associated with a tracker object.
It indicates where the dataset is currently located. A legend of locations is given below

=========  ========================
TrackerID  Location
=========  ========================
0          Dataset request received
1          Dataset downloaded
2          Dataset in staging area
3          Dataset in S3 Bucket
4          Dataset in cBioPortal
5          Dataset in Cavatica
=========  =========================

Developer's Note
================
A dataset may sit in both cBioPortal and Cavatica. In case of this situation,
we may add one more Tracker 6 to indicate that the dataset sits in both applications.
