



class Questions:
    def __init__(self,sql_connection):
        self.sql_connection = sql_connection


    def quality_goal_movement_alert(self):
        question = self.sql_connection.cursor("SELECT priority_level , target_name , entity_id FROM targets WHERE priority_level == 1 OR priority_level == 2 AND movement_distance_km > 5")
        return question


    def analysis_of_collection_sources(self):
        question = self.sql_connection.cursor("SELECT signal_type , COUNT(*) FROM  intel_signals GROUP BY signal_type ORDER BY DESC ")
        return question


    def finding_new_targets(self):
        question = self.sql_connection.cursor("SELECT entity_id COUNT(*) FROM intel_signals WHERE entity_id = 99 GROUP BY entity_id HAVING DESC LIMIT 3  ")
        return question















    def identifying_awakened_sleeping_cells(self):
        pass


    def visualization_of_a_target_trajectory(self):
        pass



