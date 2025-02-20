from backend.database import get_session, Activity

class ActivityRecommender:
    def __init__(self):
        self.session = get_session()

    def recommend(self, category, zone, age_range):
        query = self.session.query(Activity)

        # Normalize zone and age_range values in the database to lowercase for comparison
        if category:
            query = query.filter(Activity.category == category)
        if zone:
            query = query.filter(Activity.zone.ilike(zone))  # case-insensitive match
        if age_range:
            query = query.filter(Activity.age_range.ilike(age_range))  # case-insensitive match

        # Fetching all matching activities (no limit)
        activities = query.all()

        if not activities:
            return []

        # A simple scoring mechanism based on zone and age range
        def score_activity(activity):
            score = 0
            if activity.zone.lower() == zone:
                score += 1
            if activity.age_range.lower() == age_range:
                score += 1
            return score

        # Sorting activities by their scores (higher score first)
        activities = sorted(activities, key=score_activity, reverse=True)

        # Returning the list of activities with the required details
        return [{
            "name": act.name,
            "description": act.description,
            "zone": act.zone,
            "time_required": act.time_required,
            "age_range": act.age_range,
            "category": act.category,
            "instructions": act.description,
            "objective": f"Cognitive improvement in {act.category}"
        } for act in activities]
