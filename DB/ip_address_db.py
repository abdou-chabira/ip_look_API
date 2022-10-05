from db.db import Web_api_db

def abuse_report_row_mapper(row):
    return{"id":row[0],
    "ip_address":row[1],
    "abuseCategory":row[2],
    "created_dt":row[3],
    "updated_dt":row[4]
    }
   


def save_abuse_category(ip_address,abuseCategory):
    sql="""INSERT INTO ip_abuse_report(ip_address,
                                    abuseCategory,
                                    created_dt,
                                    updated_dt)
                                    VALUES(
                                        %s,
                                        %s,
                                        CURRENT_TIMESTAMP,
                                        CURRENT_TIMESTAMP
                                    )
                                    RETURNING *
                                    """
    row = Web_api_db.query_single(sql,(ip_address,abuseCategory))
    if row: return abuse_report_row_mapper(row)
    return


def get_abuse_by_ip(ip_address,category):
    result=[]
    sql="""SELECT * FROM ip_abuse_report 
                        WHERE ip_address=%s """
    if category!=-1:
        sql=sql+"AND abuseCategory =%s"
        rows = Web_api_db.query(sql,(ip_address,category))
    else:
        rows = Web_api_db.query(sql,(ip_address,))
    if rows: 
        for row in rows:
            result.append(abuse_report_row_mapper(row))
        return result
    return