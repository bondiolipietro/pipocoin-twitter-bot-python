def success_get_balance(user):
    return f"ā Successfully get balance.\n\nšŖ Balance: {user.get_balance()}"


def fail_error_occurred():
    return "ā An error occurred while trying to get your balance."


def fail_not_registered_user():
    return "ā You aren't registered. Please create an account to use $pipo bot."
