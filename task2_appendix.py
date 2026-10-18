
import random
from collections import defaultdict, Counter

# Student-specific inputs
LAST_NAME = "LANCION"
SEED_NUM = 7
FAVORITE_ARTIST = "CUP OF JOE"

random.seed(SEED_NUM)

# Subjects
subjects = [
    "PROGRAMMING",
    "MATHEMATICS",
    "ELECTRONICS",
    "PHYSICS",
    "ENGLISH"
]

# Generate five student names
students = [
    f"{LAST_NAME}_Student_{i}"
    for i in range(1, 6)
]

# Generate performance records
records = []

for i, student in enumerate(students):
    for j, subject in enumerate(subjects):

        # Use artist character positions and seed
        char_position = ord(
            FAVORITE_ARTIST[(i + j) % len(FAVORITE_ARTIST)]
        )

        score = 50 + (
            char_position + SEED_NUM + i * 7 + j * 5
        ) % 51

        # Add one incomplete record
        if i == 1 and j == 4:
            score = None

        records.append({
            "student": student,
            "subject": subject,
            "score": score
        })

# Add one repeated student-subject record
records.append(records[0].copy())

# Categorize scores
def get_category(score):
    if score is None:
        return "INCOMPLETE"
    elif score >= 90:
        return "EXCELLENT"
    elif score >= 80:
        return "GOOD"
    elif score >= 70:
        return "SATISFACTORY"
    else:
        return "NEEDS IMPROVEMENT"

for record in records:
    record["category"] = get_category(record["score"])

# Identify repeated records
seen = set()
repeated = []

for record in records:
    key = (record["student"], record["subject"])

    if key in seen:
        repeated.append(record)
    else:
        seen.add(key)

# Identify incomplete records
incomplete = [
    r for r in records if r["score"] is None
]

# Organize records by student and subject
organized = defaultdict(dict)

for record in records:
    organized[record["student"]][record["subject"]] = record

# Display generated records
print("=" * 75)
print("STUDENT PERFORMANCE DATA ANALYZER")
print("=" * 75)

print("\n1. GENERATED PERFORMANCE RECORDS")

for r in records:
    print(
        f"{r['student']:22} | "
        f"{r['subject']:15} | "
        f"{str(r['score']):5} | {r['category']}"
    )

# Repeated and incomplete records
print("\n2. REPEATED RECORDS")
for r in repeated:
    print(f"{r['student']} - {r['subject']}")

print("\n3. INCOMPLETE RECORDS")
for r in incomplete:
    print(f"{r['student']} - {r['subject']} - Missing score")

# Performance category summary
categories = Counter(
    r["category"] for r in records
)

print("\n4. PERFORMANCE CATEGORY SUMMARY")
for category, count in sorted(categories.items()):
    print(f"{category}: {count}")

# Student summaries
print("\n5. STUDENT PERFORMANCE SUMMARY")

for student in students:
    # Exclude duplicate records and missing scores
    valid_scores = [
        r["score"] for r in records
        if r["student"] == student
        and r["score"] is not None
    ]

    # Remove duplicate student-subject entries
    unique_scores = {}
    for r in records:
        if (r["student"] == student
                and r["score"] is not None):
            unique_scores[r["subject"]] = r["score"]

    scores = list(unique_scores.values())

    average = sum(scores) / len(scores) if scores else 0

    print(
        f"{student}: Average = {average:.2f}, "
        f"Valid Subjects = {len(scores)}"
    )

# Subject summaries
print("\n6. SUBJECT PERFORMANCE SUMMARY")

for subject in subjects:
    unique_records = {}

    for r in records:
        if r["subject"] == subject and r["score"] is not None:
            unique_records[r["student"]] = r["score"]

    scores = list(unique_records.values())

    average = sum(scores) / len(scores) if scores else 0

    print(
        f"{subject}: Average = {average:.2f}, "
        f"Students = {len(scores)}"
    )

# Ordered results
print("\n7. ORDERED RESULTS (HIGHEST TO LOWEST)")

ordered = sorted(
    [
        r for r in records
        if r["score"] is not None
    ],
    key=lambda r: r["score"],
    reverse=True
)

# Display each student-subject combination once
displayed = set()

for r in ordered:
    key = (r["student"], r["subject"])

    if key not in displayed:
        print(
            f"{r['student']:22} | "
            f"{r['subject']:15} | "
            f"{r['score']:3} | {r['category']}"
        )
        displayed.add(key)

print("\nREPORT COMPLETE")
