import os

# Set the DATABASE_URL for production environment (Render's external database URL)
DATABASE_URL = os.environ.get(
    'DATABASE_URL', 
    'postgresql://cognitive_activity_recommendation_system_user:VyR8CAl9FSHJ8AbcAvdXTwaIp8XKAKde@dpg-curjj01opnds73f3mej0-a.oregon-postgres.render.com:5432/cognitive_activity_recommendation_system'
)

DEBUG = True
