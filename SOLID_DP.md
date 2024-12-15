# SOLID Principles and Design Patterns in the Pizza Restaurant System

## 1. Factory Pattern

### SOLID Principles Addressed:
- **Single Responsibility Principle (SRP):**
  - The `PizzaFactory` class has one responsibility: creating pizza objects.
- **Open/Closed Principle (OCP):**
  - Adding a new pizza type doesn’t require modifying existing code, only extending the factory.

### How It Helps:
- Keeps the creation logic centralized and separate from the main application.
- Avoids code duplication and makes adding new pizza types easier.

---
