S3 Bucket folder structure
==============================

[[https://github.research.chop.edu/github-enterprise-assets/0000/0132/0000/0087/0adfddd4-eab4-11e5-9eeb-08fb4e4c60cb.png]]


## The folder tree for one example dataset:

     TCGA_MBL_PA_01
         data_mutations.txt
         meta_mutations.txt
         meta_study.txt
         case_lists
             cases_all.txt
             cases_mutations.txt

### Dataset Essentials
A dataset must contain a meta_study.txt. The meta_study.txt file has a field called cancer_study_identifier which cBioPortal uses to identify the study and its' associated meta files.

Warning: Each meta file must contain a field called stable_identifier which must begin with the cancer_study_identifier for it to be recognized.
