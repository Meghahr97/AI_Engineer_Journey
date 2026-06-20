# Day 02 - June 20 2026
# Goal: loops, conditionals, functions that make decisions
# Why: LangGraph nodes are functions that look at state and decide what to do next

# --- PART 1: A function that processes a list ---

def process_messages(messages):
    results = []

    for message in messages :
        if len(message) > 20 :
            results.append("Long: " +message)
        else:
            results.append("SHORT: " + message)

    return results

my_messages = [
    "Hi",
    "This is a longer message that has more content",
    "Hello",
    "Please summarize this document for me"
]

processed = process_messages(my_messages)

print(processed)

for item in processed:
    print(item)

print("------")

# --- PART 2: A function that decides next step ---
# This is EXACTLY how LangGraph routing works

def decide_next_step(state):
    messages = state["messages"]
    steps = state["steps_done"]

    if steps == 0:
        return "start"
    elif steps < 3:
        return "continue"
    else:
        return "finish"
    
# Test it

state1 = {"messages": [], "steps_done": 0}
state2 = {"messages": ["hello"], "steps_done": 1}
state3 = {"messages": ["hello", "world", "done"], "steps_done": 3}

print(decide_next_step(state1))
print(decide_next_step(state2))
print(decide_next_step(state3))

print("---")

# --- PART 3: Put it together ---

def run_agent(state):
    print("Current step:", state["steps_done"])

    next_step = decide_next_step(state)
    print("Next action:", next_step)

    if next_step == "finish":
        state["is_complete"] = True
        print("Agent finished!")
    else:
        state["steps_done"] +=1 
        state["messages"].append(f"Completed step {state['steps_done']}")
    
    return state

agent_state = {
    "messages": [],
    "steps_done": 0,
    "is_complete": False
}

for i in range(4):
    print(f"\n--- Run {i+1} ---")
    agent_state = run_agent(agent_state)

print("\nFinal state:", agent_state)


