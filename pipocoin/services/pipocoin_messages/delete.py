def success_user_deleted(user):
    return f"""ā Account successfully deleted. \n\nš¤” Deleted Id: {user.get_id()}"""


def fail_error_occurred():
    return "ā An error occurred while trying to delete your account."


def fail_not_registered_user():
    return "ā You aren't registered. Please create an account before delete it."
