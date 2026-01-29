from datetime import datetime
from typing import List, Dict
from collections import defaultdict
import itertools
from movie import Movie
from theater import Theater
from show import Show
from booking import Booking, BookingStatus
from seat import Seat, SeatStatus
from user import User
from seat_lock_provider import SeatLockProvider


class MovieTicketBookingSystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.movies = []
            cls._instance.theaters = []
            cls._instance.shows = {}
            cls._instance.bookings = {}
            cls._instance.booking_counter = itertools.count(1)
            cls._instance.lock_provider = SeatLockProvider()
        return cls._instance

    @staticmethod
    def get_instance():
        if MovieTicketBookingSystem._instance is None:
            MovieTicketBookingSystem()
        return MovieTicketBookingSystem._instance

    def add_movie(self, movie: Movie):
        self.movies.append(movie)

    def add_theater(self, theater: Theater):
        self.theaters.append(theater)

    def add_show(self, show: Show):
        self.shows[show.id] = show

    def get_movies(self) -> List[Movie]:
        return self.movies

    def get_theaters(self) -> List[Theater]:
        return self.theaters

    def get_show(self, show_id: str) -> Show:
        return self.shows.get(show_id)

    def book_tickets(self, user: User, show: Show, selected_seats: List[Seat]) -> Booking:
        seat_ids = [seat.id for seat in selected_seats]
        if self._are_seats_available(show, seat_ids, user):
            # Only lock seats that are not already locked by the same user
            for seat_id in seat_ids:
                if not self.lock_provider.is_seat_locked_by_user(show.id, seat_id, user.id):
                    try:
                        self.lock_provider.lock_seats(show.id, [seat_id], user.id, 10)
                    except Exception as e:
                        print(f"Failed to lock seat {seat_id}: {str(e)}")
                        return None

            self._mark_seats_as_booked(show, selected_seats)
            total_price = self._calculate_total_price(selected_seats)
            booking_id = self._generate_booking_id()
            booking = Booking(booking_id, user, show, selected_seats, total_price, BookingStatus.PENDING)
            self.bookings[booking_id] = booking
            return booking

        return None

    def _are_seats_available(self, show: Show, seat_ids: List[str], user: User) -> bool:
        for seat_id in seat_ids:
            # allow if not locked or locked by the same user
            if not self.lock_provider.is_seat_available(show.id, seat_id):
                if not self.lock_provider.is_seat_locked_by_user(show.id, seat_id, user.id):
                    return False

            show_seat = show.seats.get(seat_id)
            if show_seat is None or show_seat.status != SeatStatus.AVAILABLE:
                return False
        return True

    def _mark_seats_as_booked(self, show: Show, selected_seats: List[Seat]):
        for seat in selected_seats:
            show_seat = show.seats.get(seat.id)
            show_seat.status = SeatStatus.BOOKED

    def _calculate_total_price(self, selected_seats: List[Seat]) -> float:
        return sum(seat.price for seat in selected_seats)

    def _generate_booking_id(self) -> str:
        booking_number = next(self._instance.booking_counter)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"BKG{timestamp}{booking_number:06d}"

    def confirm_booking(self, booking_id: str):
        booking = self.bookings.get(booking_id)
        if booking and booking.status == BookingStatus.PENDING:
            booking.status = BookingStatus.CONFIRMED
            # Process payment and send confirmation
            # ...
            self.lock_provider.unlock_seats(booking.show.id, [seat.id for seat in booking.seats])

    def cancel_booking(self, booking_id: str):
        booking = self.bookings.get(booking_id)
        if booking and booking.status != BookingStatus.CANCELLED:
            booking.status = BookingStatus.CANCELLED
            self._mark_seats_as_available(booking.show, booking.seats)
            # Process refund and send cancellation notification
            # ...
            self.lock_provider.unlock_seats(booking.show.id, [seat.id for seat in booking.seats])


    def _mark_seats_as_available(self, show: Show, seats: List[Seat]):
        for seat in seats:
            show_seat = show.seats.get(seat.id)
            show_seat.status = SeatStatus.AVAILABLE

    # def get_locked_seats(self, show: Show) -> List[str]:
    #     return self.seat_lock_provider.get_locked_seats(show)