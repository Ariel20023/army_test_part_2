from questions import *
from sql_connection import *
from config import *
from fastapi import APIRouter



cfg = Config()


router = APIRouter()



sql = SqlConnector(cfg.mysql_host,cfg.mysql_port,cfg.mysql_password,cfg.mysql_database)


question = Questions(sql)


@router.get("/quality_goal_movement_alert")
def question_1_quality_goal_movement_alert():
    return question.quality_goal_movement_alert()




@router.get("/analysis_of_collection_sources")
def question_2_analysis_of_collection_sources():
    return question.analysis_of_collection_sources()




@router.get("/finding_new_targets")
def question_2_finding_new_targets():
    return question.finding_new_targets()
