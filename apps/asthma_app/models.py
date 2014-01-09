from django.db import models


class Centres(models.Model):

    Centre_ID = models.IntegerField(max_length=64,primary_key=True)
    Centre_Name = models.CharField(max_length=64)
   
    def __unicode__(self):
        return u"%s - %s"%(self.key,self.text)


class Treatments(models.Model):

    Treat_ID = models.IntegerField(max_length=64,primary_key=True)
    Severity_level = models.CharField(max_length=64)
    Treat_Msg = models.TextField()
    
    def __unicode__(self):
        return u"%s - %s"%(self.key,self.text)


class Patients(models.Model):
   
    Patients_PK = models.CharField(max_length=64,primary_key=True)
    Patient_ID = models.IntegerField(max_length=64)
    Centre_ID = models.ForeignKey(Centres)
    Gender = models.CharField(max_length=64)
    Phone = models.CharField(max_length=64,null=True)
    Age = models.IntegerField(max_length=64,null=True)

    def __unicode__(self):
        return u"%s - %s"%(self.key,self.text)

class Asthma_Mgmt(models.Model):

    Asthma_Mgmt_PK = models.CharField(max_length=64,primary_key=True)
    First_Date = models.DateField(null=True)
    Lung_Function = models.IntegerField(max_length=64,null=True)
    Severity_Level = models.ForeignKey(Treatments)
    Year_ER_Visits = models.IntegerField(max_length=64,null=True)
    Year_Hospital_Visits = models.IntegerField(max_length=64,null=True)
    Followup_Date = models.DateField(null=True)

    def __unicode__(self):
        return u"%s - %s"%(self.key,self.text)

class Followup_Visits(models.Model):

    Pk = models.CharField(max_length=64,primary_key=True)
    Follow_Visits = models.CharField(max_length=64)
    Follow_Date = models.DateField(null=True)
    F_Lung_Function = models.IntegerField(max_length=64,null=True)
    F_Severity_Level = models.ForeignKey(Treatments)
    Monthly_ER_Visits = models.IntegerField(max_length=64,null=True)
    Monthly_Hospital_Visits = models.IntegerField(max_length=64,null=True)
    Nxt_Follow_up_Date = models.DateField(null=True)

    def __unicode__(self):
        return u"%s - %s"%(self.key,self.text)

class Date_by_week(models.Model):

    DW_PK = models.AutoField(primary_key=True,max_length=64)
    Date_week = models.DateField(null=True)
    T_Msg = models.ForeignKey(Treatments)
    P_ID= models.CharField(max_length=64)

    def __unicode__(self):
        return u"%s - %s"%(self.key,self.text)
    
class Defaulter(models.Model):

    Defaulter_PK = models.AutoField(primary_key=True,max_length=64)
    Default_Date = models.CharField(max_length=64,null=True)
    Last_Flowup_date = models.CharField(max_length=64,null=True)
    Defaulter_ID= models.CharField(max_length=64,null=True)

    def __unicode__(self):
        return u"%s - %s"%(self.key,self.text)
