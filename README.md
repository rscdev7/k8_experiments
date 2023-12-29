# Repo Title
![Alt -> Project Logo](./readme_data/logo.svg)

Project Description.......


## BUSINESS-LOGIC

### *[DOMAIN_SPECIFIC-PIPELINE]*
>- 

### *[DASHBOARD-PIPELINE]*
>- 

### *[ADMIN-PIPELINE]*
>- 


## PERSISTENCE
- 

## PRESENTATION
- 

------------------------------------------------------------------------------------------
## PROJECT CUES


### *[DOMAIN_SPECIFIC CUES]*
>- 


### *[SOFTWARE ARCHITECTURE]*
>- 


### *[SESSION MANAGEMENT]*
>- 


### *[SECURITY]*
>- 


### *[MONITORING]*
>- 


### *[MODULARITY]*
>- 
    
------------------------------------------------------------------------------------------
## SOFTWARE ARCHITECTURE
![Alt -> Software Architecture](./readme_data/arch.svg)


## DESIGN PATTERN
- 


## STACK SOFTWARE - GENERAL
![Alt -> General Software Stack](./readme_data/general_sw.svg)

## STACK SOFTWARE - DOMAIN_SPECIFIC
![Alt -> Domain Specific Software Stack](./readme_data/domain_sw.svg)

------------------------------------------------------------------------------------------
## INSTRUCTIONS FOR EXECUTING THE PROJECT
1. Install *Docker* on your system
2. Setup your Env Variables modifying properly the *$HOME_REPO/docker/production_env/.env* file
3. Execute the following commands:

    cd $HOME_REPO/docker/production_env/

    ./build_img.sh
    
    docker-compose up -d


## DEMO
![Alt -> Demo](./readme_data/img_1.jpg)

------------------------------------------------------------------------------------------
## BRANCHING STRATEGY
- **MAIN**, production-ready code.
- **DEVELOP**, devolpment code.
- **EXPERIMENTAL**, experimental code.

## REPOSITORY STRUCTURE
- **artifcats**, contains binaries of the developed Software.
- **code**, contains code of the project.
    - **0.legacy**, contains old Milestone Code.
    - **api**, project libraries
        - **classes**, contains Class Components of the project.
        - **modules**, contains Module Components (set of functions)  of the project.
    - **frameworks**, contains frameworks (set of correlated classes) of the project.
    - **solutions**, contains production-ready code.
- **envs**, contains Information and/or Images of Enviroment used for the project.
- **readme_data**, contains data used into repository readme.
- **report**, contains the report of the project.
- **summary**, contains a summary spreadsheet of the project results.
- **talk**, contains a set of slide describing the project cues.

------------------------------------------------------------------------------------------
## REFERENCES
- [[1]](https://*.com/*) Dataset 1
- [[2]](https://*.com/*) Library 1
- [[3]](https://*.com/*) Model 1


## AUTHORS
- [@nickname](https://*.com/*) Name Surname
- [@nickname](https://*.com/*) Name Surname


## ACKNOWLEDGEMENTS 
- [@nickname](https://*.com/*) Name Surname
- [@nickname](https://*.com/*) Name Surname