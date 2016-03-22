
Naming Convention
******************

Data sets already in the cBioPortal (TCGA, etc..) will keep their original names. This will be kept in parity with any L1 data we have in S3 buckets. For new data sets the format will be as follows.

      “Source”_“Cancer Type”_“Sample Type”_“Sample ID”

Source: The consortium, group, or lab that generated the data i.e. Broad institute, Resnick Lab, TCGA etc… No spaces are to be used in the source name nor special characters. If it’s a consortium, abbreviation is used, if it is a lab or institute only the proper names are used.

Cancer Type: Abbreviation of type of cancer, full list of abbreviations found in document CavaticaDataSetNaming_Cancer_Abbrev.xlsx. If multiple cancers are part of study the term MIXED will be used.

Sample Type: cell line [CL], xenografts [XE], or patient [PA]

Sample ID: 01 if it is the first dataset of this name. If a second dataset comes from the same source, cancer type, and sample type, then avoid duplicating the name by incrementing the sample ID to 02.

Example Names and what they mean

      Resnick_MB_PA_01 - patient medulloblastoma samples from Resnick lab

      Broad_NB_CL_01 - cell line neuroblastoma samples from the Broad institute

      ICGC_MIXED_XE_01 - xenograft samples (of different origin) from ICGC


## Sub Folder

Subfolders (below the dataset folder) will hold samples profiled by a particular technology and platform. So for instance,  a particular dataset could be profiled by whole exome sequencing and whole transcriptome sequencing. The corresponding FASTQ files would be broken into 2 folders underneath the dataset folder corresponding to the platform (Whole exome sequencing FASTQ files in one folder, Whole transcriptome sequencing FASTQ files in another). The naming convention for these folders is as follows.


      “Technology”_“Vendor”


Technology: This is the platform by which the samples were run.

Vendor: This is the vendor used such as illumina, affymetrix etc.

Example Names and what they mean

      WES_ILLU – Whole Exome Sequencing by Illumina

      MEXP_AFFY – Microarray expression from Affymetrix
