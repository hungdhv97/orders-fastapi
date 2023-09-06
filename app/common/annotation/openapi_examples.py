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

CREATE_MERCHANT_EXAMPLES = {
    "merchant1": {
        "summary": "Create Merchant Grab",
        "value": {
            "merchant_id": "5-C3C2T8MUVN4HLT",
            "delivery_type": "grab",
            "user_id": "64f6318231e3ac649c61d2e8",
        }
    },
    "merchant2": {
        "summary": "Create Merchant Shopee",
        "value": {
            "merchant_id": "merchant_shopee_id",
            "delivery_type": "shopee",
            "user_id": "64f6318231e3ac649c61d2e8",
        }
    },
}

CREATE_USER_EXAMPLES = {
    "account1": {
        "summary": "Create Nghia account",
        "value": {
            "username": "nghia.nguyen4",
            "password": "1234",
            "full_name": "Nguyễn Bá Nghĩa",
        }
    },
    "account2": {
        "summary": "Create Hung account",
        "value": {
            "username": "hung.thai",
            "password": "1234",
            "full_name": "Thái Doãn Hùng",
        }
    },
    "account3": {
        "summary": "Create Nam account",
        "value": {
            "username": "nam.nguyen12",
            "password": "1234",
            "full_name": "Nguyễn Văn Nam",
        }
    },
}

UPDATE_USER_EXAMPLES = {
    "update_username": {
        "summary": "Update Username",
        "value": {
            "username": "updated.username100",
        }
    },
    "update_password": {
        "summary": "Update Password",
        "value": {
            "password": "Updated Password",
        }
    },
    "update_fullname": {
        "summary": "Any Fullname",
        "value": {
            "full_name": "Updated Fullname",
        }
    },
}
