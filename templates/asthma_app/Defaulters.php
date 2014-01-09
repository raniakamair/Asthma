{% load i18n %}
{% load php %}

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
		<title>Defaulters Report</title>
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
				
					<li class="app- active">
					    <a href="/asthma_app/Defaulters"><span>Defaulters Report</span></a>
					</li>

					<li class="app-">
					    <a href="/asthma_app/Severity_Levels"><span>Severity Levels Report</span></a>
					</li>

					<li class="app-">
					    <a href="/asthma_app/ER_and_Hospital"><span>ER and Hospital Report</span></a>
					</li>
					
				

								
			</div>
                                    
			
<form action="Defaulters" name="cfrm" method="post">{% csrf_token %}
	
<br><table cellpadding=0 width=100%><tr><td><font size =2 >Please choose report type : </font><br><br>&nbsp;&nbsp;&nbsp;&nbsp;
<input type="checkbox" name="CB" value="a" id="by_center" />By Center&nbsp;&nbsp;
<input type="checkbox" name="CB" value="b" id ="by_age" />By Age&nbsp;&nbsp;
<input type="checkbox" name="CB" value="c" id="by_gender" />By Gender<br /><td><td>
<font size =2 >Please choose report period : </font><br><br>&nbsp;&nbsp;&nbsp;&nbsp;
From : 
<select name="lf">
<option values="">2006</option>
<option values="">2007</option>
<option values="">2008</option>
<option values="">2009</option>
<option values="">2010</option>
<option values="">2011</option>
<option values="">2012</option>
<option values="">2013</option>
</select>
To : 
<select  name="lt" >
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
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type=submit value="View Report"></td></tr></table></form><br><br><br>
 {{ pf }} &nbsp; {{ pt }} </b> <br><br>
<br> 
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



