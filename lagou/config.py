# coding=utf8
import ConfigParser
import time

path_config = "config.cfg"
section_database = "DataBase"
section_config = "MsutParam"

def write_config():
    config = ConfigParser.RawConfigParser()
    
    config.add_section(section_config) 
    config.set(section_config, "crawl_min_time", "2016/5/3 17:00:00")
    config.set(section_config, "db_max_time", "2016/5/3 16:33:37")
    config.set(section_config, "path_log", "log")
    config.set(section_config, "path_files", "files")
    
    config.add_section(section_database)
    config.set(section_database, "base_name", "lagou")
    config.set(section_database, "base_ip", "127.0.0.1")
    config.set(section_database, "base_port", "")
    config.set(section_database, "base_username", "tt")
    config.set(section_database, "base_password", "123456")
    config.set(section_database, "table_result", "result")
    
    fp = open(path_config, "w") 
    config.write(fp)
    print "write ok !"

def _config(option, isint = False):
    config = ConfigParser.ConfigParser()
    config.read(path_config)
    
    for sectioni in config.sections():
        if config.has_option(sectioni, option):
            if isint:
                return config.getint(sectioni, option)
            else:
                return config.get(sectioni, option)
    raise Exception, "not find option !"

def _config_time(option, leng=13):
    value = _config(option)
    try:
        timeStamp = int(time.mktime(time.strptime(value,'%Y/%m/%d %H:%M:%S')))
        return timeStamp
    except:
        return None

def _upconfig(select_name, key_name, value):
    config = ConfigParser.RawConfigParser()
    config.read(path_config)
     
    config.set(select_name, key_name, value)
     
    fp = open(path_config, "w") 
    config.write(fp)

def _update_dbmaxtime():
    import MySQLdb
    db = MySQLdb.connect(host="127.0.0.1", user="jss", passwd="123456",
                         port=3306, db="lagou", charset="utf8"
                         )
    cursor = db.cursor()
    cursor.execute("select Max(createTimeSort) from result;")
    cursor.fetchall()
    max_time = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(int(cursor.fetchall())))
    _upconfig("MsutParam", "db_max_time", max_time)
    #_upconfig("MsutParam", "db_max_time", "2016/5/3 16:33:37")

if __name__ == "__main__":
    write_config()
#     print _config_time("crawl_min_time")
    
