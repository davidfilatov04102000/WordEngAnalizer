from .GetRatingOfWord.independent_classes import CheckAvailability


def abstract_check_availability(*args):
    check_object = CheckAvailability(*args)
    check_object.parsing_object()
    check_object.execute_checking()
    return check_object.get_result()
