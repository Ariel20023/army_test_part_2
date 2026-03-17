from DigitalHunter_map import *



class Questions:
    def __init__(self,sql_connection):
        self.sql_connection = sql_connection



    def quality_goal_movement_alert(self):
        self.sql_connection.cursor.execute("""SELECT priority_level , target_name , entity_id 
                                           FROM targets 
                                           WHERE (priority_level = 1 OR priority_level = 2) 
                                           AND movement_distance_km > 5 
                                           ;""")
        result = self.sql_connection.cursor.fetchall()
        return result



    def analysis_of_collection_sources(self):
        self.sql_connection.cursor.execute("""SELECT signal_type , COUNT(*) as cnt 
                                           FROM  intel_signals 
                                           GROUP BY signal_type 
                                           ORDER BY cnt DESC 
                                           ; """)
        result = self.sql_connection.cursor.fetchall()
        return result



    def finding_new_targets(self):
        self.sql_connection.cursor.execute("""SELECT entity_id ,COUNT(*) as cnt 
                                           FROM intel_signals 
                                           WHERE priority_level = 99 
                                           GROUP BY entity_id 
                                           ORDER BY cnt DESC 
                                           LIMIT 3 
                                           ; """)
        result = self.sql_connection.cursor.fetchall()
        return result




    def identifying_awakened_sleeping_cells(self):
        self.sql_connection.cursor.execute("""SELECT entity_id
                                            FROM intel_signals
                                            GROUP BY entity_id
                                            HAVING SUM(CASE 
                                                    WHEN (HOUR(created_at) BETWEEN 8 AND 19) 
                                                    AND distance_from_last = 0 THEN 1 END) > 0
                                            AND SUM(CASE 
                                                WHEN (HOUR(created_at) >= 20 OR HOUR(created_at)< 8)
                                                AND distance_from_last >= 10 THEN 1 END) > 0
                                           ; """)
        result = self.sql_connection.cursor.fetchall()
        return result





    def visualization_of_a_target_trajectory(self,entity_id):
        question = """SELECT reported_lon , reported_lat
                        FROM intel_signals
                        WHERE entity_id = %s"""
        
        self.sql_connection.cursor.execute(question,(entity_id,))
        result = self.sql_connection.cursor.fetchall()
        return plot_map_with_geometry(result)



