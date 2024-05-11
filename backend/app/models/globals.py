# All local operations
import json
from .baseDAO import BaseDAO
class GlobalStatisticsDAO(BaseDAO):
        
    def getTopThreeTotalRevenue(self, json): # Top 3 chains with the highest total revenue.
        try:
            with self.conn.cursor() as cur:
                    cur.execute("select position from employee where eid = %s;", (json["user_id"],))

                    position = cur.fetchone()[0]
                    print(position)

                    if not (position == "Administrator"):
                        return "User can't access data!"
                    
                    query = """
                  SELECT chains.chid, TRUNC(SUM(reserve.total_cost))::numeric(1000, 2) as Total_Revenue
                    FROM chains
                    NATURAL INNER JOIN hotel
                    NATURAL INNER JOIN room
                    NATURAL INNER JOIN roomunavailable
                    NATURAL INNER JOIN reserve
                    GROUP BY chains.chid
                    ORDER BY Total_Revenue DESC
                    LIMIT 3;
                    """

                    cur.execute(query)
                    result = []
                    
                    for row in cur:
                        result.append(dict(zip(["id", "Total_Revenue"], row)))  

            return result
        except Exception as e:
            self.conn.rollback()
            return str(e)  
        finally:
            self.conn.close()

    def getpercentageByPaymentMethod(self, json): # Total reservation percentage by payment method.
        try:
            with self.conn.cursor() as cur:
                    cur.execute("select position from employee where eid = %s;", (json["user_id"],))

                    position = cur.fetchone()[0]

                    if not (position == "Administrator"):
                        return "User can't access data!"
                    
                    query = """
                WITH PaymentCounts AS (
                    SELECT payment, COUNT(*) as Count
                    FROM Reserve
                    GROUP BY payment
                ),
                TotalReservations AS (
                    SELECT COUNT(*) as Total
                    FROM Reserve
                )
                SELECT PaymentCounts.payment, ROUND(PaymentCounts.Count * 100.0 / TotalReservations.Total, 1)::numeric(1000,2) as Percentage
                FROM PaymentCounts, TotalReservations
                ORDER by Percentage DESC;
                    """

                    cur.execute(query)
                    result = []
                    
                    for row in cur:
                        result.append(dict(zip(["payment", "Percentage"], row)))  

            return result
        except Exception as e:
            self.conn.rollback()
            return str(e)   
        finally:
            self.conn.close()

    def getTopThreeLeastRooms(self, json): # Top 3 chain with the least rooms.
        try:
            with self.conn.cursor() as cur:
                cur.execute("select position from employee where eid = %s;", (json["user_id"],))

                position = cur.fetchone()[0]
                print(position)

                if not (position == "Administrator"):
                    return "User can't access data!"
                
                query = """
                SELECT cname, COUNT(room.rid) as numberofrooms
                FROM chains
                natural inner join hotel
                natural inner join room 
                GROUP BY cname
                ORDER BY COUNT(room.rid) ASC
                LIMIT 3;
                """

                cur.execute(query)
                result = []
                
                for row in cur:
                    result.append(dict(zip(["cname", "numberofrooms"], row)))
                    
                
            return result
        except Exception as e:
            self.conn.rollback()
            return str(e)   
        finally:
            self.conn.close()

    def getTopFiveHotelsMostCapacity(self, json): # Top 5 hotels with the most capacity.
        try:
            with self.conn.cursor() as cur:
                cur.execute("select position from employee where eid = %s;", (json["user_id"],))

                position = cur.fetchone()[0]
                print(position)

                if not (position == "Administrator"):
                    return "User can't access data!"
                query = """
                SELECT hotel.hid, SUM(roomdescription.capacity) as total_capacity
                FROM hotel
                NATURAL INNER JOIN room
                NATURAL INNER JOIN roomdescription
                GROUP BY hotel.hid
                ORDER BY total_capacity DESC
                LIMIT 5;
                """

                cur.execute(query)
                result = []
                
                for row in cur:
                    result.append(dict(zip(["id", "total_capacity"], row)))
                    
                
            return result
        except Exception as e:
            self.conn.rollback()
            return str(e)  
        finally:
            self.conn.close()

    def getTopTenByHotelReservation(self, json): #Top 10% hotels that had the most reservations.
        try:            
            with self.conn.cursor() as cur:
                cur.execute("select position from employee where eid = %s;", (json["user_id"],))

                position = cur.fetchone()[0]
                print(position)

                if not (position == "Administrator"):
                    return "User can't access data!"
                
                query = """
               select hid, count(hid)
               from roomunavailable natural inner join reserve natural inner join room natural inner join hotel
               group by hid
               order by count(hid) DESC
               limit (select count(hid) from hotel) * 0.1;
                """

                cur.execute(query)
                result = []
                
                for row in cur:
                    result.append(dict(zip(["id", "count"], row)))
                    
                
            return result
        except Exception as e:
            self.conn.rollback()
            return str(e)    
        finally:
            self.conn.close()

    def getTopThreeMonthByChain(self, json): # Top 3 month with the most reservation by chain
        try:
            with self.conn.cursor() as cur:
                cur.execute("select position from employee where eid = %s;", (json["user_id"],))

                position = cur.fetchone()[0]
                print(position)

                if not (position == "Administrator"):
                    return "User can't access data!"

                query = """
                with top_three as
            (select chid, count(extract(month from startdate)) as count, extract(month from startdate) as month
            from roomunavailable natural inner join reserve natural inner join room natural inner join hotel natural inner join chains
            group by chid, month
            order by count(extract(month from startdate)) DESC)

            select chid, month, count as total
            from top_three as top
            where ((top.count = (select count from top_three where top_three.chid = top.chid offset 2 limit 1) and top.month = (select month from top_three where top_three.chid = top.chid offset 2 limit 1))
                or (top.count = (select count from top_three where top_three.chid = top.chid offset 1 limit 1) and top.month = (select month from top_three where top_three.chid = top.chid offset 1 limit 1))
                or (top.count = (select count from top_three where top_three.chid = top.chid limit 1) and top.month = (select month from top_three where top_three.chid = top.chid limit 1))
                )
            group by chid, month, count
            order by chid ASC, total DESC
                """

                cur.execute(query)
                result = []
                
                for row in cur:
                    result.append(dict(zip(["id", "month", "count"], row)))
                    
                
                return result
        except Exception as e:
            self.conn.rollback()
            return str(e)    
        finally:
            self.conn.close()
    