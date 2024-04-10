# All local operations
import json
from .baseDAO import BaseDAO
class GlobalStatisticsDAO(BaseDAO):
        
    def getTopThreeTotalRevenue(self): # Top 3 chains with the highest total revenue.
        try:
            with self.conn.cursor() as cur:
                    query = """
                  SELECT chains.cname, SUM(reserve.total_cost) as TotalRevenue
                    FROM chains
                    NATURAL INNER JOIN hotel
                    NATURAL INNER JOIN room
                    NATURAL INNER JOIN roomunavailable
                    NATURAL INNER JOIN reserve
                    GROUP BY chains.cname
                    ORDER BY TotalRevenue DESC
                    LIMIT 3;
                    """

                    cur.execute(query)
                    result = []
                    
                    for row in cur:
                        result.append(dict(zip(["cname", "TotalRevenue"], row)))  

            return result
        except Exception as e:
            raise e  
        finally:
            self.conn.close()

    def getpercentageByPaymentMethod(self): # Top 3 chains with the highest total revenue.
        try:
            with self.conn.cursor() as cur:
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
                SELECT PaymentCounts.payment, (PaymentCounts.Count * 100.0 / TotalReservations.Total) as Percentage
                FROM PaymentCounts, TotalReservations;
                    """

                    cur.execute(query)
                    result = []
                    
                    for row in cur:
                        result.append(dict(zip(["payment", "Percentage"], row)))  

            return result
        except Exception as e:
            raise e  
        finally:
            self.conn.close()

    def getTopThreeLeastRooms(self): # Top 3 chain with the least rooms.
        try:
            with self.conn.cursor() as cur:
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
            raise e  
        finally:
            self.conn.close()

    def getTopFiveHotelsMostCapacity(self): # Top 5 hotels with the most capacity.
        try:
            with self.conn.cursor() as cur:
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
                    result.append(dict(zip(["hid", "total_capacity"], row)))
                    
                
            return result
        except Exception as e:
            raise e  
        finally:
            self.conn.close()

    def getTopTenByHotelReservation(self): #Top 10% hotels that had the most reservations.
        try:
            with self.conn.cursor() as cur:
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
                    result.append(dict(zip(["hid", "count"], row)))
                    
                
            return result
        except Exception as e:
            raise e  
        finally:
            self.conn.close()

    def getTopThreeMonthByChain(self): # Top 3 month with the most reservation by chain
        try:
            with self.conn.cursor() as cur:
                query = """
            select chid, count(extract(month from startdate)), extract(month from startdate) as month
            from roomunavailable natural inner join reserve natural inner join room natural inner join hotel natural inner join chains
            group by chid, month
            order by count(extract(month from startdate)) DESC
            limit 3;
                """

                cur.execute(query)
                result = []
                
                for row in cur:
                    result.append(dict(zip(["chid", "count", "month"], row)))
                    
                
                return result
        except Exception as e:
            raise e  
        finally:
            self.conn.close()
    