import requests
import sqlite3

BASE_URL = "http://localhost:7777"

# Function to get session name by session id using the API
def get_session_name(session_id):
    try:
        url = f"{BASE_URL}/sessions/{session_id}?type=agent"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("session_name") or "Unnamed Session"
    except Exception as e:
        print(f"Error getting session name for {session_id}: {e}")
        return "Unnamed Session"

def create_session():
    db_id = "21138089-9477-5cb5-98c0-fdc32ef6f1e0"
    session_url = f"{BASE_URL}/sessions?type=agent&db_id={db_id}"

    try:
        response = requests.post(session_url, json={})
        response.raise_for_status()
        session_data = response.json()
        session_id = session_data.get("session_id")
        print(f"Created session ID: {session_id}")

        # Prompt user to rename immediately after creation
        rename_session(session_id)

        return session_id

    except Exception as e:
        print(f"Error creating session: {e}")

def list_sessions():
    """Returns a dictionary mapping session_id -> session_name"""
    conn = sqlite3.connect("./agent/agno.db")
    cursor = conn.cursor()
    cursor.execute("SELECT session_id FROM agno_sessions;")
    session_ids = [s[0] for s in cursor.fetchall()]
    conn.close()

    session_map = {}
    if session_ids:
        for i, session_id in enumerate(session_ids, 1):
            name = get_session_name(session_id)
            session_map[session_id] = name
            print(f"{i}. {name} (ID: {session_id})")
    else:
        print("No sessions found.")

    return session_map

def delete_session():
    session_map = list_sessions()
    if not session_map:
        return
    choice = input("Enter the session number to delete: ")
    try:
        idx = int(choice) - 1
        session_id = list(session_map.keys())[idx]
        url = f"{BASE_URL}/sessions/{session_id}"
        headers = {"accept": "*/*"}
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        print(f"Deleted session: {session_map[session_id]} (ID: {session_id})")
    except Exception as e:
        print(f"Error deleting session: {e}")

def rename_session(session_id=None):
    """Rename a session given a session_id, or select one from the list"""
    if not session_id:
        session_map = list_sessions()
        if not session_map:
            return
        choice = input("Enter the session number to rename: ")
        try:
            idx = int(choice) - 1
            session_id = list(session_map.keys())[idx]
        except Exception as e:
            print(f"Invalid choice: {e}")
            return

    new_name = input(f"Enter a new name for session {session_id}: ")
    try:
        rename_url = f"{BASE_URL}/sessions/{session_id}/rename?type=agent"
        rename_payload = {"session_name": new_name}
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        rename_response = requests.post(rename_url, headers=headers, json=rename_payload)
        rename_response.raise_for_status()
        print(f"Session {session_id} renamed to: {new_name}")
    except Exception as e:
        print(f"Error renaming session: {e}")

def chat():
    session_map = list_sessions()
    if not session_map:
        print("No sessions to chat with. Create a session first.")
        return
    choice = input("Enter the session number to chat with: ")
    try:
        idx = int(choice) - 1
        session_id = list(session_map.keys())[idx]
        agent_url = f"{BASE_URL}/agents/agno-agent/runs"

        print(f"Chatting with session: {session_map[session_id]} (ID: {session_id}). Type 'exit' to quit.")
        while True:
            message = input("You: ")
            if message.lower() in {"exit", "quit"}:
                break

            files = {
                "message": (None, message),
                "stream": (None, "false"),
                "session_id": (None, session_id)
            }

            agent_response = requests.post(agent_url, files=files)
            agent_response.raise_for_status()
            data = agent_response.json()
            content = data.get("content") or data.get("response") or data
            print(f"Agent: {content}")

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
