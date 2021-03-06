-- use:  `cat data/insert_data_vo_noparams.sql | sqlite3 db.sqlite3`
DELETE FROM prov_vo_activity;
DELETE FROM prov_vo_activitydescription;
DELETE FROM prov_vo_entity;
DELETE FROM prov_vo_entitydescription;
DELETE FROM prov_vo_used;
DELETE FROM prov_vo_useddescription;
DELETE FROM prov_vo_wasgeneratedby;
DELETE FROM prov_vo_wasgeneratedbydescription;
DELETE FROM prov_vo_agent;
DELETE FROM prov_vo_wasassociatedwith;
DELETE FROM prov_vo_wasattributedto;

INSERT INTO prov_vo_activitydescription (id, label, type, subtype, parametertypes, description, docuLink) VALUES
  ("cs:actdesc_cosmosimulation", "Cosmological simulation", "cs:simulation", "", "{'code': {'datatype': 'string'}, 'force resolution': {'datatype': 'string', 'unit': 'h-1.kpc'}, 'starting redshift': {'datatype': 'float', 'ucd':'time.epoch'}}", "A cosmological simulation", ""),
  ("cs:actdesc_fof", "FOF halo finding", "cs:post-processing", "cs:halofinder", "{'code': {'dataype': 'string'}, 'rel. linking length': {'datatype': 'float', 'ucd': 'meta.code.qual'}}", "Running the FOF halo finder", "Riebe et al. (2013), AN, 334, 691, http://adsabs.harvard.edu/abs/2013AN....334..691R"),
  ("cs:actdesc_mergertree", "Merger tree building", "cs:post-processing", "cs:mergertreebuilding", "{'code': {'dataype': 'string'}}", "Building the merger tree", ""),
  ("cs:actdesc_sam", "SAM galaxy building", "cs:post-processing", "cs:galaxybuilding", "{'code': {'dataype': 'string'}}", "Using a semi-analytical model (SAM) for producing galaxy information for dark matter halos", "")
  ;

-- activitydescription: should it contain the code? many activities share the same code, same version?
-- or rather: same descriptions for those that share the same "type" of code?

-- version?
-- where should I store the code?
INSERT INTO prov_vo_activity (id, label, description_id, parametervalues, annotation, startTime, endTime, docuLink) VALUES 
  ("mdr1:act_simulation", "MDR1 simulation", "cs:actdesc_cosmosimulation", "{'code': 'ART', 'force resolution': '7.0', 'starting redshift': 65.0}", "The simulation MultiDark Run 1","2012", "2012", "Prada et al. (2012), MNRAS, 423, 3018, http://adsabs.harvard.edu/abs/2012MNRAS.423.3018P"),
  ("mdpl2:act_simulation", "MDPL2 simulation", "cs:actdesc_cosmosimulation", "{'code': 'ART', 'force resolution': '5.0 to 13.0', 'starting redshift': 120.0}", "The MDPL2 simulation","2014", "2014", "Klypin, Yepes, Gottlöber, Prada, Heß, (2016) MNRAS 457, 4340"),
  ("mdr1:act_fof", "MDR1 FOF halo finding", "cs:actdesc_fof", "{'code': 'FOF', 'rel. linking length': 0.17}", "Running the FOF halo finder, basic linking length 0.17", "-", "-", "Riebe et al. (2013), AN, 334, 691, http://adsabs.harvard.edu/abs/2013AN....334..691R"),
  ("mdr1:act_fofc", "MDR1 FOFc halo finding, c-version", "cs:actdesc_fof", "{'code': 'FOF', 'rel. linking length': 0.2}", "Running the FOF halo finder, basic linking length 0.2", "-", "-", "Riebe et al. (2013), AN, 334, 691, http://adsabs.harvard.edu/abs/2013AN....334..691R"),
  ("mdr1:act_fofmtree", "MDR1 FOFMtree building", "cs:actdesc_mergertree", "{}", "Building the merger tree for a FOF halo finder", "-", "-", "-"),
  ("mdr1:act_rockstar", "MDR1 Rockstar building", "cs:actdesc_mergertree", "{'code': 'Rockstar'}", "Building the Rockstar catalog + merger tree", "-", "-", "Behroozi, Wechsler and Wu, 2013, APJ 762, 109"),
  ("mdpl2:act_fof", "MDPL2 FOF halo finding", "cs:actdesc_fof", "{}", "Running the FOF halo finder, basic linking length 0.17", "-", "-", "Riebe et al. (2013), AN, 334, 691, http://adsabs.harvard.edu/abs/2013AN....334..691R"),
  ("mdpl2:act_rockstar", "MDPL2 Rockstar building", "cs:actdesc_mergertree", "{'code': 'Rockstar'}", "Building the Rockstar catalog + merger tree", "-", "-", "Behroozi, Wechsler and Wu, 2013, APJ 762, 109"),
  ("mdpl2:act_galacticus", "Running Galacticus on MDPL2", "cs:actdesc_sam", "{'code': 'Galacticus'}", "Building the Galacticus galaxy catalog", "2015-07-01", "2015-09-01", "Benson et al.")
  ;

INSERT INTO prov_vo_entitydescription (id, label, description, docuLink, dataproduct_type, dataproduct_subtype, level) VALUES
  ("cs:edesc_snapshots", "Simulation snapshots", 
    "snapshots for different times of the simulation, usually containing enough information to restart the simulation, param: snapnums",
    "", "ds:catalog", "", "0"),
  ("cs:edesc_halocatalog", "Halo catalog",
    "A catalog of dark matter objects and their properties, possibly for different snapshot numbers, param: snapnums",
    "", "ds:catalog", "", "1"),
  ("cs:edesc_mergertree", "Merger trees",
    "Merger trees that contain the merging history of dark matter objects",
    "", "ds:catalog", "", "2"),
  ("cs:edesc_halocatalog_mergertree", "Halo catalog with merger tree links",
    "A combination of halo catalog and merger tree information",
    "", "ds:catalog", "", "2"),
  ("cs:edesc_samgalaxycatalog", "SAM galaxies",
    "Semi-analytical galaxy catalog",
    "", "ds:catalog", "", "4")
  ;

INSERT INTO prov_vo_entity (id, label, type, location, access, size, format, annotation, description_id) VALUES
  ("mdr1:snapshots", "MDR1 simulation snapshots", "prov:entity", "erebos.aip.de", 
    "internal", "some GB", "binary-files", "The raw files in original format, partially also uploaded to the database",
    "cs:edesc_snapshots"),
  ("mdr1:fof", "MDR1 FOF catalog", "prov:entity", "https://www.cosmosim.org/", 
    "public", "some GB", "database-table", "FOF tables (FOF, FOF1, ... FOF4) with object properties for different times and linking lengths",
    "cs:edesc_halocatalog"),
  ("mdr1:fofc", "MDR1 FOFc catalog", "prov:entity", "https://www.cosmosim.org/", 
    "public", "some GB", "database-table", "FOFc table with object properties for different times",
    "cs:edesc_halocatalog"),
  ("mdr1:fofmtree", "MDR1 FOF mtree", "prov:entity", "https://www.cosmosim.org/", 
    "public", "some GB", "database-table", "FOF merger tree",
    "cs:edesc_mergertree"),
  ("mdr1:rockstar", "MDR1 Rockstar catalog+trees", "prov:entity", "https://www.cosmosim.org/", 
    "public", "some GB", "database-table", "Rockstar table including merger trees",
    "cs:edesc_halocatalog_mergertree"),
  ("mdpl2:snapshots", "MDPL2 simulation snapshots", "prov:entity", "erebos.aip.de", 
    "internal", "some GB", "binary-files", "The raw files in original format, partially also uploaded to the database",
    "cs:edesc_snapshots"),
  ("mdpl2:fof", "MDPL2 FOF catalog", "prov:entity", "https://www.cosmosim.org/", 
    "public", "some GB", "database-table", "FOF tables (FOF, FOF1, ... FOF5) with object properties for different times and linking lengths",
    "cs:edesc_halocatalog"),
  ("mdpl2:rockstar", "MDPL2 Rockstar catalog+trees", "prov:entity", "https://www.cosmosim.org/", 
    "public", "some GB", "database-table", "Rockstar table including merger trees",
    "cs:edesc_halocatalog_mergertree"),
  ("mdpl2:galacticus", "MDPL2 Galacticus catalog", "prov:entity", "https://www.cosmosim.org/", 
    "public", "some GB", "database-table", "Galacticus galaxy catalog, SAM",
    "cs:edesc_samgalaxycatalog")
  ;

-- what if:
-- * an entitity consists of multiple datasets? (e.g. "FOF" entity, but tables FOF, FOF1 to FOF5 belong to this, have different parameters -- no, their generation-activity has diff. params.)
-- * an entitity is a combination of different types of datasets (e.g. Rockstar =catalog+consistent merger trees!)

INSERT INTO prov_vo_useddescription(id, activitydescription_id, entitydescription_id, role) VALUES
  ("cs:usedesc_fof_snapshots", "cs:actdesc_fof", "cs:edesc_snapshots", "simulation raw data"),
  ("cs:usedesc_mergertree_halocatalog", "cs:actdesc_mergertree", "cs:edesc_halocatalog", "halo catalogue"),
  ("cs:usedesc_mergertree_snapshots", "cs:actdesc_mergertree", "cs:edesc_snapshots", "simulation raw data"),
  ("cs:usedesc_sam_mergertree", "cs:actdesc_sam", "cs:edesc_mergertree", "merger tree"),
  ("cs:usedesc_sam_halocatalog_mergertree", "cs:actdesc_sam", "cs:edesc_halocatalog_mergertree", "merger tree") -- alternative
--  ("cs:actdesc_sam", "cs:snapshots", "simulation raw data") -- alternative, does that really happen?
  ;

INSERT INTO prov_vo_used(activity_id, entity_id, description_id) VALUES
  ("mdr1:act_fof", "mdr1:snapshots", "cs:usedesc_fof_snapshots"),
  ("mdr1:act_fofc", "mdr1:snapshots", "cs:usedesc_fof_snapshots"),
  ("mdr1:act_rockstar", "mdr1:snapshots", "cs:usedesc_mergertree_snapshots"),
  ("mdr1:act_fofmtree", "mdr1:fof", "cs:usedesc_mergertree_halocatalog"),
  ("mdpl2:act_fof", "mdpl2:snapshots", "cs:usedesc_fof_snapshots"),
  ("mdpl2:act_rockstar", "mdpl2:snapshots", "cs:usedesc_mergertree_snapshots"),
  ("mdpl2:act_galacticus", "mdpl2:rockstar", "cs:usedesc_sam_halocatalog_mergertree")
  ;

INSERT INTO prov_vo_wasgeneratedbydescription(id, entitydescription_id, activitydescription_id, role) VALUES
  ("cs:wgdesc_snapshots_cosmosimulation", "cs:edesc_snapshots", "cs:actdesc_cosmosimulation", "simulation raw data"),
  ("cs:wgdesc_halocatalog_fof", "cs:edesc_halocatalog", "cs:actdesc_fof", "halo catalogue"),
  ("cs:wgdesc_halocatalog_mergertree_mergertree", "cs:edesc_halocatalog_mergertree", "cs:actdesc_mergertree", "halo catalogue+merger tree"),
  ("cs:wgdesc_mergertree_mergertree", "cs:edesc_mergertree", "cs:actdesc_mergertree", "merger tree"),
  ("cs:wgdesc_samgalaxycatalog_sam", "cs:edesc_samgalaxycatalog", "cs:actdesc_sam", "galaxy catalogue")
  ;  

INSERT INTO prov_vo_wasgeneratedby(entity_id, activity_id, description_id) VALUES
  ("mdr1:snapshots", "mdr1:act_simulation", "cs:wgdesc_snapshots_cosmosimulation"),
  ("mdr1:fof", "mdr1:act_fof", "cs:wgdesc_halocatalog_fof"),
  ("mdr1:fofc", "mdr1:act_fofc", "cs:wgdesc_halocatalog_fof"),
  ("mdr1:rockstar", "mdr1:act_rockstar", "cs:wgdesc_halocatalog_mergertree_mergertree"),
  ("mdr1:fofmtree", "mdr1:act_fofmtree", "cs:wgdesc_mergertree_mergertree"),
  ("mdpl2:snapshots", "mdpl2:act_simulation", "cs:wgdesc_snapshots_cosmosimulation"),
  ("mdpl2:fof", "mdpl2:act_fof", "cs:wgdesc_halocatalog_fof"),
  ("mdpl2:rockstar", "mdpl2:act_rockstar", "cs:wgdesc_halocatalog_mergertree_mergertree"),
  ("mdpl2:galacticus", "mdpl2:act_galacticus", "cs:wgdesc_samgalaxycatalog_sam")
  ;

INSERT INTO prov_vo_agent(id, name, type, affiliation) VALUES
  ("cs:Stefan_Gottloeber", "Stefan Gottlöber", "prov:Person", "AIP, Potsdam, Germany"),
  ("cs:Jaime_Forero_Romero", "Jaime Forero-Romero", "prov:Person", "AIP, Potsdam, Germany"),
  ("cs:Gustavo_Yepes", "Gustavo Yepes", "prov:Person", "UAM, Madrid, Spain"),
  ("cs:Peter_Behroozi", "Peter Behroozi", "prov:Person", "UC Berkeley, Berkeley, USA"),
  ("cs:Christoph_Behrens", "Christoph Behrens", "prov:Person", "Georg-August-Universität Göttingen, Göttingen, Germany"),
  ("cs:MultiDark", "MultiDark project", "prov:organization", "Spain+Germany+USA")
  ;

INSERT INTO prov_vo_wasassociatedwith(activity_id, agent_id, role) VALUES
  ("mdr1:act_simulation", "cs:Gustavo_Yepes", "operator"),
  ("mdpl2:act_simulation", "cs:Gustavo_Yepes", "operator"),
  ("mdr1:act_fof", "cs:Stefan_Gottloeber", "operator"),
  ("mdr1:act_fofc", "cs:Stefan_Gottloeber", "operator"),
  ("mdr1:act_fofmtree", "cs:Jaime_Forero_Romero", "operator"),
  ("mdr1:act_rockstar", "cs:Peter_Behroozi", "operator"),
  ("mdpl2:act_fof", "cs:Stefan_Gottloeber", "operator"),
  ("mdpl2:act_rockstar", "cs:Peter_Behroozi", "operator"),
  ("mdpl2:act_galacticus", "cs:Christoph_Behrens", "operator")
  ;
--  ("mdpl2:act_galacticus", "cs:Andrew_Benson", "creator"),

INSERT INTO prov_vo_wasattributedto(entity_id, agent_id, role) VALUES
  ("mdr1:snapshots", "cs:MultiDark", "publisher"),
  ("mdr1:fof", "cs:MultiDark", "publisher"),
  ("mdr1:fofc", "cs:MultiDark", "publisher"),
  ("mdr1:rockstar", "cs:MultiDark", "publisher"),
  ("mdr1:fofmtree", "cs:MultiDark", "publisher"),
  ("mdpl2:snapshots", "cs:MultiDark", "publisher"),
  ("mdpl2:fof", "cs:MultiDark", "publisher"),
  ("mdpl2:rockstar", "cs:MultiDark", "publisher"),
  ("mdpl2:galacticus", "cs:MultiDark", "publisher")
  ;


-- should be fine now! TODO: check tomorrow for errors when imorting to db!