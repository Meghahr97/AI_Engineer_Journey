# Day 01 - June 19 2026
# Goal: understand dictionaries and functions
# Why: LangGraph state IS a dictionary. 

# 1. Create an agent state dictionary

agent_state = {
    "agent_name" : "my_first_agent",
    "messages" : [],
    "steps_done" : 0,
    "is_complete" : False
}

def add_message(state, message):
    state["messages"].append(message)
    state["steps_done"] = state["steps_done"] + 1
    return state

def check_complete(state) :
    if state["steps_done"] >= 2:
        state["is_complete"] = True
    return state

# 4. Run it

agent_state = add_message(agent_state, "Hello, I am starting")
agent_state = add_message(agent_state, "I am processing")
agent_state = add_message(agent_state, "I am finishing")
agent_state = check_complete(agent_state)

# 5. Print results
print("Agent name:", agent_state["agent_name"])
print("Messages:", agent_state["messages"])
print("Steps done:", agent_state["steps_done"])
print("Complete:", agent_state["is_complete"])
