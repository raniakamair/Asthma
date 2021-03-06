import rapidsms
import re
import MySQLdb
import pygsm
import threading
import time
from rapidsms.apps.base import AppBase
from models import *
from datetime import datetime
from datetime import timedelta
from django.db import connection, transaction

class App (AppBase):

    def start (self):
        db1=MySQLdb.connect (host = "localhost", user = "root",passwd = "romo",db = "asthma")
        t = datetime.now()
        t1 = t.strftime("%Y-%m-%d") 
        while t1 == datetime.now():
            n = datetime.now() + timedelta(days=2)
            cur_date = n.strftime("%Y-%m-%d") 
            cursor1 = db1.cursor()
            sql1 = "SELECT Phone,Treat_Msg from asthma_app_asthma_mgmt,asthma_app_patients,asthma_app_treatments where asthma_app_asthma_mgmt.Followup_Date='%s' and asthma_app_asthma_mgmt.Asthma_Mgmt_PK=asthma_app_patients.Patients_PK and asthma_app_asthma_mgmt.Severity_Level_id=asthma_app_treatments.Treat_ID" % (cur_date)
            cursor1.execute(sql1)
            results1 = cursor1.fetchall()
            #'Command Two'
            cursor2 = db1.cursor()
            sql2 = "SELECT Phone,Treat_Msg from asthma_app_followup_visits,asthma_app_patients,asthma_app_treatments where asthma_app_followup_visits.Nxt_Follow_up_Date= '%s' and asthma_app_followup_visits.Follow_Date = asthma_app_patients.Patients_PK and asthma_app_followup_visits.F_Severity_Level_id = asthma_app_treatments.Treat_ID" % (cur_date)
            cursor2.execute(sql2)
            results2 = cursor2.fetchall()
            #'Command Three'
            cursor3 = db1.cursor()
            sql3 = "SELECT Date_week,Treat_Msg,Phone from asthma_app_date_by_week,asthma_app_treatments,asthma_app_patients where asthma_app_date_by_week.T_Msg_id = asthma_app_treatments.Treat_ID  and asthma_app_date_by_week.P_ID=asthma_app_patients.Patients_PK  and asthma_app_date_by_week.Date_week='%s'" % (datetime.now().strftime("%Y-%m-%d"))
            cursor3.execute(sql3)
            results3 = cursor3.fetchall()
            #'Command Four'
            cursor4 = db1.cursor()
            sql4 = "SELECT Date_week,Treat_Msg,Phone from asthma_app_date_by_week,asthma_app_treatments,asthma_app_patients where asthma_app_date_by_week.T_Msg_id = asthma_app_treatments.Treat_ID  and asthma_app_date_by_week.P_ID=asthma_app_patients.Patients_PK  and asthma_app_date_by_week.Date_week='%s'" % (datetime.now().strftime("%Y-%m-%d"))
            cursor4.execute(sql4)
            results4 = cursor4.fetchall()
            if results1:
                for row_mgt in results1:
                    modem = pygsm.GsmModem(port="/dev/ttyUSB0")
                    modem.send_sms(str(row_mgt[0]),"You have followup visit after 2 days" )
            if results2:
                for row_flo in results2:
                    modem = pygsm.GsmModem(port="/dev/ttyUSB0")
                    modem.send_sms(str(row_flo[0]),"You have followup visit after 2 days")
            if results3:
                for row_w in results3:
                    modem = pygsm.GsmModem(port="/dev/ttyUSB0")
                    modem.send_sms(str(row_w[2]),row_w[1])
            if results4:
                for row_4 in results4:
                    modem = pygsm.GsmModem(port="/dev/ttyUSB0")
                    modem.send_sms(str(row_4[2]),row_4[1])
            # Defaluter Procedure
            Last_Flow_date11 = datetime.now().strftime("%Y-%m-%d") 
            Last_Flow_date = datetime.now() - timedelta(days=15)
            Last_Flow_date = Last_Flow_date.strftime("%Y-%m-%d") 
            #1
            Defaulter_cursor1 = db1.cursor()
            Defaulter_cursor2 = db1.cursor()
            Defaulter_cursor3 = db1.cursor()
            Defaulter_sql1 =  "SELECT Asthma_Mgmt_PK,Followup_Date from asthma_app_asthma_mgmt where Followup_Date='%s'"  % (Last_Flow_date)
            Defaulter_cursor1.execute(Defaulter_sql1)   
            Defaulter_results1 = Defaulter_cursor1.fetchall()
            #2
            Defaulter_sql2 = "SELECT Follow_Date from asthma_app_followup_visits where Nxt_Follow_up_Date= '%s' " % (Last_Flow_date)
            Defaulter_cursor2.execute(Defaulter_sql2)
            Defaulter_results2 = Defaulter_cursor2.fetchall()
            if Defaulter_results1 :
                for d_m_row in Defaulter_results1:
                    Defaulter_sql3 = "SELECT count(Follow_Date) from asthma_app_followup_visits where Follow_Date='%s'" % (d_m_row[1])
                    Defaulter_cursor3.execute(Defaulter_sql3)
                    Defaulter_results3 = Defaulter_cursor3.fetchone()
                    if Defaulter_results3[0] == 0:
                        Defaulter_tab = Defaulter(Last_Flowup_date=Last_Flow_date,Defaulter_ID=d_m_row[0],Default_Date=Last_Flow_date11)
                        Defaulter_tab.save()
            elif Defaulter_results2:
                for Defaulter_row in Defaulter_results2:
                    Defaulter_tab = Defaulter(Last_Flowup_date=Last_Flow_date,Defaulter_ID=d_m_row[0],Default_Date=Last_Flow_date11)
                    Defaulter_tab.save()
            t = t + timedelta(days=1)
            t1 = t.strftime("%Y-%m-%d")
    def parse (self, message):
        """Parse and annotate messages in the parse phase."""
        pass
    
    def handle (self, message):
        self.debug("got message %s", message.text)
        db1=MySQLdb.connect (host = "localhost", user = "root",passwd = "romo",db = "asthma")
        t = message.text
        t1= t.upper()
        t2= t1.strip()
        r = t2.split(',')
        CK = r[1] + "-" + r[2] 
        if len(r) == 10:
            if int(r[7])==1:
		d1 = datetime.strptime(r[0],'%Y-%m-%d')
                d2 = timedelta(days=14)
                d3 = d1+d2
                w1 = d1 + timedelta(days=7)
                w2 = d1 + timedelta(days=14)
                w3 = d1 + timedelta(days=21)
                w4 = d1 + timedelta(days=28)
                tab1 = Patients(Patients_PK=CK,Patient_ID=int(r[2]),Centre_ID_id=int(r[1]),Gender=r[3],Phone=r[5],Age=int(r[4]))
                tab1.save()
                tab2 = Asthma_Mgmt(Asthma_Mgmt_PK=CK,First_Date=d1,Lung_Function=int(r[6]),Severity_Level_id=int(r[7]),Year_ER_Visits=int(r[8]),Year_Hospital_Visits=int(r[9]),Followup_Date=d3)
                tab2.save()
                tab_w1 = Date_by_week(Date_week=w1,T_Msg_id=int(r[7]),P_ID=CK)
                tab_w1.save()
                tab_w2 = Date_by_week(Date_week=w2,T_Msg_id=int(r[7]),P_ID=CK)
                tab_w2.save()
                tab_w3 = Date_by_week(Date_week=w3,T_Msg_id=int(r[7]),P_ID=CK)
                tab_w3.save()
                tab_w4 = Date_by_week(Date_week=w4,T_Msg_id=int(r[7]),P_ID=CK)
                tab_w4.save()
                response = "Your Message was recieved successfully"
                self.debug("responding with %s", response)
                message.respond(response)
                return True	
            elif int(r[7])==2:
                d1 = datetime.strptime(r[0],'%Y-%m-%d')
                d2 = timedelta(days=30)
                d3 = d1+d2
                w1 = d1 + timedelta(days=7)
                w2 = d1 + timedelta(days=14)
                w3 = d1 + timedelta(days=21)
                w4 = d1 + timedelta(days=28)
                tab1 = Patients(Patients_PK=CK,Patient_ID=int(r[2]),Centre_ID_id=int(r[1]),Gender=r[3],Phone=r[5],Age=int(r[4]))
                tab1.save()
                tab2 = Asthma_Mgmt(Asthma_Mgmt_PK=CK,First_Date=d1,Lung_Function=int(r[6]),Severity_Level_id=int(r[7]),Year_ER_Visits=int(r[8]),Year_Hospital_Visits=int(r[9]),Followup_Date=d3)
                tab2.save()
                tab_w1 = Date_by_week(Date_week=w1,T_Msg_id=int(r[7]),P_ID=CK)
                tab_w1.save()
                tab_w2 = Date_by_week(Date_week=w2,T_Msg_id=int(r[7]),P_ID=CK)
                tab_w2.save()
                tab_w3 = Date_by_week(Date_week=w3,T_Msg_id=int(r[7]),P_ID=CK)
                tab_w3.save()
                tab_w4 = Date_by_week(Date_week=w4,T_Msg_id=int(r[7]),P_ID=CK)
                tab_w4.save()
                response = "Your Message was recieved successfully"
                self.debug("responding with %s", response)
                message.respond(response)
                db1.close ()
                return True
            elif int(r[7])==3:
                d1 = datetime.strptime(r[0],'%Y-%m-%d')
                d2 = timedelta(days=90)
                d3 = d1+d2
                w1 = d1 + timedelta(days=7)
                w2 = d1 + timedelta(days=14)
                w3 = d1 + timedelta(days=21)
                w4 = d1 + timedelta(days=28)
                tab1 = Patients(Patients_PK=CK,Patient_ID=int(r[2]),Centre_ID_id=int(r[1]),Gender=r[3],Phone=r[5],Age=int(r[4]))
                tab1.save()
                tab2 = Asthma_Mgmt(Asthma_Mgmt_PK=CK,First_Date=d1,Lung_Function=int(r[6]),Severity_Level_id=int(r[7]),Year_ER_Visits=int(r[8]),Year_Hospital_Visits=int(r[9]),Followup_Date=d3)
                tab2.save()
                tab_w1 = Date_by_week(Date_week=w1,T_Msg_id=int(r[7]),P_ID=CK)
                tab_w1.save()
                tab_w2 = Date_by_week(Date_week=w2,T_Msg_id=int(r[7]),P_ID=CK)
                tab_w2.save()
                tab_w3 = Date_by_week(Date_week=w3,T_Msg_id=int(r[7]),P_ID=CK)
                tab_w3.save()
                tab_w4 = Date_by_week(Date_week=w4,T_Msg_id=int(r[7]),P_ID=CK)
                tab_w4.save()
                response = "Your Message was recieved successfully"
                self.debug("responding with %s", response)
                message.respond(response)

                db1.close ()
                return True
        elif len(r) == 8:
            ck1 = CK + "-" + str(datetime.strptime(r[0],'%Y-%m-%d'))
            if int(r[5])==1:
                d1 = datetime.strptime(r[0],'%Y-%m-%d')
                d2 = timedelta(days=14)
                d3 = d1+d2
                w1 = d1 + timedelta(days=7)
                w2 = d1 + timedelta(days=14)
                w3 = d1 + timedelta(days=21)
                w4 = d1 + timedelta(days=28)
                s = "UPDATE asthma_app_patients SET Phone = '%s' WHERE Patient_ID = '%d'" % (r[3],int(r[2]))
                cursor = db1.cursor()
                cursor.execute(s)
                tab3 = Followup_Visits(Pk=ck1,Follow_Visits=CK,Follow_Date=d1,F_Lung_Function=int(r[4]),F_Severity_Level_id=int(r[5]),Monthly_ER_Visits=int(r[6]),Monthly_Hospital_Visits=int(r[7]),Nxt_Follow_up_Date=d3)
                tab3.save()
                tab_w1 = Date_by_week(Date_week=w1,T_Msg_id=int(r[5]),P_ID=CK)
                tab_w1.save()
                tab_w2 = Date_by_week(Date_week=w2,T_Msg_id=int(r[5]),P_ID=CK)
                tab_w2.save()
                tab_w3 = Date_by_week(Date_week=w3,T_Msg_id=int(r[5]),P_ID=CK)
                tab_w3.save()
                tab_w4 = Date_by_week(Date_week=w4,T_Msg_id=int(r[5]),P_ID=CK)
                tab_w4.save()
                response = "Your Message was recieved successfully"
                self.debug("responding with %s", response)
                message.respond(response)

                db1.close ()
                return True                        
            elif int(r[5])==2:
                d1 = datetime.strptime(r[0],'%Y-%m-%d')
                d2 = timedelta(days=30)
                d3 = d1+d2
                w1 = d1 + timedelta(days=7)
                w2 = d1 + timedelta(days=14)
                w3 = d1 + timedelta(days=21)
                w4 = d1 + timedelta(days=28)
                s = "UPDATE asthma_app_patients SET Phone = '%s' WHERE Patient_ID = '%d'" % (r[3],int(r[2]))
                cursor = db1.cursor()
                cursor.execute(s) 
                tab3 = Followup_Visits(Pk=ck1,Follow_Visits =CK,Follow_Date=d1,F_Lung_Function=int(r[4]),F_Severity_Level_id=int(r[5]),Monthly_ER_Visits=int(r[6]),Monthly_Hospital_Visits=int(r[7]),Nxt_Follow_up_Date=d3)
                tab3.save()
                tab_w1 = Date_by_week(Date_week=w1,T_Msg_id=int(r[5]),P_ID=CK)
                tab_w1.save()
                tab_w2 = Date_by_week(Date_week=w2,T_Msg_id=int(r[5]),P_ID=CK)
                tab_w2.save()
                tab_w3 = Date_by_week(Date_week=w3,T_Msg_id=int(r[5]),P_ID=CK)
                tab_w3.save()
                tab_w4 = Date_by_week(Date_week=w4,T_Msg_id=int(r[5]),P_ID=CK)
                tab_w4.save()
                response = "Your Message was recieved successfully"
                self.debug("responding with %s", response)
                message.respond(response)

                db1.close ()
                return True                        
            elif int(r[5])==3:
                d1 = datetime.strptime(r[0],'%Y-%m-%d')
                d2 = timedelta(days=90)
                d3 = d1+d2
                w1 = d1 + timedelta(days=7)
                w2 = d1 + timedelta(days=14)
                w3 = d1 + timedelta(days=21)
                w4 = d1 + timedelta(days=28)
                s = "UPDATE asthma_app_patients SET Phone = '%s' WHERE Patient_ID = '%d'" % (r[3],int(r[2]))
                cursor = db1.cursor()
                cursor.execute(s)
                db1.commit()
                tab3 = Followup_Visits(Pk=ck1,Follow_Visits =CK,Follow_Date=d1,F_Lung_Function=int(r[4]),F_Severity_Level_id=int(r[5]),Monthly_ER_Visits=int(r[6]),Monthly_Hospital_Visits=int(r[7]),Nxt_Follow_up_Date=d3)
                tab3.save()
                tab_w1 = Date_by_week(Date_week=w1,T_Msg_id=int(r[5]),P_ID=CK)
                tab_w1.save()
                tab_w2 = Date_by_week(Date_week=w2,T_Msg_id=int(r[5]),P_ID=CK)
                tab_w2.save()
                tab_w3 = Date_by_week(Date_week=w3,T_Msg_id=int(r[5]),P_ID=CK)
                tab_w3.save()
                tab_w4 = Date_by_week(Date_week=w4,T_Msg_id=int(r[5]),P_ID=CK)
                tab_w4.save()
                response = "Your Message was recieved successfully"
                self.debug("responding with %s", response)
                message.respond(response)

                db1.close ()
                return True
                        
        else:       
            response = "wrong message! "
            self.debug("responding with %s", response)
            message.respond(response)
            return True
            
    def cleanup (self, message):
            """Perform any clean up after all handlers have run in the
            cleanup phase."""
            pass

    def outgoing (self, message):
        pass



    def stop (self):
        """Perform global app cleanup when the application is stopped."""
        pass        

