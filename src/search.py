class Search:
    def search_train(self, schedules, route):
        results = []
        for s in schedules:
            if route.lower() in s["route"].lower():
                results.append(s)
        return results