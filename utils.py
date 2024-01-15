def add_years_to_date(original_date, years_to_add):
    """Add a number of years to a date."""
    result = original_date.replace(year=original_date.year + years_to_add)
    return result
