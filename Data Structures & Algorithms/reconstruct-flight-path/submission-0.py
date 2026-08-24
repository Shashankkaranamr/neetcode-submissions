class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticket_path=defaultdict(list)
        for source,destination in sorted(tickets,reverse=True):
            ticket_path[source].append(destination)
        route=[]
        def dfs(airport):
            while ticket_path[airport]:
                next_airport=ticket_path[airport].pop()
                dfs(next_airport)
            route.append(airport)
        dfs("JFK")
        return route[::-1]