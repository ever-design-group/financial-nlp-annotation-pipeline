#!/usr/bin/env python3
"""Dataset Validation Script - Project 1B"""

import json
import jsonschema
from collections import Counter

def validate_dataset(filepath='data/final_dataset.json'):
    """Validate final dataset against schema."""
    
    schema = {
        "type": "object",
        "properties": {
            "communication_id": {"type": "string"},
            "channel": {"type": "string", "enum": ["email", "live_chat", "social_media", "call_transcript"]},
            "raw_text": {"type": "string"},
            "word_count": {"type": "integer", "minimum": 1},
            "language_primary": {"type": "string"},
            "language_secondary": {"type": ["string", "null"]},
            "code_switched": {"type": "boolean"},
            "sentiment": {
                "type": "object",
                "properties": {
                    "satisfaction": {"type": "integer", "minimum": 1, "maximum": 5},
                    "urgency": {"type": "integer", "minimum": 1, "maximum": 5},
                    "frustration": {"type": "integer", "minimum": 1, "maximum": 5},
                    "confusion": {"type": "integer", "minimum": 1, "maximum": 5}
                },
                "required": ["satisfaction", "urgency", "frustration", "confusion"]
            },
            "intent": {
                "type": "object",
                "properties": {
                    "complaint": {"type": "boolean"},
                    "query": {"type": "boolean"},
                    "request": {"type": "boolean"},
                    "feedback": {"type": "boolean"},
                    "escalation": {"type": "boolean"}
                }
            },
            "topic": {
                "type": "object",
                "properties": {
                    "billing": {"type": "boolean"},
                    "fraud": {"type": "boolean"},
                    "account_access": {"type": "boolean"},
                    "product_inquiry": {"type": "boolean"},
                    "regulatory_complaint": {"type": "boolean"}
                }
            },
            "metadata": {
                "type": "object",
                "properties": {
                    "sarcasm_detected": {"type": "boolean"},
                    "contains_pii_placeholder": {"type": "boolean"},
                    "escalation_event_present": {"type": "boolean"},
                    "annotator_notes": {"type": "string"},
                    "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
                    "edge_case": {"type": "boolean"},
                    "guideline_version_used": {"type": "string"}
                }
            },
            "annotator_id": {"type": "string"},
            "annotation_timestamp": {"type": "string"},
            "annotation_duration_seconds": {"type": "integer"}
        },
        "required": ["communication_id", "channel", "raw_text", "sentiment", "intent", "topic", "metadata"]
    }
    
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return False
    
    print("=" * 60)
    print("DATASET VALIDATION REPORT")
    print("=" * 60)
    
    total = len(data)
    if total == 500:
        print(f"✅ Total items: {total}")
    else:
        print(f"❌ Expected 500 items, got {total}")
        return False
    
    ids = [item.get('communication_id') for item in data]
    if len(set(ids)) == len(ids):
        print("✅ All communication_id unique")
    else:
        print("❌ Duplicate communication_id found")
        return False
    
    errors = []
    for i, item in enumerate(data):
        try:
            jsonschema.validate(instance=item, schema=schema)
        except jsonschema.ValidationError as e:
            errors.append(f"Item {i}: {e.message}")
    
    if errors:
        print(f"❌ Found {len(errors)} validation errors")
        for error in errors[:5]:
            print(f"  - {error}")
        return False
    else:
        print("✅ All items validate against schema")
    
    missing_intent = []
    for item in data:
        if not any(item.get('intent', {}).values()):
            missing_intent.append(item.get('communication_id'))
    
    if missing_intent:
        print(f"❌ {len(missing_intent)} items have no intent")
        return False
    else:
        print("✅ All items have at least one intent")
    
    missing_topic = []
    for item in data:
        if not any(item.get('topic', {}).values()):
            missing_topic.append(item.get('communication_id'))
    
    if missing_topic:
        print(f"❌ {len(missing_topic)} items have no topic")
        return False
    else:
        print("✅ All items have at least one topic")
    
    channels = Counter([item.get('channel') for item in data])
    print("\n📊 Channel Distribution:")
    for channel, count in channels.items():
        print(f"  {channel}: {count} ({count/len(data)*100:.1f}%)")
    
    print("\n📊 Sentiment Distribution (Averages):")
    for dim in ['satisfaction', 'urgency', 'frustration', 'confusion']:
        values = [item.get('sentiment', {}).get(dim, 0) for item in data]
        avg = sum(values) / len(values) if values else 0
        print(f"  {dim.capitalize()}: {avg:.2f}")
    
    print("\n" + "=" * 60)
    print("✅ DATASET VALIDATION COMPLETE")
    print("=" * 60)
    return True

if __name__ == "__main__":
    validate_dataset()
