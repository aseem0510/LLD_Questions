from typing import Dict, List
from seat_lock import SeatLock

class SeatLockProvider:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.locks = {}  # {show_id: {seat_id: SeatLock}}
        return cls._instance

    def lock_seats(self, show_id: str, seat_ids: List[str], user_id: str, duration: int = 10):
        if show_id not in self.locks:
            self.locks[show_id] = {}

        for seat_id in seat_ids:
            if not self.is_seat_available(show_id, seat_id):
                raise Exception(f"Seat {seat_id} already locked")

            print(f"Locking seat {seat_id} for user {user_id} until {SeatLock(seat_id, user_id, duration).expiry_time}")
            self.locks[show_id][seat_id] = SeatLock(seat_id, user_id, duration)

    def is_seat_available(self, show_id: str, seat_id: str) -> bool:
        if show_id not in self.locks:
            return True

        lock = self.locks[show_id].get(seat_id)
        if lock is None:
            return True

        if lock.is_expired():
            # ✅ Clean up expired lock
            del self.locks[show_id][seat_id]
            return True

        return False

    def get_locked_seats(self, show_id: str) -> List[str]:
        if show_id not in self.locks:
            return []

        expired_seats = []
        locked_seats = []

        for seat_id, lock in self.locks[show_id].items():
            if lock.is_expired():
                expired_seats.append(seat_id)
            else:
                locked_seats.append(seat_id)

        # ✅ Remove all expired seat locks
        for seat_id in expired_seats:
            del self.locks[show_id][seat_id]

        return locked_seats

    def unlock_seats(self, show_id: str, seat_ids: List[str]):
        if show_id in self.locks:
            for seat_id in seat_ids:
                if seat_id in self.locks[show_id]:
                    del self.locks[show_id][seat_id]
    
    def is_seat_locked_by_user(self, show_id: str, seat_id: str, user_id: str) -> bool:
        if show_id not in self.locks:
            return False

        lock = self.locks[show_id].get(seat_id)
        if lock is None or lock.is_expired():
            return False

        return lock.user_id == user_id
