# All local operations
import json
from .baseDAO import BaseDAO
class LocalStatisticsDAO(BaseDAO):

    # Local operations

    def handicapRoom(self, hid): # Top 5 handicap rooms that were reserve the most.
        try:
            with self.conn.cursor() as cur:

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
            raise e  
        finally:
            self.conn.close()
        

    def leastReserve(self, hid): # Top 3 rooms that were the least time unavailable.
        try:
            with self.conn.cursor() as cur:
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
            raise e  
        finally:
            self.conn.close()
        

    def mostCreditCard(self, hid): # Top 5 clients under 30 that made the most reservation with a credit card.
        try:
            with self.conn.cursor() as cur:
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
            raise e  
        finally:
            self.conn.close()

    def highestPaid(self, hid): # Top 3 highest paid regular employees.
        try:
            with self.conn.cursor() as cur:
                query = """
            
                """

                cur.execute(query, (hid,))
                result = []
                
                for row in cur:
                    result.append(dict(zip([], row)))
                    
                
            return result
        except Exception as e:
            raise e  
        finally:
            self.conn.close()

    def mostDiscount(self, hid): # Top 5 clients that received the most discounts.
        try:
            with self.conn.cursor() as cur:
                query = """
            
                """

                cur.execute(query, (hid,))
                result = []
                
                for row in cur:
                    result.append(dict(zip([], row)))
                    
                
            return result
        except Exception as e:
            raise e  
        finally:
            self.conn.close()

    def roomType(self, hid): # Total reservation by room type.
        try:
            with self.conn.cursor() as cur:
                query = """
            
                """

                cur.execute(query, (hid,))
                result = []
                
                for row in cur:
                    result.append(dict(zip([], row)))
                    
                
            return result
        except Exception as e:
            raise e  
        finally:
            self.conn.close()
    
    def leastGuests(self, hid): # Top 3 rooms that were reserved that had the least guest-to-capacity ratio.
        try:
            with self.conn.cursor() as cur:
                query = """
            
                """

                cur.execute(query, (hid,))
                result = []
                
                for row in cur:
                    result.append(dict(zip([], row)))
                    
                
            return result
        except Exception as e:
            raise e  
        finally:
            self.conn.close()