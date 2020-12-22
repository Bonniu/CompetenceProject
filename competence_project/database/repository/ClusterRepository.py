import pandas
from IPython.display import display
from sklearn import cluster as sk_cluster
from database.initDB import connect_to_mysql_with_sqlalchemy


class ClusterRepository:
    class Cluster:
        def __init__(self, hotspot_name, user_id, cnt, total_min):
            self.hotspot_name = hotspot_name
            self.user_id = user_id
            self.cnt = cnt
            self.total_min = total_min

    @staticmethod
    def perform_clustering(db_cursor):

        dbConnection = connect_to_mysql_with_sqlalchemy()

        input_query = '''WITH obj1 AS
        (
          SELECT
            '' AS hotspot
            ,MIN(t1.visits_no) AS min_visits_no
            ,MAX(t1.visits_no) AS max_visits_no
            ,(MAX(t1.visits_no)-MIN(t1.visits_no)) / 4.0 AS diff_visits_no
            ,MIN(t1.avg_min) AS min_avg_min
            ,MAX(t1.avg_min) AS max_avg_min
            ,(MAX(t1.avg_min)-MIN(t1.avg_min)) / 4.0 AS diff_avg_min
            ,MIN(t1.user_cnt) AS min_user_cnt
            ,MAX(t1.user_cnt) AS max_user_cnt
            ,(MAX(t1.user_cnt)-MIN(t1.user_cnt)) / 4.0 AS diff_user_cnt
          FROM
          (
            SELECT
              t4.hotspot AS hotspot,Count(t4.user_id) AS user_cnt,Sum(t4.visits_no) AS visits_no
              ,AVG(t4.total_min) AS avg_min
            FROM
            (
              SELECT 
                h.name AS hotspot, t.user_id, COUNT(t.user_id) AS visits_no 
                ,Sum(TIMESTAMPDIFF(MINUTE,entry_time, exit_time)) AS total_min
              FROM CP_database.traces t 
              INNER JOIN CP_database.hotspots h 
                ON t.hotspot_id = h.id 
              GROUP BY h.name,t.user_id
            ) t4
            GROUP BY t4.hotspot
          ) t1
        )
        SELECT
          t3.hotspot AS hotspot
          ,t3.visits_no/obj1.max_visits_no AS visits_no
          ,t3.avg_min/obj1.max_avg_min AS avg_min
          ,t3.user_cnt/obj1.max_user_cnt AS user_cnt
        FROM
        (
          SELECT
            t2.hotspot AS hotspot,Count(t2.user_id) AS user_cnt,Sum(t2.visits_no) AS visits_no
            ,AVG(t2.total_min) AS avg_min
          FROM
          (
            SELECT 
              h.name AS hotspot, t.user_id, COUNT(t.user_id) AS visits_no 
              ,Sum(TIMESTAMPDIFF(MINUTE,entry_time, exit_time)) AS total_min
            FROM CP_database.traces t 
            INNER JOIN CP_database.hotspots h 
              ON t.hotspot_id = h.id 
            GROUP BY h.name,t.user_id
          ) t2
          GROUP BY t2.hotspot
        ) t3
        INNER JOIN obj1 ON obj1.hotspot <> t3.hotspot'''


        hotspot_data = pandas.read_sql(input_query, dbConnection)

        print("Data frame:", hotspot_data.head(n=5))
        n_clusters = 3

        means_cluster = sk_cluster.KMeans(n_clusters=n_clusters, random_state=111)
        columns = ["visits_no", "avg_min", "user_cnt"]
        est = means_cluster.fit(hotspot_data[columns])
        clusters = est.labels_
        hotspot_data['cluster'] = clusters

        # For each cluster, count the members.
        for c in range(n_clusters):
            cluster_members = hotspot_data[hotspot_data['cluster'] == c][:]
            print('Cluster{}(n={}):'.format(c, len(cluster_members)))
            print('-' * 17)
        print(hotspot_data.groupby(['cluster']).mean())

        records = []
        for res in db_cursor.fetchall():
            records.append(ClusterRepository.get_record_from_result(res))
        return records

    @staticmethod
    def get_record_from_result(res) -> Cluster:
        return ClusterRepository.Cluster(res[0], res[1], res[2], res[3])
