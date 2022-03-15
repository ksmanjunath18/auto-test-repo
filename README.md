# auto-test-repo
Test Repo for verifying AUH

* meta-test Branch added for testing AUH workflow:

├── conf
│   └── layer.conf
├── COPYING.MIT
├── README
└── recipes-auh
    ├── auh_failed
    │   ├── COPYING
    │   └── recipe-failed_0.1.bb
    ├── auh_match
    │   ├── COPYING
    │   └── recipe-match_0.1.bb
    └── auh_successful
        ├── COPYING
        └── recipe-successful_0.1.bb

contains Recipes for testing test cases like: SUCCESSFUL, MATCH and FAILED test case.


* test_cases_auh :
----------------------------------------------------------------------------

contains test cases for verfying auto-upgrade-helper script

** Testing instructions **
1.You must source oe-init-build-env before running this test  script.
(It is recommended to create a fresh build directory with it).

2.Run test script in a command line inside test_cases_auh folder as:
	> pytest -svx --script <path to upgrade-helper.py script> \
	  --recipe_successful <recipe to check SUCCESS case>\
	  --recipe_match <recipe to check MATCH case>\
          --recipe_failed <recipe to check failure  case> 

3. Default settings :
    > --script = "auto-upgrade-helper/upgrade-helper.py" 
    
    > --recipe_successful = "recipe-successful" (from meta-test layer)

    > --recipe_match = "recipe-match" (from meta-test layer)

    > --recipe_failed = "recipe-failed" (from meta-test layer)

