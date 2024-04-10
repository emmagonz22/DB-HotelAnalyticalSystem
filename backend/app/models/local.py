# All local operations
import json
from .baseDAO import BaseDAO
class LocalStatisticsDAO(BaseDAO):

    # Local operations

    def handicapRoom(self, hid, json): # Top 5 handicap rooms that were reserve the most.
        try:
            with self.conn.cursor() as cur:

                cur.execute("select chid, hid, position from hotel natural join employee where eid = %s;", (json["user_id"],))

                chid, fetchhid, position = cur.fetchone()

                cur.execute("select chid from hotel where hid = %s;", (hid,))

                chainid = cur.fetchone()[0]


                if not ((position == "Regular" and fetchhid == hid) or (position == "Supervisor" and chid == chainid) or (position == "Administrator")):
                    return "User can't access data!"

                query = """SELECT rid, hid, rdid, rprice, COUNT(reserve.ruid) as reservation_number from room
                        NATURAL JOIN hotel
                        NATURAL JOIN roomdescription
                        NATURAL JOIN roomunavailable
                        NATURAL JOIN reserve
                        WHERE roomdescription.ishandicap = TRUE AND hid = %s
                        GROUP BY rid, hid, rdid, rprice
                        ORDER BY reservation_number DESC
                        LIMIT 5;
                        """

                
                cur.execute(query, (hid,))
                result = []
                
                for row in cur:
                    result.append(dict(zip(["rid", "hid", "rdid", "rprice", "amount_of_reservations"], row)))
                    
                
            return result
        except Exception as e:
            self.conn.rollback()
            return str(e)  
        finally:
            self.conn.close()
        

    def leastReserve(self, hid, json): # Top 3 rooms that were the least time unavailable.
        try:
            with self.conn.cursor() as cur:
                cur.execute("select chid, hid, position from hotel natural join employee where eid = %s;", (json["user_id"],))

                chid, fetchhid, position = cur.fetchone()

                cur.execute("select chid from hotel where hid = %s;", (hid,))

                chainid = cur.fetchone()[0]


                if not ((position == "Regular" and fetchhid == hid) or (position == "Supervisor" and chid == chainid) or (position == "Administrator")):
                    return "User can't access data!"
                
                query = """
                SELECT rid, hid, rdid, rprice,
                    COUNT(roomunavailable.ruid) as times_unavailable ,
                    SUM(AGE(roomunavailable.enddate, roomunavailable.startdate)) as total_time_unavailable
                FROM room
                NATURAL JOIN hotel
                NATURAL JOIN roomunavailable
                WHERE hid = %s
                GROUP BY rid, hid, rdid, rprice
                ORDER BY times_unavailable ASC, total_time_unavailable ASC
                LIMIT 3;
                """

                cur.execute(query, (hid,))
                result = []
                
                for row in cur:
                    print(row)
                    result.append(dict(zip(["rid", "hid", "rdid", "rprice"], row)))
                    
                
            return result
        except Exception as e:
            self.conn.rollback()
            return str(e)  
        finally:
            self.conn.close()
        

    def mostCreditCard(self, hid, json): # Top 5 clients under 30 that made the most reservation with a credit card.
        try:
            with self.conn.cursor() as cur:

                cur.execute("select chid, hid, position from hotel natural join employee where eid = %s;", (json["user_id"],))

                chid, fetchhid, position = cur.fetchone()

                cur.execute("select chid from hotel where hid = %s;", (hid,))

                chainid = cur.fetchone()[0]


                if not ((position == "Regular" and fetchhid == hid) or (position == "Supervisor" and chid == chainid) or (position == "Administrator")):
                    return "User can't access data!"
                
                query = """
                SELECT  clid, fname, lname, age, memberyear, COUNT(reserve.reid) as number_reservation
                FROM client
                NATURAL JOIN reserve
                NATURAL JOIN roomunavailable
                NATURAL JOIN room
                NATURAL JOIN hotel
                WHERE age < 30 AND hotel.hid = %s AND reserve.payment = 'credit card'
                GROUP BY clid, fname, lname, age, memberyear
                ORDER BY number_reservation DESC
                LIMIT 5;
                """

                cur.execute(query, (hid,))
                result = []
                
                for row in cur:
                    result.append(dict(zip(["clid", "fname", "lname", "age", "memberyear"], row)))
                    
                
            return result
        except Exception as e:
            self.conn.rollback()
            return str(e)  
        finally:
            self.conn.close()

    def highestPaid(self, hid, json): # Top 3 highest paid regular employees.
        try:
            with self.conn.cursor() as cur:

                cur.execute("select chid, hid, position from hotel natural join employee where eid = %s;", (json["user_id"],))

                chid, fetchhid, position = cur.fetchone()

                cur.execute("select chid from hotel where hid = %s;", (hid,))

                chainid = cur.fetchone()[0]


                if not ((position == "Regular" and fetchhid == hid) or (position == "Supervisor" and chid == chainid) or (position == "Administrator")):
                    return "User can't access data!"
                
                query = """
                    SELECT eid, fname, lname, age, position, salary, hid
                    FROM employee
                    NATURAL JOIN hotel
                    WHERE hotel.hid = %s AND position = 'Regular'
                    GROUP BY eid,
                            fname,
                            lname,
                            age,
                            position,
                            salary,
                            hid
                    ORDER BY salary DESC
                    LIMIT 3;
                """

                cur.execute(query, (hid,))
                result = []
                
                for row in cur:
                    result.append(dict(zip(["eid", "fname", "lname", "age", "position", "salary", "hid"], row)))
                    
                
            return result
        except Exception as e:
            self.conn.rollback()
            return str(e)  
        finally:
            self.conn.close()

    def mostDiscount(self, hid, json): # Top 5 clients that received the most discounts.
        try:
            with self.conn.cursor() as cur:

                cur.execute("select chid, hid, position from hotel natural join employee where eid = %s;", (json["user_id"],))

                chid, fetchhid, position = cur.fetchone()

                cur.execute("select chid from hotel where hid = %s;", (hid,))

                chainid = cur.fetchone()[0]


                if not ((position == "Regular" and fetchhid == hid) or (position == "Supervisor" and chid == chainid) or (position == "Administrator")):
                    return "User can't access data!"
                

                query = """
                SELECT clid,
                fname,
                lname,
                age,
                memberyear,
                 ROUND( CAST(room.rprice * (roomunavailable.enddate - roomunavailable.startdate) AS NUMERIC), 2) AS reservation_cost,
                ROUND(
                        CAST(room.rprice * (roomunavailable.enddate - roomunavailable.startdate) *
                        (CASE
                            WHEN EXTRACT(MONTH FROM roomunavailable.startdate) IN (3, 4, 5) THEN chains.springmkup
                            WHEN EXTRACT(MONTH FROM roomunavailable.startdate) IN (6, 7, 8) THEN chains.summermkup
                            WHEN EXTRACT(MONTH FROM roomunavailable.startdate) IN (9, 10, 11) THEN chains.fallmkup
                            ELSE chains.wintermkup
                        END) *
                        (CASE
                            WHEN memberyear > 0 AND memberyear < 5 THEN .02
                            WHEN memberyear > 4 AND memberyear < 10 THEN .05
                            WHEN memberyear > 9 AND memberyear < 15 THEN .08
                            ELSE .12
                        END) as NUMERIC),
                        2
                    )  AS total_discount
                    FROM client
                    NATURAL JOIN reserve
                    NATURAL JOIN roomunavailable
                    NATURAL JOIN room
                    NATURAL JOIN hotel
                    NATURAL JOIN chains
                    WHERE hotel.hid = %s
                    GROUP BY clid,
                            fname,
                            lname,
                            age,
                            memberyear,
                            room.rprice,
                            roomunavailable.startdate,
                            roomunavailable.enddate,
                            chains.fallmkup,
                            chains.springmkup,
                            chains.wintermkup,
                            chains.summermkup,
                            reserve.total_cost
                    ORDER BY total_discount DESC
                    LIMIT 5;
                """

                cur.execute(query, (hid,))
                result = []
                
                for clid, fname, lname, age, memberyear, reservation_cost, total_discount in cur:
                    result.append(dict(zip(['clid', 'fname', 'lname', 'age', 'memberyear', 'reservation_cost', 'total_discount'], (clid, fname, lname, age, memberyear, reservation_cost, round(total_discount, 2)))))
                    
                
            return result
        except Exception as e:
            self.conn.rollback()
            return str(e)   
        finally:
            self.conn.close()

    def roomType(self, hid, json): # Total reservation by room type.
        try:
            with self.conn.cursor() as cur:

                cur.execute("select chid, hid, position from hotel natural join employee where eid = %s;", (json["user_id"],))

                chid, fetchhid, position = cur.fetchone()

                cur.execute("select chid from hotel where hid = %s;", (hid,))

                chainid = cur.fetchone()[0]


                if not ((position == "Regular" and fetchhid == hid) or (position == "Supervisor" and chid == chainid) or (position == "Administrator")):
                    return "User can't access data!"
                

                query = """
                    SELECT COUNT(roomdescription.rtype) as total_reservation, roomdescription.rtype as room_type
                    FROM reserve
                    NATURAL JOIN roomunavailable
                    NATURAL JOIN room
                    NATURAL JOIN roomdescription
                    WHERE hid = %s
                    GROUP BY room_type;
                """

                cur.execute(query, (hid,))
                result = []
                
                for row in cur:
                    result.append(dict(zip(["total_reservation", "room_type"], row)))
                    
                
            return result
        except Exception as e:
            self.conn.rollback()
            return str(e)   
        finally:
            self.conn.close()
    
    def leastGuests(self, hid, json): # Top 3 rooms that were reserved that had the least guest-to-capacity ratio.
        try:
            with self.conn.cursor() as cur:


                cur.execute("select chid, hid, position from hotel natural join employee where eid = %s;", (json["user_id"],))

                chid, fetchhid, position = cur.fetchone()

                cur.execute("select chid from hotel where hid = %s;", (hid,))

                chainid = cur.fetchone()[0]


                if not ((position == "Regular" and fetchhid == hid) or (position == "Supervisor" and chid == chainid) or (position == "Administrator")):
                    return "User can't access data!"
                
                
                query = """
                    SELECT
                        room.rid,
                        roomdescription.rname,
                        ROUND(AVG(reserve.guests::decimal / roomdescription.capacity)*100, 2) AS avg_guest_to_capacity_ratio
                    FROM
                        reserve
                    NATURAL JOIN roomunavailable 
                    NATURAL JOIN room 
                    NATURAL JOIN roomdescription 
                    NATURAL JOIN hotel
                    WHERE hotel.hid = %s
                    GROUP BY
                        room.rid, roomdescription.rname
                    ORDER BY
                        avg_guest_to_capacity_ratio ASC
                    LIMIT 3;
                """

                cur.execute(query, (hid,))
                result = []
                
                for row in cur:
                    result.append(dict(zip(["rid", "rname", "avg_guest_to_capacity_ratio"], row)))
                    
                
            return result
        except Exception as e:
            self.conn.rollback()
            return str(e)   
        finally:
            self.conn.close()