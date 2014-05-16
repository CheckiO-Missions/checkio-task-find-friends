"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": (
                ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
                 "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
                "scout2", "scout3"),
            "answer": True,
            "explanation": ["dr101", "mr99", "out00", "scout1", "scout2", "scout3", "scout4", "sscout", "super"]
        },
        {
            "input": (
                ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
                 "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
                "super", "scout2"),
            "answer": True,
            "explanation": ["dr101", "mr99", "out00", "scout1", "scout2", "scout3", "scout4", "sscout", "super"]
        },
        {
            "input": (
                ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
                 "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
                "dr101", "sscout"),
            "answer": False,
            "explanation": ["dr101", "mr99", "out00", "scout1", "scout2", "scout3", "scout4", "sscout", "super"]
        },

    ],
    "Edge": [
        {
            "input": (['night-nikola'],
                      "nikola", "night"),
            "answer": True,
            "explanation": ['nikola', 'night']
        },
        {
            "input": (['nic-batman', 'cat-super'],
                      "batman", "cat"),
            "answer": False,
            "explanation": ['batman', 'cat', 'super', 'nic']
        },
        {
            "input": (['scout1-scout3', 'plane1-robin', 'scout3-sscout', 'scout1-base', 'pingin-scout1', 'sscout-base',
                       'scout3-plane1', 'scout3-robin', 'plane1-nikola', 'plane1-pingin', 'base-scout3',
                       'plane1-sobhia',
                       'base-pingin', 'scout3-sobhia', 'robin-stevan', 'robin-base', 'nikola-robin', 'sobhia-sscout',
                       'stevan-sscout', 'robin-sobhia', 'robin-sscout', 'pingin-sscout', 'scout3-nikola', 'nikola-base',
                       'plane1-scout1', 'plane1-base', 'sscout-plane1', 'sobhia-scout1', 'sscout-scout1',
                       'robin-pingin',
                       'pingin-stevan', 'pingin-sobhia', 'scout3-pingin', 'nikola-sscout', 'nikola-pingin',
                       'stevan-base',
                       'stevan-scout1', 'scout1-nikola', 'nikola-sobhia', 'stevan-sobhia', 'stevan-scout3',
                       'scout1-robin',
                       'nikola-stevan', 'sobhia-base', 'stevan-plane1'],
                      "pingin", "sobhia"),
            "answer": True,
            "explanation": ['pingin', 'sobhia', 'sscout', 'scout3', 'stevan', 'scout1', 'plane1', 'nikola', 'base',
                            'robin']
        },
        {
            "input": (
                ['sscout-batman', 'plane1-scout3', 'stevan-batman', 'super-sscout', 'scout2-batman', 'scout2-sscout',
                 'doc-mega', 'night-batman', 'scout3-doc'],
                "scout2", "plane1"),
            "answer": False,
            "explanation": ['scout2', 'plane1', 'stevan', 'night', 'mega', 'sscout', 'super', 'scout3', 'doc', 'batman']
        },
        {
            "input": (
                ['scout2-plane1', 'plane1-stevan', 'stevan-night', 'night-mega', 'mega-sscout', 'sscout-super',
                 'super-scout3',
                 'scout3-doc', 'doc-batman'],
                "scout2", "batman"),
            "answer": True,
            "explanation": ['scout2', 'plane1', 'stevan', 'night', 'mega', 'sscout', 'super', 'scout3', 'doc', 'batman']
        },
        {
            "input": (
                ['scout2-plane1', 'plane1-stevan', 'stevan-night', 'night-mega', 'sscout-super',
                 'super-scout3', 'scout3-doc', 'doc-batman'],
                "night", "batman"),
            "answer": False,
            "explanation": ['scout2', 'plane1', 'stevan', 'night', 'mega', 'sscout', 'super', 'scout3', 'doc', 'batman']
        },
        {
            "input": (['scout1-scout3', 'plane1-robin', 'scout3-sscout', 'pingin-scout1',
                       'scout3-plane1', 'scout3-robin', 'plane1-nikola', 'plane1-pingin',
                       'plane1-sobhia', 'scout3-sobhia', 'nikola-robin', 'sobhia-sscout',
                       'robin-sobhia', 'robin-sscout', 'pingin-sscout', 'scout3-nikola',
                       'plane1-scout1', 'sscout-plane1', 'sobhia-scout1', 'sscout-scout1',
                       'robin-pingin', 'pingin-sobhia', 'scout3-pingin', 'nikola-sscout', 'nikola-pingin',
                       'stevan-base', 'scout1-nikola', 'nikola-sobhia',
                       'scout1-robin', ],
                      "base", "nikola"),
            "answer": False,
            "explanation": ['pingin', 'sobhia', 'sscout', 'scout3', 'stevan', 'scout1', 'plane1', 'nikola', 'base',
                            'robin']
        },


    ]
    # "Extra": [
    #     {
    #         "input": [6, 3],
    #         "answer": 9,
    #         "explanation": "6+3=?"
    #     },
    #     {
    #         "input": [6, 7],
    #         "answer": 13,
    #         "explanation": "6+7=?"
    #     }
    # ]
}
