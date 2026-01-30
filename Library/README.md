1️⃣ Requirements

✅ Functional Requirements

1- Add, remove, update, and search books.
2- Register and unregister members.
3- Borrow a book:
    - Book must be available
    - Member must not exceed max borrow limit
4- Return a book:
    - Calculate overdue days
    - Calculate fine if overdue
    - Trigger fine payment
5- Track borrowing history with timestamps.
6- Prevent unregistering members with active borrowings.
7- Support multiple fine calculation rules.
8- Support multiple payment methods.

✅ Non-Functional Requirements

- Extensibility – New fine rules / payment modes without code changes.
- Maintainability – Clear separation of responsibilities.
- Scalability – Ready for DB/search service integration.
- Consistency – No invalid borrow / return operations.
- Testability – Each component independently testable.
- Thread-safety (future) – Design allows safe synchronization.

2️⃣ Classes, Interfaces & Responsibilities
1- Core Domain
    - Book – Represents a book in catalog.
    - Member – Represents a library member.
    - BorrowTransaction – Tracks borrow timestamp & ownership.

2- Management
    - LibraryManager (Singleton) – Orchestrates system operations.

3- Policy
    - FinePolicy (interface) – Fine calculation abstraction.
    - DefaultFinePolicy – Default fine logic.

4- Payment
    - PaymentStrategy (interface) – Payment abstraction.
    - UPIPayment / CreditCardPayment – Concrete strategies.
    - PaymentProcessor – Executes payment.


UML Relationships (Explain verbally)

    - LibraryManager has-a FinePolicy
    - PaymentProcessor uses PaymentStrategy
    - BorrowTransaction associates Member ↔ Book
    - Concrete strategies implement interfaces

3️⃣ SOLID Principles Used
| Principle | Applied Where                                  |
| --------- | ---------------------------------------------- |
| SRP       | Book, Member, FinePolicy, PaymentProcessor     |
| OCP       | Add new fine/payment without modifying manager |
| LSP       | Any FinePolicy can replace another             |
| ISP       | Small, focused interfaces                      |
| DIP       | LibraryManager depends on abstractions         |

4️⃣ Design Patterns Used
| Pattern     | Usage                       |
| ----------- | --------------------------- |
| Singleton   | LibraryManager              |
| Strategy    | Payment methods             |
| Policy      | Fine calculation            |
| Composition | Manager → Policy / Strategy |
