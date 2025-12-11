# Minimal helpers for converting ObjectId
from bson import ObjectId

def oid(oid):
    return str(oid) if isinstance(oid, ObjectId) else oid