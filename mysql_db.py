import mysql.connector as conn

DB_HOST_NAME = "mytubedb.cnaqs2xve1td.ap-south-1.rds.amazonaws.com"
DB_USER = "admin"
DB_PWD = "MyTube123$"
mysql_db = ""
cursor = ""

PORT="3306"
REGION="ap-south-1b"
DBNAME="mytubedb"


# Initializing the mysql db connection

def init():
    global mysql_db, cursor
    mysql_db = conn.connect(host=DB_HOST_NAME, user=DB_USER, passwd=DB_PWD)
    cursor = mysql_db.cursor()


"""
     Save the video Data in mysql Data base
    :rtype: object
    :param video_id: 
    :param vurl: 
    :param download_link: 
    :param like: 
    :param comment_count: 
    :param video_title: 
    :param thumbnail: 
    """


def saveVideoData(video_id, vurl, download_link, like, comment_count, video_title, thumbnail):
    try:
        # Add validation data exist or not
        video_title = video_title.translate(
            {ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
        print(thumbnail)
        insert_qry = "insert into youtubedb.youtuber_data values('" + video_id + "','" + vurl + "','" + \
            vurl + "','" + like + "','" + comment_count + \
            "','" + video_title + "','" + thumbnail + "')"
        cursor.execute(insert_qry)
        mysql_db.commit()
    except Exception as e:
        print("Error : ", e)
