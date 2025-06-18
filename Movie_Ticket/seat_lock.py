from datetime import datetime, timedelta

class SeatLock:
    def __init__(self, seat_id: str, user_id: str, lock_duration_minutes: int):
        self.seat_id = seat_id
        self.user_id = user_id
        self.lock_time = datetime.now()
        self.expiry_time = self.lock_time + timedelta(minutes=lock_duration_minutes)

    def is_expired(self) -> bool:
        return datetime.now() > self.expiry_time
