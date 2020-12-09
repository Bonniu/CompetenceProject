from collections import Counter

def analyze(hotspots, persons, traces):
    ranking = create_ranking(hotspots, persons, traces)

    i=0

def create_ranking(hotspots, persons,traces):
    grouped = Counter(getattr(t, 'hotspot_id') for t in traces)
    return sorted(grouped.items(), key=lambda item: item[1], reverse=True)