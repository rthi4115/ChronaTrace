from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
import os
import sys

# Add the current directory to sys.path to find the api module
sys.path.append(os.getcwd())

from api.db.models import Base, Evidence, TimelineEvent

# Use a relative path or absolute path to the database
DB_PATH = "api/db/chronatrace.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def seed():
    db = SessionLocal()
    try:
        # 1. Create a Mock Evidence
        evidence = Evidence(
            filename="autopsy_report_ethan_roy.pdf",
            file_type="PDF",
            source_path="api/db/uploads/autopsy_report_ethan_roy.pdf",
            processed=True
        )
        db.add(evidence)
        db.commit()
        db.refresh(evidence)

        # 2. Add Contradictory Events
        # Event 1: Time of Death (TOD)
        tod_event = TimelineEvent(
            evidence_id=evidence.id,
            timestamp=datetime.datetime(2023, 10, 27, 21, 0, 0), # 9:00 PM
            actor="Medical Examiner",
            action="Pronounced Dead",
            location="Saint Jude Hospital",
            description="Official TOD established via body temperature and rigor mortis analysis."
        )
        db.add(tod_event)

        # Event 2: Phone Activity AFTER TOD
        phone_event = TimelineEvent(
            evidence_id=evidence.id,
            timestamp=datetime.datetime(2023, 10, 27, 22, 30, 0), # 10:30 PM
            actor="Victim's Phone",
            action="Outgoing WhatsApp Message",
            location="12th Ave Sector 4",
            description="Device sent a message: 'I'm almost home, see you soon.'"
        )
        db.add(phone_event)

        db.commit()
        print(f"SUCCESS: Seeded Evidence ID {evidence.id}")
        print(f"LOGIC GAP: TOD at 21:00 vs Phone activity at 22:30.")

    finally:
        db.close()

if __name__ == "__main__":
    seed()
