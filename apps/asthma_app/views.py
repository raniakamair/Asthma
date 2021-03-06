from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect

def Home(request):
    return render_to_response("asthma_app/Home.html", {}, context_instance=RequestContext(request) )

@login_required(login_url='/account/login/')
@csrf_protect
def Message_log(request):
    return render_to_response("asthma_app/Message_log.php", {}, context_instance=RequestContext(request) )

@login_required(login_url='/account/login/')
@csrf_protect
def Defaulters(request):
    errors = []
    c = {}
    c.update(csrf(request)) 
    if request.method == 'POST':
        rr = request.POST.getlist('CB')
        pf = request.POST['lf']
        pt = request.POST['lt']
        pf_out=" Period From : "+ pf 
        pt_out=" To : "+ pt
        if "a" in rr :
            if "b" in rr:
                if "c" in rr:
                    return render_to_response("asthma_app/Defaulters_by_All.php", {'pf' :pf_out,'pt' : pt_out }, context_instance=RequestContext(request) )
                else:
                    return render_to_response("asthma_app/Defaulters_by_Centre_And_Age.php", {'pf' :pf_out,'pt' : pt_out }, context_instance=RequestContext(request) )
            elif "c" in rr:
                return render_to_response("asthma_app/Defaulters_by_Centre_And_Gender.php", {'pf' :pf_out,'pt' : pt_out }, context_instance=RequestContext(request) )
            else:
                return render_to_response("asthma_app/Defaulters_by_Centre.php", {'pf' :pf_out,'pt' : pt_out }, context_instance=RequestContext(request) )
        elif "b" in rr :
            if "c" in rr:
                return render_to_response("asthma_app/Defaulters_by_Gender_And_Age.php", {'pf' :pf_out,'pt' : pt_out }, context_instance=RequestContext(request) )
            else:
                return render_to_response("asthma_app/Defaulters_by_Age.php", {'pf' :pf_out,'pt' : pt_out }, context_instance=RequestContext(request) )
        elif "c" in rr :
            return render_to_response("asthma_app/Defaulters_by_Gender.php", {'pf' :pf_out,'pt' : pt_out }, context_instance=RequestContext(request) )
        else:
            return render_to_response("asthma_app/Defaulters.php", {}, context_instance=RequestContext(request) )

    return render_to_response("asthma_app/Defaulters_by_Centre.php", {}, context_instance=RequestContext(request) )

@login_required(login_url='/account/login/')
@csrf_protect
def Severity_Levels(request):
    if request.method == 'POST':
        SP = request.POST['SV_P']
        rr = request.POST['CB']
        if rr == "a"  :
            return render_to_response("asthma_app/Severity_Levels_By_Center.php",{'SP' : SP }, context_instance=RequestContext(request) )
        elif rr == "b":
            return render_to_response("asthma_app/Severity_Levels_By_Age.php",{'SP' : SP }, context_instance=RequestContext(request) )
        elif rr == "c":
            return render_to_response("asthma_app/Severity_Levels_By_Gender.php",{'SP' : SP }, context_instance=RequestContext(request) )
        else:
            return render_to_response("asthma_app/Severity_Levels.php",{'SP' : SP }, context_instance=RequestContext(request)  )
    
    return render_to_response("asthma_app/Severity_Levels_By_Center.php",{}, context_instance=RequestContext(request)  )

 
@login_required(login_url='/account/login/')
@csrf_protect
def ER_and_Hospital(request):
    if request.method == 'POST':
        ER = request.POST['ER_HO']
        return render_to_response("asthma_app/ER_and_Hospital.php",{'ER' : ER }, context_instance=RequestContext(request)  )
    return render_to_response("asthma_app/ER_and_Hospital.php",{}, context_instance=RequestContext(request)  )
  





