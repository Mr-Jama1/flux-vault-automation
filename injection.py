import requests
import time

# --- CONFIGURATION ---
ENDPOINT = 'endpoint'
PROJECT_ID = 'project_id'
DATABASE_ID = 'database_id'
COLLECTION_ID = 'courses'
API_KEY = 

headers = {
    'Content-Type': 'application/json',
    'X-Appwrite-Project': PROJECT_ID,
    'X-Appwrite-Key': API_KEY
}

# --- THE 100 COURSE MASTER LIST ---
course_templates = [
    ("Harvard CS50x: Computer Science", "Computer Science"),
    ("Google Cybersecurity Professional", "Cybersecurity"),
    ("IBM Data Science Professional", "Data Science"),
    ("MIT: Introduction to Algorithms", "Computer Science"),
    ("Stanford: Machine Learning", "AI"),
    ("Meta Front-End Developer", "Web Dev"),
    ("AWS Certified Solutions Architect", "Cloud"),
    ("The Odin Project: Full Stack", "Web Dev"),
    ("Python for Everybody", "Python"),
    ("DeepLearning.AI: Generative AI", "AI"),
    ("Ethical Hacking: CEH Prep", "Cybersecurity"),
    ("Flutter & Dart Mastery", "Mobile Dev"),
    ("Blockchain Council: Certified Developer", "Blockchain"),
    ("Microsoft Azure Fundamentals", "Cloud"),
    ("Data Structures in C++", "Computer Science"),
    ("React Native Blueprint", "Mobile Dev"),
    ("Penetration Testing with Kali Linux", "Cybersecurity"),
    ("Rust for Systems Programming", "Coding"),
    ("Natural Language Processing Specialization", "AI"),
    ("Go: The Complete Boot Camp", "Coding")
]

def inject():
    print(f"🚀 Starting injection of 100 premium courses...")
    for i in range(100):
        # Rotate through templates to fill 100 slots
        template = course_templates[i % len(course_templates)]
        title = f"{template[0]} (Batch {i//len(course_templates) + 1})" if i >= len(course_templates) else template[0]
        
        payload = {
            "documentId": "unique()",
            "data": {
                "title": title,
                "category": template[1],
                "redirectUrl": "https://google.com",
                "isHot": i % 4 == 0, # Every 4th course gets the 'Hot' badge
                "isPremium": True,
                "description": f"Master {template[1]} with this world-class syllabus and hands-on projects."
            }
        }
        
        response = requests.post(
            f"{ENDPOINT}/databases/{DATABASE_ID}/collections/{COLLECTION_ID}/documents",
            headers=headers,
            json=payload
        )
        
        if response.status_code == 201:
            print(f"✅ [{i+1}/100] Successfully Created: {title}")
        else:
            print(f"❌ Error at {title}: {response.text}")
        
        # 0.1s sleep to be polite to the Appwrite API
        time.sleep(0.1)

if __name__ == "__main__":
    inject()
    print("\n🎉 Injection complete! Refresh your Appwrite Dashboard now.")
