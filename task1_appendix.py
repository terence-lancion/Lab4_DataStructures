
# Engineering Test Data Organizer

LAST_NAME = "LANCION"
SEED_NUM = 8
FAVORITE_ARTIST = "CUP OF JOE"

CATEGORIES = [
    "TEMPERATURE",
    "VOLTAGE",
    "CURRENT",
    "PRESSURE",
    "SPEED"
]

# Category-specific bases, ranges, and units
CATEGORY_SETTINGS = {
    "TEMPERATURE": (20, 31, "°C"),
    "VOLTAGE": (100, 201, "V"),
    "CURRENT": (1, 10, "A"),
    "PRESSURE": (90, 41, "kPa"),
    "SPEED": (10, 91, "m/s")
}

# Remove spaces so character positions can be used
artist_chars = FAVORITE_ARTIST.replace(" ", "")

# Generate five test sources
sources = [f"{LAST_NAME}_T{i}" for i in range(1, 6)]

records = []

# Generate ten original records
for i in range(10):
    source = sources[i % 5]
    category = CATEGORIES[i % 5]

    # Use the artist's character position and seed number
    char_position = i % len(artist_chars)
    character_code = ord(artist_chars[char_position].upper())

    base, span, unit = CATEGORY_SETTINGS[category]

    value = base + (
        character_code + (char_position + 1) * SEED_NUM
    ) % span

    records.append({
        "source": source,
        "category": category,
        "value": value,
        "unit": unit
    })

# Add one repeated source/category combination
first_record = records[0]
records.append({
    "source": first_record["source"],
    "category": first_record["category"],
    "value": first_record["value"],
    "unit": first_record["unit"]
})

# 1. Display original generated data
print("=" * 75)
print("ENGINEERING TEST DATA ORGANIZER")
print("=" * 75)
print(f"LAST_NAME: {LAST_NAME}")
print(f"SEED_NUM: {SEED_NUM}")
print(f"FAVORITE_ARTIST: {FAVORITE_ARTIST}")
print(f"Number of records: {len(records)}")

print("\n1. GENERATED TEST DATA")
print("-" * 75)
print(f"{'No.':<5}{'Source':<18}{'Category':<18}{'Value':<12}{'Unit'}")

for i, record in enumerate(records, start=1):
    print(
        f"{i:<5}{record['source']:<18}"
        f"{record['category']:<18}"
        f"{record['value']:<12}{record['unit']}"
    )

# 2. Organize records by source and category
organized = sorted(
    records,
    key=lambda r: (r["source"], r["category"], r["value"])
)

print("\n2. ORGANIZED TEST DATA")
print("-" * 75)

for record in organized:
    print(
        f"{record['source']:<18}"
        f"{record['category']:<18}"
        f"{record['value']} {record['unit']}"
    )

# 3. Identify repeated and distinct records
seen = set()
repeated = []
distinct = []

for record in records:
    key = (record["source"], record["category"])

    if key in seen:
        repeated.append(key)
    else:
        seen.add(key)
        distinct.append(key)

print("\n3. REPEATED AND DISTINCT DATA")
print("-" * 75)
print("Repeated source/category combinations:")

if repeated:
    for source, category in repeated:
        print(f"{source} - {category}")
else:
    print("None")

print(f"Distinct source/category combinations: {len(seen)}")
print(f"Total records: {len(records)}")
print(f"Unique source/category combinations: {len(seen)}")

# 4. Numerical and categorical summaries
print("\n4. NUMERICAL AND CATEGORICAL SUMMARIES")
print("-" * 75)

for category in CATEGORIES:
    values = [
        r["value"] for r in records
        if r["category"] == category
    ]

    if values:
        print(f"\nCategory: {category}")
        print(f"Count: {len(values)}")
        print(f"Minimum: {min(values)}")
        print(f"Maximum: {max(values)}")
        print(f"Mean: {sum(values) / len(values):.2f}")

print("\nRecords per source:")
for source in sources:
    count = sum(1 for r in records if r["source"] == source)
    print(f"{source}: {count}")

# 5. Processed results by source and category
print("\n5. PROCESSED RESULTS")
print("-" * 75)

for source in sources:
    print(f"\nSource: {source}")

    for category in CATEGORIES:
        values = [
            r["value"] for r in records
            if r["source"] == source
            and r["category"] == category
        ]

        if values:
            print(
                f"  {category}: {values} "
                f"| Count: {len(values)}"
                f" | Mean: {sum(values) / len(values):.2f}"
            )

# 6. Ordered results
ordered_values = sorted(
    records,
    key=lambda r: (r["category"], r["value"])
)

print("\n6. ORDERED RESULTS (CATEGORY, THEN VALUE)")
print("-" * 75)

for record in ordered_values:
    print(
        f"{record['category']:<18}"
        f"{record['value']:<8}"
        f"{record['unit']:<8}"
        f"{record['source']}"
    )

# 7. Final consolidated summary
print("\n7. FINAL SUMMARY")
print("-" * 75)
print(f"Total measurement records: {len(records)}")
print(f"Test sources: {len(sources)}")
print(f"Measurement categories: {len(CATEGORIES)}")
print(f"Distinct source/category combinations: {len(seen)}")
print(f"Repeated source/category entries: {len(repeated)}")
print("Dataset successfully generated, organized, and summarized.")


# FINAL OUTPUT: FINAL ORGANIZED AND SUMMARIZED TEST DATASET

from collections import defaultdict

final_dataset = defaultdict(list)

# 1. Organize measurements by test source and category
for record in records:
    key = (record["source"], record["category"])
    final_dataset[key].append(record["value"])

# 2. Display the consolidated dataset with summaries
print("\n" + "=" * 65)
print("FINAL ORGANIZED AND SUMMARIZED TEST DATASET")
print("=" * 65)

for (source, category), measurements in sorted(final_dataset.items()):
    total = sum(measurements)
    count = len(measurements)
    average = total / count

    print(f"\nTest Source: {source}")
    print(f"Category: {category}")
    print(f"Measurements: {measurements}")
    print(f"Number of Measurements: {count}")
    print(f"Total: {total}")
    print(f"Minimum: {min(measurements)}")
    print(f"Maximum: {max(measurements)}")
    print(f"Average: {average:.2f}")

# 3. Overall dataset summary
all_values = [
    value
    for measurements in final_dataset.values()
    for value in measurements
]

print("\n" + "=" * 65)
print("OVERALL DATASET SUMMARY")
print("=" * 65)
print(f"Total Test Sources: {len(set(r['source'] for r in records))}")
print(f"Total Categories: {len(set(r['category'] for r in records))}")
print(f"Total Measurement Records: {len(records)}")
print(f"Distinct Source-Category Groups: {len(final_dataset)}")
print(f"Overall Minimum: {min(all_values)}")
print(f"Overall Maximum: {max(all_values)}")
print(f"Overall Average: {sum(all_values) / len(all_values):.2f}")
print(f"Overall Total: {sum(all_values)}")
print("=" * 65)