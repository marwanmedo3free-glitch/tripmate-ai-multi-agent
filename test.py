from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

user_input=input("enter travel requests: ")

res=run_travel_agent(user_input=user_input,thread_id="test_user")
print("\nFinal response:\n")
print(res["answer"])

# res=search_flights("plan a 7 days japan trip from Bangladesh")
# print(res)

# res=tavily_search("best hotels in egypt")
# print(res)