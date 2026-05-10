<<<<<<< HEAD
from src.user import User
from src.schedule import Schedule
from src.booking import Booking
from src.payment import Payment
from src.database import Database
from src.notification import Notification
from src.search import Search


def main():
    print("===== PRASA SMART PASSENGER SYSTEM =====\n")

    # -------------------------
    # 1. USER LOGIN
    # -------------------------
    user = User("admin", "1234")
    print("LOGIN:")
    print(user.login("admin", "1234"))

    print("\n-------------------------")

    # -------------------------
    # 2. VIEW TRAIN SCHEDULE
    # -------------------------
    schedule = Schedule()
    print("LIVE TRAIN SCHEDULE:")
    schedules = schedule.display()

    for s in schedules:
        print(s)

    print("\n-------------------------")

    # -------------------------
    # 3. SEARCH MODULE
    # -------------------------
    search = Search()
    print("SEARCH RESULTS (JHB-Pretoria):")
    results = search.search_train(schedules, "JHB-Pretoria")
    for r in results:
        print(r)

    print("\n-------------------------")

    # -------------------------
    # 4. BOOKING SYSTEM
    # -------------------------
    booking = Booking("admin", "PRASA001")
    print("BOOKING:")
    print(booking.create_booking())

    print("\n-------------------------")

    # -------------------------
    # 5. PAYMENT SYSTEM
    # -------------------------
    payment = Payment(150)
    print("PAYMENT:")
    print(payment.process_payment())

    print("\n-------------------------")

    # -------------------------
    # 6. NOTIFICATIONS (DELAYS)
    # -------------------------
    notification = Notification()
    updates = schedule.get_updates()

    print("NOTIFICATIONS:")
    for u in updates:
        print(notification.send(u))

    print("\n-------------------------")

    # -------------------------
    # 7. DATABASE (SINGLETON)
    # -------------------------
    db = Database()
    db.save("last_booking", "PRASA001")

    print("DATABASE:")
    print("Saved booking:", db.get("last_booking"))

    print("\n===== SYSTEM COMPLETE =====")


if __name__ == "__main__":
    main()
=======
from factories.repository_factory import RepositoryFactory
from models.train import Train

repo = RepositoryFactory.get_train_repository("MEMORY")

train1 = Train("T001", "Blue Train", "Johannesburg to Pretoria")
train2 = Train("T002", "Metro Rail", "Soweto to Johannesburg")

repo.save(train1)
repo.save(train2)

print("All Trains:")
for train in repo.find_all():
    print(train)

print("\nFind Train By ID:")
print(repo.find_by_id("T001"))

repo.delete("T002")

print("\nAfter Delete:")
for train in repo.find_all():
    print(train)
>>>>>>> 8cfd57e75642603a85c57726a420044696d55afc
