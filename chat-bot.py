# Knowledge base with all states in India
knowledge_base = {
    "emergency_contacts": {
        "police": "100",
        "ambulance": "102",
        "fire": "101",
        "disaster_management": "1070",
    },
    "safety_tips": {
        "earthquake": [
            "Drop, cover, and hold on.",
            "Stay indoors until the shaking stops.",
            "If outdoors, move away from buildings and trees."
        ],
        "flood": [
            "Move to higher ground immediately.",
            "Avoid walking or driving through floodwaters.",
            "Disconnect electrical appliances."
        ],
        "cyclone": [
            "Secure loose items outdoors.",
            "Stay indoors and away from windows.",
            "Keep a radio or mobile device for updates."
        ],
    },
    "locations": {
        "andhra pradesh": {
            "flood_shelters": ["NTR Stadium, Vijayawada", "Indira Gandhi Stadium, Visakhapatnam"],
            "cyclone_shelters": ["Gandhi Grounds, Kakinada", "Municipal Schools, Nellore"],
        },
        "bihar": {
            "flood_shelters": ["Rajendra Nagar, Patna", "Gandhi Maidan, Patna"],
        },
        "gujarat": {
            "cyclone_shelters": ["Nirma University, Ahmedabad", "Kutch Sports Complex, Bhuj"],
        },
        "west bengal": {
            "flood_shelters": ["Salt Lake Stadium, Kolkata", "Rabindra Bharati University, Kolkata"],
            "cyclone_shelters": ["Eco Park, Kolkata", "Jadavpur University Grounds, Kolkata"],
        },
        "tamil nadu": {
            "cyclone_shelters": ["Marina Beach Relief Camps, Chennai", "Anna University Grounds, Chennai"],
        },
        # Add other states here with similar structure
    },
}

# Chatbot logic
def get_emergency_contact(service):
    return knowledge_base["emergency_contacts"].get(service.lower(), "Service not found.")

def get_safety_tips(disaster):
    return knowledge_base["safety_tips"].get(disaster.lower(), "No tips available for this disaster.")

def get_shelter_locations(state, disaster_type):
    state_info = knowledge_base["locations"].get(state.lower())
    if state_info and f"{disaster_type}_shelters" in state_info:
        return state_info[f"{disaster_type}_shelters"]
    return "No shelters found for this state or disaster type."

# Main chatbot function
def chatbot():
    print("Welcome to the Emergency Assistance Chatbot!")
    print("You can ask about emergency contacts, safety tips, or shelter locations in India.")
    print("Type 'exit' to quit the chatbot.\n")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == "exit":
            print("Chatbot: Stay safe! Goodbye!")
            break
        
        if "ambulance" in user_input:
            print(f"Chatbot: The ambulance helpline number is {get_emergency_contact('ambulance')}.")
        elif "police" in user_input:
            print(f"Chatbot: The police helpline number is {get_emergency_contact('police')}.")
        elif "fire" in user_input:
            print(f"Chatbot: The fire department number is {get_emergency_contact('fire')}.")
        elif "earthquake" in user_input:
            tips = ", ".join(get_safety_tips("earthquake"))
            print(f"Chatbot: Safety tips for earthquakes: {tips}")
        elif "flood" in user_input:
            tips = ", ".join(get_safety_tips("flood"))
            print(f"Chatbot: Safety tips for floods: {tips}")
        elif "cyclone" in user_input:
            tips = ", ".join(get_safety_tips("cyclone"))
            print(f"Chatbot: Safety tips for cyclones: {tips}")
        elif "shelter" in user_input:
            state = input("Chatbot: Please provide the state name: ").strip().lower()
            disaster_type = "flood" if "flood" in user_input else "cyclone"
            shelters = get_shelter_locations(state, disaster_type)
            if isinstance(shelters, list):
                print(f"Chatbot: Shelters in {state.title()} for {disaster_type}s: " + ", ".join(shelters))
            else:
                print(f"Chatbot: {shelters}")
        else:
            print("Chatbot: I'm sorry, I don't have information about that. Please try again.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
