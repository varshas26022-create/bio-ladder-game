# BioLadder Questions Module

Save this file as:

```bash
questions.py
```

Use this along with your main `bioladder.py` file.

---

```python
# Biology Questions Database

questions = {
    1: {
        "question": "What is the basic unit of life?",
        "answer": "cell"
    },

    2: {
        "question": "Which organ pumps blood throughout the body?",
        "answer": "heart"
    },

    3: {
        "question": "What is the powerhouse of the cell?",
        "answer": "mitochondria"
    },

    4: {
        "question": "Which blood group is called universal donor?",
        "answer": "o negative"
    },

    5: {
        "question": "Largest organ in the human body?",
        "answer": "skin"
    },

    6: {
        "question": "What carries oxygen in blood?",
        "answer": "hemoglobin"
    },

    7: {
        "question": "Which vitamin is produced from sunlight?",
        "answer": "vitamin d"
    },

    8: {
        "question": "Human body has how many lungs?",
        "answer": "2"
    },

    9: {
        "question": "Which organ filters blood in the body?",
        "answer": "kidney"
    },

    10: {
        "question": "What is the normal temperature of the human body in Celsius?",
        "answer": "37"
    },

    11: {
        "question": "Which part of the brain controls balance?",
        "answer": "cerebellum"
    },

    12: {
        "question": "What is the study of bones called?",
        "answer": "osteology"
    },

    13: {
        "question": "Which blood cells help fight infection?",
        "answer": "white blood cells"
    },

    14: {
        "question": "What is the largest bone in the human body?",
        "answer": "femur"
    },

    15: {
        "question": "Which gas do humans inhale for respiration?",
        "answer": "oxygen"
    }
}


# Function to Retrieve Question

def get_question(number):
    return questions.get(number, None)


# Example Usage
if __name__ == "__main__":
    q = get_question(1)

    print("Question:", q["question"])
    print("Answer:", q["answer"])
```

---

## Purpose of This File

This module stores biology-related quiz questions separately from the main game file.

Benefits:

* Cleaner code structure
* Easy question management
* Better project organization
* Scalable educational gameplay
