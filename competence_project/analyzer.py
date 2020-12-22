from collections import Counter
from IPython.display import display
import pandas as pd
from database.repository.ClusterRepository import ClusterRepository
from database.repository.PairedHotspotsRepository import PairedHotspotsRepository

def analyze(hotspots, persons, traces,db_cursor):
    ranking = create_ranking(hotspots, persons, traces)
    ranking_list = []
    for e in ranking:
        sublist = []
        sublist.append(e[0])
        sublist.append(e[1])
        ranking_list.append(sublist)
    new_df = pd.DataFrame(columns=['hotspot_id', 'cnt'], data=ranking_list)
    display(new_df)
    paired = pair_hotspots(db_cursor)
    paired_list = []
    for e in paired:
        sublist = []
        sublist.append(e.first_hotspot_name)
        sublist.append(e.second_hotspot_name)
        sublist.append(e.cnt)
        paired_list.append(sublist)
    new_df = pd.DataFrame(columns=['first_hotspot_name', 'second_hotspot_name', 'cnt'], data=paired_list)
    pd.set_option('display.max_rows', new_df.shape[0] + 1)
    display(new_df)
    i=0


def     create_ranking(hotspots,persons,traces):
    grouped = Counter(getattr(t, 'hotspot_id') for t in traces)
    return sorted(grouped.items(), key=lambda item: item[1], reverse=True)

def cluster_hotspots(db_cursor):
    return ClusterRepository.perform_clustering(db_cursor)

def pair_hotspots(db_cursor):
    return PairedHotspotsRepository.select_all_records(db_cursor)