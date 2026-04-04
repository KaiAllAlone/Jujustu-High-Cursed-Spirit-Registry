from app import create_app, db
from app.models import User, Encounter
import random

app = create_app()

# Sample data
usernames = ["Gojo Satoru","Geto Suguru","Nanami Kento","Itadori Yuji","Megumi Fushiguro","Yuta Okkotsu","Panda","Toge Inumaki","Maki Zenin","Nobara Kugisaki"]
emails = [f"{u}@jjk.com" for u in usernames]
password = "test"

titles = [
    "Shibuya Residual Distortion",
    "Subway Platform Entity Sighting",
    "Abandoned Ward Manifestation",
    "Tunnel Breach Incident",
    "School Rooftop Apparition",
    "Forest Boundary Curse",
    "Temple Ruins Disturbance",
    "Late-Night Alley Phenomenon",
    "Highway Overpass Haunting",
    "Cursed Shrine Awakening",
    "Underground Parking Anomaly",
    "Dormitory Whisper Entity",
    "Elevator Loop Incident",
    "Riverbank Shadow Manifestation",
    "Mall Closing Hour Incident",
    "Cinema Hall Presence",
    "Hospital Corridor Entity",
    "Bridge Crossing Apparition",
    "Railway Signal Distortion",
    "Library Silence Phenomenon",
    "Construction Site Curse",
    "Storm Drain Entity Report",
    "Festival Night Disturbance",
    "Warehouse Sector Manifestation",
    "Cursed Playground Event",
    "Mountain Path Haunting",
    "Office Floor Residual Energy",
    "Abandoned Factory Awakening",
    "Basement Entity Containment Failure",
    "Water Tower Distortion",
    "Suburban House Poltergeist",
    "Night Market Curse Activity",
    "School Gym Disturbance",
    "Fog Zone Manifestation",
    "Train Cabin Entity",
    "Parking Lot Shadow Activity",
    "Temple Bell Resonance Incident",
    "Cursed Artifact Awakening",
    "Rooftop Isolation Entity",
    "Sewer Network Disturbance",
    "Underground Lab Anomaly",
    "Bridge Underpass Curse",
    "Hostel Corridor Entity",
    "Night Bus Route Distortion",
    "Graveyard Perimeter Breach",
    "Cursed Mirror Incident",
    "Old Theater Manifestation",
    "Flooded Zone Entity",
    "Deserted Street Phenomenon",
    "Unknown Domain Expansion Trace"
]

grades = ["Special Grade", "Grade 1", "Grade 2", "Grade 3"]

locations = [
    "Tokyo", "Kyoto", "Osaka", "Shibuya", "Unknown Rural Area"
]

descriptions = [
    "A grotesque entity formed from accumulated fear, displaying irregular limb extension and erratic movement.",
    "Residual cursed energy spikes detected, entity appears intermittently under low-light conditions.",
    "Victims report auditory hallucinations followed by sudden disappearance within the affected zone.",
    "Barrier-like distortion observed, suggesting incomplete domain expansion.",
    "Highly aggressive cursed spirit exhibiting rapid regeneration and unstable form.",
    "Entity remains stationary but emits overwhelming pressure affecting nearby individuals.",
    "Multiple witnesses describe a shadow-like figure mimicking human movement patterns.",
    "Cursed energy concentrated around a central object, likely acting as a core.",
    "Distortion field causes spatial disorientation and looping pathways.",
    "Manifestation linked to repeated emotional trauma within the location.",
    "Entity reacts violently to direct observation, escalating in intensity.",
    "Low-grade curse swarm detected, collectively forming a larger pseudo-entity.",
    "Sudden temperature drops accompany the entity’s appearance.",
    "Cursed presence spreads through reflective surfaces, increasing unpredictability.",
    "Victims experience paralysis before visual confirmation of the entity.",
    "Entity appears bound to a specific area, unable to move beyond set limits.",
    "Signs of partial intelligence observed in movement and targeting.",
    "Energy signature fluctuates, making detection inconsistent.",
    "Cursed spirit exhibits territorial aggression toward intruders.",
    "Auditory distortions precede physical manifestation by several seconds.",
    "Entity shows signs of adapting to previous exorcism attempts.",
    "Disturbance intensifies during late hours, especially after midnight.",
    "Cursed energy leaks from underground structures into surrounding area.",
    "Victims report recurring dreams before encountering the entity physically.",
    "Entity leaves behind residual markings resembling unknown symbols.",
    "Multiple overlapping presences detected, possibly indicating layered curses.",
    "Movement pattern suggests hunting behavior rather than random activity.",
    "Entity exhibits sudden bursts of speed followed by complete stillness.",
    "Visual form remains unstable, constantly shifting shape.",
    "Cursed energy density exceeds typical grade classification.",
    "Area remains contaminated even after temporary disappearance of entity.",
    "Entity interacts with electronic devices, causing interference.",
    "Localized gravity distortion observed near manifestation point.",
    "Victims report intense dread without visible cause prior to encounter.",
    "Cursed spirit appears to feed on fear and negative emotions.",
    "Distortion expands gradually, consuming nearby space.",
    "Entity shows resistance to standard exorcism techniques.",
    "Manifestation triggered by specific environmental conditions.",
    "Energy readings suggest presence of a dormant secondary entity.",
    "Cursed zone expands unpredictably, altering terrain perception.",
    "Entity mimics voices of known individuals to lure victims.",
    "Visual contact results in temporary cognitive disruption.",
    "Entity displays coordinated behavior despite lack of physical structure.",
    "Cursed energy pulses rhythmically, similar to a heartbeat.",
    "Affected area shows signs of long-term spiritual contamination.",
    "Entity becomes more visible as emotional tension increases.",
    "Presence detected only through indirect observation methods.",
    "Distortion causes time perception irregularities.",
    "Entity leaves behind a trail of decaying cursed energy.",
    "Possible domain expansion residue detected at epicenter."
]


def seed():
    with app.app_context():
        db.session.query(Encounter).delete()
        db.session.query(User).delete()
        db.session.commit()
        users = []

        # Create users
        for username, email in zip(usernames, emails):
            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            users.append(user)

        db.session.commit()

        # Create encounters
        for _ in range(100):
            u = random.choice(users)

            encounter = Encounter(
                title=random.choice(titles),
                grade=random.choice(grades),
                description=random.choice(descriptions),
                location=random.choice(locations),
                user=u
            )

            db.session.add(encounter)

        db.session.commit()

        print("✅ Database seeded successfully!")


if __name__ == "__main__":
    seed()