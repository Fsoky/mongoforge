<h1 align="center">MongoForge</h1>
<p align="center">Magic filters for MongoDB</p>

## Installation

```bash
pip install mongoforge
```

## Basic example

```python
from pymongo import MongoClient
from mongoforge import F

cluster = MongoClient(...)
collection = cluster.db.users

if user := collection.find_one(F._id == 1): # {"_id": 1}
    print(user)
else:
    collection.insert_one(...)
```

## Available filters

| MongoDB Operator | Python Expression | Example Output          |
| ---------------- | ----------------- | ----------------------- |
| `$eq`            | `F.age == 21`     | `{"age": 21}`           |
| `$gt`            | `F.age > 21`      | `{"age": {"$gt": 21}}`  |
| `$lt`            | `F.age < 21`      | `{"age": {"$lt": 21}}`  |
| `$gte`           | `F.age >= 21`     | `{"age": {"$gte": 21}}` |
| `$lte`           | `F.age <= 21`     | `{"age": {"$lte": 21}}` |
