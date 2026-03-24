def generate_test_cases(requirement):
    return [
        {
            "id": "TC_001",
            "scenario": "Valid Login",
            "steps": [
                "Open application",
                "Enter valid email and password",
                "Click login"
            ],
            "expected": "User should login successfully",
            "priority": "High"
        },
        {
            "id": "TC_002",
            "scenario": "Invalid Login",
            "steps": [
                "Enter invalid credentials",
                "Click login"
            ],
            "expected": "Error message should be displayed",
            "priority": "High"
        },
        {
            "id": "TC_003",
            "scenario": "Empty Fields",
            "steps": [
                "Leave fields empty",
                "Click login"
            ],
            "expected": "Validation error should appear",
            "priority": "Medium"
        }
    ]