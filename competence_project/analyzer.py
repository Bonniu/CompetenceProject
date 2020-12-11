from collections import Counter
from database.repository.ClusterRepository import ClusterRepository
from database.repository.PairedHotspotsRepository import PairedHotspotsRepository

def analyze(hotspots, persons, traces,db_cursor):
    ranking = create_ranking(hotspots, persons, traces)
    clustered = cluster_hotspots(db_cursor)
    paired = pair_hotspots(db_cursor)
    i=0


def create_ranking(hotspots,persons,traces):
    grouped = Counter(getattr(t, 'hotspot_id') for t in traces)
    return sorted(grouped.items(), key=lambda item: item[1], reverse=True)

def cluster_hotspots(db_cursor):
    return ClusterRepository.select_all_records(db_cursor)

def pair_hotspots(db_cursor):
    return PairedHotspotsRepository.select_all_records(db_cursor)