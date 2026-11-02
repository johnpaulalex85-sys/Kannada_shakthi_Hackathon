# Phrase data: (Kannada, Roman transliteration, English)
SCENARIOS = {
    "travel": {"title": "Travel", "icon": "🧳", "phrases": [
        ("ನಮಸ್ಕಾರ", "Namaskara", "Hello"),
        ("ಬಸ್ ನಿಲ್ದಾಣ ಎಲ್ಲಿದೆ?", "Bus nildana ellide?", "Where is the bus stand?"),
        ("ಹೋಟೆಲ್ ಎಲ್ಲಿದೆ?", "Hotel ellide?", "Where is the hotel?"),
        ("ಟಿಕೆಟ್ ಎಷ್ಟು?", "Ticket eshtu?", "How much is the ticket?"),
        ("ನನಗೆ ಸಹಾಯ ಬೇಕು", "Nanage sahaya beku", "I need help"),
        ("ಧನ್ಯವಾದಗಳು", "Dhanyavadagalu", "Thank you")]},
    "shopping": {"title": "Shopping", "icon": "🛍️", "phrases": [
        ("ಇದು ಎಷ್ಟು?", "Idu eshtu?", "How much is this?"),
        ("ತುಂಬಾ ದುಬಾರಿ", "Tumba dubari", "Too expensive"),
        ("ಸ್ವಲ್ಪ ಕಡಿಮೆ ಮಾಡಿ", "Svalpa kadime maadi", "Please reduce the price a little"),
        ("ನನಗೆ ಒಂದು ಕೆಜಿ ಬೇಕು", "Nanage ondu kg beku", "I want one kilo"),
        ("ಚಿಲ್ಲರೆ ಇದೆಯಾ?", "Chillare ideya?", "Do you have change?"),
        ("ಯುಪಿಐ ಮೂಲಕ ಪಾವತಿಸಬಹುದಾ?", "UPI moolaka paavatisabahuda?", "Can I pay by UPI?")]},
    "education": {"title": "Education", "icon": "📚", "phrases": [
        ("ನಿಮ್ಮ ಹೆಸರೇನು?", "Nimma hesarenu?", "What is your name?"),
        ("ನನಗೆ ಅರ್ಥವಾಗಲಿಲ್ಲ", "Nanage arthavagalilla", "I did not understand"),
        ("ದಯವಿಟ್ಟು ಮತ್ತೊಮ್ಮೆ ಹೇಳಿ", "Dayavittu mattomme heli", "Please say it once more"),
        ("ನಾನು ಒಂದು ಪ್ರಶ್ನೆ ಕೇಳಬಹುದಾ?", "Naanu ondu prashne kelabahuda?", "May I ask a question?"),
        ("ಗ್ರಂಥಾಲಯ ಎಲ್ಲಿದೆ?", "Granthalaya ellide?", "Where is the library?"),
        ("ಮನೆಕೆಲಸ ಏನು?", "Manekelasa enu?", "What is the homework?")]},
    "healthcare": {"title": "Healthcare", "icon": "🩺", "phrases": [
        ("ನನಗೆ ಹುಷಾರಿಲ್ಲ", "Nanage hushaarilla", "I am not feeling well"),
        ("ನನಗೆ ಜ್ವರ ಇದೆ", "Nanage jvara ide", "I have a fever"),
        ("ನನಗೆ ತಲೆನೋವು ಇದೆ", "Nanage talenovu ide", "I have a headache"),
        ("ಔಷಧಿ ಅಂಗಡಿ ಎಲ್ಲಿದೆ?", "Aushadhi angadi ellide?", "Where is the pharmacy?"),
        ("ನನಗೆ ಇದರಿಂದ ಅಲರ್ಜಿ ಇದೆ", "Nanage idarinda alarji ide", "I am allergic to this"),
        ("ಆಂಬ್ಯುಲೆನ್ಸ್ ಕರೆಯಿರಿ", "Ambulance kareyiri", "Call an ambulance")]},
    "transport": {"title": "Transport", "icon": "🚌", "phrases": [
        ("ರೈಲ್ವೆ ನಿಲ್ದಾಣಕ್ಕೆ ಕರೆದುಕೊಂಡು ಹೋಗಿ", "Railway nildanakke karedukondu hogi", "Take me to the railway station"),
        ("ಮೀಟರ್ ಹಾಕಿ", "Meter haaki", "Please use the meter"),
        ("ಇಲ್ಲಿ ನಿಲ್ಲಿಸಿ", "Illi nillisi", "Stop here"),
        ("ಎಡಕ್ಕೆ ತಿರುಗಿ", "Edakke tirugi", "Turn left"),
        ("ಬಲಕ್ಕೆ ತಿರುಗಿ", "Balakke tirugi", "Turn right"),
        ("ಮೆಜೆಸ್ಟಿಕ್‌ಗೆ ಯಾವ ಬಸ್ ಹೋಗುತ್ತದೆ?", "Majestic-ge yaava bus hoguttade?", "Which bus goes to Majestic?")]},
    "workplace": {"title": "Workplace", "icon": "💼", "phrases": [
        ("ಶುಭೋದಯ", "Shubhodaya", "Good morning"),
        ("ನಾನು ಒಳಗೆ ಬರಬಹುದಾ?", "Naanu olage barabahuda?", "May I come in?"),
        ("ನೀವು ನನಗೆ ಸಹಾಯ ಮಾಡಬಹುದಾ?", "Neevu nanage sahaya maadabahuda?", "Can you help me?"),
        ("ಸಭೆ ಮೂರು ಗಂಟೆಗೆ ಇದೆ", "Sabhe mooru gantege ide", "The meeting is at 3 o'clock"),
        ("ನಾನು ಇದನ್ನು ಇವತ್ತು ಮುಗಿಸುತ್ತೇನೆ", "Naanu idannu ivattu mugisuttene", "I will finish this today"),
        ("ನನಗೆ ನಾಳೆ ರಜೆ ಬೇಕು", "Nanage naale raje beku", "I need leave tomorrow")]},
}

def phrase_dicts(sid):
    s = SCENARIOS[sid]
    return [{"id": f"{sid}-{i}", "scenario": sid, "kn": k, "roman": r, "en": e}
            for i, (k, r, e) in enumerate(s["phrases"])]

def all_phrases():
    return [p for sid in SCENARIOS for p in phrase_dicts(sid)]
