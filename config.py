import re

conferenceTier = {"sigmod": 1, "vldb": 1, "pvldb": 1, "kdd": 1,
                     "edbt": 2, "icde": 2, "icdm": 2, "sdm": 2, "cikm": 2,
                     "dasfaa": 3, "pakdd": 3, "pkdd": 3, "dexa": 3}

conferencesName = {"sigmod": "international conference on management of data",
                   "vldb": "very large data bases conference",
                   "pvldb": "proceedings of the vldb endowment",
                   "kdd": "knowledge discovery and data mining",
                   "edbt": "international conference on extending database technology",
                   "icde": "ieee international conference on data engineering",
                   "icdm": "ieee international conference on data mining",
                   "sdm": "siam international conference on data mining",
                   "cikm": "international conference on information and knowledge management",
                   "dasfaa": "international conference on database systems for advanced applications",
                   "pakdd": "pacific-asia conference on knowledge discovery and knowledge discovery",
                   "pkdd": "european conference on principles of data mining and knowledge discovery",
                   "dexa": "international conference on database and expert systems application"}

sigmodRegex = re.compile("international conference on management of data")
vldbRegex = re.compile("international conference on very large (data bases|databases)")
kddRegex = re.compile("international conference on knowledge discovery (&|and) data mining")
edbtRegex = re.compile("international conference on extending database technology")
icdeRegex = re.compile("international conference on data engineering")
icdmRegex = re.compile("ieee(.*)international conference on data mining")
sdmRegex = re.compile("siam international conference on data mining")
cikmRegex = re.compile("conference on information and knowledge management")
dasfaaRegex = re.compile("database systems for advance(d|s) applications")
pakddRegex = re.compile("knowledge discovery and data mining(.*)pacific-asia conference")
pkddRegex = re.compile("(machine learning and )?knowledge discovery in databases|principles of data mining and knowledge discovery")
dexaRegex = re.compile("database and expert systems applications")

conferencesRegex = {"sigmod": sigmodRegex,
                   "vldb": vldbRegex,
                   "pvldb": vldbRegex,
                   "kdd": kddRegex,
                   "edbt": edbtRegex,
                   "icde": icdeRegex,
                   "icdm": icdmRegex,
                   "sdm": sdmRegex,
                   "cikm": cikmRegex,
                   "dasfaa": dasfaaRegex,
                   "pakdd": pakddRegex,
                   "pkdd": pkddRegex,
                   "dexa": dexaRegex}


