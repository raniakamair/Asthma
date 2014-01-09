{% load php %}
{% load i18n %}


<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
		<title>Severity Levels Report</title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />



<link type="text/css" rel="stylesheet" href="/static/rapidsms/stylesheets/layout.css" />
<link type="text/css" rel="stylesheet" href="/static/rapidsms/stylesheets/splits.css" />
<link type="text/css" rel="stylesheet" href="/static/rapidsms/stylesheets/modules.css" />
<link type="text/css" rel="stylesheet" href="/static/rapidsms/stylesheets/tables.css" />
<link type="text/css" rel="stylesheet" href="/static/rapidsms/stylesheets/forms.css" />
<link type="text/css" rel="stylesheet" href="/static/rapidsms/stylesheets/icons.css" />



<script type="text/javascript" src="/static/rapidsms/javascripts/jquery-1.3.2.min.js"></script>
<script type="text/javascript" src="/static/rapidsms/javascripts/collapse.js"></script>

<style type="text/css">
	#inner {
		margin: 4em 25%;
	}

	div.module div {
		border: 1px solid #ddd;
		border-top-color: #636363;
		margin-top: -1px;
	}

	div.module p {
		padding-left: 1em;
		padding-right: 1em;
	}

	code, pre {
		background: #ffe;
	}

	pre {
		padding: 1em;
		margin: 0;
	}
#f {
		font-size: 12px;
		
	}
#w {
		font-size: 12px;
		color:white
	}
</style>



</head>
{% block content%}

       <body>


<div id="wrapper">
	

			
			<div id="header">
				<div id="branding">
					<h1>
						<a title="welcome">
							<span>RapidSMS</span>
						</a>
					</h1>
				</div>

				
				<div id="auth">
					<a href="/account/logout/">Log out root</a>
				</div>
				
				<ul id="tabs">
			   <li class="app- ">
					   <a href="/asthma_app/Home"><span>Home</span></a>
					</li>
					

					<li class="app-">
					    <a href="/asthma_app/Message_log"><span>Message log</span></a>
					</li>
				
					<li class="app- ">
					    <a href="/asthma_app/Defaulters"><span>Defaulters Report</span></a>
					</li>

					<li class="app- active">
					    <a href="/asthma_app/Severity_Levels"><span>Severity Levels Report</span></a>
					</li>

					<li class="app-">
					    <a href="/asthma_app/ER_and_Hospital"><span>ER and Hospital Report</span></a>
					</li>
					
				

								
			</div>

{% php $con = mysql_connect("localhost","root","romo"); mysql_select_db ("asthma",$con);mysql_query("SET NAMES 'utf8' COLLATE 'utf8_unicode_ci'"); %}
<form action="Severity_Levels" method="post">{% csrf_token %}<br>
<table cellpadding=0 width=100%><tr><td><font size =2 >Please choose report type : </font><br><br>&nbsp;&nbsp;&nbsp;&nbsp;
<input type="radio" name="CB" value="a" id="by_center" />By Center&nbsp;&nbsp;
<input type="radio" name="CB" value="b" id ="by_age" checked />By Age&nbsp;&nbsp;
<input type="radio" name="CB" value="c" id="by_gender" />By Gender</td><td>
<font size =2 >Please choose report Date : </font><br><br>&nbsp;&nbsp;&nbsp;&nbsp;
From : 
<select name="SV_P">
<option values="">2006</option>
<option values="">2007</option>
<option values="">2008</option>
<option values="">2009</option>
<option values="">2010</option>
<option values="">2011</option>
<option values="">2012</option>
<option values="">2013</option>
</select>

 </td><td>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type=submit value="View Report"></td></tr></table></form><br>
<font size= 3 >Report of severity level by age </font>
<br>
<br>
<br>
<center>

<table  border=1 cellpadding=10 width=100%>
<tr bgcolor=#C0C0C0 id=f><th rowspan=2 width=25%><center><font size= 3 bold>Severity Level</font></center></th><th colspan=6 width=75%><center><font size= 3 bold>Age Group</font></center></th></tr>
<tr bgcolor=#C0C0C0 id=f><th><center><15   </center></th><th><center> 15 - 24 </center></th><th><center> 25 - 44 </center></th><th><center> 45 - 64 </center></th><th><center> >=65  </center></th></tr>  
{% php $q1 = mysql_query("select Treat_ID from asthma_app_treatments");while($row_list1=mysql_fetch_array($q1)){$q2 = mysql_query("select count(*) from asthma_app_asthma_mgmt, asthma_app_patients where asthma_app_asthma_mgmt.Asthma_Mgmt_PK = asthma_app_patients.Patients_PK and asthma_app_patients.Age<15 and asthma_app_asthma_mgmt.Severity_Level_id ={$row_list1[0]}"); $q3 = mysql_query("select count(*) from asthma_app_followup_visits, asthma_app_patients where asthma_app_followup_visits.Follow_PK = asthma_app_patients.Patients_PK and asthma_app_patients.Age<15 and asthma_app_followup_visits.F_Severity_Level_id = {$row_list1[0]}"); $q4 = mysql_query("select count(*) from asthma_app_asthma_mgmt, asthma_app_patients where asthma_app_asthma_mgmt.Asthma_Mgmt_PK = asthma_app_patients.Patients_PK and (asthma_app_patients.Age between 14 and 25) and asthma_app_asthma_mgmt.Severity_Level_id ={$row_list1[0]}"); $q5 = mysql_query("select count(*) from asthma_app_followup_visits, asthma_app_patients where asthma_app_followup_visits.Follow_PK = asthma_app_patients.Patients_PK and (asthma_app_patients.Age between 14 and 25) and asthma_app_followup_visits.F_Severity_Level_id ={$row_list1[0]}"); $q6 = mysql_query("select count(*) from asthma_app_asthma_mgmt, asthma_app_patients where asthma_app_asthma_mgmt.Asthma_Mgmt_PK = asthma_app_patients.Patients_PK  and (asthma_app_patients.Age between 24 and 45) and asthma_app_asthma_mgmt.Severity_Level_id ={$row_list1[0]}"); $q7 = mysql_query("select count(*) from asthma_app_followup_visits, asthma_app_patients where asthma_app_followup_visits.Follow_PK = asthma_app_patients.Patients_PK and (asthma_app_patients.Age between 24 and 45) and asthma_app_followup_visits.F_Severity_Level_id ={$row_list1[0]}"); $q8 = mysql_query("select count(*) from asthma_app_asthma_mgmt, asthma_app_patients where asthma_app_asthma_mgmt.Asthma_Mgmt_PK = asthma_app_patients.Patients_PK  and (asthma_app_patients.Age between 44 and 65) and asthma_app_asthma_mgmt.Severity_Level_id ={$row_list1[0]}"); $q9 = mysql_query("select count(*) from asthma_app_followup_visits, asthma_app_patients where asthma_app_followup_visits.Follow_PK = asthma_app_patients.Patients_PK  and (asthma_app_patients.Age between 44 and 65) and asthma_app_followup_visits.F_Severity_Level_id ={$row_list1[0]}"); $q10 = mysql_query("select count(*) from asthma_app_asthma_mgmt, asthma_app_patients where asthma_app_asthma_mgmt.Asthma_Mgmt_PK = asthma_app_patients.Patients_PK  and asthma_app_patients.Age>=65 and asthma_app_asthma_mgmt.Severity_Level_id ={$row_list1[0]}"); $q11 = mysql_query("select count(*) from asthma_app_followup_visits, asthma_app_patients where asthma_app_followup_visits.Follow_PK = asthma_app_patients.Patients_PK  and asthma_app_patients.Age>=65 and asthma_app_followup_visits.F_Severity_Level_id ={$row_list1[0]}"); %}
{% php  $row_list2=mysql_fetch_row($q2);$row_list3=mysql_fetch_row($q3);$row_list4=mysql_fetch_row($q4);$row_list5=mysql_fetch_row($q5);$row_list6=mysql_fetch_row($q6);$row_list7=mysql_fetch_row($q7);$row_list8=mysql_fetch_row($q8);$row_list9=mysql_fetch_row($q9);$row_list10=mysql_fetch_row($q10);$row_list11=mysql_fetch_row($q11);if($row_list1[0]==1){$SL="Severe";}else if($row_list1[0]==2){$SL="Moderate";}else if($row_list1[0]==3){$SL="Mild";}  %}
{% php  echo"<tr><td>".$SL."</td><td>".($row_list2[0]+$row_list3[0])."</td><td>".($row_list4[0]+$row_list5[0])."</td><td>".($row_list6[0]+$row_list7[0])."</td><td>".($row_list8[0]+$row_list9[0])."</td><td>".($row_list10[0]+$row_list11[0])."</td><tr>"; } %}


</table></center>

<div id="footer">
<p class="rights">Copyright &copy; 2008 &#8211; 2010
<a href="http://unicef.org">UNICEF</a> et al.<br />
<a href="http://github.com/rapidsms/rapidsms">RapidSMS</a> is available under
<a href="http://github.com/rapidsms/rapidsms/raw/master/LICENSE">the BSD license</a>.
				</p>

				<div class="footer-region">&bull; <a href="/export/database" class="db-export">Export to SQL</a>
</div>
			</div>
			
		</div>
	</body>{% endblock %}
</html>

