from dotenv import load_dotenv
import os
from typing import Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from typing_extensions import TypedDict

load_dotenv()

llm = init_chat_model(
    "claude-sonnet-4-20250514"
)


class MessageClassifier(BaseModel):
    message_types: Literal["emotional", "logical"] = Field(
        ...,
        description="Classify if the message requires an emotional (therapist) or logical response."
    )

class State(TypedDict):
    messages: Annotated[list, add_messages]
    message_types: str | None
    
graph_builder = StateGraph(State)

def classify_message(state: State):
    pass

def router(state: State):
    pass

def therapist_agent(state: State);
    pass

def logical_agent(state: State):
    pass


graph = graph_builder.compile()

