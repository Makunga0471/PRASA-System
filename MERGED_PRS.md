<img width="1323" height="633" alt="image" src="https://github.com/user-attachments/assets/3eeb42c0-6093-4c6e-b39d-a7c38a264c43" /># MERGED PRS

## PR 1
Project: the it code academy

PR Link: https://github.com/keo-codes/the-it-code-academy/pull/55

##   Pull Request Title

Added a search endpoint for students.

## Summary
Allow viewing all courses for a student.

## Changes

- Added GET /api/students/search
- Added search logic in StudentService

## Testing

- Tested with multiple names
- API returns matching students


Status: Merged

---

## PR 2
Project: UniMatch University Application System

PR Link:https://github.com/Mabotse-Mosima/UniMatch-University-Application-System/pull/79

##   Pull Request Title

Feature: Validate required documents before application submission

## Summary

Added validation to ensure all required programme documents
have been uploaded before an application can be submitted.

## Changes

- Added missing_documents() method
- Updated can_submit() validation
- Improved submission error handling

## Benefits

Prevents incomplete applications from being submitted and
improves application data quality.s


Status: Merged
---

## PR 3
Project:  Manga Book Store System

PR Link:
https://github.com/Vanessa-Ndomba/manga-book-store-system/pull/24
##   Pull Request Title

Feature: Validate required documents before application submission

## Summary

This pull request adds validation to the Manga entity to prevent the creation of manga records with negative prices.
## Problem

Previously, the system allowed manga objects to be created with invalid negative prices, for example:

Manga(
    isbn="123",
    title="Naruto",
    author="Masashi Kishimoto",
    price=-100
)

Negative pricing can lead to incorrect inventory valuation, reporting issues, and inconsistent business data.

## Changes Made

- Added a __post_init__() method to the Manga dataclass.
- Implemented validation to ensure that price is not less than zero.
- Raises a ValueError when an invalid negative price is supplied.

## Example

Before:
- Manga objects could be created with negative prices.

After:
- The system raises:
  ValueError: Price cannot be negative

## Benefits

- Improves data integrity.
- Prevents invalid product records.
- Reduces the risk of pricing and inventory calculation errors.
- Aligns the system with standard e-commerce and bookstore validation practices.

## Testing

Tested with:
- Valid positive prices (accepted).
- Zero price (accepted).
- Negative prices (correctly rejected with ValueError).


Status: Merged
---
