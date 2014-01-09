from django.conf.urls.defaults import *



urlpatterns = patterns('asthma.apps.asthma_app.views',

    url(r'^Home$','Home',name="asthma_app_Home"),
   url(r'^Message_log$','Message_log',name="asthma_app_Message_log"),
    url(r'^Defaulters$','Defaulters',name="asthma_app_Defaulters"),
   url(r'^Severity_Levels$','Severity_Levels',name="asthma_app_Severity_Levels"),
   url(r'^ER_and_Hospital$','ER_and_Hospital',name="asthma_app_ER_and_Hospital"),
   )
