from backend.models import TrafficItem


def save_items(db, items: list[dict]):
    """Persist new traffic items to the database.

    This function stores each traffic item if it does not already exist
    based on its URL.
    
    Args:
        db: The active database session used for querying and persisting
            items.
        items (list[dict]): A list of traffic item dictionaries to
            persist.
    """
    for item in items:
        if db.query(TrafficItem).filter(TrafficItem.url == item["url"]).first():
            continue

        db.add(TrafficItem(**item))
