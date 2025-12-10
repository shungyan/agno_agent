import requests

BASE_URL = "http://localhost:7777"

def create_session():
    name = input("Enter session name: ")
    url = f"{BASE_URL}/sessions?type=agent"
    headers = {"Content-Type": "application/json"}
    data = {"session_name": name}
    
    response = requests.post(url, json=data, headers=headers)
    if response.ok:
        session_data = response.json()
        print(f"Created session: {session_data.get('session_name')} (ID: {session_data.get('session_id')})")
    else:
        print(f"Error: {response.status_code} {response.text}")

def list_sessions():
    url = f"{BASE_URL}/sessions?type=agent"
    headers = {"Content-Type": "application/json"}
    
    response = requests.get(url, headers=headers)
    if response.ok:
        sessions = response.json().get("data", [])
        if not sessions:
            print("No sessions found.")
            return []
        for i, session in enumerate(sessions, start=1):
            print(f"{i}. {session.get('session_name')} (ID: {session.get('session_id')})")
        return sessions
    else:
        print(f"Error: {response.status_code} {response.text}")
        return []

def choose_session():
    sessions = list_sessions()
    if not sessions:
        return None
    print("0. Go back to main menu")
    try:
        index = int(input("Select a session by number: "))
        if index == 0:
            return None
        index -= 1
        if 0 <= index < len(sessions):
            return sessions[index]
        else:
            print("Invalid selection.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

def delete_session():
    session = choose_session()
    if not session:
        return
    session_id = session.get("session_id")
    url = f"{BASE_URL}/sessions/{session_id}"
    headers = {"accept": "*/*"}
    
    response = requests.delete(url, headers=headers)
    if response.ok:
        print(f"Deleted session: {session.get('session_name')}")
    else:
        print(f"Error: {response.status_code} {response.text}")

def rename_session():
    session = choose_session()
    if not session:
        return
    new_name = input("Enter new session name: ")
    session_id = session.get("session_id")
    url = f"{BASE_URL}/sessions/{session_id}"
    headers = {"Content-Type": "application/json"}
    data = {"session_name": new_name}
    
    response = requests.patch(url, json=data, headers=headers)
    if response.ok:
        print(f"Session renamed to: {new_name}")
    else:
        print(f"Error: {response.status_code} {response.text}")

def chat():
    session = choose_session()
    if not session:
        return
    session_id = session.get("session_id")
    agent_url = f"{BASE_URL}/agents/agno-agent/runs"

    print("Start chatting! Type 'exit' or 'quit' to leave.")
    while True:
        try:
            message = input("You: ")
            if message.lower() in {"exit", "quit"}:
                break

            files = {
                "message": (None, message),
                "stream": (None, "false"),
                "session_id": (None, session_id)
            }

            response = requests.post(agent_url, files=files)
            response.raise_for_status()
            data = response.json()
            content = data.get("content") or data.get("response") or data
            print(f"Agent: {content}")

        except KeyboardInterrupt:
            print("\nExiting chat...")
            break
        except Exception as e:
            print(f"Error: {e}")

def main():
    while True:
        print("\nOptions:")
        print("1. Create session")
        print("2. Delete session")
        print("3. Chat")
        print("4. List sessions")
        print("5. Rename session")
        print("6. Exit")
        choice = input("Select an option (1-6): ")

        if choice == "1":
            create_session()
        elif choice == "2":
            delete_session()
        elif choice == "3":
            chat()
        elif choice == "4":
            list_sessions()
        elif choice == "5":
            rename_session()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
