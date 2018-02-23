ABI Reports
===========

This is a repository with machine-readable JSON-format backward compatibility analysis reports for hundreds of open-source C/C++ libraries. The reports are generated by the ABI Tracker project (https://github.com/lvc/upstream-tracker).

Original detailed HTML-format reports are available here: https://abi-laboratory.pro/tracker/

The reports in this repository can be used or redistributed under the terms of the CC-BY-4.0 license.

The repository is AUTO updated three times a week (Mon, Wed, Fri approx. at 11:00 UTC) after each run of the ABI Tracker.

Report Details
--------------

The version of the library can be considered incompatible if: `BC!=100%` or `Removed!=0` or `ObjectsRemoved!=0` or `ChangedSoname!=0`

If `BC==100%` then non-zero value of `TotalProblems` indicates minor compatibility warnings.

The list of report attributes:

| Attr              | Value                                                                          |
|-------------------|--------------------------------------------------------------------------------|
| Version           | Analyzed version of the library                                                |
| From              | Reference version of the library                                               |
| BC                | Avg. backward binary compatibility rate in percents                            |
| Added             | The number of added symbols                                                    |
| Removed           | The number of removed symbols                                                  |
| TotalProblems     | Total number of backward binary compatibility<br>problems (including warnings) |
| ObjectsAdded      | The number of added shared objects                                             |
| ObjectsRemoved    | The number of removed shared objects                                           |
| ChangedSoname     | The number of objects with changed SONAME                                      |
| TotalObjects      | Total shared objects                                                           |
| Src_BC            | Avg. backward source compatibility rate in percents                            |
| Src_TotalProblems | Total number of backward source compatibility<br>problems (including warnings) |
