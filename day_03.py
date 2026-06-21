# Day 03 - June 21 2026
# Goal: TypedDict and Classes
# Why: LangGraph state is defined as TypedDict 

from typing import TypedDict, List, Optional

class AgentState(TypedDict):
    messages : List[str]
    steps_done : int
    is_complete : bool
    current_ocation : Optional[str]

# Create a state - notice it looks like a dictionary

state : AgentState = {
    "messages": [],
    "steps_done": 0,
    "is_complete": False,
    "current_action": None
 }

print("Initial state:", state)
print("Type:", type(state))

# It still behaves like a dictionary
state["messages"].append("first message")
state["steps_done"] = 1
state["current_action"] = "processing"


print("Updated state:", state)


print("---")

# --- PART 3: A real agent node using TypedDict ---
# In LangGraph, every node is a function that takes state and returns state

def process_node(state : AgentState) -> AgentState:
    print("Processing node called")
    print("Current messages:", state["messages"])

    state["messages"].append("processed by node")
    state["steps_done"] += 1
    state["current_action"] = "processed"
    
    return state

def decision_node(state: AgentState) -> AgentState:
    print("Decision node called")
    
    if state["steps_done"] >= 2:
        state["is_complete"] = True
        state["current_action"] = "complete"
    else:
        state["current_action"] = "need_more_steps"
    
    return state

def router(state: AgentState) -> str:
    # Router looks at state and returns a string
    # That string tells LangGraph which node to go to next
    if state["is_complete"]:
        return "end"
    else:
        return "process"
    
print("=== Manual Agent Run ===")
state = process_node(state)
print("After process:", state["current_action"])
print("Router says:", router(state))

print("---")
state = process_node(state)
print("After second process:", state["steps_done"])

state = decision_node(state)
print("After decision:", state["current_action"])
print("Router says:", router(state))
print("Is complete:", state["is_complete"])