def success_get_stats(user):
    return f"ā Successfully get stats.\n\nš¤ Id: {user.get_id()}\n" \
        + f"š¤” Username: {user.get_name()}\nšŖ Balance: {user.get_balance()}"


def fail_error_occurred():
    return "ā An error occurred while trying to get your stats."


def fail_not_registered_user():
    return "ā You aren't registered. Please create an account to use $pipo bot."
