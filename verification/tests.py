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
    "Extra": [
        {
            "input": [6, 3],
            "answer": 9,
            "explanation": "6+3=?"
        },
        {
            "input": [6, 7],
            "answer": 13,
            "explanation": "6+7=?"
        }
    ]
}
