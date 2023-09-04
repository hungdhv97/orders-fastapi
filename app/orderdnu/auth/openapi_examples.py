LOGIN_EXAMPLES = {
    "success": {
        "summary": "Login Nghia account",
        "value": {
            "username": "nghia.nguyen4",
            "password": "1234",
        }
    },
    "wrong_password": {
        "summary": "Login Nghia wrong password",
        "value": {
            "username": "nghia.nguyen4",
            "password": "wrong_password",
        }
    },
    "non_exist": {
        "summary": "Login non-exist account",
        "value": {
            "username": "non-exist",
            "password": "1234",
        }
    },
}

REGISTER_EXAMPLES = {
    "account1": {
        "summary": "Register Nghia account",
        "value": {
            "username": "nghia.nguyen4",
            "password": "1234",
            "full_name": "Nguyễn Bá Nghĩa",
        }
    },
    "account2": {
        "summary": "Register Hung account",
        "value": {
            "username": "hung.thai",
            "password": "1234",
            "full_name": "Thái Doãn Hùng",
        }
    },
    "account3": {
        "summary": "Register Nam account",
        "value": {
            "username": "nam.nguyen12",
            "password": "1234",
            "full_name": "Nguyễn Văn Nam",
        }
    },
}
