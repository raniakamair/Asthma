{% load i18n %}
{% load php %}

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
		<title>ER and Hospital Report</title>
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

					<li class="app-">
					    <a href="/asthma_app/Severity_Levels"><span>Severity Levels Report</span></a>
					</li>

					<li class="app- active">
					    <a href="/asthma_app/ER_and_Hospital"><span>ER and Hospital Report</span></a>
					</li>				
			</div>
                
{% php $con = mysql_connect("localhost","root","romo"); mysql_select_db ("asthma",$con);mysql_query("SET NAMES 'utf8' COLLATE 'utf8_unicode_ci'"); %}
	 

<form action="ER_and_Hospital" method="post">{% csrf_token %}
 <table cellpadding=0 width=100%><tr><td>
<font size= 2 >Please choose report Year: </font>&nbsp;&nbsp;
<select name="ER_HO">
  <option value="2009">2009</option>
  <option value="2010">2010</option>
  <option value="2011">2011</option>
  <option value="2012">2012</option>
  <option value="2013" selected>2013</option>
  <option value="2014">2014</option>
  <option value="2015">2015</option>
<option value="2016">2016</option>
<option value="2017">2017</option>
</select> &nbsp;
<input type="submit" name="Submit" value="Submit" />
 </td></tr></table>
</form>
 <br>
<font size= 3 >ER and Hospital Report</font>
<br>
<br>
<br>
<center>
<table  border=1 cellpadding=10 width=100%>
<tr bgcolor=#C0C0C0 id=f><th><center><font size= 3 bold>Patient ID</font></center></th><th><center><font size= 3 bold>Total annual ER Visits</font></center></th><th><center><font size= 3 bold>Total annual Hospital Visits</font></center></th><th><center><font size= 3 bold>Total of ER Visits on Followup</font></center></th><th><center><font size= 3 bold>Total of Hospital Visits on Followup</font></center></th></tr>


{% php  $q1 = mysql_query("select Patients_PK from asthma_app_patients");$q2 = mysql_query("select Year_ER_Visits from asthma_app_asthma_mgmt, asthma_app_patients where asthma_app_asthma_mgmt.Asthma_Mgmt_PK = asthma_app_patients.Patients_PK");$q3 = mysql_query("select Year_Hospital_Visits from asthma_app_asthma_mgmt, asthma_app_patients where asthma_app_asthma_mgmt.Asthma_Mgmt_PK = asthma_app_patients.Patients_PK");$q4 = mysql_query("select sum(Monthly_ER_Visits) from asthma_app_followup_visits, asthma_app_patients where asthma_app_followup_visits.Follow_Visits = asthma_app_patients.Patients_PK group by asthma_app_patients.Patients_PK");$q5 = mysql_query("select sum(Monthly_Hospital_Visits) from asthma_app_followup_visits, asthma_app_patients where asthma_app_followup_visits.Follow_Visits = asthma_app_patients.Patients_PK group by asthma_app_patients.Patients_PK"); %}
{% php  while($row_list1=mysql_fetch_array($q1) and  $row_list2=mysql_fetch_array($q2) and $row_list3=mysql_fetch_array($q3) and $row_list4=mysql_fetch_array($q4) and $row_list5=mysql_fetch_array($q5) ){ %}
{% php echo "<tr><td>".$row_list1[0]."</td>"."<td>".$row_list2[0]."</td>"."<td>".$row_list3[0]."</td><td>".$row_list4[0]."</td><td>".$row_list5[0]."</td></tr>"; } %}

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
	</body>
</html>



