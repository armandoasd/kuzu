from datetime import date, datetime, timedelta

TINY_SNB_PERSONS_GROUND_TRUTH = {
    0: {
        "ID": 0,
        "fName": "Alice",
        "gender": 1,
        "isStudent": True,
        "isWorker": False,
        "age": 35,
        "eyeSight": 5.0,
        "birthdate": date(1900, 1, 1),
        "registerTime": datetime(2011, 8, 20, 11, 25, 30),
        "lastJobDuration": timedelta(days=1082, seconds=46920),
        "workedHours": [10, 5],
        "usedNames": ["Aida"],
        "courseScoresPerTerm": [[10, 8], [6, 7, 8]],
        "_label": "person",
        "_id": {"offset": 0, "table": 0},
    },
    2: {
        "ID": 2,
        "fName": "Bob",
        "gender": 2,
        "isStudent": True,
        "isWorker": False,
        "age": 30,
        "eyeSight": 5.1,
        "birthdate": date(1900, 1, 1),
        "registerTime": datetime(2008, 11, 3, 15, 25, 30, 526),
        "lastJobDuration": timedelta(days=3750, seconds=46800, microseconds=24),
        "workedHours": [12, 8],
        "usedNames": ["Bobby"],
        "courseScoresPerTerm": [[8, 9], [9, 10]],
        "_label": "person",
        "_id": {"offset": 1, "table": 0},
    },
    3: {
        "ID": 3,
        "fName": "Carol",
        "gender": 1,
        "isStudent": False,
        "isWorker": True,
        "age": 45,
        "eyeSight": 5.0,
        "birthdate": date(1940, 6, 22),
        "registerTime": datetime(1911, 8, 20, 2, 32, 21),
        "lastJobDuration": timedelta(days=2, seconds=1451),
        "workedHours": [4, 5],
        "usedNames": ["Carmen", "Fred"],
        "courseScoresPerTerm": [[8, 10]],
        "_label": "person",
        "_id": {"offset": 2, "table": 0},
    },
    5: {
        "ID": 5,
        "fName": "Dan",
        "gender": 2,
        "isStudent": False,
        "isWorker": True,
        "age": 20,
        "eyeSight": 4.8,
        "birthdate": date(1950, 7, 23),
        "registerTime": datetime(2031, 11, 30, 12, 25, 30),
        "lastJobDuration": timedelta(days=3750, seconds=46800, microseconds=24),
        "workedHours": [1, 9],
        "usedNames": ["Wolfeschlegelstein", "Daniel"],
        "courseScoresPerTerm": [[7, 4], [8, 8], [9]],
        "_label": "person",
        "_id": {"offset": 3, "table": 0},
    },
    7: {
        "ID": 7,
        "fName": "Elizabeth",
        "gender": 1,
        "isStudent": False,
        "isWorker": True,
        "age": 20,
        "eyeSight": 4.7,
        "birthdate": date(1980, 10, 26),
        "registerTime": datetime(1976, 12, 23, 11, 21, 42),
        "lastJobDuration": timedelta(days=2, seconds=1451),
        "workedHours": [2],
        "usedNames": ["Ein"],
        "courseScoresPerTerm": [[6], [7], [8]],
        "_label": "person",
        "_id": {"offset": 4, "table": 0},
    },
    8: {
        "ID": 8,
        "fName": "Farooq",
        "gender": 2,
        "isStudent": True,
        "isWorker": False,
        "age": 25,
        "eyeSight": 4.5,
        "birthdate": date(1980, 10, 26),
        "registerTime": datetime(1972, 7, 31, 13, 22, 30, 678559),
        "lastJobDuration": timedelta(seconds=1080, microseconds=24000),
        "workedHours": [3, 4, 5, 6, 7],
        "usedNames": ["Fesdwe"],
        "courseScoresPerTerm": [[8]],
        "_label": "person",
        "_id": {"offset": 5, "table": 0},
    },
    9: {
        "ID": 9,
        "fName": "Greg",
        "gender": 2,
        "isStudent": False,
        "isWorker": False,
        "age": 40,
        "eyeSight": 4.9,
        "birthdate": date(1980, 10, 26),
        "registerTime": datetime(1976, 12, 23, 4, 41, 42),
        "lastJobDuration": timedelta(days=3750, seconds=46800, microseconds=24),
        "workedHours": [1],
        "usedNames": ["Grad"],
        "courseScoresPerTerm": [[10]],
        "_label": "person",
        "_id": {"offset": 6, "table": 0},
    },
    10: {
        "ID": 10,
        "fName": "Hubert Blaine Wolfeschlegelsteinhausenbergerdorff",
        "gender": 2,
        "isStudent": False,
        "isWorker": True,
        "age": 83,
        "eyeSight": 4.9,
        "birthdate": date(1990, 11, 27),
        "registerTime": datetime(2023, 2, 21, 13, 25, 30),
        "lastJobDuration": timedelta(days=1082, seconds=46920),
        "workedHours": [10, 11, 12, 3, 4, 5, 6, 7],
        "usedNames": ["Ad", "De", "Hi", "Kye", "Orlan"],
        "courseScoresPerTerm": [[7], [10], [6, 7]],
        "_label": "person",
        "_id": {"offset": 7, "table": 0},
    },
}

TINY_SNB_ORGANISATIONS_GROUND_TRUTH = {
    1: {
        "ID": 1,
        "name": "ABFsUni",
        "orgCode": 325,
        "mark": 3.7,
        "score": -2,
        "history": "10 years 5 months 13 hours 24 us",
        "licenseValidInterval": timedelta(days=1085),
        "rating": 1.0,
        "_label": "organisation",
        "_id": {"offset": 0, "table": 2},
    },
    4: {
        "ID": 4,
        "name": "CsWork",
        "orgCode": 934,
        "mark": 4.1,
        "score": -100,
        "history": "2 years 4 days 10 hours",
        "licenseValidInterval": timedelta(days=9414),
        "rating": 0.78,
        "_label": "organisation",
        "_id": {"offset": 1, "table": 2},
    },
    6: {
        "ID": 6,
        "name": "DEsWork",
        "orgCode": 824,
        "mark": 4.1,
        "score": 7,
        "history": "2 years 4 hours 22 us 34 minutes",
        "licenseValidInterval": timedelta(days=3, seconds=36000, microseconds=100000),
        "rating": 0.52,
        "_label": "organisation",
        "_id": {"offset": 2, "table": 2},
    },
}

TINY_SNB_KNOWS_GROUND_TRUTH = {
    0: [2, 3, 5],
    2: [0, 3, 5],
    3: [0, 2, 5],
    5: [0, 2, 3],
    7: [8, 9],
}

TINY_SNB_KNOWS_PROPERTIES_GROUND_TRUTH = {
    (0, 2): {
        "date": date(2021, 6, 30),
        "meetTime": datetime(1986, 10, 21, 21, 8, 31, 521000),
        "validInterval": timedelta(days=3750, seconds=46800, microseconds=24),
        "comments": ["rnme", "m8sihsdnf2990nfiwf"],
        "summary": {
            "locations": ["'toronto'", "'waterloo'"],
            "transfer": {"day": date(2021, 1, 2), "amount": [100, 200]},
        },
        "notes": 1,
        "someMap": {"a": "b"},
    },
    (0, 3): {
        "date": date(2021, 6, 30),
        "meetTime": datetime(1946, 8, 25, 19, 7, 22),
        "validInterval": timedelta(days=7232),
        "comments": ["njnojppo9u0jkmf", "fjiojioh9h9h89hph"],
        "summary": {"locations": None, "transfer": None},
        "notes": date(2020, 10, 10),
        "someMap": {"c": "d", "e": "f", "1": "2"},
    },
    (0, 5): {
        "date": date(2021, 6, 30),
        "meetTime": datetime(2012, 12, 11, 20, 7, 22),
        "validInterval": timedelta(days=10),
        "comments": ["ioji232", "jifhe8w99u43434"],
        "summary": {"locations": ["'shanghai'"], "transfer": {"day": date(1990, 9, 10), "amount": [10]}},
        "notes": "nice weather",
        "someMap": None,
    },
    (2, 0): {
        "date": date(2021, 6, 30),
        "meetTime": datetime(1946, 8, 25, 19, 7, 22),
        "validInterval": timedelta(days=3750, seconds=46800, microseconds=24),
        "comments": ["2huh9y89fsfw23", "23nsihufhw723"],
        "summary": {"locations": ["'paris'"], "transfer": {"day": date(2000, 1, 1), "amount": [20, 5000]}},
        "notes": 4,
        "someMap": None,
    },
    (2, 3): {
        "date": date(1950, 5, 14),
        "meetTime": datetime(1946, 8, 25, 19, 7, 22),
        "validInterval": timedelta(seconds=1380),
        "comments": ["fwehu9h9832wewew", "23u9h989sdfsss"],
        "summary": {"locations": ["'paris'"], "transfer": {"day": date(2011, 5, 1), "amount": [2000, 5340]}},
        "notes": "cool stuff found",
        "someMap": None,
    },
    (2, 5): {
        "date": date(1950, 5, 14),
        "meetTime": datetime(2012, 12, 11, 20, 7, 22),
        "validInterval": timedelta(days=7232),
        "comments": ["fwh9y81232uisuiehuf", "ewnuihxy8dyf232"],
        "summary": {"locations": ["'vancouver'"], "transfer": {"day": date(2020, 1, 1), "amount": [120, 50]}},
        "notes": "matthew perry",
        "someMap": None,
    },
    (3, 0): {
        "date": date(2021, 6, 30),
        "meetTime": datetime(2002, 7, 31, 11, 42, 53, 123420),
        "validInterval": timedelta(days=41, seconds=21600),
        "comments": ["fnioh8323aeweae34d", "osd89e2ejshuih12"],
        "summary": {
            "locations": ["'london'", "'toronto'"],
            "transfer": {"day": date(2012, 11, 21), "amount": [223, 5230]},
        },
        "notes": 10,
        "someMap": None,
    },
    (3, 2): {
        "date": date(1950, 5, 14),
        "meetTime": datetime(2007, 2, 12, 12, 11, 42, 123000),
        "validInterval": timedelta(seconds=1680, microseconds=30000),
        "comments": ["fwh983-sdjisdfji", "ioh89y32r2huir"],
        "summary": {
            "locations": ["'paris'", "'beijing'"],
            "transfer": {"day": date(2011, 3, 11), "amount": [2323, 50]},
        },
        "notes": 1,
        "someMap": None,
    },
    (3, 5): {
        "date": date(2000, 1, 1),
        "meetTime": datetime(1998, 10, 2, 13, 9, 22, 423000),
        "validInterval": timedelta(microseconds=300000),
        "comments": ["psh989823oaaioe", "nuiuah1nosndfisf"],
        "summary": {"locations": [], "transfer": {"day": date(1980, 11, 21), "amount": [20, 5]}},
        "notes": 2,
        "someMap": None,
    },
    (5, 0): {
        "date": date(2021, 6, 30),
        "meetTime": datetime(1936, 11, 2, 11, 2, 1),
        "validInterval": timedelta(microseconds=480),
        "comments": ["fwewe"],
        "summary": {
            "locations": ["'shanghai'", "'nanjing'"],
            "transfer": {"day": date(1998, 11, 12), "amount": [22, 53240]},
        },
        "notes": 15,
        "someMap": None,
    },
    (5, 2): {
        "date": date(1950, 5, 14),
        "meetTime": datetime(1982, 11, 11, 13, 12, 5, 123000),
        "validInterval": timedelta(seconds=1380),
        "comments": ["fewh9182912e3", "h9y8y89soidfsf", "nuhudf78w78efw", "hioshe0f9023sdsd"],
        "summary": {"locations": ["'paris'"], "transfer": {"day": date(2000, 1, 1), "amount": [20, 5000]}},
        "notes": "happy new year",
        "someMap": None,
    },
    (5, 3): {
        "date": date(2000, 1, 1),
        "meetTime": datetime(1999, 4, 21, 15, 12, 11, 420000),
        "validInterval": timedelta(days=2, microseconds=52000),
        "comments": ["23h9sdslnfowhu2932", "shuhf98922323sf"],
        "summary": {"locations": ["'paris'"], "transfer": {"day": date(2000, 1, 1), "amount": [20, 5000]}},
        "notes": 4,
        "someMap": None,
    },
    (7, 8): {
        "date": date(1905, 12, 12),
        "meetTime": datetime(2025, 1, 1, 11, 22, 33, 520000),
        "validInterval": timedelta(seconds=2878),
        "comments": ["ahu2333333333333", "12weeeeeeeeeeeeeeeeee"],
        "summary": {
            "locations": ["'toronto'", "'thisisalongcityname'"],
            "transfer": {"day": date(1930, 11, 22), "amount": [18, 323]},
        },
        "notes": 8,
        "someMap": None,
    },
    (7, 9): {
        "date": date(1905, 12, 12),
        "meetTime": datetime(2020, 3, 1, 12, 11, 41, 655200),
        "validInterval": timedelta(seconds=2878),
        "comments": ["peweeeeeeeeeeeeeeeee", "kowje9w0eweeeeeeeee"],
        "summary": {
            "locations": ["'waterloo'"],
            "transfer": {"day": date(2000, 1, 1), "amount": [1000, 5000]},
        },
        "notes": 10,
        "someMap": None,
    },
}

TINY_SNB_WORKS_AT_GROUND_TRUTH = {
    3: [4],
    5: [6],
    7: [6],
}

TINY_SNB_WORKS_AT_PROPERTIES_GROUND_TRUTH = {(3, 4): {"year": 2015}, (5, 6): {"year": 2010}, (7, 6): {"year": 2015}}

TENSOR_LIST_GROUND_TRUTH = {
    0: {
        "boolTensor": [True, False],
        "doubleTensor": [[0.1, 0.2], [0.3, 0.4]],
        "intTensor": [[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
    },
    3: {
        "boolTensor": [True, False],
        "doubleTensor": [[0.1, 0.2], [0.3, 0.4]],
        "intTensor": [[[3, 4], [5, 6]], [[7, 8], [9, 10]]],
    },
    4: {
        "boolTensor": [False, True],
        "doubleTensor": [[0.4, 0.8], [0.7, 0.6]],
        "intTensor": [[[5, 6], [7, 8]], [[9, 10], [11, 12]]],
    },
    5: {
        "boolTensor": [True, True],
        "doubleTensor": [[0.4, 0.9], [0.5, 0.2]],
        "intTensor": [[[7, 8], [9, 10]], [[11, 12], [13, 14]]],
    },
    6: {
        "boolTensor": [False, True],
        "doubleTensor": [[0.2, 0.4], [0.5, 0.1]],
        "intTensor": [[[9, 10], [11, 12]], [[13, 14], [15, 16]]],
    },
    8: {
        "boolTensor": [False, True],
        "doubleTensor": [[0.6, 0.4], [0.6, 0.1]],
        "intTensor": [[[11, 12], [13, 14]], [[15, 16], [17, 18]]],
    },
}

PERSONLONGSTRING_GROUND_TRUTH = {
    "AAAAAAAAAAAAAAAAAAAA": {
        "name": "AAAAAAAAAAAAAAAAAAAA",
        "spouse": "Bob",
    },
    "Bob": {
        "name": "Bob",
        "spouse": "AAAAAAAAAAAAAAAAAAAA",
    },
}

PERSONLONGSTRING_KNOWS_GROUND_TRUTH = {
    "AAAAAAAAAAAAAAAAAAAA": ["Bob"],
}
