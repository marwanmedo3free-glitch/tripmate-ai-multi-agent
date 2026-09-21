from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

res=search_flights("plan a 7 days japan trip from Bangladesh")
print(res)

# res=tavily_search("best hotels in egypt")
# print(res)