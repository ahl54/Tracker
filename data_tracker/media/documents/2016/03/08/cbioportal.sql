-- MySQL dump 10.13  Distrib 5.6.29, for Linux (x86_64)
--
-- Host: localhost    Database: cbioportal
-- ------------------------------------------------------
-- Server version	5.6.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attribute_metadata`
--

DROP TABLE IF EXISTS `attribute_metadata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attribute_metadata` (
  `ATTR_ID` varchar(255) NOT NULL,
  `DISPLAY_NAME` varchar(255) NOT NULL,
  `DESCRIPTION` varchar(2048) NOT NULL,
  `DATATYPE` varchar(255) NOT NULL,
  `TYPE` varchar(255) NOT NULL,
  PRIMARY KEY (`ATTR_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COMMENT='DATATYPE can be NUMBER, BOOLEAN, STRING';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `authorities`
--

DROP TABLE IF EXISTS `authorities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authorities` (
  `EMAIL` varchar(128) NOT NULL,
  `AUTHORITY` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cancer_study`
--

DROP TABLE IF EXISTS `cancer_study`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cancer_study` (
  `CANCER_STUDY_ID` int(11) NOT NULL AUTO_INCREMENT,
  `CANCER_STUDY_IDENTIFIER` varchar(255) DEFAULT NULL,
  `TYPE_OF_CANCER_ID` varchar(25) NOT NULL,
  `NAME` varchar(255) NOT NULL,
  `SHORT_NAME` varchar(64) NOT NULL,
  `DESCRIPTION` varchar(1024) NOT NULL,
  `PUBLIC` tinyint(1) NOT NULL,
  `PMID` varchar(20) DEFAULT NULL,
  `CITATION` varchar(200) DEFAULT NULL,
  `GROUPS` varchar(200) DEFAULT NULL,
  `LINK_TO_HARVEST` tinyint(1) NOT NULL DEFAULT '0',
  `NORMALS_TISSUE_MAPPING` binary(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`CANCER_STUDY_ID`),
  UNIQUE KEY `CANCER_STUDY_IDENTIFIER` (`CANCER_STUDY_IDENTIFIER`),
  KEY `TYPE_OF_CANCER_ID` (`TYPE_OF_CANCER_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=229 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clinical_attribute`
--

DROP TABLE IF EXISTS `clinical_attribute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clinical_attribute` (
  `ATTR_ID` varchar(255) NOT NULL,
  `DISPLAY_NAME` varchar(255) NOT NULL,
  `DESCRIPTION` varchar(2048) NOT NULL,
  `DATATYPE` varchar(255) NOT NULL,
  `PATIENT_ATTRIBUTE` tinyint(1) NOT NULL,
  `PRIORITY` varchar(255) NOT NULL,
  PRIMARY KEY (`ATTR_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COMMENT='DATATYPE can be NUMBER, BOOLEAN, STRING';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clinical_event`
--

DROP TABLE IF EXISTS `clinical_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clinical_event` (
  `CLINICAL_EVENT_ID` int(11) NOT NULL AUTO_INCREMENT,
  `PATIENT_ID` int(11) NOT NULL,
  `START_DATE` int(11) NOT NULL,
  `STOP_DATE` int(11) DEFAULT NULL,
  `EVENT_TYPE` varchar(20) NOT NULL,
  PRIMARY KEY (`CLINICAL_EVENT_ID`),
  KEY `PATIENT_ID` (`PATIENT_ID`,`EVENT_TYPE`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clinical_event_data`
--

DROP TABLE IF EXISTS `clinical_event_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clinical_event_data` (
  `CLINICAL_EVENT_ID` int(255) NOT NULL,
  `KEY` varchar(255) NOT NULL,
  `VALUE` varchar(5000) NOT NULL,
  KEY `CLINICAL_EVENT_ID` (`CLINICAL_EVENT_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clinical_patient`
--

DROP TABLE IF EXISTS `clinical_patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clinical_patient` (
  `INTERNAL_ID` int(11) NOT NULL,
  `ATTR_ID` varchar(255) NOT NULL,
  `ATTR_VALUE` varchar(255) NOT NULL,
  PRIMARY KEY (`INTERNAL_ID`,`ATTR_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clinical_sample`
--

DROP TABLE IF EXISTS `clinical_sample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clinical_sample` (
  `INTERNAL_ID` int(11) NOT NULL,
  `ATTR_ID` varchar(255) NOT NULL,
  `ATTR_VALUE` varchar(255) NOT NULL,
  PRIMARY KEY (`INTERNAL_ID`,`ATTR_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clinical_trial_keywords`
--

DROP TABLE IF EXISTS `clinical_trial_keywords`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clinical_trial_keywords` (
  `PROTOCOLID` char(50) NOT NULL,
  `KEYWORD` varchar(256) NOT NULL DEFAULT '',
  PRIMARY KEY (`PROTOCOLID`,`KEYWORD`),
  KEY `KEYWORD` (`KEYWORD`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clinical_trials`
--

DROP TABLE IF EXISTS `clinical_trials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clinical_trials` (
  `PROTOCOLID` char(50) NOT NULL,
  `SECONDARYID` char(50) NOT NULL,
  `TITLE` varchar(512) DEFAULT NULL,
  `PHASE` char(128) DEFAULT NULL,
  `LOCATION` varchar(256) DEFAULT NULL,
  `STATUS` char(50) DEFAULT NULL,
  PRIMARY KEY (`PROTOCOLID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cna_event`
--

DROP TABLE IF EXISTS `cna_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cna_event` (
  `CNA_EVENT_ID` int(255) NOT NULL AUTO_INCREMENT,
  `ENTREZ_GENE_ID` bigint(20) NOT NULL,
  `ALTERATION` tinyint(4) NOT NULL,
  PRIMARY KEY (`CNA_EVENT_ID`),
  UNIQUE KEY `ENTREZ_GENE_ID` (`ENTREZ_GENE_ID`,`ALTERATION`)
) ENGINE=MyISAM AUTO_INCREMENT=58665 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `copy_number_seg`
--

DROP TABLE IF EXISTS `copy_number_seg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `copy_number_seg` (
  `SEG_ID` int(255) NOT NULL AUTO_INCREMENT,
  `CANCER_STUDY_ID` int(11) NOT NULL,
  `SAMPLE_ID` int(11) NOT NULL,
  `CHR` varchar(5) NOT NULL,
  `START` int(11) NOT NULL,
  `END` int(11) NOT NULL,
  `NUM_PROBES` int(11) NOT NULL,
  `SEGMENT_MEAN` double NOT NULL,
  PRIMARY KEY (`SEG_ID`),
  KEY `CANCER_STUDY_ID` (`CANCER_STUDY_ID`,`SAMPLE_ID`),
  KEY `SAMPLE_ID` (`SAMPLE_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=5218492 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `copy_number_seg_file`
--

DROP TABLE IF EXISTS `copy_number_seg_file`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `copy_number_seg_file` (
  `SEG_FILE_ID` int(11) NOT NULL AUTO_INCREMENT,
  `CANCER_STUDY_ID` int(11) NOT NULL,
  `REFERENCE_GENOME_ID` varchar(10) NOT NULL,
  `DESCRIPTION` varchar(255) NOT NULL,
  `FILENAME` varchar(255) NOT NULL,
  PRIMARY KEY (`SEG_FILE_ID`),
  KEY `CANCER_STUDY_ID` (`CANCER_STUDY_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cosmic_mutation`
--

DROP TABLE IF EXISTS `cosmic_mutation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cosmic_mutation` (
  `COSMIC_MUTATION_ID` varchar(30) NOT NULL,
  `CHR` varchar(5) DEFAULT NULL,
  `START_POSITION` bigint(20) DEFAULT NULL,
  `REFERENCE_ALLELE` varchar(255) DEFAULT NULL,
  `TUMOR_SEQ_ALLELE` varchar(255) DEFAULT NULL,
  `STRAND` varchar(2) DEFAULT NULL,
  `CODON_CHANGE` varchar(255) DEFAULT NULL,
  `ENTREZ_GENE_ID` int(255) NOT NULL,
  `PROTEIN_CHANGE` varchar(255) NOT NULL,
  `COUNT` int(11) NOT NULL,
  `KEYWORD` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`COSMIC_MUTATION_ID`),
  KEY `KEYWORD` (`KEYWORD`),
  KEY `ENTREZ_GENE_ID` (`ENTREZ_GENE_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `drug`
--

DROP TABLE IF EXISTS `drug`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `drug` (
  `DRUG_ID` char(30) NOT NULL,
  `DRUG_RESOURCE` varchar(255) NOT NULL,
  `DRUG_NAME` varchar(255) NOT NULL,
  `DRUG_SYNONYMS` varchar(4096) DEFAULT NULL,
  `DRUG_DESCRIPTION` varchar(4096) DEFAULT NULL,
  `DRUG_XREF` varchar(4096) DEFAULT NULL,
  `DRUG_ATC_CODE` varchar(1024) DEFAULT NULL,
  `DRUG_APPROVED` int(1) DEFAULT '0',
  `DRUG_CANCERDRUG` int(1) DEFAULT '0',
  `DRUG_NUTRACEUTICAL` int(1) DEFAULT '0',
  `DRUG_NUMOFTRIALS` int(11) DEFAULT '-1',
  PRIMARY KEY (`DRUG_ID`),
  KEY `DRUG_NAME` (`DRUG_NAME`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `drug_interaction`
--

DROP TABLE IF EXISTS `drug_interaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `drug_interaction` (
  `DRUG` char(30) NOT NULL,
  `TARGET` bigint(20) NOT NULL,
  `INTERACTION_TYPE` char(50) NOT NULL,
  `DATA_SOURCE` varchar(256) NOT NULL,
  `EXPERIMENT_TYPES` varchar(1024) DEFAULT NULL,
  `PMIDS` varchar(1024) DEFAULT NULL,
  KEY `DRUG` (`DRUG`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `entity`
--

DROP TABLE IF EXISTS `entity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `entity` (
  `INTERNAL_ID` int(11) NOT NULL AUTO_INCREMENT,
  `STABLE_ID` varchar(50) NOT NULL,
  `ENTITY_TYPE` varchar(50) NOT NULL,
  PRIMARY KEY (`INTERNAL_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COMMENT='ENTITY_TYPE can be STUDY, PATIENT, SAMPLE';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `entity_attribute`
--

DROP TABLE IF EXISTS `entity_attribute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `entity_attribute` (
  `ENTITY_ID` int(11) NOT NULL,
  `ATTR_ID` varchar(255) NOT NULL,
  `ATTR_VALUE` varchar(255) NOT NULL,
  PRIMARY KEY (`ENTITY_ID`,`ATTR_ID`),
  KEY `ATTR_ID` (`ATTR_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `entity_link`
--

DROP TABLE IF EXISTS `entity_link`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `entity_link` (
  `INTERNAL_ID` int(11) NOT NULL AUTO_INCREMENT,
  `PARENT_ID` int(11) NOT NULL,
  `CHILD_ID` int(11) NOT NULL,
  PRIMARY KEY (`INTERNAL_ID`),
  KEY `PARENT_ID` (`PARENT_ID`),
  KEY `CHILD_ID` (`CHILD_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gene`
--

DROP TABLE IF EXISTS `gene`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gene` (
  `ENTREZ_GENE_ID` int(255) NOT NULL,
  `HUGO_GENE_SYMBOL` varchar(255) NOT NULL,
  `TYPE` varchar(50) DEFAULT NULL,
  `CYTOBAND` varchar(50) DEFAULT NULL,
  `LENGTH` int(11) DEFAULT NULL,
  PRIMARY KEY (`ENTREZ_GENE_ID`),
  KEY `HUGO_GENE_SYMBOL` (`HUGO_GENE_SYMBOL`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gene_alias`
--

DROP TABLE IF EXISTS `gene_alias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gene_alias` (
  `ENTREZ_GENE_ID` int(255) NOT NULL,
  `GENE_ALIAS` varchar(255) NOT NULL,
  PRIMARY KEY (`ENTREZ_GENE_ID`,`GENE_ALIAS`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `genetic_alteration`
--

DROP TABLE IF EXISTS `genetic_alteration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `genetic_alteration` (
  `GENETIC_PROFILE_ID` int(11) NOT NULL,
  `ENTREZ_GENE_ID` int(255) NOT NULL,
  `VALUES` longtext NOT NULL,
  KEY `QUICK_LOOK_UP` (`ENTREZ_GENE_ID`),
  KEY `QUICK_LOOK_UP2` (`ENTREZ_GENE_ID`,`GENETIC_PROFILE_ID`),
  KEY `GENETIC_PROFILE_ID` (`GENETIC_PROFILE_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `genetic_profile`
--

DROP TABLE IF EXISTS `genetic_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `genetic_profile` (
  `GENETIC_PROFILE_ID` int(11) NOT NULL AUTO_INCREMENT,
  `STABLE_ID` varchar(255) NOT NULL,
  `CANCER_STUDY_ID` int(11) NOT NULL,
  `GENETIC_ALTERATION_TYPE` varchar(255) NOT NULL,
  `DATATYPE` varchar(255) NOT NULL,
  `NAME` varchar(255) NOT NULL,
  `DESCRIPTION` mediumtext,
  `SHOW_PROFILE_IN_ANALYSIS_TAB` binary(1) NOT NULL,
  `NORMALS_MAPPING_ID` int(11) NOT NULL DEFAULT '-1',
  PRIMARY KEY (`GENETIC_PROFILE_ID`),
  UNIQUE KEY `STABLE_ID` (`STABLE_ID`),
  KEY `CANCER_STUDY_ID` (`CANCER_STUDY_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=788 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `genetic_profile_samples`
--

DROP TABLE IF EXISTS `genetic_profile_samples`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `genetic_profile_samples` (
  `GENETIC_PROFILE_ID` int(11) NOT NULL,
  `ORDERED_SAMPLE_LIST` longtext NOT NULL,
  UNIQUE KEY `GENETIC_PROFILE_ID` (`GENETIC_PROFILE_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gistic`
--

DROP TABLE IF EXISTS `gistic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gistic` (
  `GISTIC_ROI_ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `CANCER_STUDY_ID` int(11) NOT NULL,
  `CHROMOSOME` int(11) NOT NULL,
  `CYTOBAND` varchar(255) NOT NULL,
  `WIDE_PEAK_START` int(11) NOT NULL,
  `WIDE_PEAK_END` int(11) NOT NULL,
  `Q_VALUE` double NOT NULL,
  `AMP` tinyint(1) NOT NULL,
  PRIMARY KEY (`GISTIC_ROI_ID`),
  KEY `CANCER_STUDY_ID` (`CANCER_STUDY_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=2030 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gistic_to_gene`
--

DROP TABLE IF EXISTS `gistic_to_gene`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gistic_to_gene` (
  `GISTIC_ROI_ID` bigint(20) NOT NULL,
  `ENTREZ_GENE_ID` bigint(20) NOT NULL,
  PRIMARY KEY (`GISTIC_ROI_ID`,`ENTREZ_GENE_ID`),
  KEY `ENTREZ_GENE_ID` (`ENTREZ_GENE_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `interaction`
--

DROP TABLE IF EXISTS `interaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `interaction` (
  `GENE_A` bigint(20) NOT NULL,
  `GENE_B` bigint(20) NOT NULL,
  `INTERACTION_TYPE` varchar(256) NOT NULL,
  `DATA_SOURCE` varchar(256) NOT NULL,
  `EXPERIMENT_TYPES` varchar(1024) NOT NULL,
  `PMIDS` varchar(1024) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `micro_rna`
--

DROP TABLE IF EXISTS `micro_rna`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `micro_rna` (
  `ID` varchar(50) NOT NULL,
  `VARIANT_ID` varchar(50) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `micro_rna_alteration`
--

DROP TABLE IF EXISTS `micro_rna_alteration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `micro_rna_alteration` (
  `GENETIC_PROFILE_ID` int(11) NOT NULL,
  `MICRO_RNA_ID` varchar(50) NOT NULL,
  `VALUES` longtext NOT NULL,
  UNIQUE KEY `QUICK_LOOK_UP1` (`GENETIC_PROFILE_ID`,`MICRO_RNA_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `mut_sig`
--

DROP TABLE IF EXISTS `mut_sig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mut_sig` (
  `CANCER_STUDY_ID` int(11) NOT NULL,
  `ENTREZ_GENE_ID` bigint(20) NOT NULL,
  `RANK` int(11) NOT NULL,
  `NumBasesCovered` int(11) NOT NULL,
  `NumMutations` int(11) NOT NULL,
  `P_VALUE` float NOT NULL,
  `Q_VALUE` float NOT NULL,
  PRIMARY KEY (`CANCER_STUDY_ID`,`ENTREZ_GENE_ID`),
  KEY `ENTREZ_GENE_ID` (`ENTREZ_GENE_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `mutation`
--

DROP TABLE IF EXISTS `mutation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mutation` (
  `MUTATION_EVENT_ID` int(255) NOT NULL,
  `GENETIC_PROFILE_ID` int(11) NOT NULL,
  `SAMPLE_ID` int(11) NOT NULL,
  `ENTREZ_GENE_ID` int(255) NOT NULL,
  `CENTER` varchar(100) DEFAULT NULL,
  `SEQUENCER` varchar(255) DEFAULT NULL,
  `MUTATION_STATUS` varchar(25) DEFAULT NULL COMMENT 'Germline, Somatic or LOH.',
  `VALIDATION_STATUS` varchar(25) DEFAULT NULL,
  `TUMOR_SEQ_ALLELE1` varchar(255) DEFAULT NULL,
  `TUMOR_SEQ_ALLELE2` varchar(255) DEFAULT NULL,
  `MATCHED_NORM_SAMPLE_BARCODE` varchar(255) DEFAULT NULL,
  `MATCH_NORM_SEQ_ALLELE1` varchar(255) DEFAULT NULL,
  `MATCH_NORM_SEQ_ALLELE2` varchar(255) DEFAULT NULL,
  `TUMOR_VALIDATION_ALLELE1` varchar(255) DEFAULT NULL,
  `TUMOR_VALIDATION_ALLELE2` varchar(255) DEFAULT NULL,
  `MATCH_NORM_VALIDATION_ALLELE1` varchar(255) DEFAULT NULL,
  `MATCH_NORM_VALIDATION_ALLELE2` varchar(255) DEFAULT NULL,
  `VERIFICATION_STATUS` varchar(10) DEFAULT NULL,
  `SEQUENCING_PHASE` varchar(100) DEFAULT NULL,
  `SEQUENCE_SOURCE` varchar(255) NOT NULL,
  `VALIDATION_METHOD` varchar(255) DEFAULT NULL,
  `SCORE` varchar(100) DEFAULT NULL,
  `BAM_FILE` varchar(255) DEFAULT NULL,
  `TUMOR_ALT_COUNT` int(11) DEFAULT NULL,
  `TUMOR_REF_COUNT` int(11) DEFAULT NULL,
  `NORMAL_ALT_COUNT` int(11) DEFAULT NULL,
  `NORMAL_REF_COUNT` int(11) DEFAULT NULL,
  `AMINO_ACID_CHANGE` varchar(255) DEFAULT NULL,
  KEY `GENETIC_PROFILE_ID` (`GENETIC_PROFILE_ID`,`ENTREZ_GENE_ID`),
  KEY `GENETIC_PROFILE_ID_2` (`GENETIC_PROFILE_ID`,`SAMPLE_ID`),
  KEY `GENETIC_PROFILE_ID_3` (`GENETIC_PROFILE_ID`),
  KEY `ENTREZ_GENE_ID` (`ENTREZ_GENE_ID`),
  KEY `SAMPLE_ID` (`SAMPLE_ID`),
  KEY `MUTATION_EVENT_ID` (`MUTATION_EVENT_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COMMENT='Mutation Data Details';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `mutation_count`
--

DROP TABLE IF EXISTS `mutation_count`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mutation_count` (
  `GENETIC_PROFILE_ID` int(11) NOT NULL,
  `SAMPLE_ID` int(11) NOT NULL,
  `MUTATION_COUNT` int(11) NOT NULL,
  KEY `GENETIC_PROFILE_ID` (`GENETIC_PROFILE_ID`,`SAMPLE_ID`),
  KEY `SAMPLE_ID` (`SAMPLE_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `mutation_event`
--

DROP TABLE IF EXISTS `mutation_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mutation_event` (
  `MUTATION_EVENT_ID` int(255) NOT NULL AUTO_INCREMENT,
  `ENTREZ_GENE_ID` int(255) NOT NULL,
  `CHR` varchar(5) DEFAULT NULL,
  `START_POSITION` bigint(20) DEFAULT NULL,
  `END_POSITION` bigint(20) DEFAULT NULL,
  `REFERENCE_ALLELE` varchar(255) DEFAULT NULL,
  `TUMOR_SEQ_ALLELE` varchar(255) DEFAULT NULL,
  `PROTEIN_CHANGE` varchar(255) DEFAULT NULL,
  `MUTATION_TYPE` varchar(255) DEFAULT NULL COMMENT 'e.g. Missense, Nonsence, etc.',
  `FUNCTIONAL_IMPACT_SCORE` varchar(50) DEFAULT NULL COMMENT 'Result from OMA/XVAR.',
  `FIS_VALUE` float DEFAULT NULL,
  `LINK_XVAR` varchar(500) DEFAULT NULL COMMENT 'Link to OMA/XVAR Landing Page for the specific mutation.',
  `LINK_PDB` varchar(500) DEFAULT NULL,
  `LINK_MSA` varchar(500) DEFAULT NULL,
  `NCBI_BUILD` varchar(10) DEFAULT NULL,
  `STRAND` varchar(2) DEFAULT NULL,
  `VARIANT_TYPE` varchar(15) DEFAULT NULL,
  `DB_SNP_RS` varchar(25) DEFAULT NULL,
  `DB_SNP_VAL_STATUS` varchar(255) DEFAULT NULL,
  `ONCOTATOR_DBSNP_RS` varchar(255) DEFAULT NULL,
  `ONCOTATOR_REFSEQ_MRNA_ID` varchar(64) DEFAULT NULL,
  `ONCOTATOR_CODON_CHANGE` varchar(255) DEFAULT NULL,
  `ONCOTATOR_UNIPROT_ENTRY_NAME` varchar(64) DEFAULT NULL,
  `ONCOTATOR_UNIPROT_ACCESSION` varchar(64) DEFAULT NULL,
  `ONCOTATOR_PROTEIN_POS_START` int(11) DEFAULT NULL,
  `ONCOTATOR_PROTEIN_POS_END` int(11) DEFAULT NULL,
  `CANONICAL_TRANSCRIPT` tinyint(1) DEFAULT NULL,
  `KEYWORD` varchar(50) DEFAULT NULL COMMENT 'e.g. truncating, V200 Missense, E338del, ',
  PRIMARY KEY (`MUTATION_EVENT_ID`),
  UNIQUE KEY `CHR` (`CHR`,`START_POSITION`,`END_POSITION`,`TUMOR_SEQ_ALLELE`,`ENTREZ_GENE_ID`,`PROTEIN_CHANGE`,`MUTATION_TYPE`),
  KEY `KEYWORD` (`KEYWORD`),
  KEY `ENTREZ_GENE_ID` (`ENTREZ_GENE_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=1599309 DEFAULT CHARSET=latin1 COMMENT='Mutation Data';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `mutation_frequency`
--

DROP TABLE IF EXISTS `mutation_frequency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mutation_frequency` (
  `ENTREZ_GENE_ID` int(11) NOT NULL,
  `SOMATIC_MUTATION_RATE` double NOT NULL,
  `CANCER_STUDY_ID` int(11) NOT NULL,
  KEY `CANCER_STUDY_ID` (`CANCER_STUDY_ID`),
  KEY `ENTREZ_GENE_ID` (`ENTREZ_GENE_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `normals_sample_data`
--

DROP TABLE IF EXISTS `normals_sample_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `normals_sample_data` (
  `NORMALS_MAPPING_ID` int(11) NOT NULL,
  `HUGO_GENE_SYMBOL` varchar(255) NOT NULL,
  `VALUES` longtext NOT NULL,
  KEY `QUICK_LOOK_UP` (`NORMALS_MAPPING_ID`,`HUGO_GENE_SYMBOL`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `normals_sample_list`
--

DROP TABLE IF EXISTS `normals_sample_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `normals_sample_list` (
  `NORMALS_MAPPING_ID` int(11) NOT NULL AUTO_INCREMENT,
  `TECHNOLOGY_NAME` varchar(50) NOT NULL,
  `ORDERED_SAMPLE_LIST` longtext NOT NULL,
  PRIMARY KEY (`NORMALS_MAPPING_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `normals_sample_mapping`
--

DROP TABLE IF EXISTS `normals_sample_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `normals_sample_mapping` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `NORMALS_MAPPING_ID` int(11) NOT NULL,
  `TISSUE` varchar(255) NOT NULL DEFAULT '',
  `SAMPLES` longtext NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=153 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patient` (
  `INTERNAL_ID` int(11) NOT NULL AUTO_INCREMENT,
  `STABLE_ID` varchar(50) NOT NULL,
  `CANCER_STUDY_ID` int(11) NOT NULL,
  PRIMARY KEY (`INTERNAL_ID`),
  KEY `CANCER_STUDY_ID` (`CANCER_STUDY_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=32070 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `patient_list`
--

DROP TABLE IF EXISTS `patient_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patient_list` (
  `LIST_ID` int(11) NOT NULL AUTO_INCREMENT,
  `STABLE_ID` varchar(255) NOT NULL,
  `CATEGORY` varchar(255) NOT NULL,
  `CANCER_STUDY_ID` int(11) NOT NULL,
  `NAME` varchar(255) NOT NULL,
  `DESCRIPTION` mediumtext,
  PRIMARY KEY (`LIST_ID`),
  UNIQUE KEY `STABLE_ID` (`STABLE_ID`),
  KEY `CANCER_STUDY_ID` (`CANCER_STUDY_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=950 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `patient_list_list`
--

DROP TABLE IF EXISTS `patient_list_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patient_list_list` (
  `LIST_ID` int(11) NOT NULL,
  `PATIENT_ID` int(11) NOT NULL,
  PRIMARY KEY (`LIST_ID`,`PATIENT_ID`),
  KEY `PATIENT_ID` (`PATIENT_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pdb_uniprot_alignment`
--

DROP TABLE IF EXISTS `pdb_uniprot_alignment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pdb_uniprot_alignment` (
  `ALIGNMENT_ID` int(11) NOT NULL,
  `PDB_ID` char(4) NOT NULL,
  `CHAIN` char(1) NOT NULL,
  `UNIPROT_ID` varchar(50) NOT NULL,
  `PDB_FROM` varchar(10) NOT NULL,
  `PDB_TO` varchar(10) NOT NULL,
  `UNIPROT_FROM` int(11) NOT NULL,
  `UNIPROT_TO` int(11) NOT NULL,
  `EVALUE` float DEFAULT NULL,
  `IDENTITY` float DEFAULT NULL,
  `IDENTP` float DEFAULT NULL,
  `UNIPROT_ALIGN` text,
  `PDB_ALIGN` text,
  `MIDLINE_ALIGN` text,
  PRIMARY KEY (`ALIGNMENT_ID`),
  KEY `UNIPROT_ID` (`UNIPROT_ID`),
  KEY `PDB_ID` (`PDB_ID`,`CHAIN`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pdb_uniprot_residue_mapping`
--

DROP TABLE IF EXISTS `pdb_uniprot_residue_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pdb_uniprot_residue_mapping` (
  `ALIGNMENT_ID` int(11) NOT NULL,
  `PDB_POSITION` int(11) NOT NULL,
  `PDB_INSERTION_CODE` char(1) DEFAULT NULL,
  `UNIPROT_POSITION` int(11) NOT NULL,
  `MATCH` char(1) DEFAULT NULL,
  KEY `ALIGNMENT_ID` (`ALIGNMENT_ID`,`UNIPROT_POSITION`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pfam_graphics`
--

DROP TABLE IF EXISTS `pfam_graphics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pfam_graphics` (
  `UNIPROT_ACC` varchar(255) NOT NULL,
  `JSON_DATA` longtext NOT NULL,
  PRIMARY KEY (`UNIPROT_ACC`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `protein_array_cancer_study`
--

DROP TABLE IF EXISTS `protein_array_cancer_study`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `protein_array_cancer_study` (
  `PROTEIN_ARRAY_ID` varchar(50) NOT NULL,
  `CANCER_STUDY_ID` int(11) NOT NULL,
  PRIMARY KEY (`PROTEIN_ARRAY_ID`,`CANCER_STUDY_ID`),
  KEY `CANCER_STUDY_ID` (`CANCER_STUDY_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `protein_array_data`
--

DROP TABLE IF EXISTS `protein_array_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `protein_array_data` (
  `PROTEIN_ARRAY_ID` varchar(50) NOT NULL,
  `CANCER_STUDY_ID` int(11) NOT NULL,
  `SAMPLE_ID` int(11) NOT NULL,
  `ABUNDANCE` double NOT NULL,
  PRIMARY KEY (`PROTEIN_ARRAY_ID`,`CANCER_STUDY_ID`,`SAMPLE_ID`),
  KEY `CANCER_STUDY_ID` (`CANCER_STUDY_ID`),
  KEY `SAMPLE_ID` (`SAMPLE_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `protein_array_info`
--

DROP TABLE IF EXISTS `protein_array_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `protein_array_info` (
  `PROTEIN_ARRAY_ID` varchar(50) NOT NULL,
  `TYPE` varchar(50) NOT NULL,
  `GENE_SYMBOL` varchar(50) NOT NULL,
  `TARGET_RESIDUE` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`PROTEIN_ARRAY_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `protein_array_target`
--

DROP TABLE IF EXISTS `protein_array_target`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `protein_array_target` (
  `PROTEIN_ARRAY_ID` varchar(50) NOT NULL,
  `ENTREZ_GENE_ID` int(255) NOT NULL,
  PRIMARY KEY (`PROTEIN_ARRAY_ID`,`ENTREZ_GENE_ID`),
  KEY `ENTREZ_GENE_ID` (`ENTREZ_GENE_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sample`
--

DROP TABLE IF EXISTS `sample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample` (
  `INTERNAL_ID` int(11) NOT NULL AUTO_INCREMENT,
  `STABLE_ID` varchar(50) NOT NULL,
  `SAMPLE_TYPE` varchar(255) NOT NULL,
  `PATIENT_ID` int(11) NOT NULL,
  `TYPE_OF_CANCER_ID` varchar(25) NOT NULL,
  PRIMARY KEY (`INTERNAL_ID`),
  KEY `PATIENT_ID` (`PATIENT_ID`),
  KEY `TYPE_OF_CANCER_ID` (`TYPE_OF_CANCER_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=32308 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sample_cna_event`
--

DROP TABLE IF EXISTS `sample_cna_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample_cna_event` (
  `CNA_EVENT_ID` int(255) NOT NULL,
  `SAMPLE_ID` int(11) NOT NULL,
  `GENETIC_PROFILE_ID` int(11) NOT NULL,
  PRIMARY KEY (`CNA_EVENT_ID`,`SAMPLE_ID`,`GENETIC_PROFILE_ID`),
  KEY `GENETIC_PROFILE_ID` (`GENETIC_PROFILE_ID`,`SAMPLE_ID`),
  KEY `SAMPLE_ID` (`SAMPLE_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sample_pathology_report`
--

DROP TABLE IF EXISTS `sample_pathology_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample_pathology_report` (
  `STABLE_ID` varchar(50) NOT NULL,
  `LINK` varchar(1000) NOT NULL,
  UNIQUE KEY `STABLE_ID` (`STABLE_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sample_profile`
--

DROP TABLE IF EXISTS `sample_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample_profile` (
  `SAMPLE_ID` int(11) NOT NULL,
  `GENETIC_PROFILE_ID` int(11) NOT NULL,
  KEY `GENETIC_PROFILE_ID` (`GENETIC_PROFILE_ID`),
  KEY `SAMPLE_ID` (`SAMPLE_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sanger_cancer_census`
--

DROP TABLE IF EXISTS `sanger_cancer_census`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sanger_cancer_census` (
  `ENTREZ_GENE_ID` bigint(20) NOT NULL,
  `CANCER_SOMATIC_MUT` tinyint(1) NOT NULL,
  `CANCER_GERMLINE_MUT` tinyint(1) NOT NULL,
  `TUMOR_TYPES_SOMATIC_MUT` text NOT NULL,
  `TUMOR_TYPES_GERMLINE_MUT` text NOT NULL,
  `CANCER_SYNDROME` text NOT NULL,
  `TISSUE_TYPE` text NOT NULL,
  `MUTATION_TYPE` text NOT NULL,
  `TRANSLOCATION_PARTNER` text NOT NULL,
  `OTHER_GERMLINE_MUT` tinyint(1) NOT NULL,
  `OTHER_DISEASE` text NOT NULL,
  KEY `ENTREZ_GENE_ID` (`ENTREZ_GENE_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COMMENT='Sanger Cancer Gene Census';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `technology_mapping`
--

DROP TABLE IF EXISTS `technology_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `technology_mapping` (
  `CANCER_STUDY_ID` varchar(255) NOT NULL,
  `TECHNOLOGY` varchar(50) NOT NULL,
  `SAMPLES` longtext NOT NULL,
  KEY `QUICK_LOOK_UP` (`CANCER_STUDY_ID`,`TECHNOLOGY`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `text_cache`
--

DROP TABLE IF EXISTS `text_cache`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `text_cache` (
  `HASH_KEY` varchar(32) NOT NULL,
  `TEXT` longtext NOT NULL,
  `DATE_TIME_STAMP` datetime NOT NULL,
  PRIMARY KEY (`HASH_KEY`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tumor_sample_data`
--

DROP TABLE IF EXISTS `tumor_sample_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tumor_sample_data` (
  `TECHNOLOGY` varchar(50) NOT NULL,
  `CANCER_STUDY_ID` varchar(255) NOT NULL,
  `HUGO_GENE_SYMBOL` varchar(255) NOT NULL,
  `VALUES` longtext NOT NULL,
  KEY `QUICK_LOOK_UP` (`CANCER_STUDY_ID`,`HUGO_GENE_SYMBOL`,`TECHNOLOGY`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `type_of_cancer`
--

DROP TABLE IF EXISTS `type_of_cancer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `type_of_cancer` (
  `TYPE_OF_CANCER_ID` varchar(63) NOT NULL,
  `NAME` varchar(255) NOT NULL,
  `CLINICAL_TRIAL_KEYWORDS` varchar(1024) NOT NULL,
  `DEDICATED_COLOR` char(31) NOT NULL,
  `SHORT_NAME` varchar(127) DEFAULT NULL,
  `PARENT` varchar(63) DEFAULT NULL,
  PRIMARY KEY (`TYPE_OF_CANCER_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `uniprot_id_mapping`
--

DROP TABLE IF EXISTS `uniprot_id_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `uniprot_id_mapping` (
  `UNIPROT_ACC` varchar(255) NOT NULL,
  `UNIPROT_ID` varchar(255) NOT NULL,
  `ENTREZ_GENE_ID` int(255) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ENTREZ_GENE_ID`,`UNIPROT_ID`),
  KEY `UNIPROT_ID` (`UNIPROT_ID`),
  KEY `UNIPROT_ACC` (`UNIPROT_ACC`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `EMAIL` varchar(128) NOT NULL,
  `NAME` varchar(255) NOT NULL,
  `ENABLED` tinyint(1) NOT NULL,
  PRIMARY KEY (`EMAIL`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-03-07 11:15:49
